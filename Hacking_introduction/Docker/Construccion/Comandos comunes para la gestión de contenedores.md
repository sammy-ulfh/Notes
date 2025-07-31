# Índice

# Introducción

Ahora tomaremos un enfoque a la eliminación de los contenedores e imágenes que tengamos en el ordenador. Los comandos que se verán en la práctica son:

- **docker rm $(docker ps -a -q) --force**: Este comando se utiliza para eliminar todos los contenedores en el sistema, incluyendo los contenedores detenidos. La opción **-q** se utiliza para mostrar solo los identificadores numéricos de los contenedores, y la opción **--force** se utiliza para forzar la eliminación de los contenedores que están en ejecución. Es importante que la eliminación de todos los contenedores en el sistema pueda ser peligrosa, ya que puede borrar accidentalmente contenedores importantes o datos importantes. Por lo tanto, se recomienda tener precaución al utilizar este comando.
- **docker rm id_contenedor**: Este comando se utiliza para eliminar un contenedor específico a partir de su identificador. Es importante tener en cuenta que la eliminación de un contenedor eliminara también cualquier cambio que se haya realizado dentro del contenedor, como la instalación de paquetes o la modificación de archivos.
- **docker rmi $(docker images -q)**: Este comando se utiliza para eliminar todas las imágenes de docker en el sistema. La opción **-q** se utiliza para mostrar solo los identificadores numéricos de las imágenes. Es importante tener en cuenta que la eliminación de todas las imágenes de Docker en el sistema puede ser peligrosa, ya que puede borrar accidentalmente imágenes importantes o datos importantes. Por lo tanto, se recomienda tener precaución al utilizar este comando.
- **docker rmi id_imagen**: Este comando se utiliza para eliminar una imagen específica a partir de su identificador. Es importante tener en cuenta que la eliminación de una imagen eliminaría también cualquier contenedor que se haya creado a partir de esa imagen. Si se desea eliminar una imagen que tiene contenedores en ejecución, se deben detener primero los contenedores y luego eliminar la imagen.
# Práctica

## docker stop

Cuando nosotros queremos detener un contenedor, utilizaremos **docker stop** y le pasaremos el ID de dicho contenedor que se encuentre corriendo. Los id podremos visualizarlos al hacer un **docker ps**, ya que esto nos mostrará los que se encuentran corriendo:

![[Docker/Construccion/images/012.png]]

Finalmente, después de detener el contenedor, con **docker ps** veremos únicamente los que están corriendo, pero con **docker ps -a** veremos incluso los que se han detenido.

## docker rm

Cuando un contenedor se ha detenido, nosotros podremos eliminar el contenedor para ya no tenerlo en el registro de contenedores que se han desplegado. Esto sería utilizando **docker rm** y pasándole el ID de dicho contenedor:

![[Docker/Construccion/images/013.png]]

Con ello, veremos cómo nos queda únicamente el contenedor que está actualmente corriendo y no hemos tenido ningún problema al eliminar aquellos que ya se han detenido. Lo que sucede aquí es que si intentamos eliminar el contenedor que aún se encuentra corriendo, nos dará error solicitando que primero se detenga:

![[Docker/Construccion/images/014.png]]

La cosa es que esto se puede forzar. Si al final de tratar de eliminarlo con **docker rm id_contenedor** le agregamos un **--force**, esto nos detendra y eliminará el contenedor:

![[Docker/Construccion/images/015.png]]

Con esto en mente, ahora, como ejemplo práctico pondremos a correr tres contenedores de la misma imagen, con distinto nombre:

![[Docker/Construccion/images/016.png]]

Si quisiéramos listar los ID de todos los contenedores, podríamos agregar el parámetro **-q** cuando los listemos, esto nos retornaría únicamente los ID:

![[Docker/Construccion/images/017.png]]

Si quisiéramos considerar también aquellos que se hayan detenido, tendríamos que agregar el parámetro **-a**. En este caso solo tenemos tres contenedores existentes y estos 3 se encuentran corriendo. 

Lo interesante de esto, es que al utilizarlo con **docker rm**, es capaz de interpretarlo con los saltos de línea que tiene de un ID a otro y nos eliminaría cada uno de los contenedores, por lo tanto, esto lo pasaríamos como si de un argumento de ejecución de comando se tratase para que nos retorne el ID de cada contenedor **$(docker ps -q)**. Como al intentar eliminar contenedores sin haberlos detenido antes, falla, le agregaremos la opción **--force** y esto nos permitirá eliminarlos completamente:

![[Docker/Construccion/images/018.png]]

Con ello ya se habrían eliminado, al ser capaz de interpretar los ID con todo y el salto de líneas que nos retorna el parámetro **-q** al listar los contenedores.

## docker rmi

Cuando nosotros queremos eliminar imágenes, tendremos que utilizar **docker rmi** y pasarle el nombre de la imagen correspondiente:

![[Docker/Construccion/images/019.png]]

Anteriormente, **docker rmi** daba errores cuando se quería eliminar una imagen que tenía hijos. En este caso, lo podremos ver así como al crear nuestra imagen, viene siendo hijo de la imagen **ubuntu** que se descarga, así como la imagen con el tag **v2** es hija de la que tiene el tag **v1**. 

Entonces, al querer eliminar imágenes que fuesen los padres, daba error si antes no se eliminaban los hijos, pero en versiones más recientes esto ya no nos da error al eliminar y funciona sin más.

Aquí también podríamos aplicar lo del parámetro **-q**. Al listar las imágenes, esto nos retornará el ID de todas las existentes y **docker rmi** será capaz de interpretarlo para eliminarlas:

![[Docker/Construccion/images/020.png]]

Algo más a destacar, es que no podremos eliminar una imagen si se encuentra corriendo un contenedor de la misma, por lo tanto, antes se tendrá que detener el contenedor y posiblemente eliminarlo.
# Siguientes apuntes

[[Port Forwarding en Docker y uso de monturas]]