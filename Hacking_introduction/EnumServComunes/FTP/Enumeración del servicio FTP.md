
# Índice


# Introducción

En este caso mostraremos cómo se podría enumerar el servicio FTP (**File Transfer Protocol**) para recopilar información que pueda ser de ayuda para determinar cómo avanzar.

FTP es un protocolo ampliamente utilizado para la **transferencia de archivos** en redes. La enumeración del servicio FTP implica recopilar información relevante, como la versión del servidor FTP, la configuración de permisos de archivos, los usuarios y las contraseñas (mediante ataques de fuerza bruta o guessing), entre otros.

Enlace al primer proyecto de github:

- [Primer proyecto](https://github.com/garethflowers/docker-ftp-server)

En el primer proyecto emplearemos un ataque de fuerza bruta. Para ello utilizaremos la herramienta **Hydra**. Hydra es una herramienta de pruebas de penetración de código abierto que se utiliza para realizar ataques de fuerza bruta contra sistemas y servicios protegidos por contraseña. La herramienta es altamente personalizable y admite una amplia gama de protocolos de red, como HTTP, FTP, SSH, Telnet, SMTP, entre otros. 

El otro proyecto utilizado permite la autenticación de usuarios invitados para FTP, este es el proyecto **docker-anon-ftp** de **metabrainz**.

- [Segundo proyecto](https://github.com/metabrainz/docker-anon-ftp)

# Práctica

## Ataque de fuerza bruta

Para el primer proyecto, nos iremos al readme y copearemos las primeras líneas que nos aparecen del comando de docker:

```shell
docker run \
	--detach \
	--env FTP_PASS=123 \
	--env FTP_USER=user \
	--env PUBLIC_IP=192.168.0.1 \
	--name my-ftp-server \
	--publish 20-21:20-21/tcp \
	--publish 40000-40009:40000-40009/tcp \
	--volume /data:/home/user \
	garethflowers/ftp-server
```

Esto nos ayudará a desplegar el contenedor con el servicio FTP, el cual contenga un usuario y una contraseña. En este caso realizaremos unos cambios antes de ejecutar el comando:

```shell
docker run \
	--detach \
	--env FTP_PASS=louise \
	--env FTP_USER=s4mmy \
	--env PUBLIC_IP=192.168.0.1 \
	--name my-ftp-server \
	--publish 20-21:20-21/tcp \
	--publish 40000-40009:40000-40009/tcp \
	--volume /data:/home/user \
	garethflowers/ftp-server
```

Se modificó la línea del usuario y la contraseña, el usuario podrá ser el que deseemos y, en cuanto a contraseña, en este caso emplearemos una del diccionario de contraseñas **rockyou.txt**. Este es un diccionario que contiene más de 14 millones de contraseñas. 

En este casi tomamos específicamente la línea 132, siendo la contraseña **louise**.

Con ello desplegaríamos el entorno en un contenedor de docker y finalmente podríamos loguearnos al mismo con ftp, indiciando el usuario y contraseña que colocamos en el comando:

![[EnumServComunes/FTP/images/001.png]]

En este caso sabemos usuario y contraseña, pero como veremos cómo enumerar este servicio, nos enfocaremos a con NMAP lanzar un escaneo hacia nuestro propio host, el cual lance los scripts más comunes y descubra además las versiones de los servicios que se encuentran corriendo:

```shell
nmap -sCV 127.0.0.1
```

Este escaneo nos descubrirá los servicios en los puertos, así como su versión, y además lanzará los scripts más comunes para descubrimiento de posibles cosas interesantes que podrían ser de ayuda.

Existe un script que se lanza entre los comunes, el cual es **ftp-anom** el cual verifica si el usuario Anonymous está activo, ya que, este usuario permitiría conectarse sin proporcionar una contraseña y empezar a subir o descargar archivos de este servicio. 

En este caso no encontró el usuario Anonymous activo, debido a que no lo reportó en el escaneo:

![[EnumServComunes/FTP/images/002.png]]

Como hemos colocado una contraseña del diccionario **rockyou**, lo que haremos será tomar las primeras 200 líneas de este archivo y crearnos un archivo **password.txt** el cual utilizaremos como diccionario para un ataque de fuerza bruta con **hydra**:

```shell
cat /usr/share/wordlists/rockyou.txt | head -n 200 > passwords.txt
```

Finalmente, utilizarmeos hydra con el siguiente comando:

```shell
hydra -l sammy -P passwords.txt ftp://127.0.0.1 -t 2
```

Cuando vamos a hacer un ataque con hydra, el parámetro en letra mayúscula es para indicar una lista y en minúscula para indicar un único elemento. Esto nos puede servir, por ejemplo, para intentar una sola contraseña para diversos usuarios, donde ahora **-l** sería **-L** y le pasaríamos un archivo con distintos usuarios. Mientras que **-P** ahora sería **-p** y le pasaríamos una única contraseña a probar con cada uno de los usuarios de la lista. 

Emplear el ataque con una mayor cantidad de hilos podría llegar a cerrar el contenedor debido a la cantidad de errores que pueden llegar a darse al momento del ataque. Una de las cosas que podremos hacer es agregar la siguiente línea al inicio del comando **docker run** al momento de desplegar el contenedor `--restart unless-stopped`. Esto hace que si en algún punto se detiene, se vuelva a levantar el contenedor.

Para evitar tumbar el contenedor, trabajamos el ataque únicamente con 2 hilos, aunque esto hace que vaya un poco más lento:

![[EnumServComunes/FTP/images/003.png]]

Vemos cómo nos ha encontrado la contraseña para el usuario que hemos colocado. En este caso, desplegando el contenedor nuevamente, yo he asignado el usuario **sammy** y ha encontrado la contraseña.

## Usuario anonymous
# Siguientes apuntes