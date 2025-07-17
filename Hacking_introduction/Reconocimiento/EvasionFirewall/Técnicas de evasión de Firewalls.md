# Técnicas de evasión de Firewalls (MTU, Data Length, Source Port, Decoy, etc.)


# Apuntes anteriores

[[Nmap y sus diferentes modos de escaneo]]

# Indice


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

Con Nmap podremos realizar escaneos que nos permitiran poder detectar de forma correcta aquellos puertos que se encuentren abiertos pero el Firewall evite que puedamos detectarlos.

Por ello podremos realizar un escaneo, en este caso al puerto 22 del router para verificar que detecta si fragmentamos los paquetes:

```shell
nmap -p22 10.43.87.254 -f
```

![[Reconocimiento/EvasionFirewall/images/001.png]]

A simple vista no notaremos ninguna diferencia, pero podremos utilizar **tcpdump** justo antes del escaneo para capturar el trafico y despues abrirlo con **wireshark**, esto se hace capturando el trafico de la tarjeta de red que esta conectada al internet, esta la podremos ver haciendo un **ifconfig**.

Entonces la colocamos con el parametro **-i** el nombre de nuestra tarjeta de red, asi como con el parametro **-w** el nombre del archivo que se creara para almacenar los archivos y finalmente el parametro **-v** de verbose:

```shell
tcpdump -i wlan0 -w Captura.cap -v
```

![[Reconocimiento/EvasionFirewall/images/002.png]]

Finalmente, abrimos el archivo con **wireshark**:

```shell
wireshark Captura.cap &> /dev/null & disown
```

![[Reconocimiento/EvasionFirewall/images/003.png]]

En la parte superior podemos filtrar el contenido capturado, en este caso con **ip.flags.mf == 0**, si esta en 1 filtramos por el trafico fragmentado y si esta en cero por el trafico que no ha sido fragmentado.

Realizaremos un filtrado para observar solmanete el trafico fragmentado, si vemos que no nos captura trafico fragmentado, intentemos realizar un escaneo mucho mas grande, como hacia todos los puertos en general, para que aseguremos que se capturen.

Al filtrarlo, veriamos el trafico de la siguiente manera:

![[Reconocimiento/EvasionFirewall/images/004.png]]

![[Reconocimiento/EvasionFirewall/images/005.png]]

viendo los primeros dos, podremos irnos a la parte inferior y seleccionar **Data** del lado izquierdo, aqui veremos como esta la informacion en hexadecimal transmitiendose:

![[Reconocimiento/EvasionFirewall/images/006.png]]

En la parte superior, si observamos bien, los primeros dos nos menciona que son reensamblados en la traza #11, esto podremos observarlo bien si quitamos el friltro que habiamos colocado y nos vamos a la traza #11:

![[Reconocimiento/EvasionFirewall/images/007.png]]

El fragmentar un paquete nos da cierta seguridad de llegar a mostrar algunos puertos sin que el Firewall los oculte, esto se debe a que el Firewall espera ciertos tipos de paquetes especificos para evitarlos, al fragmentarlos lo que hacemos es dividir este paquete y al final el Firewall no detecta el tipo de paquete que esta siendo enviado.

## MTU

Agregado a esto, podremos utilizar el **MTU (Maximum Transmission Unit)**. Esto puede ser de ayuda ya que hay casos en los que el Firewall espera cantidades fijas en el tamano de cada paquete y si enviamos algunos de forma mas pequena, podrian no ser detectados y permitirnos llegar a visualizar puertos filtrados o ocultos hacia los escaneos detectados.

**--mtu** ocupa un valor mayor a cero y siempre tiene que ser multiplo de 8, de no ser asi nos lo dira el propio Nmap:

![[Reconocimiento/EvasionFirewall/images/008.PNG]]

Si nosotros quisieramos listar las posibilidades que tenemos para evitar estas detecciones por parte de un Firewal o un sistema de deteccion IDS, podriamos utilizar la flag **--help** de nmap para mostrar las opciones que tenemos:

```shell
nmap --help
```

![[Reconocimiento/EvasionFirewall/images/009.PNG]]

Buscando especificamente por este apartado, veremos como tenemos la que recien hemos visto y ahora nos enfocaremos en el **-D**.
## Cloak a scan with decoys

