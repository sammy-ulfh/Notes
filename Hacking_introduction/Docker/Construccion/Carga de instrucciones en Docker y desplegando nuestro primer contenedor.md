# Índice

# Introducción

Con lo anterior, ahora ya podremos arrancar nuestro primer contenedor. El comando **docker run** se utiliza para crear y arrancar un contenedor a partir de una imagen. Algunas de las opciones más comunes para el comando **docker run** son las siguientes:

- **-d** o **--detach** que se utiliza para arrancar el contenedor en segundo plano en lugar de primer plano.
- **-i** o **--interactive** que se utiliza para permitir la entrada interactiva al contenedor.
- **-t** o **--tty** que se utiliza para asignar una seudoterminal al contenedor.
- **--name** que se utiliza para asignar un nombre al contenedor.

Para arrancar un contenedor a partir de una imagen, la sintaxis sería de la siguiente manera:

`docker run [options] nombre_de_la_imagen`

Por ejemplo, si se espera arrancar un contenedor a partir de la imagen **my_image**, en segundo plano y con un seudoterminal asignado, se puede utilizar el siguiente comando:

`docker run -dit mi_imagen`

Una vez que el contenedor está en ejecución, se puede utilizar el comando **docker ps** para listar los contenedores que están en ejecución en el sistema. Algunas de las opciones más comunes para este comando son:

- **-a** o **--all** se utiliza para listar todos los contenedores, incluyendo los contenedores detenidos.
- **-q** o **--quiet** se utiliza para mostrar solo identificadores numéricos de los contenedores.

Por ejemplo, si se desean listar todos los contenedores que están en ejecución en el sistema, se puede utilizar el siguiente comando:

`docker ps -a`

Para ejecutar comando en un contenedor que ya está en ejecución, se utiliza el comando **docker exec** con diferentes opciones. Algunas de las más comunes son:

- **-i** o **--interactive** se utiliza para permitir la entrada interactiva al contenedor.
- **-t** o **--tty** se utiliza para asignar una seudoterminal al contenedor.

Por ejemplo, si se desea ejecutar el comando **bash** para obtener una terminal interactiva del propio contenedor, el cual tenga el identificado **123456789**, se puede utilizar el comando:

`docker exec -it 123456789 bash`

Otra alternativa es que utilizar el nombre del contenedor en lugar del identificador. Si nosotros le asignamos un nombre, podríamos utilizarlo o, si no se lo asignamos, Docker le asigna uno. 

Esta información la podremos ver con `docker ps`.
# Práctica

Cuando desplegamos un contenedor lo hariamos de la siguientre manera:

![[Docker/Construccion/images/003.png]]

Con **docker run** generamos el contenedor y automaticamente estara corriendo, lo hicimos con las opciones **d**, **i** y **t**, lo que nos permite tenerlo corriendo en segundo plano, asignarle una seudoterminal y ademas permite la entrada interactiva de comandos.

Cuando ejecutamos **docker ps** podremos ver que ya se encuentra corriendo y podremos referirnos a este contenedor con el ID completo que nos retorna el **docker run** o con el ID compacto que nos retorna la hacer un **docker ps**, pero tambien podremos utilizar el nombre, que en este caso al no asignarle uno, Docker se lo asigno de forma automatica.

Si quisieramos tener una shell interactiva del contenedor, lo hariamos con **docker exec** para ejecutar un comando en el contenedor refiriendonos a este con el ID o nombre y con las opciones **it**:

![[Docker/Construccion/images/004.png]]

En este caso vemos como el **hostname** del contenedor es el propio ID de este.

Los contenedores por defecto vienen practicamente limpios, por lo que no tendremos comandos como **ifconfig** o **ping**. Si quisieramos llegar a utilizar ciertas herramientas tendriamos que instalarlas de la forma convencional, sin embargo en un inicio no funcionaria un simple **apt install** en este caso al estar basado en debian el ubuntu.

Primeramiente tendriamos que hacer un update del sistema y con ello ya nos funcionaria correctamente la instalacion de paquetes:

![[Docker/Construccion/images/005.png]]

Con net-tools instalado ahora si que nos funcionaria **ifconfig**:

![[Docker/Construccion/images/006.png]]

Si vemos la IP de nuestro ordenador a comparacion de la que tiene el contenedor es totalmente distinta. Esto se debe que a nosotros en nuestra maquina se nos asigna una interfaz **docker0** la cual tiene cierto rango de IP y a partir de esta se le asigna un IP distinta a cada contenedor:

![[Docker/Construccion/images/007.png]]


# Siguientes apuntes