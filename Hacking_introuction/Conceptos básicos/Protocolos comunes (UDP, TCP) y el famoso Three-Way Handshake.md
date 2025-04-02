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
- 23: **Telnet** - un protocolo utilizado para la conexión remota a dispositivos de red
- 80: **HTTP** (Hypertext Transfer Protocol) - el protocolo se utiliza para la transferencia de datos en la World Wide Web
- 443: **HTTPS** (Hypertext Transfer Protocol Secure) - la versión segura de HTTP, que utiliza la encriptación SSL/TLS para proteger las comunicaciones web

#### Puertos UDP comunes

- 53: **DNS** (Domain Name System) - un sistema que se traduce con dominio en direcciones IP
- 67/68: **DHCP** (Dynamic Host Configuration Protocol) - un protocolo utilizado para asignar direcciones IP y otros parámetros de configuración a los dispositivos en una red
- 69: **TFTP** (Trivial File Transfer Protocol) - un protocolo simple utilizado para transferir archivos entre dispositivos de una red
- 123: **NTP** (Network Time Protocol) - un protocolo utilizado para sincronizar los relojes de dispositivos en una red
- 161: **SNMP** (Single Network Management Protocol) - un protocolo utilizado para administrar y supervisar dispositivos en una red

Es importante destacar que estos son **algunos de los más comunes**. Existen muchos mas puertos en los cuales operan tanto pot TCP como por UDP.

## Práctica

