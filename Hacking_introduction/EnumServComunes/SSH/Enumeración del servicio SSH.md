# Índice

# Introducción

Nos enfocaremos en la explotación del servicio SSH (**Secure Shell**), aprenderemos a cómo realizar reconocimiento para recopilar información sobre los sistemas que ejecutan este servicio. 

SSH es un protocolo de administración remota que permite a los usuarios **controlar** y **modificar** sus servidores remotos a través de internet mediante un mecanismo de **autenticación seguro**. Como una alternativa más segura al protocolo **Telnet**, que transmite información sin cifrar, SSH utiliza **técnicas criptográficas** para garantizar que todas las comunicaciones hacia y desde el servidor remoto estén cifradas.

SSH proporciona un mecanismo para autenticar un usuario remoto, transferir entradas desde el cliente al host y retransmitir la salida de vuelta al cliente. Esto es especialmente útil para administrar sistemas remotos de manera segura y eficiente, sin tener que estar físicamente presentes en el sitio. 

Primer proyecto que utilizaremos para desplegar el contenedor:

- [Primer proyecto](https://hub.docker.com/r/linuxserver/openssh-server)

Además, a través de la versión SSH también podremos identificar el codename de la distribución que se está ejecutando en el sistema. 

Por ejemplo, si la versión del servicio es **OpenSSH 8.2p1 Ubuntu 4ubuntu0.5**. Podemos determinar que el sistema está ejecutando una distribución de Ubuntu. El número de versión **4ubuntu0.5** se refiere a la revisión específica del paquete de SSH en esa distribución de Ubuntu. A partir de esto, podemos identificar el **codename** de la distribución de Ubuntu, que en este caso sería **Focal** para Ubuntu 20.04.

La búsqueda sobre la distribución que pudiese estar corriendo el sistema, la realizamos sobre el sitio de **launchpad.net**, donde indicamos la versión encontrada del servicio corriendo y nos retorna el **codename** para saber ante qué nos estamos enfrentando.

- [Launchpad - Ubuntu](https://launchpad.net/ubuntu)

# Práctica

## SSH

SSH es un servicio el cual nos permite acceder a una terminal interactiva de forma segura y con tráfico codificado de un ordenador para controlarlo remotamente. 

SSH es un servicio que se implementó como mejora al servicio de Telnet, el cual no utilizaba ninguna técnica de cifrado en su tráfico. 

Por lo tanto, el servicio SSH es una buena herramienta que permite controlar un ordenador de forma remota y segura para realizar cambios o configuraciones en una infraestructura de ordenadores o equipos electrónicos conectados a la red.
## Desplegando el entorno

Nos iremos a la página del proyecto dada en la introducción, luego buscaremos entre la documentación el comando de Docker que ayuda a desplegar el contenedor, en este caso el siguiente:

```shell
docker run -d \
  --name=openssh-server \
  --hostname=openssh-server `#optional` \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e PUBLIC_KEY=yourpublickey `#optional` \
  -e PUBLIC_KEY_FILE=/path/to/file `#optional` \
  -e PUBLIC_KEY_DIR=/path/to/directory/containing/_only_/pubkeys `#optional` \
  -e PUBLIC_KEY_URL=https://github.com/username.keys `#optional` \
  -e SUDO_ACCESS=false `#optional` \
  -e PASSWORD_ACCESS=false `#optional` \
  -e USER_PASSWORD=password `#optional` \
  -e USER_PASSWORD_FILE=/path/to/file `#optional` \
  -e USER_NAME=linuxserver.io `#optional` \
  -e LOG_STDOUT= `#optional` \
  -p 2222:2222 \
  -v /path/to/openssh-server/config:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/openssh-server:latest
```

Con esto en mente, realizaremos algunos cambios en los argumentos opcionales.

```shell
docker run -d \
  --name=openssh-server \
  --hostname=sammy_pc \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e PASSWORD_ACCESS=true \
  -e USER_PASSWORD=louise \
  -e USER_NAME=sammy \
  -p 2222:2222 \
  -v /path/to/openssh-server/config:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/openssh-server:latest
```

Cambiamos el nombre de la máquina host, eliminamos las referencias a una llave pública y el sudo access. El acceso por contraseña lo habilitamos y colocamos tanto nombre de usuario como contraseña, eliminando el user password file y el log del stdout. 

El port forwarding que se aplica es que nuestro puerto 2222 sea el puerto 2222 del contenedor. Si queremos, nosotros podríamos hacer que nuestro puerto 22 sea el puerto 2222 del contenedor. En este caso lo dejaremos como ya está.

## SSH

Cuando tengamos el contenedor desplegado, podremos ver que ya está corriendo y, por ende el servicio SSH en nuestro puerto 2222. Podremos conectarnos a ssh con el siguiente comando:

```shell
ssh username@localhost -p 2222
```

En este caso, el nombre de usuario dado en el comando fue sammy y el parámetro **-p**, es para indicar el puerto, ya que por defecto el que toma es el 22.

![[EnumServComunes/SSH/images/001.png]]

## Ataque de fuerza bruta

Lo que hemos hecho es asignarle nuevamente una contraseña que se encuentre en el rockyou.txt, con ello aplicaremos un ataque de fuerza bruta a este servicio para el usuario **sammy**.

```shell
hydra -l sammy -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1 -p 2222 -t 4
```

Si vemos que el contenedor nos da problemas, debido a que puede ser posible que el propio contenedor se autoproteja a este tipo de ataques y se cierre automáticamente. 

De ser el caso, podríamos nosotros agregar un nuevo usuario a nuestra máquina y asignarle la misma contraseña "**louise**", que se encuentra en el diccionario de contraseñas.

Con ello, podríamos levantar el servicio SSH en nuestro ordenador, este si se levantará en el puerto 22. Finalmente, podríamos aplicar en ataque, pero tendríamos que hacerlo con una cantidad baja de hilos para que no llegue a dar errores debido a las configuraciones de SSH. 

Lo haremos a un total de 2 hilos:

```shell
hydra -l sam -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1 -t 2
```

![[EnumServComunes/SSH/images/002.png]]

Si en el ataque con hydra quisiéramos indicar un puerto para el servicio SSH al que estamos aplicando el ataque de fuerza bruta está en un puerto distinto al 22, podríamos agregar un puerto específico con el parámetro **-s**.
# Siguientes apuntes