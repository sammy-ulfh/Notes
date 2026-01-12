# Índice

# Introducción

A continuación se verán dos tipos de explotación utilizados en ataques informáticos: Manuales y Automatizados.

- __Explotación Manual__: Es un tipo de explotación que se realiza de __manera manual__ y requiere que el atacante tenga conocimiento profundo del sistema y sus vulnerabilidades. En este enfoque, el atacante utiliza herramientas y técnicas específicas para identificar y explotar vulnerabilidades en un sistema operativo. Este enfoque es más lento y requiere más esfuerzo y habilidad por parte del atacante, pero también es más preciso y permite un mayor control sobre el proceso de explotación.
- __Explotación Automatizada__: Es un tipo de explotación que se realiza __automáticamente__ mediante el uso de __herramientas automatizadas__, como scripts o programas diseñados específicamente para identificar y explotar vulnerabilidades de un sistema objetivo. Este enfoque es más rápido y menos laborioso que el enfoque manual, pero también puede ser menos preciso y puede generar más ruido en la red objetivo, lo que aumenta el riesgo de detección.

Es importante tener en cuenta que el tipo de explotación utilizado en un ataque dependerá de los objetivos del atacante, sus habilidades y del nivel de seguridad implementado en el sistema objetivo. En general, los ataques de explotación manual son más precisos y discretos, pero también requieren más tiempo y habilidades. Por otro lado, los ataques de explotación automatizada son más rápidos y menos laboriosos, pero también pueden ser más ruidosos y menos precisos.

[Proyecto utilizado para mostrar ambos enfoques](https://github.com/appsecco/sqlinjection-training-app).

# Practica

## Visión general

El proyecto utilizado para mostrar ambos tipos de explotación lo clonaremos en nuestro dispositivo y lo inicializaremos con __docker-compose__:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/001.PNG]]

Esperaremos un momento a que todo se despliegue y este proyecto básicamente lo que nos permite es practicar inyecciones SQL en distintos laboratorios. Como lo dicen las indicaciones del proyecto, se desplegará una web en el puerto 8000 y esto podremos verlo en la web:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/002.PNG]]

Primeramente, iremos al enlace __reset database__ para que, en cuanto a la práctica que tendremos para la explicación de ambos enfoques, tengamos todo correctamente. 

Una vez hecho, volvemos a la página principal. 

De los enlaces que se muestran como laboratorios, entraremos al que es el __login 1__, a veces puede darnos fallas para redirigirnos con los usuarios y contraseñas proporcionados para testing; por ello agregaremos uno nuevo en __register.php__ y, al darle submit, nos redirigirá automáticamente a la página:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/003.png]]

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/004.png]]

Ahora en el buscador, podemos empezar a jugar un poco, buscando por __123__, __test__, etc. 

Con ello vemos que no tenemos ningún resultado, pero si intentamos darle a __search__ sin escribir nada en la barra de búsqueda, sucede lo siguiente:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/005.png]]

Con ello veremos que si escribimos algo similar a alguno de los datos mostrados, será lo que nos retornará. Existe una forma de saber si tenemos la posibilidad de llegar a romper la query que corre por detrás para verificar los datos en la base de datos; esto se debe a que SQL cuenta con una sintaxis; si esta no se encuentra bien sanitizada, es posible aprovecharse de esta misma sintaxis para, con comillas simples, insertar alguna posible acción maliciosa. 

Nos podremos dar cuenta si tenemos esta posibilidad al intentar buscar algo y colocar una comilla simple, por ejemplo __a'__:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/006.png]]

Esto nos da información de que sí tenemos la posibilidad de realizar inyecciones SQL (__SQLI__).
## Explotación automatizada

Para una explotación automatizada de este tipo de vulnerabilidad, existe una herramienta muy interesante y conocida, la cual es __sqlmap__. 

Cuando nosotros hacemos una búsqueda, lo que se tramita por detrás es una petición y necesitaremos esta petición; por ende, utilizaremos __BurpSuite__ en este caso.

Nos vamos al proxy; sabemos que este corre de forma automatizada en localhost mediante el puerto 8080. 

Para los navegadores tenemos una utilidad, la cual es __FoxyProxy,__ el cual es un add-on que nos permite hacer que BurpSuite sea capaz de ver el flujo de información. 

Buscamos __FoxyProxy add on firefox__ y lo agregamos:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/007.png]]

Una vez agregado, veremos el símbolo en la parte superior derecha, lo presionaremos, le daremos a opciones y después a proxies:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/008.png]]

Le daremos a __Add__, colocaremos la siguiente información que es donde corre el proxy de __BurpSuite__ y lo guardaremos:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/009.png]]

Una vez agregado, nos vamos a la página del laboratorio y, para habilitar BurpSuite, seleccionaremos el símbolo de FoxyProxy en la parte superior derecha y seleccionaremos __BurpSuite__, ya que es el que hemos agregado:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/010.png]]

Finalmente, en Burp Suite seleccionaremos __Intercept Off__ para que cambie a __Intercept On__ y empiece a capturar el tráfico. Con ello realizamos cualquier búsqueda en el buscador de la plataforma; la página parecerá congelada, pero en BurpSuite tendremos la captura de la solicitud esperando a ser procesada:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/011.png]]

