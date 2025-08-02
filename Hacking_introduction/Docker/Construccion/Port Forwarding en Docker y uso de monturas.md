# Índice

- [[#Introducción]]
- [[#Port forwarding]]
- [[#Monturas]]
- [[#Práctica]]
- [[#Por forwarding]]
- [[#Monturas]]
- [[#COPY]]
- [[#docker logs]]
- [[#Siguientes apuntes]]
# Introducción

## Port forwarding

El **Port Forwarding**, también conocido como reenvío de puertos, nos permite **redirigir el tráfico de red** desde un puerto específico en el host a un puerto específico en el contenedor. Esto nos permitirá acceder a los servicios que se ejecutan dentro del contenedor, desde el exterior. 

Para utilizar el port forwarding, se utiliza la opción **-p** o **--publish** en el comando **docker run**. Esta opción se utiliza para especificar la redirección de puertos y se puede utilizar de varias maneras. Por ejemplo, si se desea redirigir el puerto 80 del host al puerto 8080 del contenedor, se puede utilizar la siguiente sintaxis:

`docker run -p 80:8080 mi_imagen`

Esto redirigirá cualquier tráfico entrante en el puerto 80 del host al puerto 8080 del contenedor. Si se desea especificar un protocolo diferente al protocolo TCP predeterminado, se puede utilizar la opción **-p** con un formato diferente. Por ejemplo, si se desea redirigir el puerto 53 del host al puerto 53 del contenedor utilizando el protocolo UDP, se puede utilizar la siguiente sintaxis:

`docker run -p 53:53/udp mi_umagen`

## Monturas

Las **monturas**, por otro lado, nos permiten compartir un directorio o archivo entre el sistema host y el contenedor. Esto nos permitirá persistir la información entre ejecuciones de contenedores y compartir datos entre diferentes contenedores. 

Para utilizar las monturas, se utiliza la opción **-v** o **--volume** en el comando **docker run**. Esta opción se utiliza para especificar la montura y se puede utilizar de varias maneras. Por ejemplo, si se desea montar el directorio **/home/usuario/datos** del host en el directorio **/datos** del contenedor, se puede utilizar la siguiente sintaxis:

`docker run -v /home/usuario/datos:/datos mi_imagen`

Esto muestra el directorio **/home/usuario/datos** en el directorio **/datos** del contenedor. Si se desea especificar una opción adicional, como la de montar el directorio en modo de solo lectura, se puede utilizar la opción **-v** con un formato diferente. Por ejemplo, si se desea montar el directorio en modo de solo lectura, se puede utilizar la siguiente sintaxis:

`docker run -v /home/usuario/datos:/datos:ro mi_imagen`
# Práctica

## Por forwarding

Ahora, con nuestro Dockerfile que teníamos, vamos a agregar que se instalen los paquetes **apache2** y **php** para levantar un servicio http y que además sea capaz de interpretarnos código PHP. 

Además, utilizaremos otra palabra clave, la cual es **ENTRYPOINT** para indicar qué comando queremos que nos ejecute el contenedor apenas se haya desplegado con **docker run**. Tendremos que iniciar el servicio de **apache2** y esto será con uno de los siguientes comandos:

`systemctl start apache2` o `service apache2 start`

Esto nos levantará un servicio web en el puerto 80 de nuestro contenedor. Como nosotros requeriremos de comunicación hacia este puerto desde nuestra máquina host para poder proveer este servicio y acceder a él, tendremos que exponer el puerto 80 del contenedor con otra palabra clave, la cual es **EXPOSE** e indicar el puerto:

![[Docker/Construccion/images/021.png]]

Al hacer esto, ya estaría entrando en el terreno el concepto del port forwarding, ya que básicamente es mediante un puerto que asignemos en nuestra máquina host tener acceso al servicio de un puerto dado en el contenedor y esto será de ayuda para ello. 

Con este archivo, ahora a la hora de ejecutar el contenedor, crearemos una regla para asignar un puerto de nuestro host al puerto 80 de nuestro contenedor y así tener comunicación con el servicio. Primeramente construiríamos nuestra imagen:

`docker build -t web_server .`

En ocasiones, al construir una imagen con Docker, podría entrarnos en un tipo de modo interactivo donde nos pregunte cosas como la geolocalización. Este puede llegar a ser molesto, ya que solo queremos construir nuestra imagen sin que nos solicite ningún dato. 

Por ello, si detenemos la ejecución y vemos las imágenes de Docker, en ocasiones podremos ver imágenes que tengan como **Repository** o **Tag** en **\<none>** y esto puede no interesarnos, ya que son imágenes que no tienen sentido porque han dado error o algo ha pasado en su construcción. Podremos listarlas efectuando un filtrado específico con **docker images** que sería el siguiente:

`docker images --filter "dangling=true"`

![[Docker/Construccion/images/022.png]]

Recordemos que con **-q** obtenemos únicamente los identificadores de las imágenes listadas y aprovechándonos de ello podríamos utilizar **docker rmi** con esto para eliminar únicamente aquellas imágenes que no son funcionales y por ende no nos interesan.

`docker rmi $(docker images --filter "dangling=true" -q)`

Si hemos detenido la construcción del contenedor en el modo interactivo, lo mejor será borrar también la imagen dada de Ubuntu para evitar errores. Para evitar que en la construcción nos entre en el modo interactivo, tendríamos que agregar al inicio de las instrucciones la palabra clave **ENV** pasándole **DEBIAN_FRONTEND noneinteractive**, de esta forma ya no entraría en el modo interactivo:

![[Docker/Construccion/images/023.png]]

Al ya tener la imagen creada, si ahora nosotros con esto ejecutáramos el contenedor, lo que sucedería es que se apagaría automáticamente debido a la instrucción del **ENTRYPOINT**, ya que solo la ejecuta y no hay nada más que hacer. Para evitar esto tendremos que ejecutar una terminal bash para que esto nos permita seguir teniendo activo el contenedor:

![[Docker/Construccion/images/024.png]]

Con ello volveríamos a construir la imagen:

`docker build -t web_server .`

Veremos cómo ahora lo hará mucho más rápido, saltándose únicamente a lo que hemos modificado.

Si ahora que vayamos a ejecutar nuestro contenedor vemos que al hacer **docker ps** no lo muestra como activo, esto se deberá a que se estaba utilizado **systemctl start**, para Debian es más usual **service \[sevice_)name] start**, en este caso utilizaremos **service** para iniciar el servicio **apache2** y ya con eso no tendríamos problema al construir nuevamente la imagen y ejecutar el contenedor con la misma.

Aquí entra en juego directamente el concepto de port forwarding, con la opción **-p** indicaremos un argumento el cual estará como "PORT:PORT", donde el primer puerto pertenecerá al puerto de nuestro host, mientras que el segundo al puerto donde el contenedor tiene corriendo el servicio:

`docker run -dit -p 80:80 web_server`

Con ello ejecutaremos el contenedor y si vemos que sigue corriendo, ahora lo interesante es que mediante nuestro host en el puerto 80 asignado, podremos ver el servicio web que se encuentra corriendo en el contenedor:

![[Docker/Construccion/images/025.png]]

Esta es la imagen que muestra por defecto el propio servicio de apache al ejecutarse, por lo tanto, veremos cómo ya se está ejecutando. 

El concepto de port forwarding es muy interesante, ya que nos permite proveer los servicios desde la máquina host, pero si en algún momento el servicio llega a ser vulnerado, el atacante realmente estará dentro del contenedor y no dentro de la máquina host, lo cual a nivel de seguridad es muy bueno, ya que se evita que un atacante pueda directamente modificar el servidor si llega a vulnerar un servicio.

En Linux tenemos la herramienta **lsof** que mediante su opción **-i** nos permite adjuntar con puntos dobles un puerto para ver qué servicio lo está ocupando. Al hacerlo, veremos que está ocupado por el servicio que hemos desplegado:

`lsof -i:80`

Ahora podremos obtener una bash del contenedor que se encuentra corriendo e ir al directorio **/var/www/html/** el cual es un directorio común cuando se despliega un servidor con apache o nginx, el cual se tiene como principal y aquí deberíamos tener nuestro index.html:

![[Docker/Construccion/images/026.png]]

Nosotros podríamos borrar el index.html y recordemos cómo al ser la ruta principal nos interpretaría lo que está dentro de ella. Además, al momento de crear el Dockerfile agregamos que se instalara de forma automática php, por lo que si en esta ruta agregamos un archivo php debería de interpretarlo. 

Borraríamos el **index.html** y crearíamos un **index.php**. En este agregaríamos un script PHP el cual nos permita la ejecución de comandos desde un argumento **cmd** al cual se le pueda asignar algo como un comando.

El código PHP sería el siguiente: 

Primeramente, para verificar que si nos interprete el código php, realizaríamos un echo de un mensaje y al recargar la página en el navegador tendríamos que verlo:

```php
<?php
	echo "Hola esta es una prueba";
?>
```

![[Docker/Construccion/images/027.png]]

Ahora que sabemos que el servidor es capaz de interpretarnos código php, imaginemos que un atacante es capaz de subir el siguiente script **cmd.php**:

```php
<?php
	echo "<pre>" . shell_exec($_GET['cmd']) . "</pre>"
?>
```

Ahora con esto, eliminando el index.php, lo que hace el script es utilizar etiquetas pre formateadas, podriamos ejecutar un comando y mostrarlo directamente con **shell_exec** lo cual toma del enlace el parámetro **cmd** y su valor lo ejecuta como si de un valor se tratase. 

Al hacerlo de forma directa, el output lo veríamos todo en una sola línea, pero si jugamos con "\<pre>" que serían las etiquetas pre formateadas, lo que nos ayuda esto es a ver el output de cualquier comando de forma ordenada y organizada con sus saltos de línea.

Ahora en la página podríamos seleccionar el script y agregarle **?cmd=\[Comando]**:

![[Docker/Construccion/images/028.png]]

De esta manera, ahora es capaz de tomar el comando que le enviamos a través del parámetro en la url y ejecutarlo gracias al archivo **cmd.php**. La cosa es que con esto, si ha sido vulnerado, podrás pensar que ya has vulnerado la máquina, pero si ahora ejecutásemos un comando que nos dé la IP de la máquina, veríamos que no pertenecería a la misma que esté sirviendo al público el servicio que sería el servidor como tal, sino que la IP pertenecería al segmento propio de Docker debido a que lo que se ha vulnerado es el contenedor:

![[Docker/Construccion/images/029.png]]

## Monturas

Las monturas en un contenedor prácticamente son la posibilidad de compartir recursos de la máquina host con el contenedor, de tal forma que los cambios efectuados en el contenedor se verían reflejados en el archivo de la máquina host y viceversa. 

Suponiendo que ahora mismo no tenemos ningún contenedor existente, nos enfocaríamos nuevamente en nuestro Dockerfile, en la ruta donde está el mismo. Crearíamos un archivo **prueba.txt** y escribiríamos algo en el, como "Hola esto es una prueba".

Al tener estos dos archivos, al momento de correr el contenedor podríamos utilizar la opción **-v** la cual nos permitirá utilizar una montura con una sintaxis de dos rutas separadas por puntos dobles. Antes de los dos puntos iría la ruta del host y después de los dos puntos la ruta del contenedor donde se mostrarían los recursos.

```shell
docker run -dit -p 80:80 -v /host-path:/container-path --name myContainer id_imagen
```

En este caso, si quisiéramos compartir la ruta donde tenemos el Dockerfile y prueba.txt con la ruta **/var/www/html/** del contenedor, sería con el comando anterior, colocando cada una de las rutas, después al abrir el navegador lo veríamos de la siguiente manera:

![[Docker/Construccion/images/030.png]]

Si ahora abrimos el archivo txt, veremos que es el mensaje del archivo que se encuentra en la máquina host:

![[Docker/Construccion/images/031.png]]

Lo interesante aquí, es que si modificamos el archivo desde la máquina host o desde el contenedor, el archivo sufrirá el cambio en ambas partes debido a que se está compartiendo y es como si fuese un enlace directo. 

Maniéndose como archivo principal el que está en el host, podríamos verlo algo así como si de un link simbólico se tratase, pero evidentemente no es lo mismo.

Una forma de aprovechar las monturas sería, por ejemplo, en archivitos que sean o funcionen como base de datos. De esta forma siempre mantendríamos actualizados a un archivo, el cual a su vez puede compartirse con otro contenedor o recursos, sin tener el problema de tener que trabajar con distintas versiones de un archivo.

## COPY

Una alternativa a las monturas es copiar el contenido de nuestra máquina host a un lugar del contenedor. Esto lo podemos hacer con el prefijo **COPY** en el Dockerfile, indicando primeramente el recurso de la máquina host y posteriormente el lugar del contenedor en donde se almacenará:

![[Docker/Construccion/images/032.png]]

En este caso, para el archivo prueba.txt no indicamos la ruta absoluta debido a que se encuentra en el mismo directorio del Dockerfile y ahora podremos construir nuevamente la imagen y luego lanzar el contenedor con esta imagen:

![[Docker/Construccion/images/033.png]]

Al ejecutar el contenedor ya no utilizaríamos monturas y con ello ya tendremos el archivo copiado dentro del contenedor y este no sufrirá cambios en la máquina host si lo editamos desde el contenedor.

## docker logs

Con el comando **docker logs** podremos pasarle el id de un contenedor y ver que es lo que ha sucedido en un contenedor referente a los logs e incluso si quisiéramos utilizar al final el parámetro **-f** para estar en escucha de nuevos logs y visualizarlos cuando algo suceda en el momento.

`docker logs id_contenedor` o `docker logs id_contenedor -f`
# Siguientes apuntes

[[Despliegue de máquinas vulnerables con Docker-Compose (1-2)]]