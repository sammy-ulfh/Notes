# Índice

- [[#Introducción]]
- [[#docker build]]
- [[#docker pull]]
- [[#docker images]]
- [[#Práctica]]
- [[#docker pull]]
- [[#Actualización de Dockerfile]]
- [[#Siguientes apuntes]]
# Introducción

Para crear imágenes de Docker, es necesario tener un archivo **Dockerfile** que defina la configuración de la imagen. Una vez que se tiene el Dockerfile, se puede utilizar el comando **docker build** para construir la imagen. Este comando buscará el archivo **Dockerfile** en el directorio actual y utilizará las instrucciones definidas en el mismo para construir la imagen. 

Algunas de las instrucciones que veremos en la práctica son:
## docker build

Sintaxis **básica**:

`docker build [opciones] ruta_al_Dockerfile`

El parámetro **-t** se utiliza para etiquetar la imagen con un nombre y una etiqueta. Por ejemplo, si se desea etiquetar la imagen con un nombre **mi_imagen** y la etiqueta **v1**, se puede utilizar la siguiente sintaxis:

`docker build -t mi_imagen:v1 .`

El punto (**.**) al final del comando en el apartado de la ruta, se utiliza para indicar que busque el Dockerfile en el directorio actual. Por ejemplo, si nos encontramos en el directorio **/home/usuario/proyecto/** y aquí tenemos nuestro Dockerfile, sería lo mismo colocar el punto (**.**) o la ruta completa:

- `docker build -t mi_imagen:v1 /home/usuario/proyecto/`
- `docker build -t mi_imagen:v1 .`

De la misma forma, si el Dockerfile se encuentra en una ruta distinta a la que nos encontramos, solo sería colocar la ruta absoluta de donde se encuentra y crearía la imagen del mismo.

## docker pull

**docker pull** es el comando que se utiliza para descargar imágenes de Docker desde un registro de imágenes, algo similar a **PiPy** de Python, donde los usuarios pueden crear y publicar sus imágenes para después ser descargadas y utilizadas por otros. 

Sintaxis básica:

`docker pull nombre_de_la_imagen:etiqueta`

Por ejemplo, si se busca descargar la imagen **ubuntu** con la etiqueta **latest**, se puede hacer de la siguiente manera:

`docker pull ubuntu:latest`

## docker images

**docker images** es el comando que se utiliza para listar las imágenes de Docker que están disponibles en el sistema.

Sintaxis:

`docker images [opciones]`

Durante la construcción de la imagen, Docker descargará y almacenará en la caché las capas de la imagen que se han construido previamente, lo que hace que las compilaciones posteriores sean más rápidas.
# Práctica

Con el archivo Dockerfile que anteriormente creamos, vamos a generar una imagen a la cual le daremos un nombre y etiqueta, quedando el comando como:

`docker build -t my_image:v1 .`

De esta forma le estamos diciendo que busque en el directorio actual el Dockerfile y le asigne el nombre **my_image** y la etiqueta **v1**.

![[Docker/Construccion/images/001.png]]

Cuando se construye la imagen, veremos cómo va paso a paso construyéndola y, en este caso, primeramente descargo la última de Ubuntu para construirla a partir de ello y finalmente agrego lo del MAINTAINER. 

Ahora podríamos listar las imágenes que tenemos creadas:

`docker images`

![[Docker/Construccion/images/002.png]]

Con ello veremos como aislado a la de Ubuntu, ya que se ha descargado también para construir la nuestra. Tenemos la que hemos creado nosotros.

## docker pull

Si nosotros quisiéramos descargar una imagen de Debian en su última versión, tendríamos que utilizar **docker pull** indicando su nombre y tag (para la última versión no es obligatorio).

`docker pull debian:latest`

Con ello nos descargaría la imagen y si listáramos las imágenes de nuevo, ahora también tendríamos la imagen de la última versión de Debian. Esta incluso podríamos utilizarla para crear un contenedor, al igual que las otras que tenemos disponibles.

## Actualización de Dockerfile

Cuando nosotros tenemos nuestro Dockerfile, podremos seguir editándolo después de haber creado la imagen y por cada cambio que realicemos tendremos que hacer un **docker build**. Lo cómodo de esto es que Docker va guardando en caché los **build** anteriores y, por lo tanto, en nuevos cambios no irá construyendo la imagen nuevamente de inicio a fin, sino que se saltara todos esos cambios que ya se encuentren aplicados y solo aplicara los nuevos, ofreciendo una mayor velocidad al realizar cambios o agregar nuevas instrucciones.
# Siguientes apuntes

[[Carga de instrucciones en Docker y desplegando nuestro primer contenedor]]