Si por alguna razón esto no funciona, esto podrá ser por configuraciones que han surgido con las actualizaciones de Firefox y tendremos que habilitar algunas opciones del proxy, ya que el problema está en la extensión de FoxyProxy. La solución es configurar el proxy manualmente desde el navegador que usen: settings > network settings > manual proxy conf. > Ingresar la IP de localhost y el puerto.

O la otra sería utilizar el propio navegador de Burp Suite y así podríamos interceptar la comunicación sin ningún problema.

Una vez tengamos interceptada la petición que se realiza cuando acontece una búsqueda, podremos situarnos en la parte de la información de la petición y, después de hacer clic derecho > copiar a un archivo; en caso de no tener esta opción, seleccionamos todo el contenido de la petición y seleccionamos almacenar texto seleccionado en un archivo:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/012.png]]

Después de guardar, tendremos el archivo de la siguiente manera:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/013.png]]

Este contiene todo el cuerpo de la petición que se tramita y en la parte inferior podremos ver el parámetro mediante el cual se realiza la búsqueda, el cual es __searchitem__. 

Con este ya hemos visto cómo con una comilla podemos llegar a acontecer un error en la base de datos, lo cual es cosa de la cual podremos aprovecharnos para llegar a extraer información privilegiada de la base de datos. 

Con esto en mente, utilizando __sqlmap__ podríamos pasarle este archivo que tenemos ahora, mediante el parámetro __-r__, con el parámetro __-p__ le indicaremos el __parámetro de inyección__ con el que queremos que pruebe cosas, que en este caso es __searchitem__, si lo dejamos el comando únicamente con esto, lo tendremos de la siguiente manera:

```shell
sqlmap -r request.req -p searchitem
```

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/014.png]]

Empieza a trabajar, pero en este caso vemos cómo nos empieza a hacer preguntas en el proceso; esto lo hace porque en este caso ha identificado que se trata de una base de datos de MySQL y pregunta si se desean aplicar payloads para esta específica base de datos, lo cual es de ayuda, ya que evita probar algunos payloads de otras bases de datos que no tiene sentido aplicar.

Podremos ir respondiendo, pero algo que agilizaría más el proceso es agregar la opción __--batch__ para que no nos esté preguntando.

```shell
sqlmap -r request.req -p searchitem --batch
```

Esto empieza a trabajar y, una vez finaliza, podremos ver cómo la herramienta nos reporta que el parámetro __searchitem__ parece ser inyectable:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/015.png]]

Por lo tanto, esto nos ha detectado que de alguna forma es vulnerable e incluso nos da un reporte al final. Con ello en mente, podríamos agregar una opción para que nos muestre las bases de datos, la cual es __--dbs__:

```shell
sqlmap -r request.req -p searchitem --batch --dbs
```

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/016.png]]

Para las bases de datos dadas, cada una de ellas luego tendrá tablas. En este caso nos enfocaremos en la base de datos __sqlitraining__ y con sqlmap listaremos las tablas existentes en ella:

```shell
sqlmap -r request.req -p searchitem --batch -D sqlitraining --tables
```

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/017.png]]

La tabla __users__ podría ser de nuestro interés como atacantes, ya que estas suelen almacenar datos como nombres de usuario, contraseñas, etc. 

Ahora mostraremos las columnas de la tabla users:

```shell
sqlmap -r request.req -p searchitem --batch -D sqlitraining -T users --columns
```

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/018.png]]

Como vemos, por detrás automatiza toda la inyección SQL y nosotros ya no tenemos que preocuparnos al respecto. Ahora podríamos también enfocarnos únicamente en las columnas __password__ y __username__ y dumpear sus valores para verlos:

```shell
sqlmap -r request.req -p searchitem --batch -D sqlitraining -T users -C password,username --dump
```

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/019.png]]

Además de reportarnos los datos, en este caso parece ser que estaban almacenados en __md5__, por lo cual no estaban en texto claro, pero la propia herramienta aplica ataques de fuerza bruta y las muestra en texto claro. 

Para el usuario admin, la contraseña sería admin; para bob, password, y así con el resto de usuarios. 

Esto sería una explotación automatizada, ya que la herramienta aplica todas las queries por detrás y nosotros no tenemos que preocuparnos por ello; sin embargo, esto es algo muy penado en certificaciones avanzadas de ciberseguridad, ya que lo ideal es que nosotros tengamos todo el control sobre lo que realizamos.

## Explotación manual

Para la explotación manual, regresaremos nuevamente a Burp Suite, capturando la petición de búsqueda. 

En este caso tenemos dos posibilidades: click derecho sobre la información de la petición y seleccionar enviar al repeater o solo presionar CTRL + R. 

Después nos iremos a la sección de repeater; esta opción se encuentra en el nivel superior de la aplicación. 

Su orden es Proxy | Intruder | Repeater. 

Seleccionamos repeater y aquí tendremos la solicitud; tenerla en el repeater nos permitirá estar intentando múltiples cosas y ver qué es lo que sucede. 

