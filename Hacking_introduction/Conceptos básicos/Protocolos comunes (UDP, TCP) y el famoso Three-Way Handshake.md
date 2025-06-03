# Apuntes anteriores

- [[Direcciones MAC (OUI y NIC)]]

# Índice

- [[#Introducción]]
	- [[#Protocolos de transmisión]]
	- [[#Puertos TCP comunes]]
	- [[#Puertos UDP comunes]]
- [[#Práctica]]

## Introducción

### Protocolos de transmisión

Los protocolos **TCP** (Transmission Control Protocol) y **UDP** (User Datagram Protocol) son dos de los protocolos de red más comunes utilizados en la transferencia de datos a través de redes de ordenadores.

El protocolo **TCP** es un protocolo orientado a la conexión que proporciona una entrega de datos confiable, mientras que el protocolo **UDP**, es un protocolo *orientado a conexión* el cual no garantiza la entrega de datos.

Una parte crucial del protocolo **TCP** es el **Three\-Way Handshake**, un procedimiento utilizado para establecer una conexión entre dos dispositivos. Este procedimiento consta de tres pasos: **SYN**, **SYN-ACK**, **ACK**, en los que se sincronizan los números de secuencia y de reconocimiento de paquetes entre los dispositivos. El Three-Way Handshake es fundamental para establecer una conexión confiable y segura a través de TCP.

#### Puertos TCP comunes:

- 21: **FTP** (File Transfer Protocol) - permite la transferencia de archivos entre sistemas
- 22: **SSH** (Secure Shell) - un protocolo de red seguro que permite a los usuarios conectarse y administrar sistemas de forma remota
- 23: **Telnet** - un protocolo utilizado para la conexión remota a dispositivos de red, para manejarlos como si estuviesemos delante de ellos
- 25: **SMTP** (Simple Mail Transfer Protocol) - Un protocolo que se utiliza para la transferencia de correos
- 80: **HTTP** (Hypertext Transfer Protocol) - el protocolo se utiliza para la transferencia de datos en la World Wide Web
- 110: **POP3** (Post Office Protocol) - Protocolo para la gestion de correos sin cifrado
- 995: **POP3** (Post Office Protocol) - Protocolo para la gestion de correos cifrado
- 443: **HTTPS** (Hypertext Transfer Protocol Secure) - la versión segura de HTTP, que utiliza la encriptación SSL/TLS para proteger las comunicaciones web
- 139, 445: **SMB** (Server Message Protocol) - Protocolo utilizado principalmente en empresas, permiten el acceso compartido entre dispositivos
- 143: **IMAP** (Internet Message Active Protocol) - Se utiliza para clientes que reciben mensajes d eun servidor de email
 
#### Puertos UDP comunes

- 53: **DNS** (Domain Name System) - un sistema que se traduce con dominio en direcciones IP
- 67/68: **DHCP** (Dynamic Host Configuration Protocol) - un protocolo utilizado para asignar direcciones IP y otros parámetros de configuración a los dispositivos en una red
- 69: **TFTP** (Trivial File Transfer Protocol) - un protocolo simple utilizado para transferir archivos entre dispositivos de una red
- 123: **NTP** (Network Time Protocol) - un protocolo utilizado para sincronizar los relojes de dispositivos en una red
- 161: **SNMP** (Single Network Management Protocol) - un protocolo utilizado para administrar y supervisar dispositivos en una red

Es importante destacar que estos son **algunos de los más comunes**. Existen muchos mas puertos en los cuales operan tanto por TCP como por UDP.

## Práctica

TCP -> Protocolo orientado a conexión, garantizando la entrega de todos los datos en el orden en que fueron enviados.
UDP -> Protocolo no orientado a conexión, no garantiza la entrega completa de los datos.

### **Three-Way Handshake**

Esto se aplica directamente en el protocolo TCP, ya que es la forma en la que se entablan las conexiones, donde vemos una comunicación la cual mostramos con **SYN**, **SYN-ACK**, **ACK**.

Ahora, abriendo wireshark como usuario root:

```SHELL
wireshark & disown &> /dev/null
```

Monitorizaremos **Loopback**, dando doble click:

![[010.png]]

Ahora nos pondremos en escucha con netcat, por el puerto 4646, por el momento aun seguiremos sin visualizar nada en wireshark:

```Shell
nc -nlvp 4646
```

Ahora nos conectamos con netcat a nuestro mismo equipo y al puerto que hemos abierto con netcat:

```Shell
nc localhost 4646
```

![[011.png]]

Una vez que tenemos la conexión establecida, si nos enfocamos en los utlimos 3, veremos justamente lo del Three-Way Handshake:

![[012.png]]

Este principio lo veremos en cualquier conexión que se establesca por TCP, ya que consta de 3 pasos en los que, primero se da una comunicación donde tu le hablas a ese puerto especifico (SYN), si recibes respuesta es que esta abierto (SYN-ACK) y finalmente se establece la conexión (ACK).

## **Siguientes apuntes**

[[Modelo OSI]]



