# Introducción

Una **Forward Shell** es una alternativa cuando las opciones más comunes, como las reverse shells, no son viables debido a restricciones como las reglas del firewall. 

La Forward Shell es una técnica ingeniosa que se utiliza en situaciones donde, a pesar de tener acceso a un sistema a través de una webshell u otro método, no podremos establecer una reverse Shell debido a las restricciones impuestas por el firewall del sistema objetivo. En estos casos, la Forward Shell nos permite ejecutar comandos y obtener una Shell interactiva utilizando métodos alternativos que no requieren establecer una conexión TCP directa con el sistema de la forma tradicional. 

Una de las claves de esta técnica es el uso de **mkfifo**, una herramienta para crear named pipes (tuberías con nombre) en sistemas Unix/Linux. Mediante estas tuberías, podremos establecer una comunicación bidireccional entre la máquina atacante y la máquina objetivo, permitiendo una interacción más fluida y completa con la Shell del sistema comprometido. Esto nos brinda una mayor movilidad y flexibilidad para operar, incluso en entornos restringidos.
# Práctica

![[Offensive/forward_shell/images/001.PNG]]

Viendo la imagen anterior, imaginemos que tenemos una web a la cual, mediante un parámetro en su URL tenemos la posibilidad de realizar ejecución de comandos. Esto viene bien, pero tiene sus limitaciones de cara a querer efectuar cambios de directorios o abrir binarios como nano para edición de archivos o incluso querer solicitar algún tipo de terminal como abrir una bash desde una sh debido a que la ejecución de cada comando es una petición independiente y, por lo tanto, son procesos independientes, es como ejecutar el comando cada vez en una terminal distinta. 

Nuestra **Forward Shell** viene a ser la alternativa que nos permitirá llegar a realizar estas acciones, debido a que por configuraciones del firewall de la máquina víctima no podremos realizar una comunicación desde la misma hacia nuestra máquina de atacante para recibir una reverse Shell. 

Principalmente, realizaremos la misma simulación del envío de comandos enviando las peticiones **get** y recibiendo la respuesta de los comandos, lo cual sería nuestra webshell, a esto le agregaremos la utilidad **mkfifo** que es lo que nos permitirá expandir nuestras posibilidades en el sistema, teniendo de una forma más cercana lo que realmente sería una shell.

Un FIFO es un tipo de fichero especial que permite a procesos independientes comunicarse. Un proceso abre el fichero FIFO para escribir y otro para leer, tras lo cual los datos pueden fluir como con las tuberías sin nombre usuales en shells o donde sea. 

Para ello, nos montaremos nuestro servidor dejando la posibilidad de la ejecución de comandos mediante el parámetro **cmd**. Esto lo haremos montándonos un pequeño laboratorio con **docker** el cual esté corriendo un servidor http con php.

## Montando el laboratorio

Para ello, primero tendremos que instalar **docker.io** o **docker**.

Iniciaremos el servicio de docker con:

```shell
sudo service docker start
```

o una forma más moderna:

```shell
sudo systemctl start docker
```

Ahora, encontrándonos como administrador, podremos verificar si tenemos algún contenedor corriendo con docker utilizando:

```shell
docker ps
```

O si se llegó a quedar algún contenedor por ahí pendiente:

```shell
docker ps -a
```

O incluso podremos verificar si tenemos alguna imagen creada:

```shell
docker image
```

Es normal que no veamos nada de ser el caso de recién instalarlo en nuestro sistema, porque no hemos trabajado nada con docker. 

En el directorio que nos encontramos crearemos un archivo con el nombre **Dockerfile**, a este le agregaremos únicamente 3 líneas. 

Antes de esto, primeramente crearemos nuestro archivo php malicioso, el cual subiremos a nuestro contenedor y este será el archivo **index.php**. Este únicamente tendrá una ejecución en php con **system()**, lo cual permitirá la ejecución de comandos y el comando que tomará será tomado el parámetro **cmd**:

![[Offensive/forward_shell/images/002.PNG]]

Ahora en nuestro **Dockerfile** vamos a agregar las siguientes líneas:

![[Offensive/forward_shell/images/003.PNG]]

De esta manera, primeramente estamos indicando que tendremos corriendo un servidor php con apache, con la segunda línea nos estamos copeando nuestro archivo malicioso a la ruta **/var/www/html** para que sea lo que muestre nuestro servicio web y finalmente exponemos el puerto 80 de nuestra propia máquina de atacante para que sea nuestra forma de manejar el **port forwarding** debido a que los comandos que ejecutaremos se ejecutaran en el propio contenedor y no en nuestra máquina que estará corriendo el contenedor. 

Con esto listo y el contenido del archivo guardado, ahora construiremos nuestra imagen con docker utilizando el comando:

```shell
docker build . -t web_server
```

De tal manera que le estamos indicando que en nuestro directorio actual construya una imagen de nuestro **Dockerfile** y como nombre le estamos dando **web_server**. 

Esto tarda un poco, pero una vez completado, veremos cómo con el comando ```docker images``` veremos ahora la imagen creada:

![[Offensive/forward_shell/images/004.PNG]]

