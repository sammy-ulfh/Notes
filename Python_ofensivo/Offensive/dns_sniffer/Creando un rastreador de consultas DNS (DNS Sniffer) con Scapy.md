# Introduccion

Un DNS Sniffer es una herramienta ofensiva que permite interceptar y analizar las consultas DNS en una red. Estas consultas son esenciales en la comunicación de internet, ya que convierten el nombre de dominio en direcciones IP. 

on Scapy podremos capturar paquetes DNS de forma activa para explorar cómo los dispositivos de una red interactúan con los servidores DNS. Este conocimiento es crucial en el contexto ofensivo, ya que permite identificar objetivos potenciales para ataques y explotar vulnerabilidades en la comunicación DNS.
# Practica

Como trabajaremos con el sniffer será, por un lado, ejecutar el envenenamiento ARP con el ARP Spoofer para poder capturar el tráfico y con nuestro Sniffer vamos a capturar solamente las consultas DNS aplicando un filtro. En Wireshark utilizamos el filtro **dns**, pero también sabemos que las consultas DNS trabajan mediante el protocolo **UDP** y se realizan mediante el puerto **53**, por lo que el filtro que realizaremos en scapy será este mismo (**udp and port 53**). 

Para nuestro **dns_sniffer.py** vamos a hacerlo directamente sin utilizar argparse, en este caso importaremos scapy y guardaremos el nombre de nuestra interfaz en una variable, después utilizaremos **scapy.sniff** para poder ponernos en escuchar, le pasaremos la interfaz con el argumento **iface** y nuestro filtro para upd, lo aplicaremos con el atributo **filter** indicando que el filtro sea **udp and port 53**:

![[Offensive/dns_sniffer/images/001.png]]

Además, nosotros estaremos recibiendo cada paquete y podremos hacer algo con cada uno de ellos. Para procesar los paquetes que vayamos recibiendo, utilizaremos el atributo **prn** con el cual le pasaremos una función que recibirá como argumento el paquete y será ejecutada con cada paquete que sea recibido:

![[Offensive/dns_sniffer/images/002.png]]

Además, los paquetes se suelen guardar en memoria. En este caso queremos evitar esto y que se haga en el momento que se reciba el paquete la ejecución de la función que definimos para tratar ese paquete, lo que nos ayuda a tener mayor control. 

Para hacerlo de esta manera, agregaremos el argumento **store** y lo igualaremos a cero en nuestro sniff (**scapy.sniff**).

![[Offensive/dns_sniffer/images/003.png]]

Con esto, al imprimir el paquete, ya podremos visualizarlo y ver el tráfico cuando nuestro spoofer y sniffer estén corriendo:

![[Offensive/dns_sniffer/images/004.png]]
Con esto ya observamos el tráfico DNS del dispositivo target, pero buscaremos visualizarlo de una mejor manera. 

Para visualizar más a fondo el paquete, utilizaremos el método **show()** para observar de qué forma veremos algunos datos al visitar una página:

![[Offensive/dns_sniffer/images/005.png]]

![[Offensive/dns_sniffer/images/006.png]]

Aquí hemos visitado la página hack4u.io en la máquina víctima. Si nos enfocamos en el layer o capa **qd** veremos que es un **DNS Question Record** que, en otras ocasiones, podríamos visualizar como **DNS QR**. Vemos cómo esta tiene el atributo **qname** que contiene el nombre del dominio. Esto es así con todos los paquetes, ya que cada que se realice una resolución DNS existirá una capa DNS Question Record o DNS Query Record y con este campo **qname** podría darnos el nombre del dominio que está visitando nuestra víctima. 

Para ello, en nuestro sniffer, como de primeras, solo nos interesan todos aquellos paquetes que tengan esta capa en la cual se encuentra el nombre del dominio. Nos aseguraremos de que los paquetes con los que vayamos a trabajar tengan la capa de **DNS Question Record**. 

Esto lo haremos con el método **haslayer** del paquete y para indicarle que nos interesa solo aquel que tenga la capa **DNSQR** lo indicaremos a nivel de argumento con el método de scapy **scapy.DNSQR**, de esta forma solo estaríamos entrando al condicional si el paquete tiene la capa **DNSQR**:

![[Offensive/dns_sniffer/images/007.png]]

![[Offensive/dns_sniffer/images/008.png]]

En este caso, estamos recuperando el dominio a nivel de la capa **DNSQR** como si de una posición se tratase y extraemos el atributo **qname** que ya es directamente el nombre de dominio. Es necesario aplicarle un **decode** a esto, ya que lo recibimos en formato de bytes y al imprimirlo queremos ver el texto en formato legible:

![[Offensive/dns_sniffer/images/009.png]]

Como podremos ver, se repiten algunos dominios, es por ello que en este caso podríamos utilizar **set** en Python, que es algo similar a una lista, pero la diferencia es que un set solo puede almacenar elementos únicos. 

Por ello, en nuestra función principal vamos a definir una variable global **domains_seen** y la definiremos como un **set**.

![[Offensive/dns_sniffer/images/010.png]]

Ahora en nuestra función **process_dns_packet** primeramente crearemos una lista de palabras en la cual si alguna hace match con algún dominio, lo descartaríamos, ya que, navegadores o páginas suelen hacer peticiones que no nos pueden interesar, como **google**, **bing**, algunas que tienen por delante cloudflare **cloud** o incluso **static** que se puede llegar a ver en alguna petición para Google Maps o fuentes.

![[Offensive/dns_sniffer/images/011.png]]

Ahora iteraremos sobre nuestra lista de palabras que no deberían estar en un dominio que queremos considerar para almacenar y para evitar hacer una comprobación extra, directamente podemos emplear **any**, donde con un único match que llegue a existir de nuestras palabras clave regresará **True**:

![[Offensive/dns_sniffer/images/012.png]]

Si no utilizáramos **any**, podríamos emplear una lista de comprensión, donde después se verifique si en algún punto dio **True** o si **True** está dentro de la lista, lo que daría como resultado que el dominio es uno de los que quisiéramos excluir:

![[Offensive/dns_sniffer/images/013.png]]

De esta manera, estamos visualizando todos aquellos donde el **any** nos da true con las palabras clave que hemos colocado, por ende tendremos que hacer que nuestra condición tenga un **not** para solo entrar al condicional con todos esos dominios que sí nos interesan. Con ello también agregaremos el dominó a nuestro set con el método **add**:

![[Offensive/dns_sniffer/images/014.png]]

Como ya mencionamos, con un **set** solo podremos almacenar valores que no estén dentro de él, por lo que si intentamos incorporar un valor que ya se encuentra en el set nos data error, por ello en nuestro condicional colocaremos la condición **not domain in domains_seen**, con ello dará True si el dominio que interceptemos un no se encuentra en nuestro **set**:

![[Offensive/dns_sniffer/images/015.png]]

Con esto, ahora con print mostrarás todos los dominios sin repetirlos.

## Siguienes apuntes

[[]]