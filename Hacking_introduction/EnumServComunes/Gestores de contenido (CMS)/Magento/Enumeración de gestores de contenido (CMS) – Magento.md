
# Indice

- [[#Introducción]]
- [[#Practica]]
- [[#Despliegue]]
- [[#Enumeración]]
- [[#Explotación de vulnerabilidad SQLi]]
- [[#Siguientes apuntes]]
# Introducción

En esta ocasión se verá cómo enumerar el gestor de contenido __Magento__. Magento es una plataforma de comercio electrónico de código abierto, que se utiliza para construir tiendas en línea de alta calidad y escalables. Es una de las plataformas más populares para el comercio electrónico y es utilizada por grandes marcas como Nike, Coca-Cola y Ford. 

Sin embargo, con la popularidad de Magento también ha surgido la preocupación por la seguridad. Una de las herramientas que se mostrarán es __Magescan__, una herramienta de escaneo de vulnerabilidades específica para Magento.

__Magescan__ puede detectar vulnerabilidades comunes en Magento, incluyendo problemas con permisos de archivos, errores de configuración y vulnerabilidades conocidas en extensiones populares en Magento. 

Enlace a Magescan:`https://github.com/steverobbins/magescan`.

Su sintaxis y uso son bastante sencillos; ejemplo:

```shell
php magescan.phar scan:all https://example.com
```

Donde __magescan.phar__ es el archivo ejecutable de la herramienta __Magescan__, __scan:all__ es el comando específico de Magescan que indica que se realizará un escaneo exhaustivo de todas las vulnerabilidades conocidas en el sitio web objetivo y __https:\//example.com__ es la URL del sitio web objetivo que se escaneará en busca de vulnerabilidades. 

Enlace al laboratorio que se estará utilizando:`https://github.com/vulhub/vulhub/tree/master/magento/2.2-sqli`

Una de las técnicas que se explota sobre este laboratorio con este gestor de contenidos es la famosa __SQL injection__. Esta vulnerabilidad se produce cuando los datos de entrada no son debidamente validados y se pueden insertar comandos SQL maliciosos en la consulta a la base de datos. 

Un ataque de inyección SQL exitoso puede permitir al atacante obtener información confidencial, como credenciales de usuario o datos de pago, o incluso ejecutar comandos en la base de datos del sitio web.

En el caso del Magento desplegado, se explotará una inyección SQL con el objetivo de obtener una cookie de sesión, la cual podremos posteriormente utilizar para llevar a cabo un ataque de __Cookie Hijacking__. Este tipo de ataques nos permitirá, como atacantes, asumir la identidad del usuario legítimo y acceder a las funciones del usuario, que en este caso será administrador.
# Practica

## Despliegue

De la misma forma, tendremos que traer a nuestra computadora la carpeta que contiene el entorno vulnerable y lo desplegaremos con docker-compose:

```shell
docker-compose up -d
```

Una vez levantado nuestro laboratorio, podremos entrar a la página web local en el puerto 8080, donde realizaremos la configuración e instalación de Magento.

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/001.png]]


Al presionar el botón, lo siguiente será darle a __Next__, esperaremos a que se instale lo necesario y, cuando todo esté con palomitas, nuevamente __Next__, finalmente, colocaremos las siguientes configuraciones:

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/002.png]]

La contraseña en este caso es __root__, finalmente, podremos indicar en qué ruta queremos que esté nuestro login de administrador:

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/003.png]]

Cambiaremos el __admin_1tl30w__ por __administration__. Continuaremos dando Next hasta llegar a la parte de agregar un usuario administrador.

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/004.png]]

Finalmente, le damos a __Next__ e __Install Now__, con ello esperaremos a que finalice la instalación de Magento y lanzamos el Magento Admin, presionando el botón.

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/005.png]]

Si aquí colocamos las credenciales que agregamos cuando creamos el usuario de administrador, nos dejaría entrar:

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/006.png]]

## Enumeración

Para enumerar magen, utilizaremos la herramienta Magescan: `https://github.com/steverobbins/magescan`.

