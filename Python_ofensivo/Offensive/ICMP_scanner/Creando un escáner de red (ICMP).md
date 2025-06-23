
# Introduccion

Se desarrollara un escaner de red utilizando el protocolo ICMP. Siguiendo el proceso de programacion de un escaner eficiente y confiable que pueda detectar dispositivos activos en una red. Se cubriran los fundamentos del protocolo ICMP y como es utilizado en el escaneo de redes.

# Practica

Crearemos nuestro script **scanner.py**, vamos a considerar el argumento **-t** al cual podremos indicarle un target de una IP o un rango. Para el rango lo haremos de la siguiente manera **192.168.1.1-100**, de esta forma le estamos indicando que nos realice un escaneo desde la IP 192.168.1.1 hasta la 192.168.1.101. 

Para ello, empezamos definiendo la lógica inicial y nuestro menú de argumentos:

![[Offensive/ICMP_scanner/images/001.png]]

Con ello, generamos una función **parse_target** la cual nos ayudará a gestionar el string dado por el usuario para generar el rango de IP's y retornarlo:

![[Offensive/ICMP_scanner/images/002.png]]

Ahora en parse target vamos a tener en cuenta la entrada que podremos tener que es **192.168.1.1-100**, en este caso al tener que retornar una lista de una IP o una lista con un rango de IP's. Tendremos en cuenta que el único octeto que va a variar será el último, por ende comenzaremos realizando un split de todo con base en el punto. 

Con ello crearemos una variable que sea **first_three_octets** y que su valor sea los primeros tres octetos de la IP:

![[Offensive/ICMP_scanner/images/003.png]]

Aplicaríamos un join para tenerlo todo en un string y no en lista. 

Después vamos a verificar si nuestro target splitted tiene elementos, de ser así la IP está bien seteada y en ello verificaremos si el cuarto elemento tiene un **-**, lo que nos dirá si es un rango o una IP. De ser un rango, almacenaremos el inicio y el final en variables:

![[Offensive/ICMP_scanner/images/004.png]]

De esta manera, si tenemos un **-**, vamos a retornar todo el rango de IP's. De no ser así, solo tendríamos una IP y, por lo tanto, la retornaríamos.

Si target_splitted no tiene 4 elementos, quiere decir que el formato está mal. 

Si ahora imprimimos lo retornado en ambos casos, veremos lo siguiente:

![[Offensive/ICMP_scanner/images/005.png]]

Con ello ya podríamos iterar en la lista y tener cada IP de forma individual. 

Crearemos la función host_diiscovery a la cual le pasaremos como argumento la lista de IP's y iteraremos sobre ella, ejecutando el comando **ping** con subprocess y dándole un time out. Además de no querer ver el output ni errores, los enviamos al **DEVNULL** mediante un argumento en subprocess.

Finalmente, verificamos si el código de estado de la ejecución del comando, en el atributo **returncode** de **ping** es exitoso (0). De ser así, imprimimos esta IP indicando que está activa:

![[Offensive/ICMP_scanner/images/006.png]]

Esto nos generará una excepción por el time out, por ende debemos controlarla para que no suceda nada al sobrepasar este time out:

![[Offensive/ICMP_scanner/images/007.png]]

Además, será importante gestionar la salida forzada del programa utilizando CTRL + C.

![[Offensive/ICMP_scanner/images/008.png]]

Finalmente, agregaremos los hilos aprovechándonos de lo que ya tenemos para que el escaneo sea mucho más rápido.

![[Offensive/ICMP_scanner/images/009.png]]

De esta forma, al ejecutarlo ya tendremos un escáner de red ICMP rápido y potente.

![[Offensive/ICMP_scanner/images/010.png]]

## Siguientes apuntes

[[Creando un escáner de red (ARP) con Scapy]]