# Introducción

Se creará un DNS Spoofer con Scapy y NetfilterQueue, se centrará en manipular las solicitudes DNS de una red para redirigir todo el tráfico a un destino elegido por nosotros como atacantes. 

La herramienta clave en nuestro ordenador será **iptables**, una utilidad en línea de comandos en sistemas Linux que permite configurar las reglas del Firewall del sistema operativo. Utilizaremos iptables para redirigir todo el tráfico DNS (normalmente en el puerto 53) a una cola NFQUEUE. NFQUEUE es una funcionalidad de iptables que nos permite interceptar paquetes en la red, procesarlos con un programa externo (en este caso el DNS Spoofer creado con scapy y netfilterqueue) y luego podremos decidir si aceptar estos paquetes para que viajen a su destino, descartarlos o modificarlos.

Al configurar las iptables para enviar los paquetes DNS a NFQUEUE, podemos utilizar scapy para inspeccionar y modificar estos paquetes. Por ejemplo, cuando la víctima intenta resolver un dominio, podemos cambiar la respuesta para que la IP resuelta sea la nuestra, no la legítima. Esto permite realizar ataques tipo MITM, donde redirigimos al usuario a un servidor bajo nuestro control en lugar de un servidor real, lo que suele ser utilizado para una variedad de propósitos maliciosos como el phishing o inyección de contenido.

# Practica

## Teoria

**netfilterqueue** es una librería que nos permitirá que aplicaciones construidas en Python puedan interactuar con paquetes IP, los cuales están siendo manipulados principalmente con el framework **Netfilter** el cual es parte del núcleo de Linux y permite interceptar y manipular paquetes de red. 

Esto es en lo que se basan herramientas como **iptables** con la cual podremos definir reglas. En este caso aplicaremos algunas reglas para enviar los paquetes a una cola **NFQUEUE** y le asignaremos un número de cola que se encuentra asociado a la misma. En este caso, le asignaremos el 0.

De esta forma, los paquetes estarán en una cola a la espera de que una aplicación interactúe con ellos, con lo cual nosotros en nuestro script tendremos que asociarnos a la cola que, en este caso, tiene el número 0 utilizando **bind**.

Una vez puedamos tratar los paquetes que se encuentren en la NFQUEUE podremos aceptarlos, rechazarlos o incluso modificarlos. Para ello, primeramente definiríamos nuestras reglas con **iptables**. 

Con las reglas que agregaremos con **iptables** si intentamos navegar en internet no podremos hacer nada, lo cual es lógico debido a las reglas que colocaremos, ya que, todos estos paquetes se envían a una cola esperando a ser tratados por un programa. El cual construiremos nosotros con Python.

Además, es importante saber que si ya hemos colocado algunas reglas con **iptables** podremos limpiar estas reglas con el comando:

```shell
iptables --flush
```

Las reglas que nosotros colocaremos para enviar los paquetes a una NFQUEUE serán:

```shell
iptables -I INPUT -j NFQUEUE --queue-num 0
iptables -I OUTPUT -j NFQUEUE --queue-num 0
iptables -I FORWARD -j NFQUEUE --queue-num 0
iptables --policy FORWARD ACCEPT
```

- **-I (insert)** es la forma de indicar a qué tipo de paquetes aplicaremos una regla, en este caso:
	-  **INPUT** hace referencia a los paquetes que reciba nuestra máquina.
	-  **OUTPUT** hace referencia a los paquetes que salgan desde nuestra máquina, tales como nuestras propias peticiones a internet.
	- **FORWARD** hace referencia a los paquetes que redirijamos desde nuestra máquina. 
-  **-j (jump)** se refiere a la acción que queremos realizar, en este caso enviar dichos paquetes a una NFQUEUE.
-  **--queue-num** nos sirve para indicar el número asociado a la cola que estamos enviando estos paquetes, la cual posteriormente nos servirá para asociarnos desde el script.

La última regla ya la utilizamos anteriormente, esta nos ayuda a permitir los paquetes entrantes para aplicarles la redirección de paquetes para evitar que nuestro firewall las bloquee al momento de realizar nuestro arp spoofing. 

Primero iremos viendo cómo es el DNS Spofing y cómo funciona haciendo pruebas en la propia máquina local y después lo haremos aplicando ARP Spoofing a una máquina en la red para interceptar sus paquetes y también modificarlos.

