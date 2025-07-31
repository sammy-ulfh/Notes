# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Siguientes apuntes]]
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

Cuando desplegamos un contenedor lo haríamos de la siguiente manera:

![[Docker/Construccion/images/003.png]]

Con **docker run** generamos el contenedor y automáticamente estará corriendo. Lo hicimos con las opciones **d**, **i** y **t**, lo que nos permite tenerlo corriendo en segundo plano, asignarle una seudoterminal y, además, permite la entrada interactiva de comandos.

Cuando ejecutamos **docker ps** podremos ver que ya se encuentra corriendo y podremos referirnos a este contenedor con el ID completo que nos retorna el **docker run** o con el ID compacto que nos retorna al hacer un **docker ps**, pero también podremos utilizar el nombre, que en este caso al no asignarle uno, Docker se lo asigno de forma automática.

Si quisiéramos tener una Shell interactiva del contenedor, lo haríamos con **docker exec** para ejecutar un comando en el contenedor, refiriéndonos a este con el ID o nombre y con las opciones **it**:

![[Docker/Construccion/images/004.png]]

En este caso vemos cómo el **hostname** del contenedor es el propio ID de este. 

Los contenedores por defecto vienen prácticamente limpios, por lo que no tendremos comandos como **ifconfig** o **ping**. Si quisiéramos llegar a utilizar ciertas herramientas, tendríamos que instalarlas de la forma convencional; sin embargo, en un inicio no funcionaría un simple **apt install** en este caso al estar basado en Debian el Ubuntu.

Primeramente, tendríamos que hacer un update del sistema y con ello ya nos funcionaría correctamente la instalación de paquetes:

![[Docker/Construccion/images/005.png]]

Con net-tools instalado ahora si que nos funcionaría **ifconfig**:

![[Docker/Construccion/images/006.png]]

Si vemos la IP de nuestro ordenador a comparación de la que tiene el contenedor, es totalmente distinta. Esto se debe a que a nosotros en nuestra máquina se nos asigna una interfaz **docker0** la cual tiene cierto rango de IP y a partir de esta se le asigna una IP distinta a cada contenedor:

![[Docker/Construccion/images/007.png]]

Por lo tanto, estas interfaces deberían poder comunicarse entre si. Podríamos intentar hacer un ping de una a otra y para instalar ping tendríamos que instalar **iputils-ping**:

![[Docker/Construccion/images/008.png]]

En este caso, como el contenedor viene prácticamente vacío, nosotros hemos tenido que instalar dependencias, pero esto es algo que nosotros podremos automatizar desde nuestro Dockerfile con el prefijo **RUN** donde seguidamente le tendríamos que indicar los comandos:

![[Docker/Construccion/images/009.png]]

Volveremos a hacer **build** y con el parámetro **-t** le asignaremos el mismo nombre y, en este caso, el tag que le daremos será el de **v2** haciendo referencia a que es nuestra segunda versión. 

Si vemos el output, al inicio en las primeras indicaciones saldrá el mensaje **using cache**, haciendo referencia a lo que ya hicimos anteriormente y no lo volverá a hacer, ya que esto se ha quedado cacheado y pasa directamente a lo nuevo que hemos agregado a nuestro Dockerfile.

Con ello, al ver las imágenes tendríamos ahora esta nueva imagen, la cual podríamos correr en un contenedor:

![[Docker/Construccion/images/010.png]]

Ahora que tenemos corriendo nuestro contenedor al cual le hemos asignado el nombre de **mySecondContainer**, podremos ejecutar un comando en el para tener una terminal interactiva y con ello verificar si ahora tenemos los comandos de los paquetes que hemos instalado y ahora si que los tendremos:

![[Docker/Construccion/images/011.png]]

Con ello ya habremos creado y desplegado un contenedor a partir de una imagen. Esto es de mucha ayuda, ya que todo en cuanto a dependencias y lo necesario para su funcionalidad se encapsula dentro del mismo y lo podríamos pasar a un ordenador distinto, lo cual nos quita problemas a la hora de ejecutarlo en distintos ordenadores, ya que todo esta deplegando en el propio contenedor y nos evita cualquier problema. 

Además, una ventaja muy clara, a diferencia de las máquinas virtuales, es que ocupan muy poco espacio al reutilizar el mismo kernel del sistema, mientras que en una VM se almacena el sistema completo, haciéndolo más pesado.

El tamaño es algo que podremos verificar con el comando **docker images**.
# Siguientes apuntes

[[Comandos comunes para la gestión de contenedores]]