Con ello, ahora aprovechándonos de la imagen que hemos creado, lanzaremos el contenedor habilitando el port forwarding. 

Para ello utilizaremos el comando:

```shell
docker run --rm -dit -p 80:80 web_server
```

Con **--rm** estamos indicando que, cuando el contenedor deje de correr, se borre todo automáticamente. Con **-d** estamos indicando que se corra en segundo plano, **it** viene de interactive para indicar que queremos poder obtener una terminal para nuestro contenedor. Finalmente, con **-p** le estamos indicando que el puerto 80 de nuestro contenedor sea el puerto 80 de nuestra máquina. Por último, le pasamos el nombre de la, imagen y con ello ya estaría corriendo nuestro contenedor.

![[Offensive/forward_shell/images/005.PNG]]

Esto nos retornará el id de nuestro contenedor, pero si utilizamos el comando **docker ps** para ver si tenemos algún contenedor corriendo, aquí también nos mostrará el ID de una forma más corta, pero podremos utilizar este. No es necesario el ID completo si queremos referirnos a nuestro contenedor.
![[Offensive/forward_shell/images/006.PNG]]

Aquí, como no le hemos dado nombre al contenedor, vemos cómo se le asignó uno de forma automática. Con este nombre podremos ver cosas como el puerto del contenedor:

```shell
docker port awesome_zhukosky
```

O incluso obtener una terminal interactiva con:

```shell
docker exec -it awesome_zhukosky bash
```

![[Offensive/forward_shell/images/007.PNG]]

Nuestro contenedor sería como estar en otra máquina, podríamos ver perfectamente que la IP que tenemos nosotros es distinta a la de nuestra interfaz docker:

![[Offensive/forward_shell/images/008.PNG]]

Y si listamos la IP de nuestro contenedor con el comando, ```hostname -I``` veremos cómo es diferente a la de nuestra interfaz de docker0:

![[Offensive/forward_shell/images/009.PNG]]

Como podremos ver, nos encontramos en la ruta **/ar/www/html** y si listamos el contenido en esta ruta, veremos que está el archivo que hemos copiado **index.php**. Recordemos que esto lo hicimos al crear nuestro Dockerfile, llevando nuestro archivo malicioso a esta ruta, por ello es que lo tenemos:

![[Offensive/forward_shell/images/010.PNG]]

Con ello ya tendremos montado nuestro laboratorio y tendremos corriendo un servicio http por el puerto 80, el cual se encuentra corriendo en un contenedor.

## Ejecución de comandos

Si ahora en nuestro navegador colocamos **localhost**, veremos lo siguiente:

![[Offensive/forward_shell/images/011.PNG]]

Esto se debe a que nuestro archivo malicioso no puede ejecutar el comando debido a que no recibe nada del parámetro **cmd** en la url, es por ello que nosotros tendremos que pasárselo y, una vez haciéndolo, veremos cómo el comando se ejecuta:

![[Offensive/forward_shell/images/012.PNG]]

En este caso no pasa nada si no apuntamos de forma directa al archivo **index.php**, ya que, es el único recurso que existe, pero en sí la ruta sería **localhost/index.php** y aquí es donde tendríamos que enviar nuestro parámetro con el comando a ejecutar:

![[Offensive/forward_shell/images/013.PNG]]

Aquí ya podremos inyectar ciertos comandos, como por ejemplo listar el contenido del archivo /etc/hosts:

![[Offensive/forward_shell/images/014.PNG]]

Y si quisiéramos verlo en el formato en el que es como tal el output, bastaría con hacer **CTRL + U** en nuestro teclado:

![[Offensive/forward_shell/images/015.PNG]]

Esto ya sería básicamente tener una mini webshell.

### Ejecutar los comandos mediante peticiones con CURL

Tomando completamente el link de cuando hicimos nuestra petición en el navegador, para ejecutar el comando **cat /etc/hosts** utilizaremos el comando curl con ello:

```shell
curl -s -X GET 'http:/localhost/index.php?cmd=cat%20/etc/hosts'
```

![[Offensive/forward_shell/images/016.PNG]]

El **%20** que vemos corresponde al salto de línea, esto se debe a que el navegador automáticamente hace esto para ciertos caracteres especiales, aplicando un url encoding. 

Si al querer realizar la petición con Curl queremos evitar colocarlo de esta forma, podríamos utilizar el comando de la siguiente manera:

```shell
curl -s -X GET 'http:/localhost/index.php' -G --data-urlencode 'cmd=cat /etc/hosts'
```

Con esto le estamos dando primeramente la ruta para después con **-G** le estamos indicando que le vamos a pasar datos, pero esta es una forma de indicarle que se estarán enviando mediante el método **GET** y finalmente **--data-urlencode** que nos permitirá agregar el texto directamente sin tener que agregar nosotros en url encoding.

![[Offensive/forward_shell/images/017.PNG]]

De esta manera funciona exactamente de la misma manera y nos evitamos tener que colocar nosotros mismos el encoding del url. 

