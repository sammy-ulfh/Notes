# Apuntes anteriores

[[TIPS de subnetting y cálculo veloz de direccionamiento en redes]]

# Indice

- [[#Introduccion]]
- [[#Escaneo de puertos en el router]]
- [[#Escaneo de los dispositivos conectados a la red local]]
- [[#Siguientes apuntes]]

## Introducción

**Nmap** es una herramienta de **escaneo de red** gratuita y de código abierto que se utiliza en pruebas de penetración (pentesting) para explorar y auditar redes y sistemas informáticos. 

Con Nmap, los profesionales de seguridad pueden identificar los **hosts** conectados a una red, los **servicios** que se están ejecutando en ellos y las vulnerabilidades que podrían ser explotadas por un ataque. La herramienta es capaz de detectar una amplia gama de dispositivos, incluyendo enrutadores, servidores web, impresoras, cámaras IP, sistemas operativos y otros dispositivos conectados a una red.

Asimismo, esta herramienta posee una variedad de funciones y características avanzadas que permiten a los profesionales de seguridad adaptar la misma a sus necesidades específicas. Estas incluyen técnicas de escaneo agresivas, capacidades de scripting personalizadas, y un conjunto de herramientas auxiliares que pueden ser utilizadas para obtener información adicional sobre los hosts objetivos.
## Escaneo de puertos en el router

Para ello necesitaremos saber el **Gateway** lo cual es la IP asignada a nuestro router. Para ello utilizaremos el comando **route -n** y con la IP que nos de en el Gateway podremos realizar nuestro escaneo.

```shell
route -n
```

![[Reconocimiento/images/001.png]]

Con esto ya podríamos iniciar un escaneo sobre nuestro router de internet, para ello utilizaremos la herramienta **nmap**:

```shell
nmap -p- 10.43.87.254
```

Con lo anterior, estaríamos realizando un escaneo a todos los puertos existentes para verificar cuáles se reconocen. Para el escaneo de puertos podemos seleccionar puertos específicos colocándolos como **-p22,23,8080** separados por comas. En este caso, al reemplazar el puerto específico por **-**, estaríamos indicando que nos realice un escaneo de todos los puertos, que en total existen **65535**. 

Además, por defecto, los escaneos siempre se estarán haciendo para todos aquellos servicios que se encuentren corriendo por el protocolo TCP.

![[Reconocimiento/images/002.png]]

En este caso, el escaneo nos retornó solo dos puertos, los cuales se encuentran abiertos, pero también podrá retornarnos puertos filtrados o incluso de algunos servicios que se encuentran cerrados. 

Cuando realicemos un escaneo, lo esperado será únicamente visualizar aquellos que se encuentren abiertos, por ende podemos agregar delante de la indicación del escaneo a los puertos, que nos muestre únicamente los abiertos con **--open**:

```shell
nmap -p- --open 10.43.87.254
```

![[Reconocimiento/images/003.png]]

Lo anterior nos realizará el escaneo y al final nos mostrará los resultados. Si queremos ver en tiempo real lo que está sucediendo, podremos indicar el parámetro verbose que es para verlo, lo cual indicamos con **-v**:

```shell
nmap -p- --open 10.43.87.254 -v
```

Usualmente, se aplica la resolución de DNS, lo cual trata de hacer match de una IP con su dominio. Si queremos evitar que esto se aplique y agilizar más el proceso, utilizaríamos el parámetro **-n**:

```shell
nmap -p- --open 10.43.87.254 -v -n
```

Adicionalmente, cuando nosotros realizamos un escaneo primero se realiza una verificación para ver si esta IP o host se encuentra activo, pero podremos evitar esto utilizando el parámetro **-Pn**, lo cual nos ayuda a automáticamente considerar que está activo y evitar que se realice la verificación, lo cual también puede ayudarnos a agilizar el proceso:

```shell
nmap -p- --open 10.43.87.254 -v -n -Pn
```

También tenemos el parámetro **-T**, al cual le asignamos a un lado un número en el rango del 0-5, los cuales son formas en las cuales se puede llevar el escaneo para hacer en un menor o mayor tiempo, siendo 0 el más lento y 5 el más rápido. 

Los tiempos de escaneo se clasifican de la siguiente manera:

| Name       | parameter |
| ---------- | --------- |
| Paranoid   | -T0       |
| Sneaky     | -T1       |
| Polite     | -T2       |
| Normal     | -T3       |
| Aggressive | -T4       |
| Insane     | -T5       |

**-T3** es el modo que se encuentra por defecto, por lo tanto, si lo aplicamos no tendríamos diferencias. 

Entre más rápido sea un escaneo, puede ser más ruidoso y ser detectado.

```shell
nmap -p- --open -T5 10.43.87.254 -v -n -Pn
```

Al ejecutarlo, ya podríamos observar claramente cómo se realiza el escaneo de una forma mucho más rápida, en este caso, al utilizar el modo de tiempo **insane**. 

Como anteriormente se mencionó, **nmap** realiza el escaneo por defecto para encontrar puertos que se encuentren corriendo por el protocolo TCP, pero esto es algo que podemos indicar con el parámetro **-s**, agregando **T** si queremos realizar el escaneo para **TCP**:

```shell
nmap -p- --open -T5 -sT 10.43.87.254 -v -n -Pn
```

![[Reconocimiento/images/004.png]]

Si queremos que este escaneo se realice para servicios que están corriendo utilizando el protocolo **UDP**, cambiaríamos la T por **U**:

```shell
nmap -p- --open -T5 -sU 10.43.87.254 -v -n -Pn
```

![[Reconocimiento/images/005.png]]

## Escaneo de los dispositivos conectados a la red local

Para escanear la red local, utilizaremos el comando **arp-scan** y utilizaremos el parametro **-I** para indicar la tarjeta de red de nuestro dispositivo desde la cual estamos conectados a la red.

En este caso, utilizaremos **iwconfig** para ver cual es la que estamos utilizando:

![[Reconocimiento/images/006.png]]

En este caso la que tenemos es **wlan0** y la que indicaremos al realizar el escaneo:

```shell
arp-scan -I wlan0
```

Finalmente, indicaremos que realizaremos el escaneo en una red local:

```shell
arp-scan -I wlan0 --localnet
```

Teniendo como resultado las IP de los dispositivos conectados:

![[Reconocimiento/images/007.png]]

Ademas, esto tambien podremos realizarlo con **nmap** utilizando los parametros **-sn** de la siguiente manera, con la IP de la red o subred en la que nos encontremos y la bitmask:

```shell
nmap -sn 10.43.80.1/21
```

Esto nos dara las IP con un formato como el siguiente:

![[Reconocimiento/images/008.png]]

Si queremos tener solamente las IP podremos filtrar el output con **grep** y **regex** para indicar el formato de la IP:

```shell
nmap -sn 10.43.80.1/21 | grep -o -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
```

En este caso, el parametro **-o** se utiliza para que se impriman solamente aquellas coincidencias con la expresion regular y el parametro **-E** para habilitas las expresiones regulares y esta sea reconocida.

Teniendo como resultado colamente las direcciones IP:

![[Reconocimiento/images/009.png]]

## Siguientes apuntes

[[Técnicas de evasión de Firewalls]]