El **DNS Spoofing** se refiere a engañar a nuestra máquina víctima modificando el paquete para que la resolución DNS no se haga a la IP legitima del sitio que se está visitando, si no una IP bajo la cual nosotros tengamos control, tal como nuestra IP privada en la cual podremos estar corriendo un servidor local y mostrarle nosotros algo al usuario en lugar de la página legitima que se encontraba visitando.
## Script

Para nuestro script será importante instalar la librería **netfilterqueue**. 

Primeramente, importaremos esta librería y con ella crearemos un objeto que será una instancia de la clase **NetfilterQueue** de la librería que hemos importado:

![[Offensive/dns_spoofer/images/001.PNG]]

Ahora con este objeto utilizaremos el método **bind**. Este nos permitirá asociarnos a una cola que recordemos. En este caso, el número que está asociado a la cola es el 0, que fue el que definimos al agregar las reglas con **iptables**. El método **bind** requiere de dos argumentos, el primero será el número asociado a la cola y el segundo la función que tratará cada paquete, que esta será una función que creemos nosotros y recibirá los paquetes como argumento.

![[Offensive/dns_spoofer/images/002.PNG]]

Esto por sí solo no estará corriendo en bucle, por ende tendremos que finalmente utilizar el método **run** en nuestro objeto **queue** para que así este constantemente en bucle procesando cada uno de los paquetes que se encuentren en la NFQUEUE. 

Ahora, en nuestra función para el paquete, podríamos utilizar el método **accept()**, el cual nos permitirá aceptar el paquete, lo cual permitirá que este viaje a su destino:

![[Offensive/dns_spoofer/images/003.PNG]]

Con esto listo, si ya tenemos las reglas definidas, mientras no ejecutemos el script seguiremos sin internet, ya que los paquetes no viajaran, pero al ejecutar el script ahora los paquetes que automáticamente son redirigidos a la cola, serán capturados por nuestro script y aceptados automáticamente, por lo que si con el script ejecutándose intentamos acceder a internet, ahora sí que podremos navegar. 

Así como aceptamos los paquetes para que puedan viajar, podremos rechazarlos con **drop()**. 

Al momento de interceptar los paquetes, los que nos interesarán en este caso serán los que vienen de respuesta con la resolución DNS. Cuando nosotros queremos capturar a aquel que hace la solicitud, nos referimos a él con scapy como **scapy.DNSQR**, pero en el caso de la respuesta nos referiríamos a este hacia su capa como **scapy.DNSRR**.

Como ejercicio rápido, tendremos corriendo nuestro script que llevamos hasta ahora **dns_spoofer.py**, también el envenenamiento arp **arp_spoofer.py** contra la máquina víctima, esto nos permitirá interceptar el tráfico y además aceptar el tráfico de estos paquetes, ya que tenemos las reglas definidas para mandar los paquetes a la cola. 

Pero como ejercicio rápido, crearemos un script rápido con scapy el cual este en escucha capturando los paquetes con el filtro de **udp and port 53** para los paquetes DNS:

```shell
import scapy.all as scapy

def process_packet(packet):
	if packet.haslayer(scapy.DNSRR):
		qname = packet[scapy.DNSQR].qname
		if "hack4u.io" in qname:
			print("\n------------------------------")
			print(packet.show())

scapy.sniff(iface="[Your interface]", filter="udp and port 53", prn=process_packet, store=0)
```

Este último script es lo que vimos anteriormente con el dns_sniffer, capturara los paquetes DNS de la víctima y nos mostrara solamente aquellos que viajen ya como respuesta (**DNSRR**), con **show()** recordemos que nos muestra de forma detallada el paquete, por lo que aquí podremos visualizar mejor a que nos referíamos en un inicio con la interacción con paquetes IP. 

Además de filtrar por aquellos paquetes DNS que vengan como respuesta, también filtraremos por un único dominio que a nosotros nos interese, ya que, estaremos capturando bastantes paquetes posiblemente. Para ello, el script anterior recupera el nombre del dominio que recordemos, está en la capa **DNSQR** con el atributo **qname**. Si en este está el que nos interesa que es **hack4u.io** entonces lo mostramos.

Antes de imprimir la información del paquete, colocamos una línea de guiones para detectar dónde comienza la estructura de dicho paquete, debido a que podremos interceptar bastante información. 

Corremos los tres scripts en simultáneo en nuestra máquina victima visitamos una paguina en internet, como hack4u.io.

![[Offensive/dns_spoofer/images/004.PNG]]

Esto es como podremos ver el paquete de la resolución DNS. Como podremos ver, cuenta con varias capas y es como está construido un paquete a nivel de red. 

