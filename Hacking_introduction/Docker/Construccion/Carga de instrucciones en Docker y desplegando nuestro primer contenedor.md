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

# Siguientes apuntes