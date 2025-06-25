# Introduccion

Crearemos un envenenador ARP (ARP Spoofer) utilizando Scapy, una herramienta esencial en Python para el análisis y manipulación de paquetes de red. El ARP Spoofing es una técnica de ataque en redes, donde el atacante envía mensajes ARP falsificados en una red local. Esto se hace para asociar la dirección MAC del atacante con la dirección IP de otro dispositivo, como un servidor o un gateway, lo que permite al atacante interceptar el tráfico entre dos sistemas.

![[Offensive/arp_spoofer/images/001.png]]

El concepto de **Man-In-The-Middle** (MITM) es crucial aquí, ya que el atacante se posiciona estratégicamente entre dos partes para interceptar o modificar el tráfico de datos, una táctica común en ataques cibernéticos. Esta técnica es posible debido a la naturaleza de confianza del protocolo ARP, que no verifica si las respuestas a las solicitudes ARP son legítimas.

Lo cual nos permite, por un lado, decirle al modem que la IP **192.168.1.65** se encuentra asociada a la Mac Address de nuestra máquina como atacantes, mientras que a la máquina con dicha IP le diremos que la IP 192.168.1.1 se encuentra asociada a nuestra Mac Address.

![[Offensive/arp_spoofer/images/002.png]]

Interceptando el tráfico para que ambas partes tengan que pasar por mí máquina antes de llegar al destino.

# Practica

En nuestro ordenador de atacante tendremos que hacer una pequeña modificación en las **iptables** para permitir recibir y enviar de vuelta peticiones. 

Para permitir recibir solicitudes entrantes, vamos a utilizar como administrador:

```shell
iptables --policy FORWARD ACCEPT
```

Para comunicarnos de vuelta al destino sin problemas, tendremos que meter el valor **1** en el archivo **/proc/sys/net/ipv4/ip_forward**. 

Ambas cosas nos permiten recibir y enviar de vuelta las peticiones, para que así el target pueda navegar sin perder su conexión a internet.

![[Offensive/arp_spoofer/images/003.png]]

## arp_spoofer

Crearemos nuestro archivo arp_spoofer y comenzaremos creando nuestro menú con **argparse** el cual tendrá los argumentos **target** que sería una IP o rango de IP's, así como el argumento **i** para indicar la interfaz de red.

![[Offensive/arp_spoofer/images/004.png]]

Con esto listo, crearíamos una función **spoof** la cual recibirá como argumentos la IP target y la IP por la que nos haremos pasar, que será la del router. Aquí ya ocuparemos de la librería scapy. 

En el caso anterior, nosotros enviamos una solicitud con el escaneo ARP, donde preguntamos a quién correspondía cierta IP. En este caso, en lugar de solicitud, vamos a crear un paquete ARP de respuesta, donde dirá algo en lugar de preguntarlo. 

Para ello, empezamos colocando el argumento **op** con el valor 2, que es el equivalente a indicar que es un paquete de respuesta. 

Este paquete será una respuesta que tendrá como destino a nuestro target, como si el propio router le estuviese indicando cuál es su dirección Mac, que realmente será la nuestra como atacante:

![[Offensive/arp_spoofer/images/005.png]]

En este caso, con **psrc** estamos indicándole al paquete "de dónde es enviado" y con **pdst** indicamos a dónde tiene que ir, en este caso, a nuestro target. Además, con **hwsrc** indicamos la Mac Address de nosotros como atacantes. En este caso, le estaríamos diciendo a nuestro target que nosotros, como "router" tenemos esta dirección Mac, y le indicamos la nuestra para que así se comunique con nosotros. 

Anteriormente, utilizamos **srp (send receive packet)** al realizar el escaneo ARP para enviar y recibir paquetes. En este caso, al solo querer enviar el paquete ARP a nuestro target y no recibir, utilizaremos **send** colocando como argumento el paquete arp.

![[Offensive/arp_spoofer/images/006.png]]

Sí, nos da warnigs al utilizar **send**, utilizamos **sendp** 

Aquí nos aprovechamos de la misma función para hacer lo mismo para el router, de esta manera indicamos a ambos que la Mac Address a la que se tienen que comunicar es la mía como atacante. 

El enviar estos paquetes tendrá que ser de forma constante, ya que la tabla del router y del dispositivo target actualizarán sus tablas con la constante comunicación que existe donde se preguntan cuál es su dirección, esto lo haremos con un bucle while con un delay de tiempo para no sobrecargar de paquetes enviados:

![[Offensive/arp_spoofer/images/007.png]]

Con esto ya nos encontraríamos en un modo de ataque como Man-In-The-Middle, por lo que si nos abriéramos Wireshark y nos usaríamos en escucha en nuestra interfaz de red filtrado por **dns**:

![[Offensive/arp_spoofer/images/008.png]]

Si ahora desde nuestro dispositivo target nos abriéramos **hack4u.io** en el navegador, podríamos ver cómo interceptamos este tráfico. 

Si no llegamos a ver el tráfico, es porque se llegó a implementar **DNS over HTTPS** que es básicamente una medida de seguridad que hace más privadas las consultas DNS ocultándolas dentro de una petición HTTPS cifrada. 

De ser el caso, tendríamos que ir a la configuración de conectividad de nuestro dispositivo target y cambiar la configuración del DNS de forma manual y colocar **8.8.8.8**.
## Siguientes apuntes

[[]]