Aquí, por un lado, tenemos la solicitud y, por otro, la respuesta, después de presionar el botón de __send__:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/020.png]]

Del lado de la respuesta, seleccionaremos en __Render__ y cada que le demos a __send__ veremos cómo se refleja automáticamente en Render, que nos mostrará como si fuese la propia página web:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/021.png]]

Del lado de la petición, nosotros podremos editar la solicitud; por ende, para el parámetro __searchitem__ ahora probemos colocar lo siguiente: `a' order by 100-- -`:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/022.png]]

Esta acción lo que hará es que, en caso de que la columna indicada no exista, con varios intentos nos ayudará a averiguar con cuántas columnas cuenta la tabla consultada; en este caso, como no cuenta con 100, da error y bastará con ir bajando el número hasta que ya no nos dé error y ese será el número de columnas que tiene:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/023.png]]

En 5 columnas es cuando ya no nos da el error; por ende, es el número de columnas que tiene. 

Con esta información en mente, ahora podremos realizar un __union select__ para colocar el número de columnas que ahora sabemos que existe, separado por comas:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/024.png]]

Aquí es donde vemos cómo nos muestra los numeritos que hemos colocado nosotros y es donde entra en juego la parte de la inyección; para saber el usuario que está corriendo la base de datos, podríamos utilizar __user()__ o __username()__, dependiendo de qué nos funcione:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/025.png]]

Y vemos cómo se muestra dónde ha sido colocada la acción, que es donde antes mostrábamos el número de la tercera columna; de la misma forma podríamos mostrar el nombre de la base de datos que está siendo actualmente consultada con __database()__.

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/026.png]]

Con esto que podemos hacer ahora, podríamos intentar extraer los nombres de todas las bases de datos con __schema_name__ trayendo esta información de __information_schema.schemata__:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/027.png]]

Y como vemos, al aplicar la inyección, se nos muestra la información de los nombres de las bases de datos. 

Con esto ahora, podremos aprovechar para extraer los nombres de las tablas con __table_name__ y traer esta información de __information_schema.tables__ donde la base de datos (__table_schema__) es __sqlitraining__:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/028.png]]

Teniendo esto mismo en mente, ahora podríamos traer los nombres de las columnas __column_name__ de __information_schema.columns__ donde la base de datos __information_schema__ es __sqlitraining__ y el nombre de la tabla es __users__:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/029.png]]

Con ello, obtenemos las columnas de la tabla users.

### Dumpear información de columnas específicas.

Como ahora la información que nos interesa de la tabla users es __password__ y __username__, podríamos utilizar __group_concat()__, para indicar que queremos mostrar __username__ y __password__ de la tabla users; los mostraremos separados por dos puntos y, para no tener ningún problema, lo colocaremos en hexadecimal __0x3a__:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/030.png]]

Si vemos aquí se nos muestra todo, pero se muestra en una sola línea, lo cual no hace posible poder ver todo de una correcta manera, por lo que podríamos intentar para el segundo campo mostrar username, para el tercero password y así además evitaríamos tener que utilizar __group\_concat__.

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/031.png]]

Como en este caso queremos tenerlo todo centralizado, para irnos a __pretty__ en cómo se interpreta la respuesta y copiar todo, nos conviene más la primera opción que vimos:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/032.png]]

Copeamos todo y lo podemos poner en un archivo con nuestro editor vi/vim/nvim:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/033.png]]

Como lo vemos todo de esta manera y sabemos que cada dato se separa por comas, podemos aprovecharnos de esto para aplicar una sustitución de la coma por un retorno de carro "__\\r__", el cual se ve como un salto de línea, y al final agregamos "__/g__" para que lo aplique para todas las coincidencias de coma. 

Para hacer esto en Vim, primero presionamos ESC, después los dos puntos y colocamos `%s/,/\r/g`:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/034.png]]

Después de dar Enter, se aplicará; como aún nos falta aplicar los cambios, tendremos que presionar nuevamente ESC y finalmente `:wq`.

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/035.png]]

Con estos hashes de md5, podremos incluso hacer uso de herramientas en línea para que apliquen ataques de fuerza bruta y nos lo muestren en texto claro; para ello, primeramente, nos quedaríamos únicamente con los hashes de las contraseñas, tomando el segundo argumento y como delimitador los dos puntos:

```shell
cat data | awk -F':' '{print $2}'
```

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/036.png]]

Podremos copiar todo esto, visitar el sitio web de [hashes.com](https://hashes.com/), pegarlo, responder el captcha y dar submit para obtenerlos en texto claro:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/037.png]]

Podríamos, antes de dar submit, incluso seleccionar la opción de que nos muestre los algoritmos y veríamos de qué algoritmo provenía el hash. Por ejemplo, admin viene de MD5 y si hasheamos esa misma palabra nosotros con __md5sum__, evitando el salto de línea (parámetro -n) porque si no obtendremos algo distinto. 

Obtenemos el mismo:

```shell
echo -n "admin" | md5sum
```

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/038.png]]


# Next Notes

[[]]


