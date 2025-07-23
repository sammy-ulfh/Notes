
# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Siguientes apuntes]]
# Introducción

La enumeración de puertos es una tarea crucial en las pruebas de penetración y seguridad de redes. Tal y como hemos visto, Nmap es una herramienta de línea de comandos ampliamente utilizada para esta tarea, pero existen alternativas para realizar la enumeración de puertos de manera efectiva sin utilizar herramientas externas. 

Una alternativa a la enumeración de puertos utilizando herramientas externas es el poder de los **descriptores de archivo** en sistemas **Unix**. Los descriptores de archivo son una forma de acceder y manipular archivos y dispositivos en sistemas Unix. En particular, la utilización de **/dev/tcp** permite la conexión a un host y puerto específicos como si se tratara de un archivo en el sistema.

Para realizar la enumeración de puertos utilizando **/dev/tcp** en Bash, es posible crear un script que realice una conexión a cada punto de interés y compruebe si el puerto está abierto o cerrado en función de si se pueden enviar o recibir datos. Una forma de hacer esto es mediante el uso de comando como **echo** o **cat**, aplicando redireccionamientos al **/dev/tcp**. El código de estado devuelto por el comando se puede utilizar para determinar si el puerto está abierto o cerrado. 

Aunque esta alternativa puede ser menos precisa y más lenta que el uso de herramientas especializadas como Nmap, es una opción interesante y viable para aquellos que buscan una solución rápida y sencilla para la enumeración de puertos en sistemas Unix. Además, este enfoque puede proporcionar una mejor comprensión de como funcionan los descriptores de archivo en sistemas Unix y como se pueden utilizar para realizar tareas de red.
# Práctica

Nosotros en nuestra máquina podremos ver si un puerto de un host se encuentra abierto enviando una cadena vacía, por ejemplo, a un host y puerto específico. 

En este caso, a nuestro router, podremos hacerlo utilizando la ruta **/dev/tcp** y le agregaremos **/\[HOST]/\[PORT]**, si el código de estado es que se ha ejecutado correctamente, quiere decir que el puerto se encuentra abierto, de lo contrario incluso veremos un error. Tendremos que ejecutarlo en una terminal bash para no tener problemas:

```shell
echo '' > /dev/tcp/192.168.100.1/80
```

![[025.PNG]]

Esto mismo lo podremos hacer empleando descriptores de archivos, creando uno tanto para lectura como para escritura y cerrándolo al final:

![[026.PNG]]

Aquí se define el descriptor de archivo tanto para lectura como para escritura y después se cierra con **exec 3<&-** y para asegurarnos de que se cierre totalmente **exec 3>&-**, si antes de cerrarlo verificamos el código de estado con **echo $?** podremos ver si se ha ejecutado correctamente (el puerto está abierto) o no (el puerto no está abierto). 

Con ello en mente comenzaremos creando el script para el archivo **portScanner.sh** definiendo primeramente la salida del programa con **CTRL + C**:

![[027.PNG]]

Ahora declararíamos una variable sobre la cual vamos a iterar en un bucle for. La variable tendrá una secuencia desde el número 1 hasta el 65535 que equivale al total de puertos. Para asegurarnos de que sea un iterable, tendremos que declararlo con **declare -a** que **-a** viene de array.

![[028.PNG]]

En el bucle, la forma en la que podremos iterar sobre ports es la anterior.

Nosotros le pasaremos al script el host como argumento, por ende verificaremos si este argumento existe para realizar el escaneo de puertos:

![[029.PNG]]

Si el argumento existe, quiere decir que el host ha sido pasado, por ende se pasará al escaneo. De no existir el argumento, mostrará cómo debe utilizarse. 

Aquí aplicaremos lo que vimos de los descriptores de archivo y recuperando su código de estado. Si este es 0, entonces el puerto está abierto:

![[030.PNG]]

Esto se hace en la función checkPort, ocultando el output y, si el código de estado es correcto (0), entonces imprimirá el mensaje de que el puerto está abierto. Al momento de ejecutar la función, le agregamos un **&** para ejecutarlo en segundo plano y que actúe de forma similar a correrlo en hilos y vaya mucho más rápido. 

Hasta aquí hay un pequeño error y es que, como **ports[@]** no es ningún tipo de comando, sino, una variable. Tendremos que colocarla entre llaves y, además, en nuestra función tendremos que cerrar el descriptor de archivo 3:

![[031.PNG]]

Con ello ya podremos ejecutarlo:

![[032.PNG]]

Lo que sí notaremos es que esto es un poco más tardado. 

Si tal, para un mejor control del programa estaría bien agregarle al final del todo **wait** para que, al momento de que se termine de ejecutar el bucle, espere a que finalicen todos los hilos que se han lanzado:

![[033.PNG]]

Si nos interesa ocultar el cursor cuando ejecutemos un script que tardara su tiempo, podríamos utilizar **tput civit** y para mostrarlo nuevamente **tput cnorm**.
# Siguientes apuntes

[[Descubrimiento de equipos en la red local (ARP e ICMP) y Tips]]