Ignorando la capa Ethernet. Vemos cómo tenemos una capa base, la cual es la IP, después una UDP y finalmente una DNS. La capa DNS se encuentra encapsulada dentro de la capa UDP y la capa UDP dentro de la principal que es la IP. Si observamos nuestra capa DNS:

![[Offensive/dns_spoofer/images/005.PNG]]

Aquí vemos cómo vemos múltiples **DNSRR** que vendrían siendo las respuestas. Si observamos el atributo **ancount** veremos que tiene el valor de **3**. Este valor está directamente asociado con el número de respuestas que recibimos de la resolución DNS, donde cada respuesta nos trae en su atributo **rrname** el nombre de dominio y en su atributo **rdata** la IP de dicho dominio al que queremos acceder.

La idea será construir un paquete DNSRR nuevo el cual solo contenga una respuesta y dentro del paquete que interceptemos limpiar todas las respuestas y colocar solo la que nosotros hayamos creado, además de setear el **ancount** a solo 1, ya que tendrá que concordar con la única respuesta que estamos colocando. 

Con cambiar únicamente esto no bastará, ya que el paquete, a nivel de las capas UDP e IP, cuenta con los atributos **len** y **chksum** que se encargan de verificar que el paquete no haya sido manipulado. La cosa es que estos valores igual se pueden modificar o eliminar y, por ende, bastará con dejarlos vacíos para que ya no se realice esta verificación y nuestro paquete no sea descartado.

Con ello en mente podremos olvidarnos de este script y del arp spoofing por un momento. Con solo correr el dns_spoofer si desde nuestra máquina de atacante hacemos un ping a **hack4u.io** veremos lo siguiente:

![[Offensive/dns_spoofer/images/006.PNG]]

Si observamos la primera línea del output, podremos ver una IP. Esta IP es de la misma resolución DNS y es la IP a la cual por detrás nos conectamos cuando vamos a la página **hack4u.io** en el navegador. Por ende la finalidad del script será modificar el paquete para que ahora resuelva hacia nuestra IP privada que tenemos como atacantes y como prueba correremos un servidor HTTP con Python que tenga una página index.html y debería ser la que nos muestre.  
  
En el script que ya tenemos, podremos mostrar el paquete antes de aceptarle para ver cómo se ve:

![[Offensive/dns_spoofer/images/007.PNG]]

![[Offensive/dns_spoofer/images/008.PNG]]

Podremos ver más el contenido del paquete extrayendo el payload con el método **get_payload()**:

![[Offensive/dns_spoofer/images/010.PNG]]

La cosa aquí es que todo lo vemos como datos en bruto. Lo interesante es que aquí ya podremos mezclar las cosas que hemos visto como la herramienta scapy, ya que, esta es capaz de comprender este paquete y podremos transformarlo con scapy a un paquete IP como el que vimos recientemente para manipularlo y después el paquete modificado podremos agregarlo nuevamente a este paquete que tenemos utilizando **set_payload()**. 

Por ende ahora con scapy en nuestro script construiremos un paquete IP con este payload del paquete que ya tenemos, bastará con utilizar el método **IP** de scapy y como argumento pasarle el payload del paquete:

![[Offensive/dns_spoofer/images/011.PNG]]

Este paquete, si deseamos, podremos mostrarlo posteriormente con un print y veriamos algo así:

![[Offensive/dns_spoofer/images/012.PNG]]

Como vemos, capturamos bastantes paquetes, incluyendo el de **hack4u.io** después de hacerle un ping desde nuestra máquina. Como podremos ver, capturamos distintos tipos de paquetes y no todos nos interesan, pero si vemos el del dominio **hack4u.io** veremos cómo tiene la estructura que vimos anteriormente. Una capa **IP**, después una capa **UDP** que se encuentra encapsulada en la IP y finalmente una capa **DNS** encapsulada en la capa UDP. 

Con esto en mente, ahora, como vemos que estamos recibiendo muchos paquetes, filtraremos únicamente por aquellos que contengan la capa **DNSRR** que corresponde a la respuesta que nos da el servidor de la resolución DNS. 

Con ello, teniendo únicamente aquellos que son la respuesta de una resolución DNS, vamos a extraer el nombre del dominio el cual se encuentra en el atributo **qname** dentro de la capa de solicitud **DNSQR**, a pesar de filtrar primeramente por la capa de respuesta **DNSRR** se encontrara en el paquete la capa **DNSQR**, ya que, todo paquete con una respuesta cuenta con su capa de solicitud.

![[Offensive/dns_spoofer/images/013.PNG]]

