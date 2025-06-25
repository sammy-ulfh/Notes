## Introduccion

En ICMP se realiza un escaneo que da como resultado una lista de IP's activas, pero esto puede llegar a ser detectado y bloqueado por el Firewall de los propios dispositivos, por ende tenemos ARP como alternativa para poder llegar a listar dispositivos activos. 

ARP viene de **Address Resolution Protocol**, siendo un protocolo de resolución de direcciones. Este es un protocolo de comunicarnos a nivel de la capa de enlace de datos y es responsable de encontrar la dirección de hardware que corresponde a una dirección IP determinada. 

Es realmente una forma de mapear la dirección MAC para una dirección IP determinada.

La forma en la que funciona es, imaginando que estamos en la misma red conectados 50 dispositivos, cada uno corresponde a un nombre específico. 

Tenemos la IP **192.168.100.1** para **Joseph Doe** y preguntamos de forma general "¿Oye, quién es Joseph Doe cuya IP es la 192.168.100.1?". 

Esta sería una pregunta que estaríamos comunicando a todos los dispositivos en la red, de tal forma que solo nos respondería el dispositivo cuya IP sea la dada con "Yo soy Joseph Doe, puedes digirite a mí como XX:XX:XX:XX:XX:XX". 

De esta forma resumiríamos la forma en la que buscamos mapear la dirección de hardware para una IP dada de un dispositivo.

**Scapy**

Para ello estaremos utilizando scapy, que es una herramienta de manipulación de paquetes. Con ella es posible falsificar o decodificar paquetes, que es cuando entra en juego la parte de envenenamiento ARP, enviándolos por cable, capturándolos y uniendo solicitudes y respuestas.
## **Practica**

Comenzaríamos creando un script **arp_scanner.py**, como utilizaremos scapy, para poder tener en su totalidad las funcionalidades que nos ofrece, lo importaremos como:

```python3
import scapy.all as scapy
```

De esta forma nos aseguramos de que estamos importando las funcionalidades de scapy en su totalidad para emplearlas de la forma que deseemos. 

De la misma forma en la que lo hemos hecho, crearemos nuestro menú con **argparse** esperando el argumento **target**:

![[Offensive/ARP_scanner/images/001.png]]

Con esto ahora, de forma sencilla, crearemos una función **scan** y le pasaremos el target. Este tendrá que ser una IP individual o un rango. Indicando la bitmask, utilizando **arpnig** de scapy y pasándole como argumento el target y la interfaz de red, nos dará los resultados del escaneo:

![[Offensive/ARP_scanner/images/002.png]]

![[Offensive/ARP_scanner/images/004.png]]
![[Offensive/ARP_scanner/images/003.png]]

Siendo esta la forma sencilla de hacerlo, donde se envían los paquetes y nos responde con la dirección MAC de los dispositivos. 

Ya después conviene más hacerlo de forma un poco más compleja, donde nosotros tenemos el control de los paquetes que se envían para poder engañar a nivel de red e incluso hacer envenenamiento.

### Wireshark

Para visualizar los paquetes que se están enviando, utilizaremos Wireshark, el cual podremos abrir con:

```shell
wireshark &> /dev/null & disown
```

Aquí seleccionaremos nuestra interfaz de res, en mi caso, es la **wlan0**. 

Estando en nuestra interfaz, aplicaremos un filtro el cual es **arp and eth.src == ac:d5:64:2d:00:e3**, de esta manera le estamos diciendo a Wireshark que queremos ver únicamente los paquetes ARP y que tengan como dirección MAC de origen la mía, indicando que este dispositivo es el que esté tramitando los paquetes:

![[Offensive/ARP_scanner/images/005.png]]
Con el filtro aplicado, para ver de forma más clara estos paquetes, vamos a limpiar los que actualmente se encuentran que se han tramitado por detrás. Esto lo haremos presionando el icono verde, que se encuentra al lado derecho del rojo, indicando que queremos continuar sin guardar. 

Ahora ejecutaremos nuestro script, haciéndolo hacia la IP de nuestro router:

![[Offensive/ARP_scanner/images/006.png]]

Para evitar seguir observando nuevo tráfico, le damos al botón rojo y estaríamos pausando la escucha constante. 

Aquí podremos ver como nos vamos hacia la dirección Broadcast, que es básicamente comunicarnos de forma directa a todos los dispositivos de la red, preguntando quién tiene la IP **192.168.100.1**, esto lo podemos ver del lado derecho, donde pregunta quién tiene la IP 192.168.100.1 y después está la IP de quien lo está preguntando.

En la parte inferior en Wireshark podremos observar cómo el paquete enviado tiene dos capas principales, una Ethernet que es la más externa y una arp que es la más interna:

![[Offensive/ARP_scanner/images/007.png]]

De la forma en la que está compuesto, veremos que la trama ARP (Adress Resolution Protocol) presenta un encapsulamiento dentro de la trama Ethernet.

![[Offensive/ARP_scanner/images/008.png]]

Teniendo esto en consideración, si queremos tener mayor control en un escaneo por ARP, nosotros, a nivel de paquete, tendremos que crearlo, generando una trama Ethernet y luego una ARP para luego unirlas y poder tramitar el paquete para que sea un formato válido. 

La Ethernet es necesaria para poder enviar nuestros paquetes a nivel de red física. Con ello debemos tener en consideración que la trama Ethernet como destino considera la Broadcast, mientras que la trama ARP la IP sobre la que estamos preguntando (el target). 

Teniendo esto en consideración, construiremos ambas tramas y el paquete en nuestro script. 

Primeramente, la trama ARP. Para ello utilizamos el método **ARP** de scapy y, a nivel de argumentos, le pasaremos la IP o rango de IP's de destino con **pdst** (protocol destination) y lo almacenaremos en una variable arp_packet. 

Para la trama Ethernet utilizaremos el método **Ether** y le pasaremos como argumento la MAC Address del Broadcast con **dst**:

![[Offensive/ARP_scanner/images/009.png]]

Finalmente, uniríamos ambas tramas para formar un paquete válido, colocando la trama arp debajo de la trama eher con el operador **/**. Esto podría dar confunciones, ya que es el operador de división, pero a nivel de protocolos se utiliza para unificar tramas, por lo que no se está haciendo ningún tipo de división. 

Finalmente, enviaríamos el paquete utilizando el método **srp**. A nivel de argumentos, primeramente le pasaremos el paquete, después le indicaremos un time out para que no demore en algunos que no respondan y asignaremos **False** al atributo verbose para no ver en todo momento el escaneo. Recibiremos dos resultados, los que han respondido y los que no, por lo que podemos recibirlos por separado:

![[Offensive/ARP_scanner/images/010.png]]

Finalmente, si queremos ver bien los resultados, podremos extraer un sumario de los que respondan, en este caso haciéndolo con un rango de IP's:

![[Offensive/ARP_scanner/images/011.png]]

Esto es lo mismo que visualizamos en Wireshark. Si nos ponemos en escucha y observamos nuevamente el tráfico al ejecutar el script, veremos cómo obtenemos lo mismo, donde preguntamos quién tiene ciertas IP's.

## Siguientes apuntes

[[Creando un envenenador ARP (ARP Spoofer) con Scapy]]