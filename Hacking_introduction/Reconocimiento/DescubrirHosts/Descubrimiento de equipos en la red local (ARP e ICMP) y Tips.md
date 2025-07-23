# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Arp-Scan]]
- [[#Netdiscover]]
- [[#Bash]]
- [[#Masscan]]
- [[#Siguientes apuntes]]
# Introducción

Los descubrimientos de equipos en la red local es una tarea fundamental en la gestion de redes y en las pruebas de seguridad. Existen diferentes herramientas y tecnicas para realizar esta tarea, que van desde escaneo de puertos hasta el analisis de trafico en la red.

Nos enfocaremos en las tecnicas de descubrimiento de equipos basadas en los protocolos **ARP** e **ICMP**. Ademas, se presentaran diferentes herramientas que pueden ser utiles para esta tarea, como **Nmap**, **netdiscover**, **arp-scan** y **masscan**.

Entre los modos de escaneo que se explican, se utiliza el parametro **-sn** de Nmap, que permite realizar un escaneo de hosts sin realizar el escaneo de puertos. Tambien, se presentan las herramientas **netdiscover**, **arp-scan** y **masscan** que utilizan el protocolo **ARP** para descubrir hosts en la red.

Cada herramienta tiene sus propias ventajas y limitaciones. Por ejemplo, **netdiscover** es una herramienta simple y facil de usar, pero puede ser menos precisa que **arp-scan** o **masscan**. Por otro lado, **arp-scan** y **masscan** son herramientas mas potentes, capaces de descubrir hosts mas rapido y en redes mas grandes, pero tambien son mas complejas y pueden requerir mas recursos.

El descubrimiento de equipos en la red local es fundamental para cualquier administrador de redes o profesional de seguridad de la informacion. Con las tecnicas y herramientas adecuadas, es posible realizar esta tarea de manera efectiva y eficiente.
# Práctica

## Nmap

Si nosotros ejecutamos **ifconfig**, veremos lo siguiente:

![[Reconocimiento/DescubrirHosts/images/001.PNG]]

Recordando la parte de subnetting, podremos ver cómo estamos establecidos en una red que contempla la bitmask **/24** al ser una red chica. 

Con ello, al realizar el primer escaneo que será con Nmap, utilizaremos el parámetro **-sn** para únicamente enumerar hosts sin escanear puertos y pasaremos la IP con la bitmask correspondiente:

![[Reconocimiento/DescubrirHosts/images/002.PNG]]

Tardará lo suyo, pero con ello nos reportará correctamente hosts activos en nuestra red local. Esto lo hará mediante el protocolo ICMP, para hacerlo mediante ARP, tenemos la alternativa que es **arp-scan**.

## Arp-Scan

Con **arp-scan** tendremos que pasarle la interfaz de red conectada a nuestro internet mediante el parámetro **-I** y agregarle **--localnet** para que realice el escaneo en la red local. 

Cada interfaz de red tiene un nombre distinto y el nombre de esta interfaz puedes verlo si ejecutas **ifconfig**, como lo hicimos anteriormente.

![[Reconocimiento/DescubrirHosts/images/003.PNG]]

El primero está bien, pero algo adicional que puede ser de mucha utilidad es **--ignoredups**, debido a que en ocasiones uno o más hosts podrán verse de forma repetida, por lo tanto, al agregar este parámetro directamente no los mostrará y veremos hosts únicos.

## Netdiscover

Si la herramienta no está instalada, tendremos que instalarla. 

A netdiscover tendremos que pasarle la interfaz con el parámetro **-i** y, si observamos bien, en este caso no toma el CIDR (bitmask) que estábamos considerando de acuerdo a la máscara de red. Además, puede llegar a ser más lento que herramientas como **arp-scan**.

```shell
netdiscover -i ens33
```

![[Reconocimiento/DescubrirHosts/images/004.PNG]]

Al tomar este CIDR es más tardado. A pesar de esto, tomar un CIDR mayor nos puede venir bien en ciertas ocasiones. 

Esto se debe a que en una red se aplica **subnetting** para realizar segmentos de red, pero estos segmentos pueden ser parte de una red mucho más grande la cual luego emplea cierto método llamado **VLAN's**, esto es básicamente crear otros segmentos a nivel de la capa de enlace de datos los cuales no afectaran a la capa de red.

Básicamente, esto lo que hace es implementar una medida extra de seguridad y como esto no considera los segmentos que existen a nivel de red, hosts de diferente segmento de red podrán encontrarse dentro de la misma VLAN y por ende podrías comunicarte con ellos, ya que la capa de enlace de datos lo permitiría. 

Por ende puede venir bien en ciertos casos verificar segmentos de red mucho mayores como lo es el CIDR **/16** y podríamos llegar a encontrar hosts activos con los cuales podemos comunicarnos encontrándose en otros segmentos de red.
## Bash

También nosotros, de forma manual mediante un script con bash podremos realizar lo mismo, realmente al hacerlo por el protocolo **ICMP** es solo hacer **ping** a direcciones IP para verificar si el host está activo o no. 

Cuando nosotros ejecutamos un ping hacia un host, siempre veremos un stdout o un stderr. Lo que podremos hacer es verificar el código de estado (**0** es exitoso), ocultando el output. Cuando el código de estado sea 0, quiere decir que ese host está activo y podemos comunicarnos con el:

![[Reconocimiento/DescubrirHosts/images/005.PNG]]

Cuando se trata de realizar un ping con un host no activo, veremos cómo esto puede ser tardado. Por ende, lo que haremos será aplicar un timeout a un comando a ejecutar con bash y el comando lo indicaremos con el parámetro **-c**:

```shell
timeout 1 bash -c "ping -c 1 [HOST_IP]"
```

El tiempo máximo de espera en 1 es bastante bueno y nos permitirá verificar de forma correcta si un host se encuentra activo o no:

![[Reconocimiento/DescubrirHosts/images/006.PNG]]

Para nuestro script, lo que haríamos sería ocultar tanto output como errores con **&>/dev/null** y verificaremos el código de estado para mostrar si el host se encuentra activo o no:

```shell
timeout -1 bash -c "ping -c 1 [HOST_IP]" &>/dev/null && echo "[+] Host activo"
```

Lo anterior, al utilizar **&&** ejecutará el siguiente comando solamente si el primero tiene un código de estado exitoso, por ende tendríamos lo siguiente:

![[Reconocimiento/DescubrirHosts/images/007.PNG]]

Con ello podremos hacer un bucle el cual itere en una secuencia de 1 a 254 para no considerar la dirección broadcast y para que el ejercicio sea sencillo, solo modificaremos el último octeto desde el host 1 hasta el 254:

![[Reconocimiento/DescubrirHosts/images/008.PNG]]

En este caso definimos nuestro flujo de salida del programa con la función ctrl_c. Utilizamos el mismo comando que habíamos contemplado anteriormente, pero ahora iterando para múltiples hosts y mostrando el mensaje para aquellos que estén activos. Además, le agregamos el **&** para utilizar múltiples procesos o hilos y al final agregamos **wait** para que siempre espere a que todos finalicen correctamente. 

Si no empleamos los hilos, nuestro script iría mucho más lento al momento de ejecutarlo, ya que, esperaría a que finalice el anterior y llevaría un orden uno a uno. 

Si lo ejecutamos, ya tendremos el descubrimiento de hosts por ICMP:

![[Reconocimiento/DescubrirHosts/images/009.PNG]]

Es posible que en algunas máquinas no acepten paquetes ICMP por como lleguen a estar configuradas. Por ello, podremos realizar otra aproximación en la que enviemos un **echo** de una cadena vacía a **/dev/tcp/\[HOST_IP]/\[PORT]**, como no vamos a realizar directamente un escaneo de puertos, lo que podremos hacer es tratar de verificar solamente los puertos más comunes para verificar si hosts se encuentran activos en una red:

![[Reconocimiento/DescubrirHosts/images/010.PNG]]

Aquí lo que sucede es que el primer bucle establece una IP para en esa misma iterar sobre una serie de puertos comunes y tratar de verificar si se encuentra alguno de ellos abierto en un host, mostrándolo como abierto.

![[Reconocimiento/DescubrirHosts/images/011.PNG]]

Podremos ver cómo en este caso el script no nos llega a representar todos los hosts y esto es claro, ya que solo nos llegará a mostrar el host si este mismo tiene abierto alguno de los puertos comunes que consideramos, de lo contrario no nos lo mostrará. 

Con esto ya hemos visto que si con alguna herramienta no nos da nada o quizá no lleguemos a ver todos los hosts, podemos ver cómo tenemos distintas posibilidades a emplear para tratar de enumerar la mayor cantidad de hosts posibles, ya que sería información valiosa.

## Masscan

**masscan** es muy similar a nmap, pero incluso es una herramienta bastante más potente. Mientras **Nmap** nos permite descubrir miles de hosts por minuto, **masscan** incluso podría descubrir millones. 

Algo muy interesante es que incluso podría descubrirnos todos los puertos de un host específico mediante el envío de un único paquete.

![[Reconocimiento/DescubrirHosts/images/012.PNG]]

La forma de utilizarlo es la anterior, pasándole un puerto o rango que puertos, después una IP de red con su respectivo CIDR y finalmente un **rate**. Este nos permite especificar la cantidad de paquetes a enviar por segundo. Mientras mayor sea la cantidad, menos preciso podría llegar a ser el escaneo al tener un menor tiempo para verificar que el host exista, pero nos permite una mayor rapidez en el escaneo. Mientras menor sea el rate, más confianza podremos tener en los resultados del escaneo, aunque podría ser más tardado:

![[Reconocimiento/DescubrirHosts/images/013.PNG]]

Aquí estamos considerando un CIDR mayor por lo mencionado anteriormente sobre los distintos segmentos de red, que aun así podríamos llegar a encontrar hosts activos. 

Además, al considerar un segmento de red mayor, pues nuestra dirección de red también cambiaría y, por ende también iría 0 en el tercer octeto.

En cuestiones de ciertos entornos de red, nos puede llegar a suceder lo que pasa con Nmap cuando un host no está activo, que simplemente no continúa el escaneo, entonces para evitar que esto suceda, consideramos el parámetro **-Pn**. 

Finalmente, le damos un rate de 10000 y esto nos lleva el escaneo bastante rápido. Recordemos que si le damos un rate menor, como 5000, esto nos podría permitir descubrir incluso más puertos en un host o algunos que no se alcanzaron a enumerar.

Esto se debe a que el escaneo va más tranquilo y permite no perder cierta información. Esto sucede con cada una de las herramientas de escaneo, ya que, entre más rápido vaya, se podría llegar a perder cierta información.
# Siguientes apuntes

[[Validación del objetivo (Fijando un target en HackerOne)]]