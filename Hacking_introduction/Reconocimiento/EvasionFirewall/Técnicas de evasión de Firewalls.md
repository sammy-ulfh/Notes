# Técnicas de evasión de Firewalls (MTU, Data Length, Source Port, Decoy, etc.)


# Apuntes anteriores

[[Nmap y sus diferentes modos de escaneo]]

# Indice

- [[#Introduccion]]
- [[#Fragmentacion de paquetes -f]]
- [[#MTU]]
- [[#Cloak a scan with decoys]]
- [[#Puerto de origen]]
- [[#Data length]]
- [[#Spoof Mac]]
- [[#Self Scan]]
- [[#Min rate && Max rate]]
- [[#Siguientes apuntes]]
## Introduccion

Cuando se realizan pruebas de penetración, uno de los mayores desafíos es evadir la detección de los **Firewalls**, que son diseñados para proteger las redes y sistemas de posibles amenazas. Para superar este obstáculo, Nmap ofrece una variedad de técnicas de evasión que permiten a los profesionales de seguridad realizar escaneos sigilosos y evitar así la detección de los mismos.

Algunos de los parámetros que se veran son los siguientes:

- **MTU (-mtu):** La técnica de evasión de **MTU** o **Maximum  Transmission Unit** implica ajustar el tamaño de los paquetes que se envían para evitar la detección por parte del Firewall. Nmap permite configurar manualmente el tamaño máximo de los paquetes para garantizar que sean lo suficientemente pequeños para pasar por el Firewall sin ser detectados.
- **Data Length (-data-length):** La técnica se basa en ajustar la **longitud de datos** enviados para que sean lo suficientemente cortos como para pasar por el Firewall sin ser detectados. Nmap permite a los usuarios configurar manualmente la longitud de datos enviados para que sean lo suficientemente pequeños para evadir la detección del Firewall.
- **Source Port (-source-port):** Esta técnica consiste en configurar manualmente el número de **puerto origen** de los paquetes enviados para evitar la detección por parte del Firewall. Nmap permite a los usuarios especificar manualmente un puerto de origen aleatorio o un puerto específico para evadir la detección del Firewall.
- **Decoy (-D):** Esta técnica de evasión en Nmap permite al usuario enviar **paquetes falsos** a la red para confundir a los sistemas de detección de intrusos y evitar la detección del Firewall. El comando **-D** Permite al usuario enviar paquetes falsos junto con los paquetes reales de escaneo para ocultar su actividad.
- **Fragmented (-f):** Esta técnica se basa en **fragmentar los paquetes** enviados para que el Firewall no pueda reconocer el tráfico como un escaneo. La opción **-f** en Nmap permite fragmentar los paquetes  y enviarlos por separado para evitar la detección del Firewall.
- **Spoff-Mac (-spoof-mac):** Esta técnica de evasión se basa en **cambiar la dirección MAC** del paquete para evitar la detección del Firewall. Nmap permite al usuario configurar manualmente la dirección MAC para evitar ser detectado por el Firewall.
- **Stealth Scan (-sS):** Estan técnica es una de las más utilizadas para realizar escaneos sigilosos y evitar la detección del Firewall. El comando **-sS** permite a los usuarios realizar un escaneo de tipo **SYN sin estableces una conexión completa**, lo que permite evitar la detección del FIrewall.
- **min-rate (--min-rate):** Esta técnica permite al usuario **controlar la velocidad de los paquetes** enviados para evitar la detección del Firewall. El comando **--min-rate** permite al usuario reducir la velocidad de los paquetes enviados para evitar ser detectado por el FIrewall.

Es importantes mencionar que, además de las técnicas de evasión mencionadas anteriormente, existen muchas otras opciones en Nmap  que pueden ser utilizadas para realizar pruebas de penetración efectivas  y evadir la detección del Firewall. Sin embargo, las técnicas que hemos mencionado son algunas de las más populares y ampliamente utilizadas por los profesionales de seguridad para superar los obstáculos que presentan los Firewalls en la realización de pruebas de penetración.

## Fragmentacion de paquetes **-f**

Con Nmap podremos realizar escaneos que nos permitirán poder detectar de forma correcta aquellos puertos que se encuentren abiertos, pero el Firewall evite que puedamos detectarlos. 

Por ello podremos realizar un escaneo, en este caso al puerto 22 del router, para verificar que detecta si fragmentamos los paquetes:

```shell
nmap -p22 10.43.87.254 -f
```

![[Reconocimiento/EvasionFirewall/images/001.png]]

A simple vista no notaremos ninguna diferencia, pero podremos utilizar **tcpdump** justo antes del escaneo para capturar el tráfico y después abrirlo con **wireshark**. Esto se hace capturando el tráfico de la tarjeta de red que está conectada al internet, esta la podremos ver haciendo un **ifconfig**. 

Entonces la colocamos con el parámetro **-i** el nombre de nuestra tarjeta de red, asi como con el parámetro **-w** el nombre del archivo que se creará para almacenar los archivos y finalmente el parámetro **-v** de verbose para ver como va trabajando:

```shell
tcpdump -i wlan0 -w Captura.cap -v
```

![[Reconocimiento/EvasionFirewall/images/002.png]]

Finalmente, abrimos el archivo con **Wireshark**:

```shell
wireshark Captura.cap &> /dev/null & disown
```

![[Reconocimiento/EvasionFirewall/images/003.png]]

En la parte superior podemos filtrar el contenido capturado, en este caso con **ip.flags.mf == 0**, si está en 1, filtramos por el tráfico fragmentado y si está en cero por el tráfico que no ha sido fragmentado. 

Realizaremos un filtrado para observar solamente el tráfico fragmentado. Si vemos que no nos captura tráfico fragmentado, intentemos realizar un escaneo mucho más grande, como hacía todos los puertos en general, para que aseguremos que se capturen. 

Al filtrarlo, veríamos el tráfico de la siguiente manera:

![[Reconocimiento/EvasionFirewall/images/004.png]]

![[Reconocimiento/EvasionFirewall/images/005.png]]

Viendo los primeros dos, podremos irnos a la parte inferior y seleccionar **Data** del lado izquierdo. Aquí veremos cómo esta la información en hexadecimal transmitiéndose:

![[Reconocimiento/EvasionFirewall/images/006.png]]

En la parte superior, si observamos bien, los primeros dos nos mencionan que son reensamblados en la traza #11. Esto podremos observarlo bien si quitamos el filtro que habíamos colocado y nos vamos a la traza #11:

![[Reconocimiento/EvasionFirewall/images/007.png]]

El fragmentar un paquete nos da cierta seguridad de llegar a mostrar algunos puertos sin que el Firewall los oculte, esto se debe a que el Firewall espera ciertos tipos de paquetes específicos para evitarlos, al fragmentarlos lo que hacemos es dividir este paquete y al final el Firewall no detecta el tipo de paquete que está siendo enviado.

## MTU

Agregado a esto, podremos utilizar el **MTU (Maximum Transmission Unit)**. Esto puede ser de ayuda, ya que hay casos en los que el Firewall espera cantidades fijas en el tamaño de cada paquete y, si enviamos algunos de forma más pequeña, podrían no ser detectados y permitirnos llegar a visualizar puertos filtrados u ocultos hacia los escaneos detectados. 

**--mtu** ocupa un valor mayor a cero y siempre tiene que ser múltiplo de 8, de no ser asi nos lo dira el propio Nmap:

![[Reconocimiento/EvasionFirewall/images/008.PNG]]

Si nosotros quisiéramos listar las posibilidades que tenemos para evitar estas detecciones por parte de un Firewall o un sistema de detección IDS, podríamos utilizar la flag **--help** de nmap para mostrar las opciones que tenemos:

```shell
nmap --help
```

![[Reconocimiento/EvasionFirewall/images/009.PNG]]

Buscando específicamente por este apartado, veremos cómo tenemos la que recién hemos visto y ahora nos enfocaremos en el **-D**.
## Cloak a scan with decoys

Con ello podremos spoofear direcciones IP's al momento de realizar un escaneo. Nosotros, al realizar un escaneo, enviamos paquetes desde nuestra máquina que tiene una IP dada.

Los sistemas podrán tener algunos puertos en los cuales solo puedan ver ciertas IP's y nosotros, con **decoys** somos capaces de falsificar IP's que están enviando los paquetes. En este caso, si lo utilizamos con una IP y capturamos el tráfico:

![[Reconocimiento/EvasionFirewall/images/010.PNG]]

Con ello nos abrimos el archivo con wireshark y filtramos el puerto destino con **tcp.port \== 23**, con ello lo veríamos de la siguiente manera:

![[Reconocimiento/EvasionFirewall/images/011.PNG]]

Aquí vemos cómo, aunque la IP **192.168.100.200** que no existe para un dispositivo conectado en la red, ya que nos la hemos inventado, también envía un **SYN** a la máquina víctima. 

De esta manera, nosotros podríamos falsificar el hecho de que distintas direcciones IP envíen este paquete para verificar si algún puerto está abierto. Esto viene bien al hacerlo, por ejemplo, con una lista larga de IP, debido a que por reglas de los sitemas esten determinado que solo alguna IP específica pueda ver ciertos puertos. 

Por lo tanto, con ello podemos falsificar que distintas IP's envían el **SYN** y con ello llegar a ver puertos que solo puedan ver ciertas IP. Un escaneo con múltiples IP sería de la siguiente manera:

![[Reconocimiento/EvasionFirewall/images/012.PNG]]

Esto, al capturarlo y abrirlo con wireshark y esta vez filtrando por la IP que está tramitando estas solicitudes con **ip.dst \== 192.168.100.1** (IP de la máquina víctima), veremos lo siguiente:

![[Reconocimiento/EvasionFirewall/images/013.PNG]]

En este caso se tramitan bastantes solicitudes de diversas IP's que incluso podríamos evitar que el Firewall detecte cuál es la IP de la que realmente provienen estas solicitudes.

## Puerto de origen

Cuando nosotros tramitamos una solicitud de este tipo al realizar el escaneo, nuestra máquina tiene que abrir un puerto para tramitar esta solicitud. Para ello, generalmente se abre un puerto aleatorio y esto podremos verlo si lanzamos el siguiente escaneo y lo capturamos con wireshark:

```shell
nmap -p23 192.168.100.1 --open -T5 -v -n
```

Recordemos que estos escaneos son hechos siendo root y hacia nuestro router. Después de capturar el tráfico de este escaneo, lo abriremos con wireshark:

![[Reconocimiento/EvasionFirewall/images/014.PNG]]

En este caso, veremos cómo en el apartado de **info** tenemos el número **55686**. Este sería el puerto que se abrió de forma aleatoria para tramitar esta solicitud y verificar si el puerto se encuentra abierto. 

El puerto que abre nuestra máquina para tramitarla es algo que también podremos gestionar y puede venir bien en casos como que el Firewall tenga una lista blanca en la cual solo un puerto específico, como por ejemplo el 53, pueda viajar y tramitar correctamente la solicitud.

Esto lo haríamos con **--source-port 53**, de esta manera estaríamos indicando que realicé la petición mediante el puerto 53 y si volvemos a realizarla mientras capturamos el contenido con **tcpdump** y abrimos el archivo con wireshark, veremos cómo ahora la petición viaja desde nuestro puerto 53:

![[Reconocimiento/EvasionFirewall/images/015.PNG]]

## Data length

Cuando nosotros aplicamos un escaneo, los paquetes tienen un tamaño específico. En este caso, si vemos la imagen anterior en el apartado **Length** veremos cómo el tamaño del **SYN** es de 58. 

Esto puede ser conocido por el Firewall o IDS (Sistemas de detección de intrusión) para tenerlo en cuenta como que muy posiblemente se está aplicando un escaneo. Por ello, este es un valor que nosotros podremos modificar. 

El valor de **58** siempre lo tendrá de base nuestro paquete, pero si notros con **--data-length** agregamos **22**, ahora el tamaño de nuestro paquete será **80**. Si nosotros realizamos un escaneo sencillo a un puerto agregando un tamaño y capturamos con **tcpdump**, al abrirlo con wireshark lo veríamos de la siguiente manera:

```shell
nmap -p23 192.168.100.1 --data-length 22
```

![[Reconocimiento/EvasionFirewall/images/016.PNG]]

Con ello, veremos cómo el tamaño del paquete ahora es mayor. Todo esto viene bien, ya que, al modificarlo, podremos tener cosas distintas a lo que usualmente contempla un Firewall y esto puede ser de ayuda para extraer un poco más de información para un puerto que estemos enumerando.

## Spoof Mac

También podremos falsificar la dirección Mac con **--spoff-mac**. Podremos indicar una mac address totalmente inventada o, en su defecto, agregar palabras clave como **Dell** para que automáticamente nos agregue una Mac Adress que en sus primeros 3 bytes haga referencia a **Dell**:

![[Reconocimiento/EvasionFirewall/images/017.PNG]]

En este caso vemos cómo nos dice que el Host parece no estar activo. Esto lo haré porque, antes de realizar un escaneo, verifica que el Host esté activo y, si detecta que no es asi, no realizará el escaneo. 

Aquí es donde nosotros tenemos la opción **-Pn** que deshabilita la verificación enviando una traza ICMP, continuando directamente con el escaneo:

![[018.PNG]]

En este caso no nos reporta nada encontrado, debido a que aplicamos el spoof para la dirección Mac y el router no tiene esta dirección en su tabla de ruteo. Por ende, si quisiéramos que esto funcionase, tendríamos que cambiar la dirección Mac de nuestra máquina o, en su defecto, también desplegar un ARP Spoofing para que el router almacene en su tabla de ruteo dicha dirección MAC.

## Self Scan

responde, quiere decir que es un puerto filtrado por el Firewall y que no nos permite verlo. 

Con esto en mente, cuando recibimos una respuesta, si el puerto está abierto, respondemos con un **ACK**, entablando de cierta forma una pequeña conexión para concluir el escaneo para cada puerto y esto puede llegar a dejar rastros en la máquina víctima. 

Para ello tenemos un tipo de escaneo más sigiloso **-sS** (Self Scan), este sigue el mismo principio, pero cuando recibe respuesta, en lugar de responder con un **ACK**, responde con un **RST**. De esta forma no se permite que se establezca una conexión y esto usualmente no deja logs o rastro en la máquina víctima, ya que, los sistemas solo tienden a almacenar logs de conexiones que se hayan completado. 

Al realizar esto, además, el escaneo gana ciertos puntos de agilidad al no finalizar de completar la conexión enviando el **RST**. Si lo vemos de otra manera, sería como iniciar una conexión, pero en el momento que recibimos respuesta de que el puerto del que salió esta solicitud desde nuestra máquina se encuentra cerrado, por lo que no se puede establecer una conexión.

Este escaneo lo podríamos realizar como:

```shell
nmap -p- --open -sS 192.168.100.1
```

Y veremos cómo ya va teniendo mayor velocidad.

## Min rate && Max rate

Tenemos la opción **--min-rate** y **--max-rate** lo cual nos permite especificar la cantidad mínima y máxima de paquetes que vamos a estar enviando para poder agilizar el proceso del escaneo. 

Una cantidad recomendada como mínima sería **5000** paquetes, ya que esto nos da bastante agilidad con precisión, asegurando que cuando nos diga que en puerto esté abierto, si está abierto y cuando nos diga que esté cerrado, realmente esté cerrado. 

Si jugamos con una cantidad más alta en min rate como **10000**, esto podría llegar a darnos falsos positivos. 

Si ahora aplicamos el siguiente escaneo:

```shell
nmap -p- --open -sS --min-rate 5000 -v -n -Pn 192.168.100.1
```

Ya estaremos aplicando distintas de las cosas que hemos visto, agilizando un escaneo que no nos daría falsos positivos. Cuando estemos realizando un escaneo, si presionamos **Enter** esto nos dirá el porcentaje que lleva el escaneo:

![[019.PNG]]

Con todas estas opciones para evitar la detección del Firewall, nosotros podríamos combinarlas y conseguir lo que mejor nos convenga para evitar que el Firewall nos detecte y asi extraer una mayor cantidad de información.
# Siguientes apuntes

[[Uso de scripts y categorías en nmap para aplicar reconocimiento]]