# Índice

- [[#Introducción]]
- [[#Enlaces]]
- [[#Práctica]]
- [[#Mostrando el entorno]]
- [[#Desplegando el entorno]]
- [[#Siguientes apuntes]]
# Introducción

Docker Compose es una herramienta de orquestación de contenedores que permite definir y ejecutar aplicaciones multi-contenedor de manera fácil y eficiente. Con Docker Compose, podemos describir los diferentes servicios que componen nuestra aplicación en un **archivo YAML** y, a continuación, utilizar un solo comando para ejecutar y gestionar todos estos servicios de manera coordinada.

En otras palabras, Docker Compose nos permite definir y configurar múltiples contenedores en un solo archivo YAML, lo que simplifica la gestión y la coordinación de múltiples contenedores en una sola aplicación. Esto es especialmente útil para aplicaciones complejas que requieren la interacción de varios servicios diferentes, ya que Docker Compose permite definir y configurar fácilmente la conexión y la comunicación entre estos servicios.

## Enlaces

- [Repositorio Vulhub](https://github.com/vulhub/vulhub)
- [Node JS Reverse Shell](https://github.com/appsecco/vulnerable-apps/tree/master/node-reverse-shell)
# Práctica

## Mostrando el entorno

Si vemos el **About** del repositorio, veremos que es un repositorio que almacena proyectos de entornos vulnerables pre construidos en Docker Compose. 

Cuando nosotros construimos un entorno con Docker, tenemos una infinidad de opciones, las cuales, cuando ya trabajamos, Docker de una forma más avanzada, pueden llegar a quedarnos un comando gigante de tantas opciones que tiene, además de las que hemos visto.

Para evitar esto, tenemos justamente **docker-compose** que lo que nos permite es configurar todas estas opciones en un archivo **.yml**. Esto podremos verlo si en el repositorio de github buscamos por **Kibana** utilizando **CTRL + F**, ya que nos abrirá un filtro para filtrar por este texto en la página y al final es una carpeta:

![[Docker/MaquinasVulnerbales/images/001.png]]

En este caso, al no saber que es Kibana, algo muy importante es siempre por nuestra cuenta investigar qué son las cosas que nos llegamos a encontrar, ya que no tendremos el conocimiento de todo lo posible que encontremos.

![[Docker/MaquinasVulnerbales/images/002.png]]

Aquí las cosas que no lleguemos a entender también será bueno buscarlo por nuestra cuenta para saber a qué nos enfrentamos. En este caso sabemos que Kibana es una herramienta la cual nos ayuda a mostrar de forma visual datos. 

Cuando nosotros nos metemos en esta carpeta en el repositorio, veremos lo siguiente:

![[Docker/MaquinasVulnerbales/images/003.png]]

En este caso nos enfocaremos en **CVE-2018-172246**.

![[Docker/MaquinasVulnerbales/images/004.png]]

En este caso, leyendo el Readme, veremos cómo nos es mencionado que esto tiene una vulnerabilidad **Local File Inclusion**. Este es un tipo de vulnerabilidad que se verá de forma más completa más adelante. 

Básicamente, lo que esta vulnerabilidad permite es de forma externa nosotros, como atacante desde el servicio web, apuntar a un archivo local de la máquina que provee el servicio, lo que incluso nos llegaría a dar la capacidad de listar el contenido de un archivo dado.

Podremos verlo más claro al querer listar el archivo **/etc/passwd** del servicio web que esté corriendo, desde luego, esto es algo que, aunque esté corriendo en un contenedor o directamente en el host, no debería estar visible, pero esta vulnerabilidad lo permitirá si se apunta a este directamente.

La vulnerabilidad **Local File Incluso** será muy común escucharla como **LFI**. Incluso en ocasiones hay vías potenciales en las que un **LFI** lo podremos convertir en un **Remote File Inclusion (RMI)**, lo cual ya nos permite ejecutar comando en la máquina que provee el servicio.

Si ahora viésemos el archivo **.yml** del repositorio, veremos la siguiente estructura:

![[Docker/MaquinasVulnerbales/images/005.png]]

Si vemos bien, esto como servicio despliega el servicio de kibana en el puerto **5601** de la máquina host y del contenedor. Si observamos bien, despliega incluso dos contenedores de dos imágenes.

Para desplegar todo esto, cuando lo tengamos nosotros en nuestro ordenador, tendremos que ejecutar el comando:

`docker compose up -d`

Que nos lo menciona en el mismo archivo README. Esto buscará un archivo **docker-compose** para utilizarlo para desplegar todo el entorno vulnerable.

## Desplegando el entorno

Para tener esto en nuestro ordenador tendremos que traernos la carpeta que contiene el entorno vulnerable a nuestra máquina, desde luego el utilizar el comando **git clone** con toda la ruta actual en la que nos encontramos nos dará error, ya que esto solo funciona para traernos el repositorio completo. 

Para este tipo de detalles tenemos la utilidad **svn** con el comando **checkout** y pasándole nuestra URL que en este caso es `https://github.com/vulhub/vulhub/tree/master/kibana/CVE-2018-17246`, pero le quitaremos **tree/master** para colocar en su lugar **trunk**:

```shell
svn checkout https://github.com/vulhub/vulhub/trunk/kibana/CVE-2018-17246
```

Si esto llega a fallar, otra opción es utilizar una utilidad en línea, la cual es [Downgit](https://downgit.github.io) y pegando el enlace real de la sub carpeta en la que nos encontremos, esto nos permitirá descargarlo. 

Esta herramienta nos descargará un archivo que tendremos que descomprimir. Finalmente, lo tendríamos en nuestro ordenador:

![[Docker/MaquinasVulnerbales/images/006.png]]

Con ello ya podremos ejecutar el comando:

`docker-compose up -d`

Esto buscaría un archivo **docker-compose** en el directorio actual y nos permitirá desplegar el entorno vulnerable. 

Si no llega a funcionar, también tendremos que instalar la herramienta de **docker-compose** con nuestro instalador de la terminal del sistema. Con ello ya solo quedaría a esperar a que se desplieguen los contenedores y todo el entorno correctamente.

Con ello veremos que ya estará todo montado e incluso podríamos ver qué es lo que está corriendo desde el navegador:

![[Docker/MaquinasVulnerbales/images/007.png]]

![[Docker/MaquinasVulnerbales/images/008.png]]

Viendo nuevamente el repositorio, nos enfocaremos directamente en el **LFI**, a lo cual nos muestra la ruta:

```WEB
http://your-ip:5601/api/console/api_server?sense_version=%40%40SENSE_VERSION&apis=../../../../../../../../../../../etc/passwd
```

Podremos ver que esto es una ruta del servicio de kibana que estamos corriendo y al final se encuentra un parámetro **apis** el cual nos permite apuntar a un archivo del directorio dado, pero vemos que no está sanitizado e incluso nos permite movernos entre el sistema e ir a rutas importantes para llegar a apuntar a archivos importantes como lo es el **/etc/passwd**. 

Esto podremos probarlo desde la misma terminal haciendo una petición GET con curl:

```
curl -s -X GET "http://localhost:5601/api/console/api_server?sense_version=%40%40SENSE_VERSION&apis=../../../../../../../../../../../etc/passwd"
```

Lo cual nos llevará a un error en el servidor, pero si vemos el repositorio, este nos menciona que si llegamos a checar los logs del entorno con **docker-compose logs**, llegaremos a ver el contenido del archivo:

![[Docker/MaquinasVulnerbales/images/009.png]]

Podrás pensar que esto no es de ayuda, ya que al no tener control sobre el servidor y el entorno en docker no tendría sentido. La cosa aquí es que al ser capaz de permitirnos apuntar a archivos en el entorno, aunque no pueda ver los logs, esto solo lo podremos ver para saber que funciona. 

Pero realmente la forma en la que nosotros podríamos aprovechar esta vulnerabilidad de **LFI**, si mediante otro tipo de vulnerabilidad somos capaces de llegar a subir un archivo malicioso el cual permita darnos una reverse Shell y apuntando a este archivo se ejecutaría y al nosotros estar en escucha recibiríamos la consola interactiva.

Para ello, obtendremos una terminal interactiva en el docker-compose y simular de alguna manera que este archivo lo ha logrado subir el atacante. En este caso, nosotros crearemos un archivo **Reverse.js** en el directorio tmp y obtendremos una bash del contenedor con:

```shell
docker-compose exec kibana bash
```

En el contenedor no tendremos nano y si llega a dar error al instalarlo es por los repositorios que contiene de debian, por ende nos enfocaremos en el archivo **/etc/apt/sources.list**, a este lo dejaremos vacío y únicamente con la línea **deb http://archive.debian.org/debian/ jessie contrib main non-free**:

```shell
echo 'deb http://archive.debian.org/debian/ jessie contrib main non-free' > /etc/apt/sources.list
```

Con ello podremos hacer un update nuevamente y finalmente instalar nano. 

Con esto listo, creamos el archivo **Reverse.js** en el directorio **/tmp** y lo abriremos con nano. En su interior pegaremos el contenido del archivo que nos puede otorgar un reverse shell mencionado en la parte de introducción.

El código que nos dará para la reverse shell está en el mismo Readme. 

Lo que editaremos de esto será la IP colocando la de nuestra interfaz de docker para que se pueda dar la comunicación del contenedor con nuestra máquina host, ya que tendremos que poner la nuestra donde estaremos en escucha y en este caso utilizaremos el puerto 443.

![[Docker/MaquinasVulnerbales/images/010.png]]

Con ello ya tendremos el archivo en el contenedor que se comunicará con la máquina host en el puerto 443 y nos dará una shell sh. Por ende, ahora podremos salirnos del contenedor y quedamos por escucha con netcat en el puerto 443. 

Con ello, ahora si volvemos a lanzar la petición con CURL, pero ahora apuntando al archivo **Reverse.js** del directorio **tmp**, veremos lo siguiente:

![[Docker/MaquinasVulnerbales/images/011.png]]

![[Docker/MaquinasVulnerbales/images/012.png]]

Con ello al ponernos en escucha primeramente y luego realizar la petición con curl, por detrás la vulnerabilidad del **LFI** interpreta el código de JavaScript del archivo al que se está apuntando y por ello al nosotros estar en escucha recibimos una conexión y si empezamos a ejecutar comandos, ya estaríamos en una terminal interactiva:

![[Docker/MaquinasVulnerbales/images/013.png]]

Al ver la IP, podremos ver que no es la de nuestra interfaz docker0, sino del propio contenedor. Si quisiéramos ver de forma más visual una terminal, podríamos ejecutar el comando **script /dev/null -c bash** y esto ya nos daría más visualmente una bash:

![[Docker/MaquinasVulnerbales/images/014.png]]

Con ello ya tendríamos de forma algo práctica y básica cómo se podría llegar a aprovechar una vulnerabilidad de **LFI** para obtener directamente una terminal del entorno al que estamos vulnerando.

Finalmente, con el conocimiento que ya tenemos, eliminaríamos tanto los contenedores como las imágenes para dejar todo vacío para posteriormente desplegar otro entorno vulnerable.
# Siguientes apuntes

[[Despliegue de máquinas vulnerables con Docker-Compose (2-2)]]