Con ello estaríamos recuperando el dominio al que se está intentando acceder en bytes. En este caso nos enfocaremos en modificar el paquete cuando se intente acceder a **hack4u.io**, por ende verificaremos si **hack4u.io** se encuentra dentro del nombre de nuestro dominio.

![[Offensive/dns_spoofer/images/014.PNG]]

De esta manera, al ejecutar el script, veremos el mensaje únicamente cuando se intente hacer una resolución DNS para este dominio:

![[Offensive/dns_spoofer/images/015.PNG]]

Recordemos que en un paquete IP, lo que viaja como respuesta, en este caso, es **DNSRR** por lo que nosotros con scapy tendremos que construir un paquete **DNSRR** que a nivel de **rrname** siga teniendo el mismo nombre de dominio, pero a nivel de **rdata** que ahora tenga nuestra IP privada.

![[Offensive/dns_spoofer/images/016.PNG]]

Con ello estamos construyendo un nuevo paquete, pero aún no estamos modificando el paquete actual, por ende tendremos que asignar esta respuesta a la capa **DNS** de nuestro paquete, esta capa almacena las respuestas en **an**, por ende tendríamos que igualar **an** de la capa DNS a nuestro paquete **DNSRR** que acabamos de construir:

![[Offensive/dns_spoofer/images/017.PNG]]

Esto ya habrá cambiado esta parte, pero aún fallará la parte del atributo **ancount**, ya que, recordemos que este almacena el número de respuestas que son enviadas y tiene que coincidir, por lo tanto, al nosotros construir únicamente una respuesta tendremos que cambiar este valor a 1:

![[Offensive/dns_spoofer/images/018.PNG]]

Con esto, si ahora imprimiéramos el **scapy_packet** de forma detallada con **show()** veremos cómo se verá reflejado lo que hemos modificado:

![[Offensive/dns_spoofer/images/019.PNG]]

Por ende esto ya lo tenemos, pero aún falta lo que sería el atributo **len** y **chksum** de las capas **IP** y **UDP** que recordemos que son las que se encargan de verificar la integridad del paquete para verificar que no haya sido modificado, pero en este caso las eliminaremos utilizando **DEL**:

![[Offensive/dns_spoofer/images/020.PNG]]

Si ahora nosotros quisiéramos mostrar el paquete y ejecutáramos el script, veríamos como al hacerse una resolución DNS este dominio, justamente los atributos **len** y **chksum** de estas capas estarían en None, lo cual evitaría que se verificara la integridad del paquete y, por lo tanto, nuestro paquete no sería descartado. 

Recordemos que en un inicio teníamos todo el paquete que recuperamos de la NFQUEUE en formato bytes y lo recuperamos como algo que podríamos modificar con scapy construyendo con ello un paquete IP. Ahora con scapy podremos utilizar **build()** para este paquete, regresarlo a su formato de bytes y después esto sería algo que con **set_payload()** ya podríamos pasar directamente al paquete original de la NFQUEUE para modificarlo:

![[Offensive/dns_spoofer/images/021.PNG]]

Si nosotros deseáramos imprimir el propio scapy_packet.build(), veremos que tendrá exactamente el mismo formato que cuando mostramos al inicio el paquete original recién recuperado de la NFQUEUE. 

Con esto listo, habremos modificado totalmente el paquete de la resolución DNS, por ende si ahora ejecutamos nuestro script y volemos a hacer un ping a **hack4u.io** veremos cuál será la IP que nos muestre:

![[Offensive/dns_spoofer/images/022.PNG]]

Ahora vemos cómo la IP que nos está resolviendo es la IP nuestra que tenemos privada dentro de la red. 

Por ende, si ahora nosotros crearíamos un archivo **index.html** y dentro colocaríamos un texto simple como **H4cked! :D** y ejecutaríamos un servidor HTTP mediante Python por el puerto 80 con el comando:

```python3
python3 -m http.server 80
```

Al hacer un curl desde nuestra máquina, como un servidor HTTP, lo primero que busca mostrar es un archivo index.html nos retornara el contenido del mismo:

![[Offensive/dns_spoofer/images/023.PNG]]

Con esto construido si además hiciéramos el arp spoofing contra nuestra máquina víctima, al interceptar también sus paquetes si él accede desde el navegador a **hack4u.io** estaríamos modificando este paquete y haciendo que su resolución DNS sea hacia nosotros como atacantes y veremos como en el navegador nos mostrara nuestro archivo index.html:

![[Offensive/dns_spoofer/images/024.PNG]]

## Siguientes apuntes

[[Creando un Manipulador e Interceptor de Tráfico (Traffic Hijacking)]]