Si nosotros tratáramos de ejecutar un comando que no existe, esto no nos retornará nada, ya que, no podemos ver los errores. Para ello tendremos que convertir nuestro **stderr** en **stdout** y así nos lo redirigirá para poder verlo:

![[Offensive/forward_shell/images/018.PNG]]

Si esto mismo tratáramos de ejecutarlo en el navegador, no nos aplicaría correctamente el **url encode**, esto se debe a que ciertos caracteres especiales tendremos que url encodearlos nosotros mismos, en este caso el **&** que en este caso sería **%26**:

![[Offensive/forward_shell/images/019.PNG]]

![[Offensive/forward_shell/images/020.PNG]]

Si tenemos duda de qué número en hexadecimal podría tener cada uno de los caracteres, podríamos utilizar **man** con la tabla **ascii** para verlo. En caso de que no nos funcione, tendremos que instalar **ascii** y con el parámetro **-X** nos dará la tabla con el valor de cada carácter en HEXADECIMAL. En este caso podremos ver cómo para el **&** sí es el **26** y, por ende en el url encoding lo representamos como **%26**:

![[Offensive/forward_shell/images/021.PNG]]

## Creación del script

Considerando lo anterior de haciendo una petición, lo que haremos será con la librería **requests** enviar una petición por **get**, enviándole el comando a nivel de datos.

![[Offensive/forward_shell/images/022.PNG]]

Aquí hacemos lo mismo que hicimos con curl, solamente almacenamos en **data** los parámetros que queremos enviar. En este caso para **cmd** indicamos con '%s' que lo que le estaremos pasando es un string y con **% command** le estamos indicando que el string que le estaremos pasando es el comando.

Finalmente, en nuestra petición colocamos la url y, a nivel de parámetro, le pasamos data, ya que, es una petición por **GET**. Si fuese una petición por **POST**, ahí los datos ya los enviaríamos a nivel de **data**. 

En este caso, estamos recuperando la respuesta con **r.text** y finalmente lo imprimimos, retornándonos la respuesta del comando:

![[Offensive/forward_shell/images/023.PNG]]

Aquí ya podríamos jugar con **input** y un bucle para estar pidiendo constantemente los comandos, simulando una terminal. Además agregaremos color en nuestro input simulando la terminal y adicionalmente manejaremos la salida de nuestro programa con **signal**:

![[Offensive/forward_shell/images/024.PNG]]

![[Offensive/forward_shell/images/025.PNG]]

En este caso, nuestra máquina no tiene configuradas reglas en el firewall que impidan una salida de conexiones como para enviarnos una reverse Shell, pero en este caso supondremos que así es. 

Sobre lo que mencionamos en un inicio sobre la limitación de nuestra posibilidad de ejecutar comandos, lo podremos ver, aprovechando que php está instalado, al solicitar una terminal de php con **php --interactive**:

![[Offensive/forward_shell/images/026.PNG]]

Esto se queda cargando porque el navegador no es un entorno que nos pueda brindar una Shell y, por ende, no tendremos forma de poder trabajar con la misma. 

Si esto lo hiciéramos en nuestro sistema, lo veríamos de la siguiente manera:

![[Offensive/forward_shell/images/027.PNG]]

Otra forma más visible es en nuestra webshell que hemos construido con el script, tratar de movernos entre directorios:

![[Offensive/forward_shell/images/028.PNG]]

Siempre estaremos donde comenzamos a pesar de hacerlo. Esto se debe a que cada ejecución de comando es un proceso independiente que, cada vez que enviamos, se ejecuta directamente del script que nosotros colocamos, por lo que no se arrastra ninguna sesión, como lo es con nuestra terminal en el sistema. 

Incluso esto lo podríamos ver al crear una variable. Si le asignamos el valor de "Hola" y después quisiéramos mostrar su contenido, no lo veríamos debido a que son dos consultas totalmente independientes y no existe como un registro o sesión de lo que realizaron las consultas anteriores.

![[Offensive/forward_shell/images/029.PNG]]

Aquí es donde entra en juego el uso de **mkfifo** y las tuberías con nombre para poder llegar a tener como una sesión que tenga el contexto de todo lo que estamos realizando, así como que al ejecutar una Shell interactiva con php ahora sí la recibamos. 

Como concepto, si instalamos **mkfifo** y ejecutamos el siguiente comando:

```shell
mkfifo input; tail -f input | /bin/sh 2>&1 > output
```

Con esto, como tal, si mostramos lo que tenemos en el directorio, hemos creado dos tipos de archivos:

![[Offensive/forward_shell/images/030.PNG]]

De primeras tendremos los archivos vacíos. Lo que el comando hace es que está creando un archivo fifo **input** del cual con **tail -f** estamos continuamente leyendo las últimas líneas de archivo, **tail -f** sirve para leer continuamente las últimas líneas de un archivo. En este caso, lo que le corresponderá a las nuevas entradas que estemos colando como input. 

En este caso estaremos continuamente leyendo los inputs para que me los ejecute automáticamente con una Shell **sh** y, además, por lo que vimos anteriormente de los errores, los transformará en el output para así almacenarlos en **output**.

## Siguiente apuntes

[[Creación de Forward Shell (2-4)]]