# Índice

# Introducción

Docker Compose es una herramienta de orquestación de contenedores que permite definir y ejecutar aplicaciones multi-contenedor de manera fácil y eficiente. Con Docker Compose, podemos describir los diferentes servicios que componen nuestra aplicación en un **archivo YAML** y, a continuación, utilizar un solo comando para ejecutar y gestionar todos estos servicios de manera coordinada.

En otras palabras, Docker Compose nos permite definir y configurar múltiples contenedores en un solo archivo YAML, lo que simplifica la gestión y la coordinación de múltiples contenedores en una sola aplicación. Esto es especialmente útil para aplicaciones complejas que requieren la interacción de varios servicios diferentes, ya que Docker Compose permite definir y configurar fácilmente la conexión y la comunicación entre estos servicios.

## Enlaces

- [Repositorio Vulhub](https://github.com/vulhub/vulhub)
- [Node JS Reverse Shell](https://github.com/appsecco/vulnerable-apps/tree/master/node-reverse-shell)
# Práctica

## Mostrando el entorno

Si vemos el **About** del repositorio, veremos que es un repositorio que almacena proyectos de entornos vulnerables pre construidos en Docker Compose. 

Cuando nosotros construimos un entorno con Docker, tenemos una infinidad de opciones, las cuales, cuando ya trabajamos, Docker de una forma más avanzada, pueden llegar a quedarnos un comando gigante de tantas opciones que tiene además de las que hemos visto.

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
# Siguientes apuntes