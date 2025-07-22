
# Índice

# Introducción

La enumeración de puertos es una tarea crucial en las pruebas de penetración y seguridad de redes. Tal y como hemos visto, Nmap es una herramienta de línea de comandos ampliamente utilizada para esta tarea, pero existen alternativas para realizar la enumeración de puertos de manera efectiva sin utilizar herramientas externas. 

Una alternativa a la enumeración de puertos utilizando herramientas externas es el poder de los **descriptores de archivo** en sistemas **Unix**. Los descriptores de archivo son una forma de acceder y manipular archivos y dispositivos en sistemas Unix. En particular, la utilización de **/dev/tcp** permite la conexión a un host y puerto específicos como si se tratara de un archivo en el sistema.

Para realizar la enumeración de puertos utilizando **/dev/tcp** en Bash, es posible crear un script que realice una conexión a cada punto de interés y compruebe si el puerto está abierto o cerrado en función de si se pueden enviar o recibir datos. Una forma de hacer esto es mediante el uso de comando como **echo** o **cat**, aplicando redireccionamientos al **/dev/tcp**. El código de estado devuelto por el comando se puede utilizar para determinar si el puerto está abierto o cerrado. 

Aunque esta alternativa puede ser menos precisa y más lenta que el uso de herramientas especializadas como Nmap, es una opción interesante y viable para aquellos que buscan una solución rápida y sencilla para la enumeración de puertos en sistemas Unix. Además, este enfoque puede proporcionar una mejor comprensión de como funcionan los descriptores de archivo en sistemas Unix y como se pueden utilizar para realizar tareas de red.
# Práctica

# Siguientes apuntes

[[]]