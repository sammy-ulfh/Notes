
# Indice

- [[#Introducción]]
- [[#Practica]]
- [[#smbclient]]
- [[#smbmap]]
- [[#Conexión]]
- [[#Monturas]]
- [[#Crackmapexec]]
- [[#Siguientes apuntes]]

# Introducción

__SMB__ significa __Server Message Block__, es un __protocolo__ de comunicación de red utilizado para compartir archivos, impresoras y otros recursos entre dispositivos de red. Es un protocolo propietario de __Microsoft__ que se utiliza en sistemas operativos __Windows__. 

__Samba__ por otro lado, es una implementación libre y de código abierto del protocolo __SMB__, que se utiliza principalmente en sistemas operativos basados en Unix y Linux. Samba proporciona una manera de compartir archivos y recursos entre dispositivos de red que ejecutan sistemas operativos diferentes, como Windows y Linux.

Aunque SMB y Samba comparten una funcionalidad similar, existen algunas diferencias notables. SMB es un protocolo propietario de Microsoft, mientras que Samba es un proyecto de software libre y de código abierto. Además, SMB es una implementación más completa y compleja del protocolo, mientras que Samba es una implementación más ligera y limitada. 

Proyecto que se utiliza para la práctica de enumeración del servicio SMB:
`https://github.com/vulhub/vulhub/tree/master/samba/CVE-2017-7494`

Una de las herramientas que se utilizan para la fase de reconocimiento es __smbmap__. Smbmap es una herramienta de línea de comandos utilizada para enumerar recursos compartidos y permisos de un servidor SMB (Server Message Block) o Samba. Es una herramienta muy útil para la enumeración de redes y para la identificación de posibles vulnerabilidades de seguridad. 

Con smbmap, puedes enumerar recursos compartidos en un servidor SMB y obtener información detallada sobre cada recurso, como los permisos de acceso, los usuarios y grupos autorizados, y los archivos y carpetas compartidos. También puedes utilizar smbmap para identificar recursos compartidos que no requieren autenticación, lo que puede ser un problema de seguridad.

Además, smbmap permite a los administradores de sistemas y a los auditores de seguridad verificar rápidamente la configuración de permisos en los recursos compartidos en un servidor SMB, lo que puede ayudar a identificar posibles vulnerabilidades de seguridad y tomar medidas para remediarlas. 

A continuación, se proporciona una breve descripción de algunos parámetros comunes en smbmap:

- __-H__: Este parámetro se utiliza para especificar el host o dirección IP del servidor SMB al que se quiere conectar.
- __-P__: Este parámetro se utiliza para especificar el puerto TCP utilizado para la conexión SMB. El puerto predeterminado para SMB es 445, pero si el servidor SMB está configurado para utilizar un puerto diferente, este parámetro debe ser utilizado para especificar el puerto correcto.
- __-u__: Este parámetro se utiliza para especificar el nombre de usuario para la conexión SMB.
- __-p__: Este parámetro se utiliza para especificar la contraseña para la conexión SMB.
- __-d__: Este parámetro se utiliza para especificar el dominio al que pertenece el usuario que se está utilizando para la conexión SMB.
- __-s__: Este parámetro se utiliza para especificar el recurso compartido específico que se quiere enumerar. Si no se especifica, smbmap tendrá que enumerar todos los recursos compartidos en el servidor SMB.

Además, otra herramienta que se puede utilizar es __smbclient__. Smbclient es otra herramienta de línea de comandos utilizada para interactuar con servidores SMB y Samba, pero a diferencia de smbmap, que se utiliza principalmente para enumeración, smbclient proporciona una interfaz de línea de comandos para interactuar con los recursos compartidos SMB y Samba, lo que permite la descarga y subida de archivos, la ejecución de comandos remotos, la navegación por el sistema de archivos remoto, entre otras funcionalidades.

En cuanto a los parámetros más comunes de smbclient, algunos de ellos son:

- __-L__: Este parámetro se utiliza para enumerar los recursos compartidos en el servidor SMB o Samba.
- __-U__: Este parámetro se utiliza para especificar el nombre de usuario y la contraseña utilizados para la autenticación con el servidor SMB o Samba.
- __-c__: Este parámetro se utiliza para especificar un comando que se ejecutará en el servidor SMB o Samba.

Estos son algunos parámetros más comunes en smbclient, aunque existen otros disponibles. La lista completa de parámetros y sus descripciones se pueden encontrar en la documentación oficial de smbclient. 

Finalmente, otra de las herramientas que puede servir para enumerar el servicio Samba o SMB es __Crackmapexec__. Crackmapexec (CME) es una herramienta de prueba de penetración de línea de comandos que se utiliza para realizar auditorías de seguridad en entornos de Active Directory. CME se basa en las bibliotecas de Python __impacket__ y es compatible con sistemas operativos Windows, Linux y macOS.

__CME__ puede utilizarse para realizar diversas tareas de auditorías en entornos de Active Directory, como enumerar usuarios y grupos, buscar contraseñas débiles, detectar sistemas vulnerables y buscar vectores de ataque. Además, CME también puede utilizarse para ejecutar ataques de diccionarios de contraseñas, ataques __Pass-The-Hash__ y para explotar vulnerabilidades conocidas en sistemas Windows. Asimismo, cuenta con una amplia variedad de módulos y opciones de configuración, lo que la convierte en una herramienta muy flexible para la auditoría de seguridad en entornos Active Directory. La herramienta permite utilizar muchas de las tareas de auditoría comunes, lo que ahorra tiempo y aumenta la eficiencia del proceso de auditoría.

Enlace a la wiki para la instalación de Crackmapexec:`https://www.stationx.net/crackmapexec-cheat-sheet/`.
Funciona en ArchLinux: `https://snapcraft.io/install/crackmapexec/arch`

# Practica

Al hablar de Samba, hablamos de un conjunto de programas que permiten a los sistemas operativos basados en Unix compartir archivos, impresoras y otros recursos de red con sistemas operativos Windows. Samba como tal utiliza el protocolo de red SMB (Server Message Block), con el objetivo de permitir la comunicación entre sistemas operativos diferentes. 

Cuando nos referimos a SMB, nos referimos a un protocolo de red utilizado por Windows para compartir archivos, impresoras y otros recursos de red. El protocolo SMB se utiliza ampliamente en Windows para permitir la comunicación entre múltiples dispositivos y compartir recursos de red.

Samba y SMB no son lo mismo, son cosas totalmente distintas. En este caso se utilizará el siguiente proyecto vulnerable para enumerar Samba:`https://github.com/vulhub/vulhub/tree/master/samba/CVE-2017-7494`.

Una vez tengamos el proyecto y estemos dentro de la carpeta, podremos correr el contenedor con:

```shell
docker-compose up -d
```

En este caso, este entorno vulnerable contempla una vulnerabilidad que permite ejecución de comandos; sin embargo, como este no es el enfoque en este caso, únicamente checaremos cómo enumerarlo. 

Si ahora checamos el contenedor que tengamos corriendo, podremos ver con el puerto que está trabajando; en este caso, para el protocolo SMB, vemos cómo se utiliza el puerto 445:

![[EnumServComunes/SMB/images/001.png]]

### smbclient

Cuando estemos con una máquina y observemos que el puerto 445 está abierto, podremos utilizar __smbclient__ para tratar de listar (parámetro __-L__) los recursos existentes en nuestra máquina (en este caso) e intentaremos hacer uso de una sesión nula con el parámetro __-N__, debido a que no contamos con credenciales válidas para una sesión. 

Al ser una sesión nula, puede ser que nos permita o no listar los recursos compartidos a nivel de red. En este caso sí lo permite y es por ello que podemos visualizar estos recursos:

```shell
smbclient -L 127.0.0.1 -N
```

![[EnumServComunes/SMB/images/002.png]]

Esto nos permite ver que tenemos __myshare__ y __IPC__.

### smbmap

Esto nos ayuda a listar lo que tenemos compartido a nivel de red; sin embargo, esto no nos permite saber qué podemos hacer con ello. Es por eso que existen herramientas como smbmap que nos ayudan a ver más información, como el llegar a visualizar los permisos que tenemos sobre esto.

```shell
smbmap -H 127.0.0.1
```

![[EnumServComunes/SMB/images/003.png]]

En este caso vemos cómo tenemos permisos de escritura para myshare.

### Conexión

Considerando todo lo anterior, si quisiéramos conectarnos a SMB, podríamos hacerlo con smbclient. Junto al host se coloca la carpeta a la que se accederá.

```shell
smbclient //127.0.0.1/myshare -N
```

![[EnumServComunes/SMB/images/004.png]]

Esta conexión nos podría ayudar incluso a que funcionase como el servicio FTP, teniendo la capacidad de subir y obtener archivos. 

En este caso, a nivel de prueba, generamos un archivo con contenido en el ordenador y con put lo colocaremos en myshare:

```smbclient
put file.txt
get file.txt
```

![[EnumServComunes/SMB/images/005.png]]

Si nosotros borrásemos el output de nuestro ordenador, podríamos volver a obtenerlo con get output.txt. 

Esto nos permite de cierta forma movernos en el sistema; sin embargo, esto tiene sus limitaciones, como que tendríamos que ir carpeta por carpeta y donde existe una carpeta y no nos dejaría listar todo el contenido que había.

### Monturas

En nuestro sistema existen diversas herramientas que nos permiten hacer más cosas y llegar a listar contenido de múltiples carpetas y subcarpetas como si en una estructura de tipo árbol.

Una de estas es __tree__, el cual es un comando que nos representa todas las carpetas, subcarpetas y archivos en un tipo de estructura similar a un árbol, lo cual podría ahorrarnos el tener que listar carpeta por carpeta para buscar algo rápidamente.

![[EnumServComunes/SMB/images/006.png]]

Esto es algo que evidentemente no podemos hacer de forma directa conectados como clientes en SMB; por ende, lo que podremos realizar es trabajar con monturas. Esto es prácticamente montar la carpeta compartida en nuestro ordenador, como si de conectar una USB o disco se tratase. 

Esto quiere decir que cualquier cambio realizado se estaría reflejando de forma automática en el sistema que está compartiendo esta carpeta, como si realizáramos cambios directos sobre una USB que conectamos o un disco duro que tengamos en nuestro ordenador.

Para ello, crearemos una carpeta en el directorio /mnt, en la cual sepamos que vamos a tener el contenido de la carpeta compartida __myshare__. En este caso será la carpeta __mounted__, después podremos borrarla. 

Antes de montar la carpeta, tendremos que instalar __cifs-utils__, si estamos en Debian con __apt install__ o __pacman -S__ si estamos en Arch Linux. 

De esta forma, al utilizar __mount__, con el parámetro __-t__ indicaremos que nuestra montura será de tipo cifs para poder manejar este recurso compartido a nivel de red desde mi propio ordenador.

```shell
mount -t cifs //127.0.0.1/myshare /mnt/mounted
```

![[EnumServComunes/SMB/images/007.png]]

Cuando intentemos realizar la montura, nos solicitará la contraseña de una sesión; recordemos que todo este tiempo hemos estado trabajando con una sesión nula, por lo que bastará con darle ENTER sin colocar nada y esto lo tomará como sesión nula. 

A nivel de manejo, como ya se mencionó antes, si llegamos a borrar el archivo o mover algunas cosas, no es que sea como una copia y no se afecte al recurso original, sino que directamente se está trabajando con el recurso original (como si de conectar una memoria se tratase). 

En este caso, ahora sí que podríamos ver lo mencionado con __tree__ y manejarlo todo de una forma mucho más cómoda.

![[EnumServComunes/SMB/images/008.png]]

Al igual que una USB, lo mejor sería también desmontar lo que hemos montado. Esto podremos hacerlo con el comando __umount__ y pasándole la ruta donde se encuentra montado este recurso.

```shell
umount /mnt/mounted
```

![[EnumServComunes/SMB/images/009.png]]

Es importante que la carpeta no esté siendo utilizada por ningún recurso para que funcione. En el primer caso, fallo debido a que me encontraba dentro de la carpeta. 

Cuando nosotros llegamos a montar esto, tenemos otra posibilidad en la cual ya no nos solicite la contraseña; esto sería pasándole la información con el parámetro __-o__:

```shell
mount -t cifs //127.0.0.1/myshare /mnt/mounted -o username=null,password=null,domain=,rw
```

En este caso indicamos un usuario y contraseña nulos, en dominio no colocamos nada y __rw__ nos ayuda a indicar que queremos montarlo con capacidad de lectura y escritura.


### Crackmapexec

Si realizamos una instalación clonando el repositorio, lo recomendable sería hacerlo dentro del directorio __/opt__, ya que es donde nosotros podremos colocar aplicaciones o scripts para poder tenerlo en nuestro PATH, si así lo deseamos.

Opciones:

- `https://www.stationx.net/crackmapexec-cheat-sheet/`
- `https://snapcraft.io/install/crackmapexec/arch`

Una vez instalado crackmapexec con alguna de las anteriores opciones, en el caso de Arch Linux podremos correrlo con el comando:

```shell
snap run crackmapexec
```

O en el caso de una distribución basada en Debian:

```shell
poetry run crackmapexec
```

Las posibilidades anteriores de ejecutarlo son considerando los tipos de instalación proporcionados.

__Crackmapexec__ es una herramienta muy potente para este tipo de servicios; se podría considerar de buen uso para cosas más avanzadas como Active Directory, permitiendo realizar cosas muy interesantes, principalmente en sistemas Windows. 

Nota: Recordemos desmontar la montura y eliminar la carpeta creada si así lo consideramos. 

Cracmapexec no se utiliza tanto para escanear máquinas Linux, sino que está más enfocado para las máquinas Windows.

```shell
snap run crackmapexec smb 127.0.0.1
```

Se ejecuta crackmapexec, se le indica que se escaneará el servicio SMB y se le da el host al que se escaneará.

![[EnumServComunes/SMB/images/010.png]]

En este caso nos retorna servicio, host, puerto, nombre de la máquina y que está corriendo un Windows 6.1, que en este caso realmente no está corriendo un Windows. 

Con el mismo comando, tenemos una opción que es __--shares__ para que nos liste los recursos compartidos a nivel de red; la cosa es que, como es una herramienta más pensada para analizar el servicio en sistemas Windows, al hacerlo para Linux, falla:

```shell
snap run crackmapexec smb 127.0.0.1 --shares
```

![[EnumServComunes/SMB/images/011.png]]

# Siguientes apuntes

[[Enumeración de gestores de contenido (CMS) – WordPress (1-2)]]