En este caso, en lugar de clonar el repositorio, podremos irnos a la versión más reciente en el apartado de __Releases__ y presionar en el archivo __magescan.phar__. Para poder correr magescan, tendremos que tener instalado PHP para ejecutarlo con PHP.

```shell
php magescan.phar
```

En este caso realizaremos un escaneo completo, por lo que tendremos que agregarle __scan:all__ y seguido el URL de la página que se encuentra corriendo sobre Magento:

```shell
php magescan.phar scan:all http://127.0.0.1:8080
```

Esto comenzará el escaneo y nos reportará múltiples rutas encontradas, entre otras cosas. En este caso específico no se nos muestra alguna vulnerabilidad crítica y común; por ende, no se reporta con magescan.

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/007.png]]

Llegamos a ver cómo en este caso la versión de Magento que se encuentra corriendo es la 2.2.
## Explotación de vulnerabilidad SQLi

Una vulnerabilidad con la que cuenta este laboratorio es con la capacidad de aplicar inyecciones SQL; para ello, el mismo repositorio nos comparte una prueba de concepto (PoC) y se nos da un script en Python3, el cual está en el siguiente enlace en formato raw:`https://raw.githubusercontent.com/ambionics/magento-exploits/refs/heads/master/magento-sqli.py`.

El tenerlo con el enlace anterior en este formato nos permite traerlo de forma directa a nuestro ordenador con curl o wget:

```shell
curl -o magento-sqli.py https://raw.githubusercontent.com/ambionics/magento-exploits/refs/heads/master/magento-sqli.py
```

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/008.png]]

En este caso nos da error porque espera como argumento el enlace de la web. 

Lo que hará este script es que, aprovechando la vulnerabilidad existente, extraerá una sesion actual activa, en este caso nosotros como administrador estamos logueados y si nos vamos a las herramientas de desarrollador en el navegador y luego a storage, veremos lo siguiente:

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/009.png]]

Tenemos un valor que dice __admin__, el cual prácticamente es nuestro token de sesión activa. Esto es un aspecto muy interesante, ya que estos tokens se generan para mantener una sesión activa sin que te esté pidiendo loguearte de forma muy continua, pero si por alguna razón un atacante logra tener tu token de sesión, bastaría con que el mismo lo coloque en su navegador para tener acceso a tu cuenta, como si fueses tú. 

En esto el atacante no tendrá ningún problema con el doble factor de autenticación ni con ninguna otra validación, ya que simplemente está tomando una sesión activa y abriéndola en otro navegador. El único inconveniente sucede cuando se cierra esa misma sesión, ya que así el atacante ya no podría tener acceso a una sesión no activa.

Por ende, encontrándonos logueados como administrador por un lago, le pasaremos al script de Python el enlace de la web:

```shell
python3 magento-sqli.py http://127.0.0.1:8080
```

Si todo va bien, nos detectará la sesión activa y empezará a mapear mediante fuerza bruta, carácter por carácter, los elementos que componen el token de sesión:

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/010.png]]

Si comparamos este ID que nos dio con el que está en el navegador, veremos que es el mismo:

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/011.png]]

Por lo tanto, sin cerrar esta sesión, podremos abrir otro navegador y, para poder manipular fácilmente los valores de cookies, instalaremos el addon de cookie-editor.

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/012.png]]

Ahora en este navegador podremos irnos a la misma página, al panel de administrador:

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/013.png]]

Con el addon modificamos el valor de __admin__ y le agregamos el token de sesión que hemos obtenido con el script. Al guardar y recargar, ahora estaremos dentro del panel de administración como si fuésemos el mismo usuario, del cual habremos secuestrado su sesión.

![[EnumServComunes/Gestores de contenido (CMS)/Magento/images/014.png]]

Si nos llega a pasar que nos diga que la sesión ha caducado, es porque la sesión principal caducó; bastaría con repetir el proceso abriendo una nueva sesión y hacerlo todo más rápido. Generalmente, los tokens de sesión suelen tener un tiempo de funcionalidad antes de que expiren y, una vez expiran, le piden al usuario loguearse nuevamente.
# Siguientes apuntes