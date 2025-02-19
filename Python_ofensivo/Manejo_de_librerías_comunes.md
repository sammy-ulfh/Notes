
## **Índice**

- [[#Librería os y sys]]
- [[#Librería requests (1/2)]]
- [[#Librería requests (2/2)]]
- [[#Librería Urllib3]]
- [[#Librería threading y multiprocessing]]
- [[#Siguientes apuntes]]

## **Librería os y sys**

1. **Introducción**

	Las bibliotecas *os* y *sys* de Python son herramientas esenciales para cualquier desarrollador que busque interactuar eficazmente con el sistema operativo y gestionar el entorno de ejecución de sus programas. Estas bibliotecas proporcionan una amplia gama de funcionalidades que permiten una mayor flexibilidad y control en el desarrollo de software.

	*Biblioteca os*

	La biblioteca *os* en Python es una herramienta poderosa para interactuar con el sistema operativo. Proporciona una interfaz portátil para usar funcionalidades dependientes del sistema operativo, lo que significa que los programas pueden funcionar en diferentes sistemas operativos sin cambios significativos en el código. Algunas de sus capacidades incluyen:

	- *Manipulación de Archivos y Directorios:* Permite realizar operaciones como crear, eliminar, mover archivos y directorios, y consultar sus propiedades.
	  </br>
	- *Ejecución de Comandos del Sistema:* Facilita la ejecución de comandos del sistema operativo desde un programa en Python.
	  </br>
	- *Gestión de Variables de Entorno:* Ofrece funciones para leer y modificar las variables de entorno del sistema.
	  </br>
	- *Obtención de Información del Sistema:* Proporciona métodos para obtener información relevante sobre el sistema operativo, como la estructura de directorios, detalles del usuario, procesos, etc.

	*Biblioteca sys*

	La biblioteca *sys* es fundamental para interactuar con el entorno de ejecución del programa Python. A diferencia de *os*, que se centra en el sistema operativo. *sys* está más orientada a la interacción con el intérprete de Python. Sus principales usos incluyen:

	- *Argumentos de Línea de Comandos:* Permite acceder y manipular los argumentos que pasan al programa Python desde la línea de comandos.
	  </br>
	- *Gestión de la Salida del Programa:* Facilita el control sobre la salida estándar (*stdout*) y la salida de error (*stderr*), lo cual es esencial para la depuración y la presentación de resultados.
	  </br>
	- *Información del Intérprete:* Ofrece acceso a las configuraciones y funcionalidades relacionadas con el intérprete de Python, como la versión de Python en uso, la lista de módulos importados y la gestión de la ruta de búsqueda de módulos.

	Ambas bibliotecas son cruciales para el desarrollo de aplicaciones Python que requieren interacción avanzada con el entorno de sistema y el intérprete. Su comprensión y uso adecuado permite a los desarrolladores escribir código más robusto, portable y eficiente.
	</br>
2. **Práctica**

	Primeramente, crearemos un archivo y en este importaríamos la librería *os*:

	![[IMG_809.png]]

	Con esta librería tenemos diversas utilidades para interactuar con el sistema, tales como:

	*getcwd():*

	Con *getcwd()*, podremos obtener la ruta absoluta del directorio actual en el que se encuentra el script, ya que también es posible ir moviéndose entre el sistema gracias a otras utilidades de la librería *os*.

	![[IMG_810.png]]

	*lisrdir()*

	Con la utilidad *listdir()*, podremos listar el contenido de un directorio. Podremos pasarle una ruta absoluta como argumento y nos listara el contenido de esta o no pasarle nada y listará el contenido de la ruta actual.

	  En este caso le pasaremos como argumento la ruta anterior, lo que nos retornara será una lista que almacenamos en la variable *files*. Como es una lista donde cada elemento es algún archivo o directorio de nuestra ruta que le hemos pasado como argumento.

	Para realizar una representación donde no se vea la estructura de la lista, podríamos utilizar un bucle o la utilidad *' '.join()*:

	![[IMG_811.png]]

	*mkdir():*

	Con *mkdir()* pasándole como argumento el nombre del directorio que queremos crear, ya estaría listo.

	Podremos comprobarlo creándolo y volviendo a listar el directorio con lo anterior visto:

	![[IMG_812.png]]

	*path.exist():*

	Con *path.exists()*, podremos con pasarle como argumento el nombre de un archivo o directorio, comprobar si este existe.

	Esta utilidad retornará *True* o *False* en función de si existe o no. En este caso podríamos comprobar si *mi_directorio* existe (funciona de la misma manera para archivos):

	![[IMG_813.png]]

	Si ahora elimináramos el directorio y volviésemos a ejecutar el script, veríamos que ahora nos arroja el mensaje de que este no existe.

	![[IMG_814.png]]

	Esto puede venirnos bien a la hora de estar manejando archivos y directorios en Python, ya que si intentamos crear uno ya existente nos lanzará una excepción,  en caso de no existir se creará correctamente.

	Por ello, si ya existe, podría eliminarse y crearse nuevamente o directamente no crearse.

	*getenv():*

	En los sistemas operativos tenemos las variables de entorno, estas almacenan contenido que ayudan a la funcionalidad del sistema.

	Algunas, como el *PATH*, contiene rutas que el sistema utilizara para buscar binarios que queramos ejecutar. En este caso yo estoy empleando una terminal personalizada (*kitty*), si en terminal veo la variable de entorno donde la tengo instalada *KITTY_INSTALLATION_DIR*, me regresará la ruta donde está almacenada:

	![[IMG_815.png]]

	Podría obtener el contenido de las variables de entorno, utilizando *getenv()* en Python:

	![[IMG_816.png]]

	De esta manera, al nosotros pasar como argumento a *getenv()*, el nombre de una variable de entorno nos regresará su contenido.

	**Librería sys**

	Esta librería se importa como cualquier otra con `import sys`. Con esta podremos controlar el código de estado a la hora que se termina el programa, ya sea de forma forzada, por el final del código o por algún error.

	Además, nos viene mucho de ayuda para controlar los argumentos que le pasemos a un script en Python.

	*Obtener el nombre del propio script*

	Los argumentos en Python funcionan de una manera posicional, siempre el que está en la posición 0 será el propio nombre del script y los que estén en posiciones posteriores serán los argumentos que podremos definir para que el programa pueda recibir.

	Aunque nosotros no hayamos definido el funcionamiento de nuestro script para trabajar con argumentos, la posición 0 siempre existirá, ya que es el nombre de nuestro propio script y se accede como propiedad con la librería *sys*, utilizando *argv\[0\]*:

	![[IMG_817.png]]

	Con esto, si el nombre de nuestro propio script cambiara, esto no afectaría en nada, ya que el propio programa podría acceder a su nombre gracias a la librería sys.

	*Calcular el total de argumentos que le son pasados al script*

	Podremos ver *sys.argv* como una propiedad o atributo, el cual almacena en una forma de lista el total de argumentos que le son pasados. Teniendo esto en cuenta, podríamos ver cuantos argumentos le han pasado al programa con *len()* del propio Python:

	![[IMG_818.png]]

	![[IMG_819.png]]

	Nos marca uno, el cual es el nombre del propio script, y recordando que Python comienza a contar desde el 0, esto se almacena en la posición 0.

	Además, la forma en la que nosotros podremos pasarle más argumentos a nuestro script será colocarlos al momento de ejecutarlo de forma seguida, separando cada uno por espacios:

	![[IMG_820.png]]

	De esta manera, el nombre del propio script, el nombre de la persona, el correo y la serie de números son considerados cada uno un argumento y estos se separan por espacios al agregarlos.

	De esta manera estaríamos trabajando con una lista donde, de forma posicional, se guardarían los argumentos y podríamos acceder a estos en función a su índice. Dos formas de hacer esto evitando errores serían primeramente calcular si el número total de argumentos corresponden sin problemas al índice al que queremos acceder o directamente intentar acceder a este mediante un *try* y si se presenta la excepción *IndexError* gestionarla para evitar que el programa se detenga.

	*Mostrar todos los argumentos*

	Como *argv* es una lista que almacenará todos los argumentos, podríamos listarla directamente, pero para que se vea mejor estéticamente, recordemos que tenemos *''.join()*:

	![[IMG_821.png]]

	Se nos pueden presentar casos donde *join* nos represente de manera incorrecta lo esperado, en tales casos en lugar de pasarle directamente la lista, podríamos dentro de este, como argumento iterar sobre la lista e ir pasando cada elemento en cada iteración y esto nos lo representaría de la misma manera:

	![[IMG_822.png]]

	*Ver los directorios del PATH del propio Python*

	Cuando vimos de forma rápida el concepto de *Library Hijacking* con Python, vimos que era posible ver cada dirección almacenada en el *PATH* con *sys.path*, y que estas eran recorridas en orden, empezando por el directorio actual donde se esté ejecutando nuestro programa.

	De esta manera, al estar todas las rutas almacenadas en una lista, podríamos mostrar cada una con un salto de línea con *join* o iterando sobre esta y en cada iteración mostrar las rutas:

	![[IMG_823.png]]

	![[IMG_824.png]]

	*Código de estado*

	En Bash después de ejecutar cada comando, es posible verificar su código de estado:

	![[IMG_825.png]]

	De esta manera sabemos que un código de estado correcto siempre será cero y uno incorrecto, dependiendo del error que se de, será distinto de cero.

	Usualmente, para un error se suele utilizar el código de estado *1*, por lo que nosotros podríamos gestionar esto mismo con la librería *sys*, utilizando *exit()* y pasándole como argumento el código de estado con el que deseamos que salga el programa:

	![[IMG_826.png]]

## **Librería requests (1/2)**

1. **Introducción**

	La biblioteca *requests* en Python es una de las herramientas más populares y poderosas para realizar solicitudes HTTP. Su diseño es intuitivo y fácil de usar, lo que lo hace la opción preferida para interacturar con APIs y servicios web.

	*Introducción a requests*

	*requests* es una biblioteca de Python que simplifica enormemente el proceso de enviar solicitudes HTTP. Está diseñada para ser más fácil de usar que las opciones incorporadas en Python, como *Urllib*, proporcionando una API más amigable.

	*Características Principales:*

	- *Simplicidad y Facilidad de Uso:* Con requests, enviar solicitudes GET, POST, PUT, DELETE, entre otras, se puede realizar en pocas líneas de código. Su sintaxis es clara y concisa.
	  </br>
	- *Gestión de Parámetros URL:* Permite manejar parámetros de consulta y cuerpos de solicitud con facilidad, autorizando la codificación de URL.
	  </br>
	- *Manejo de Respuestas:* *requests* facilita la interpretación de respuestas HTTP, proporcionando un objeto de respuestas que incluye el contenido, el estado, los encabezados, y más. 
	  </br>
	- *Soporte para Autenticaciones:* Ofrece soporte integrado para diferentes formas de autenticación, incluyendo autenticación básica, gigest y OAuth.
	  </br>
	- *Manejo de Sesiones y Cookies:* Permite mantener sesiones y gestionar cookies, lo cual es útil para interactuar con sitios web que requieren autenticación y mantienen estado.
	  </br>
	- *Soporte para SSL:* *requests* maneja SSL (Secure Sockets Layer) y TLS (Transport Layer Security), permitiendo realizar solicitudes seguras a sitios HTTPS.
	  </br>
	- *Manejo de Excepciones y Errores:* Proporciona métodos para manejar y reportar errores de red y HTTP de manera efectiva.

	*Uso Práctico:*

	La biblioteca se utiliza ampliamene para interactuar con APIs RESTful, automatizar interacciones con sitios web, y en tareas de scrapping web. Sus capacidades para manejar solicitudes complejas y sus características de seguridad la hacen ideal para una amplia gama de aplicaciones, desde scripts simples hasta sistemas empresariales complejos.

	*Conclusión:*

	La comprensión y el uso efectivo de *requests* son habilidades esenciales para cualquier desarrollador en Python que trabaje con HTTP y APIs web. Esta biblioteca no solo facilita la realización de tareas relacionadas con la red, sino que también ayuda a escribir código más limpio y mantenible.
	</br>
2. **Práctica**

	Esta librería se llegará a utilizar mucho, sobre todo en el hacking web.

	Empezaremos creando un archivo e importando la librería, es importante mencionar que un script también entraría en conflicto si tiene el mismo nombre de alguna librería, ya que como el PATH de Python comienza a buscar por el directorio actual, básicamente se estaría importando así mismo el script.

	Esta librería nos permitiría hacer peticiones a páginas y esta nos respondería, por lo que podríamos almacenar la respuesta

	Para ello utilizaríamos el método *get()*.

	A este le pasamos como argumento la dirección de la página web a la que seremos realizar la solicitud,  y en nuestra variable *response* se almacenaría un objeto por lo que podríamos acceder a sus atributos.

	Una petición retornará un código de estado y podremos acceder a este con el objeto que nos retorna mediante el atributo *status_code*:

	![[IMG_827.png]]

	![[IMG_828.png]]

	*200* suele ser un código de estado exitoso.

	*Ver el código fuente de la respuesta*

	Para ver el código fuente de la respuesta, ahora tendríamos que utilizar *text* y esto nos retornaría como tal la respuesta, por lo que podríamos mostrarla con print:

	![[IMG_829.png]]

	Si bien, solo veremos código HTML, no sabremos que es sin verlo de forma interpretada por el navegador, por ello lo almacenaremos en un nuevo archivo:

	![[IMG_830.png]]

	![[IMG_831.png]]

	Ahora que todo el HTML está almacenado en un *index.html* y sabemos que esto puede interpretarlo un navegador, podríamos abrirnos un pequeño servidor en localhost con Python por HTTP para que interprete la página:

	```python3
	python3 -m http.server 8080
	```

	Ejecutaríamos el anterior comando en terminal, justo en el directorio donde sé en cuenta nuestro *index.html* que acabamos de crear con la respuesta.

	Con esto listo iríamos al navegador y colocaríamos *localhost* y recordemos que al comando para abrir el servidor le indicamos unos números, estos serían el puerto, por lo que se representaría como *localhost:8080*

	![[IMG_832.png]]

	Si nos vamos a la terminal donde abrimos el servidor, observaremos que además intento realizar peticiones de carpetas que claramente no existen en nuestro pequeño servidor:

	![[IMG_833.png]]

	Con esto, realmente nos hemos traído la página principal del buscador de Google, si la abrimos se ve prácticamente igual. La diferencia aquí es que nosotros en local no tenemos ni los estilos, ni los recursos faltantes para que se vea exactamente igual a cuando abrimos Google directamente en el navegador.

	*Petición en formato Json*

	Jugando con el siguiente enlace:
	
	```web
	https://httpbin.org/get
	```

	Al colocarlo en el navegador, directamente nos retorna un formato JSON:

	![[IMG_834.png]]

	Esto contiene cierta información y al final del todo vemos como nos muestra el enlace. Al inicio veremos primeramente *args* y veremos como es un conjunto o diccionario vacío.

	Esto está así, ya que nosotros seguido del enlace que ya tenemos podremos pasarle argumentos, para pasarle un primer argumento tendremos que colocar un signo interrogante *?* y seguido de este un par de clave-valor: *?key1=test*:

	![[IMG_835.png]]

	Veremos como ahora nos coloca en los argumentos el que hemos pasado por medio del enlace y también es representado en el enlace en la parte inferior.

	Con esto en mente, si quisiéramos agregar múltiples argumentos, una vez agregado el primero para agregar más tendremos que usar *&* y colocarlos juntos de la misma manera, ahora sin el interrogante:

	![[IMG_836.png]]

	Esto mismo podríamos hacerlo en Python de una forma más interesante, primeramente los parámetros que queramos agregar los almacenaremos como pares de clave-valor en un diccionario y luego con el método *get* como primer argumento le pasaremos el enlace base y como segundo argumento pasaremos nuestro diccionario, asignándolo al parámetro *params*:

	![[IMG_837.png]]

	Finalmente, podríamos ver como la URL quedara compuesta como la hemos visto antes gracias al método *url* y con *text* recordemos que podremos ver la respuesta:

	![[IMG_838.png]]

	Al ejecutarlo tendríamos lo siguiente:

	![[IMG_839.png]]

	Al realizar esta petición por *get* vemos cómo los parámetros que le pasamos son mostrados en la *url*. Si cambiáramos nuestro método de consulta por *post* en el url también tendríamos que cambiar *get* por *post* y, al momento de pasar los parámetros, ahora no sería asignarlos a *params* sino a *data*.

	Con esto en mente, nuestro diccionario con los valores que pasaremos se llama *values*, esto es totalmente opcional, pero al momento de realizar una petición mediante el método *post* puede llegar a ser más descriptivo llamarlo *payload*, lo cual nos quedaría de la siguiente manera:

	![[IMG_840.png]]

	![[IMG_841.png]]

	Lo cual nos serviría para enviar datos a través de una petición post y vemos cómo todo se ha almacenado en el apartado *form*.

	*Modificar headers*

	Si observamos la petición que realizamos, esta cuenta con sus propios *headers*, en este caso podríamos ver el *User-Agent* el cual contiene información desde donde se ha realizado la petición, en este caso de Python.

	Con esto en mente, nosotros podríamos modificarlo creando un diccionario *headers* y en este agregar el par clave-valor, que tenga como clave *User-Agent* y como valor el que nosotros deseemos. En este caso colocaremos *myapp/1.0.1*, lo cual asignaremos directamente en nuestra petición al parámetro *headers* como argumento:

	![[IMG_842.png]]

	Viendo esto, tengamos que *data* y *headers*, que son a los que les estamos asignando los diccionarios de clave-valor que hemos creado, son propiedades de la propia petición, por ende podremos asignarles valores o cambiarlos en función de lo que consideremos necesario.

	Con esto en mente, al ejecutar esto veríamos cómo ahora hemos cambiado el valor del header *User-Agent*:

	![[IMG_843.png]]

	*Header en una pagina*

	Si nos vamos a la página de google.es y abrimos la consola del navegador, podremos irnos al apartado de *Network*:

	![[IMG_844.png]]

	Al presionar, por ejemplo, en la primera petición *POST* que nos salga, veremos en *Request headers* los headers de esta petición, entre ellos el de *User-Agent*.

	![[IMG_845.png]]

	Por lo tanto, nosotros podríamos solicitar una petición mediante get a *https:\/\/google.es* y mediante *headers* asignarle un valor distinto al valor *User-Agent*:

	![[IMG_846.png]]

	Finalmente, con *response* que es donde se guarda el objeto de nuestra petición, utilizaríamos *request* para recuperar la petición de nuestro lado y *headers* para únicamente recuperar los headers y no mostrar todo:

	![[IMG_847.png]]

	Así veremos cómo hemos modificado el valor que recibimos para el *User-Agent* del header de nuestro lado en la petición.

	*Manejo de excepciones*

	A la hora de realizar solicitudes, Python nos permite realizar un manejo de excepciones. Un ejemplo sería colocar un timeout en nuestra petición *get*,  esto es importante, ya que habrá páginas que puedan tardar hasta 10 segundos en darnos una respuesta y podremos definir un límite de tiempo, que en caso de que no responda mediante el uso agregado de donde se almacene la respuesta con el método *raise_fo_status()*, nos lanzará una excepción para indicar que tuvimos un error en cuanto a una petición:

	![[IMG_848.png]]

	En este caso, sí o sí, se generará la excepción de tiempo de respuesta excedido, ya que Google no responderá en 0.1 segundos. Podremos tratar las excepciones con *try*, en el caso del timeout su excepción se gestiona con *requests.Timeout*:

	![[IMG_849.png]]

	Al nosotros trabajar con peticiones, podría presentarse un tipo de error HTTPError. Este se puede manejar como excepción e incluso gestionarse con un nombre específico para mostrarlo al usuario:

	![[IMG_850.png]]

	Esto sería para en caso de presentarse un error HTTP. Algo que también podríamos gestionar es imprimiendo un mensaje en caso de que todo salga bien, con un *else* al final de todas las excepciones y si lo ejecutamos funcionaría correctamente:

	![[IMG_851.png]]

	Para visualizar este efecto donde todo sale bien, he modificado el timeout a 1 segundo para que la petición a Google nos sea respondida.

	Además, tenemos *RequestException* la cual nos engloba de forma general errores de tiempo de espera, HTTP, errores de conexión y entre muchos más. Lo cual también podremos manejarlo de forma más descriptiva para mostrarlo al usuario:

	![[IMG_852.png]]

	Esto al final sería algo más general, englobando muchos tipos de errores para mostrarse en caso de presentarse (recordemos agregar la *f* de *F-strings*).

	Un ejemplo sería modificar nuestro url por uno que no sea correcto, lo cual terminaría dándonos un error y nos entraría a nuestra excepción recientemente agregada:

	![[IMG_853.png]]

	De esta forma se ha dado un tipo de error general que no ha coincidido con ninguno de los primeros dos y por ello se nos ha mostrado gracias a nuestra excepción *RequestException*.

	Entonces estas excepciones son las principales que nos pueden ayudar a saber qué es lo que ha pasado con nuestra solicitud.

	*Manejo de los datos de una respuesta*

	Con el ejemplo de la página *https:\/\/httpbin.org\/get*  nosotros realizamos una petición  y vemos cómo la respuesta que recibimos la obtenemos en un formato tipo JSON, con utilizar donde se nos guarda la respuesta, podremos utilizar el método *json()* para convertirlo directamente a este formato, teniendo como resultado un diccionario de diccionarios:

	![[IMG_854.png]]

	![[IMG_855.png]]

	Esto en Python realmente es de mucha ayuda, ya que directamente nos sirve para tratar los datos de forma directa sin ningún problema, al estar todo como si de un diccionario se tratase.

	Al tenerlo en un diccionario, al ver los datos, vemos cómo el *User-Agent* se encuentra almacenado dentro de los *headers*. Es por ello que primeramente podríamos realizar una validación de si se encuentran *headers* en el diccionario y luego de si se encuentra el *User-Agent* en los headers.

	De esta manera, almacenar y mostrar su valor o, de lo contrario, indicar que  este campo no se encuentra disponible:

	![[IMG_856.png]]

## **Librería requests (2/2)**

1. **Introducción**

	*Curiosidades y Aspectos Complementarios de requests*

	- *Orígenes y Popularidad:* requests fue creada por Kenneth Reitz en 2011. Su diseño enfocado en la simplicidad y la legibilidad rápidamente la convirtió en una de las bibliotecas más populares en Python. Su lema es *HTTP for Humans*, reflejando su objetivo de hacer solicitudes HTTP accesibles y fáciles para los desarrolladores.
	- ds
	- *Comunidad y Contribuciones:* requests es un proyecto de código abierto y ha recibido contribuciones de numerosos desarrolladores. Esto asegura su constante actualización y adaptación a las nuevas necesidades y estándares de la web.
	- sdd
	- *Inspiración en Otros Lenguajes:* El diseño de requests se inspira en otras bibliotecas HTTP de alto nivel de otros lenguajes de programación, buscando combinar lo mejor de cada uno para crear una experiencia de usuario óptima en Python.
	- sds
	- *Extensibilidad:* Aunque requests es poderosa por si sola, su funcionalidad se puede ampliar con varios complementos. Esto incluye adaptadores para diferentes tipos de autenticación, soporte para servicios como AWS, o herramientas para aumentar su rendimiento.
	- dsdd
	- *Uso en la Educación y la Industria:* Debido a su simplicidad y potencia, requests se ha convertido en una herramienta de enseñanza estándar para la programación de red en Python. Además, es ampliamente utilizada en la industria para desarrollar aplicaciones que requieren comunicación con servidores web.
	- dsdfe
	- *Casos de Uso Diversos:* Desde la automatización de tareas y el scraping web hasta el testing y la integración con APIs, requests tiene un rango de aplicaciones muy amplio. Su versatilidad la hace adecuada tanto para proyectos pequeños como para aplicaciones empresariales a gran escala.
	- dsdds
	- *Soporte para Proxies y Timeouts:* requests ofrece un control detallado sobre aspectos como proxies y timeouts, lo cual ews crucial en entornos de producción donde la gestión del tráfico de red y la eficiencia son importantes.
	- sdd
	- *Manejo Eficiente de Excepciones:* Proporciona una forma clara y consistente de manejar errores de red y HTTP, lo que ayuda a los desarroladores a escribir aplicaciones más robustas y confiables.

	En resumen, requests no es solo una biblioteca de alto nivel para solicitudes HTTP en Python, sino que también es un ejemplo brillando de diseño de software y colaboración comunitaria. Su facilidad de uso, junto con su potente funcionalidad, la convierte en una herramienta indispensable para cualquier desarrollador que trabaje con Python en el ámbito de la web.
	</br>
2. **Práctica**

	*Autenticarse  mediante una petición*

	Existen páginas como la siguiente:

	`https://httpbin.org/basic-auth/foo/bar`

	Esto nos servirá para realizar esta práctica, pero al nosotros abrir el sitio en el navegador lo que nos solicitara será credenciales para tener acceso.

	![[IMG_857.png]]

	El usuario correcto es *foo* y la contraseña es *bar*.

	Con esto en mente, ahora realizaríamos una petición *get* a este enlace y como argumentos estarán el enlace primeramente y como segundo tendremos la propiedad *auth* a la cual le asignaremos una tupla donde el primer elemento será el usuario y el segundo la contraseña:

	![[IMG_858.png]]

	Primeramente, lo ejecutaremos con credenciales válidas y veremos como esto no nos retorna nada; sin embargo, si en lugar de tratar de mostrar la respuesta, mostramos el código de estado, tendríamos lo siguiente:

	![[IMG_859.png]]

	Si buscáramos este error, veríamos como el error 401 en solicitudes HTTP significa de *unauthorized*, lo cual es un error que se presenta cuando no tenemos autorización de entrar, debido a que hemos colocado las credenciales incorrectas.

	Ahora, si colocáramos las credenciales correctas, veríamos como ya nos retornaría una respuesta:

	![[IMG_860.png]]

	Existe una forma más "complicada" de realizar una autenticación y esta sería autenticarnos mediante la creación de un objeto temporal.

	Para realizar esto, tendríamos que importar de *requests.auth* la clase *HTTPBasicAuth* y con esta crear la instancia temporal a donde le pasaremos los argumentos de usuario y contraseña:

	![[IMG_861.png]]

	Esto lo podríamos considerar como complicarnos más, ya que sin ningún problema podríamos autenticarnos solo con la propiedad *auth* y pasándole como tupla las credenciales correctas.

	Esto funciona correctamente debido a que la web tiene un login sencillo al cual se le llama *HTTPBasciAuth*. Si en lugar de esto fuese una web más completa con su propio formulario y que llegan a manejar más datos, no funcionaria de esta forma, ya que tendríamos que adecuarlo para iniciar sesión correctamente.

	Por lo que, lo que hemos realizado solamente es para paneles básicos de autenticación.

	*Modificar las cookies*

	De la misma forma que es posible modificar nuestros *headers* también es posible modificar nuestras *cookies*. Esto puede venir bien para no dar información de nuestro lado de la petición que estamos realizando, por lo que la información entregada al servidor sería modificada por nosotros mismos.

	En este caso, utilizando la misma página, tendremos:

	`https://httpbin.org/cookies`

	La cual no contendrá ninguna cookie, ya que no estamos enviando ni arrastrando ninguna cookie de sesión.

	![[IMG_862.png]]

	Entonces, si nosotros hiciéramos una petición *get* a esta url veríamos como nos retorna las cookies vacías. Recordando de qué manera realizábamos la petición para modificar nuestros *headers*, podremos hacer lo mismo para nuestras cookies, creando primeramente un diccionario de pares de clave-valor y pasándolo a la propiedad *cookies*.

	Ahora crearemos nuestro diccionario de forma un poco distinta, le asignaremos un valor a una variable y luego le haremos un *typecasting* para convertirlo a diccionario, donde si lo mostramos por pantalla lo tendríamos de la siguiente manera:

	![[IMG_863.png]]

	![[IMG_864.png]]

	Entonces, nosotros podríamos enviárselo a nuestra petición y al mostrar la respuesta, tendríamos lo siguiente:

	![[IMG_865.png]]

	*Enviar archivos mediante una petición*

	Recordando cuando realizamos nuestra petición por *POST*, la respuesta tenía un apartado *files:*

	![[IMG_866.png]]

	![[IMG_867.png]]

	Entonces este apartado nos listaría algún archivo en caso de subirlo.

	Para esto, primeramente crearemos por ejemplo *mi_archivo.txt* y en este pondremos cualquier cosa, como "Hola, soy el contenido del archivo".

	![[IMG_868.png]]

	En este caso, para enviar el archivo desde nuestra petición también tendríamos que crear un diccionario, donde la clase sería la que nosotros queramos, como *archivo* y el valor sería el archivo, donde con *open* lo abriremos en modo de lectura y finalmente lo pasaremos para la petición con el atributo *files*:

	![[IMG_869.png]]

	Por lo que si lo ejecutáramos, veríamos como ahora el contenido de nuestro archivo estaría en el apartado de *files*:

	![[IMG_870.png]]

	*Arrastrar cookies*

	Al momento de estar en páginas que requieren de un logueo, si se listan contenidos internos, pues para cada petición tendríamos que estar colocando las cookies *cookies=cookies*, pero existe una forma de ahorrarnos esto y directamente saber con qué usuario se está tratando. Esto es posible gracias al uso de *sesiones*.

	Un ejemplo sería primeramente setear una cookie, esto es posible gracias a:

	`https://httpbin.org/cookies/set/{name}/{value}`

	Si nosotros en name colocáramos "my_cookie" y en value "123123", nos redirige a *cookies* y vemos como aquí ya está almacenada:

	![[IMG_871.png]]

	Lo cual nos almacenará una cookie y después si cerramos y entráramos directamente a `https://httpbin.org/cookies/`, veríamos como nos sigue cargando esta cookie sin ningún problema.

	Esto se debe a que el navegador por defecto nos almacena las cookies y las arrastra en una misma sesión, pero por terminal sería distinto, ya que no tenemos nada que nos esté arrastrando una sesión.

	Lo podríamos ver si lanzamos nuevamente una petición a la página de las cookies, donde a menos que nosotros definamos una *cookie*, no nos retornara más que las cookies vacías.

	*Ejemplo:*

	Ahora podríamos replicar lo mismo que hicimos en el navegador, primeramente enviando la solicitud en la que seteamos una cookie y después otra petición en la que recuperamos los valores en la página de las cookies.

	![[IMG_872.png]]

	Pero al momento de ejecutarlo, veremos cómo el resultado final es que las cookies están vacías, lo cual se debe a que  ambas peticiones son como dos peticiones totalmente distintas y separadas una de la otra, por lo que no arrastra las cookies de la anterior.

	Esto se debe a la forma en la que trabaja Python con las peticiones, pero con *requests* podremos utilizar *Session()*, lo cual lo almacenaremos como una variable y ahora cada que ejecutemos algún método de petición en lugar de utilizar *requests* utilizaríamos el nombre de la variable, debido a que esta ya será una sesión la cual almacenara las peticiones que se realicen y en el caso de que se almacenen cosas, esto ya lo arrastrará sin ningún problema:

	![[IMG_873.png]]

	Por ende, esto viene bien cuando nos autenticamos en un sitio, ya que ya no tendríamos que preocuparnos por estar arrastrando las cookies y esto automáticamente lo haría, por lo que podremos acceder ya a rutas internas, sin ninguna preocupación, ya que ya lo considerará.

	*Preparar una solicitud antes de enviarla*

	Para esto, primeramente tendremos que traer *Request* y *Session* de la libreria *requests* y trabajaremos con la pagina `https://httpbin.org/get`:

	![[IMG_874.png]]

	Ahora, definiríamos una sesión con *Session* y lo almacenaríamos en la variable *s*, lo cual nos servirá para ir arrastrando las cosas que vayamos realizando.

	Después de esto, definiremos nuestra consulta con *Request* como si de una clase se tratase, está como argumentos principales, tendrá primeramente el método por el que vamos a  realizar la consulta, en este caso *GET*, como segundo argumento la URL y de ahí podremos agregar cosas que vayamos a modificar como headers o cookies, en este caso agregaremos un *Custom-Header*:

	![[IMG_875.png]]

	Aquí tendríamos ya definida nuestra *request*, pero esta tendríamos que prepararla, para por ejemplo poder ir realizando modificaciones en función de las peticiones que vayamos a desear realizar.

	Para esto, en una variable *prepped* guardaremos el resultado de preparar nuestra *request*, que será la  variable *req* y utilizaremos el método *prepare()*. Con esto listo ahora podremos modificar, por ejemplo, nuestro *Custom-Header* y como si de un valor en un diccionario se tratase, tendríamos que acceder a este mediante *prepped.headers* y seleccionar la posición indicada para cambiar su valor:

	![[IMG_876.png]]

	Con esto listo solo nos quedaría enviar nuestra solicitud, para ello utilizaremos nuestra sesión con el método *send()*, donde pasaremos como argumento nuestra request ya preparado *prepped* y almacenaremos la respuesta en *response*, donde finalmente podremos acceder a la respuesta como lo hemos visto antes, con el atributo *text*:

	![[IMG_877.png]]

	Quedando el código finalmente así:

	![[IMG_878.png]]

	Finalmente, tendríamos como resultado nuestra respuesta con el custom header que colocamos en un inicio, modificado:

	![[IMG_879.png]]

	Con esto en mente, realmente lo que nos permitiría hacer es irlo preparando sobre la marcha para realizar modificaciones antes de realizar el envío final de nuestra solicitud, por lo que, por ejemplo, en este caso podríamos agregar un header nuevo en el proceso de preparar nuestra solicitud:

	![[IMG_880.png]]

	![[IMG_881.png]]

	*Manejar un historio de las redirecciones que se den en una solicitud*

	Al momento de estar manejando solicitudes, puede pasar en alguna página que al momento de realizar una solicitud esta haga redirecciones hacia otras páginas, por lo cual nosotros tendremos una forma de recoger todas las url's de estas páginas, para tener como un histórico de ellas.

	Para esto podríamos poner un ejemplo propio con *github*, ya que esta página, si nosotros intentamos entrar con *http:\/\/github.com*, nos hará una redirección a *https:\/\/github.com*.

	Para ver esto, al hacer una petición con Python, podríamos realizar una solicitud por el método *get* a `http://github.com` y al final mostrar el url de la respuesta:

	![[IMG_882.png]]

	Veremos como nos aplica la redirección y nos devuelve la url de la redirección que aplica github.

	Incluso en Python, tenemos la posibilidad de evitar las redirecciones al momento de realizar una solicitud, utilizando la propiedad *allow_redirects* y asignándole el valor *False*, lo cual nos retornara la misma url que tendremos en un inicio:

	![[IMG_883.png]]

	Teniendo esto en mente, tenemos la posibilidad de ver todas las URL anteriores a la final por las que hemos pasado, utilizando el método *history* en nuestra respuesta:

	![[IMG_884.png]]

	Esto por si solo, nos retorna un iterable, que podremos ir iterando y por cada iteración, teniendo la posibilidad de extraer el url y el código de estado que nos ha dado. Finalmente, si todas las url por las que se ha pasado antes de llegar a la final se muestran sin problemas, mostraremos la final gracias al *else* en los bucles:

	![[IMG_885.png]]

	De esta forma ya podríamos gestionar todas las url por las que pasa nuestra petición cuando nos redirecciona a otras páginas.

	*Mejor manejo de sesiones*

	Las sesiones se pueden manejar de mejor manera con *with*, colocando así todo lo que deseemos realizar con la sesión correspondiente dentro de un bloque, como dos peticiones *get*

	![[IMG_886.png]]

	Una forma de ver esto sería utilizar la propiedad *auth* para setearlo a una tupla con el valor del usuario y contraseña, para la ruta, donde en la primera solicitud se autenticaría, pero ya para la segunda nos estaría arrastrando la autenticación con la sesión correspondiente:

	![[IMG_887.png]]

	Con esto ya no tendríamos que autenticarnos para la segunda petición, finalmente, pues esta sería una forma más organizada de trabajar con sesiones.

## **Librería Urllib3**

1. **Introducción**

	*urllib3* es una biblioteca de Python ampliamente utilizada para realizar solicitudes HTTP y HTTPS. Es conocida por su robustes y sus numerosas características, que la hacen una herramienta versátil para una variedad de aplicaciones de red. A continuación, se presenta una descripción detallada de *urllib3* y sus capacidades.

	**Descripción Detallada de la Biblioteca urllib3**

	*Funcionalidades Clave*

	- *Gestión de Pool de Conexiones:* Una de las características más destacadas de *urllib3* es un manejo de pools de conexiones, lo que permite reutilizar y mantener conexiones abiertas. Esto es eficiente en términos de rendimiento, especialmente cuando se hacen múltiples solicitudes al mismo host.
	- dfd
	- *Soporte para Solicitudes HTTP y HTTPS:* *urllib3* ofrece un soporte sólido para realizar solicitudes tanto HTTP como HTTPS, brindando la flexibilidad necesaria para trabajar con una variedad de servicios web.
	- dde
	- *Reintentos Automáticos y Redirecciones:* Viene con un sistema incorporado para manejar reintentos automáticos y redirecciones, lo cual es esencial para mantener la robustez de las aplicaciones en entornos de red inestables.
	- dfdf
	- *Manejo de Diferentes Tipos de Autenticación:* Proporciona soporte para varios esquemas de autenticación, incluyendo una autenticación básica y digest, lo que la hace apta para interactuar con una amplia gama de APIs y servicios web.
	- dsds
	- *Soporte para Características Avanzadas del HTTP:* Incluye soporte para características como la compresión de contenido, el streaming de solicitudes y respuestas, y la manipulación de cookies, ofreciendo así un control detallado sobre las operaciones de red.
	- scdc
	- *Gestión de SSL/TLS:* *urllib3* tiene capacidades avanzadas para manejar la seguridad SSL/TSL. Incluyendo la posibilidad de trabajar con certificados personalizados y la verificación de la conexión segura.
	- sds
	- *Tratamiento de Excepciones y Errores:* La biblioteca maneja de manera eficiente las excepciones y errores, permitiendo a los desarrolladores gestionar situaciones con tiempos de espera, conexiones fallidas y errores de protocolo.

	*Aplicaciones y Uso*

	*urllib3* se utiliza en una variedad de contextos, desde scrapping web y automatización de tareas, hasta la construcción de clientes para interactuar con APIs complejas. Su capacidad para manejar conexiones de manera eficiente y segura la hace adecuada para aplicaciones que requieren un alto grado de interacción de red, así como para escenarios donde el rendimiento y la facilidad son cruciales.

	*Importancia en el Ecosistema de Python*

	Si bien existen otras bibliotecas como *requests* que son más amigables para principiantes, *urllib3* se destaca por su control detallado y su rendimiento en situaciones que requieren un manejo más profundo de las conexiones de red. Es una biblioteca fundamental para desarrolladores que busca un control más granular sobre sus operaciones HTTP/HTTPS en Python.
	</br>
2. **Práctica**

	Esta librería tendría básicamente la misma finalidad que *requests*; sin embargo, lo que cambiara es la facilidad al usarlas, ya que *requests* es una librería enfocada más al alto nivel otorgando una mayor facilidad de uso, mientras que *urllib3* va mucho más al detalle, siendo más compleja de emplear, ya que va un poco más a bajo nivel.

	Un dato interesante es que el emplear *requests* por detrás también se emplea parte de la biblioteca *urllib3*, ya que *requests* abstrae ciertas funcionalidades de esta, por lo que estas van de la mano realmente.

	En cuanto al *manejo de errores*, hemos visto que en request son muy sencillos de manejar con excepciones. Con *urllib3* también es posible hacerlo, pero al meterse más a bajo nivel nos da una mayor posibilidad de control de los tipos de errores y excepciones, aumentando más la dificultad de implementarlo, pero tiene sus ventajas, ya que a más control tengamos empleando esta librería, podremos mejorar el rendimiento de nuestros programas, otorgando una mayor optimización de nuestro código.

	*Solicitudes get*

	Una vez importada la librería, tendríamos que definir un controlador de conexiones, utilizando *PoolManager()*:

	![[IMG_888.png]]

	De esta forma, ahora *http* sería un controlador de conexiones de cara a futuras conexiones que queramos entablar.

	Ahora con esto, utilizando *request*, indicando como primer argumento el método por el cual se empleara la solicitud y como segundo el enlace, como lo haremos por *GET* utilizaremos el enlace `https://httpbin.org/get` y almacenaremos la respuesta en *response*.

	Para acceder a la respuesta, al emplear *urllib3*, ahora se accede a esta con la propiedad  *data*:

	![[IMG_889.png]]

	![[IMG_890.png]]

	El problema con esto, es que por defecto nos retorna la respuesta en formato de *bytes* por ende tendríamos que aplicarle un *decode* para visualizarlo en el formato correcto:

	![[IMG_891.png]]

	![[IMG_892.png]]

	*Enviar datos por una petición POST*

	Ahora vamos a enviar datos en bruto mediante una petición *POST*, para nosotros enviar datos directamente y que no lo tome como formulario tendríamos que utilizar la propiedad *body*, mientras que si queremos que nos lo tome como formulario tendríamos que utilizar *fields*.

	Para ello, primeramente definiremos una variable data con un contenido y luego una variable *encoded_data* donde le pasemos el contenido de la variable data y le apliquemos un encode, para después pasarlo mediante la propiedad *body*:

	![[IMG_893.png]]

	![[IMG_894.png]]

	*Datos como diccionario*

	Si tratáramos nuestros datos a nivel de diccionario, no podremos aplicarle directamente un *encode*, ya que no es una cadena de texto, para ello tendríamos que emplear el uso de la librería *json*, ya que esta nos permite convertir un diccionario en una cadena de texto en este formato gracias a *dumps()* pasándole como argumento nuestro diccionario y a esto si que ya podríamos aplicarle un *encode:*

	![[IMG_895.png]]

	Por lo que esto ya podríamos enviarlo mediante nuestra petición:

	![[IMG_896.png]]

	![[IMG_897.png]]

	De esta forma podremos enviar datos en forma de diccionario sin que el propio servidor lo llegue a percibir como si de un formulario se tratase.

	Al momento de enviar nuestros datos de esta manera se nos pudo presentar un error, en este caso no fue así, pero no será así siempre.

	Es por ello que lo mejor sería además arrastrar o agregar una cabecera *header* con la propiedad *headers*, la cual tendrá como llave *Content-Type* y como valor *application/json*:

	![[IMG_898.png]]

	Esto nos puede servir debido a que luego Python puede no saber como interpretar los datos que le están siendo enviados y de esta forma nos lo evitariamos.

	*Enviar un formulario*

	Si lo que queremos es que esto nos lo tome directamente como si de un formulario se tratase, lo que tendríamos que hacer sería pasarle mediante la propiedad *fields* directamente nuestro diccionario, sin aplicar ningún encode:

	![[IMG_899.png]]

	![[IMG_900.png]]

	*Mejor organización de nuestro request*

	También podríamos mandar una cabecera personalizada mediante una solicitud por el método *GET*, esto ya lo hemos hecho, por lo que ahora el enfoque será en cuanto a trabajar con esto teniendo una posible mejor organización si así lo consideramos.

	Ya que por cada coma en las cosas que vayamos colocando, podríamos dar un salto de línea, viendo todo de una forma un poco mejor organizada y esto no tendría ningún problema para ejecutar exactamente lo mismo:

	![[IMG_901.png]]

	![[IMG_902.png]]

	*Redirecciones*

	Con esta librería también podremos manejar redirecciones, en caso de no querer que nos redireccione nuestra solicitud, será tan simple como colocar la propiedad *redirect* y setearla en *False*, para este caso utilizaremos la dirección `https://httpbin.org/redirect/1`, la cual nos redirige a la ruta *get*.

	Teniendo esto en cuenta evitaremos la redirección e imprimiremos el código de estado con *status*:

	![[IMG_903.png]]

	En este caso el código de estado es *302*, pero en el caso de permitir la redirección y llegar a la última página con éxito:

	![[IMG_904.png]]

	Es importante mencionar que por defecto las redirecciones están permitidas.

	*Visualizar los distintos métodos y propiedades*

	Si en algún momento olvidamos los distintos métodos y propiedades que podrá contener nuestra respuesta, bastaría con pasarlo como argumento a nuestro método especial *dir()*, lo que nos retornara todas las posibilidades que tenemos:

	![[IMG_905.png]]

	*Recuperar la redirección final:*

	Para recuperar la redirección final que nos hizo nuestra solicitud, tendríamos que utilizar el método *get_redirect_location()* y con ello podríamos mostrarlo en pantalla en caso de tener las redirecciones en *False*:

	![[IMG_906.png]]

	*Webs con certificados SSL autofirmados*

	Para este caso nos iremos a la página `https://www.shodan.io/` y buscaremos por el puerto *443*:

	![[IMG_907.png]]

	En este caso, yo seleccioné la siguiente web:

	![[IMG_908.png]]

	Si nos metemos en esta, veremos como tendremos que aceptar "riesgos", ya que contiene un certificado autofirmado:

	![[IMG_909.png]]

	Lo cual tendremos que aceptar en *advanced* y dándole en *aceptar el riesgo y continuar*:

	![[IMG_910.png]]

	Por lo tanto, si nosotros hiciéramos una petición *GET* a esta página y viéramos el output que esta nos trae, nos retornará un error, ya que tendremos que aceptar este certificado autofirmado:

	![[IMG_911.png]]

	![[IMG_912.png]]

	La forma de evitar este error sería como tal ignorar el certificado autofirmado y entrar directamente, para ello utilizaríamos seguido de la importación de la librería:

	```python3
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  
	```

	Esto lo que hará por detrás es evitar que se realice una verificación por certificados autofirmados SSL, pero no será suficiente. También se tendrá que pasar como argumento la propiedad *cert_reqs* asignándole el valor *CERT_NONE* a nuestro *PoolManager()* para que funcione correctamente:

	![[IMG_913.png]]

	De esta manera, ahora, al ejecutarlo, ya no tendríamos ningún problema:

	![[IMG_914.png]]

	Esto mismo se puede realizar con request de la siguiente manera:

	![[IMG_915.png]]

	![[IMG_914.png]]

	Como *requests* y *urllib3* son librerías que van muy de la mano, realmente queda de forma muy similar el evitar que nos dé errores al momento de que una página tenga una certificación SSL autofirmada y acceder.

## **Librería threading y multiprocessing**

1. **Introducción**

	Las bibliotecas *threading* y *multiprocessing* en Python son herramientas esenciales para la programación concurrente y paralela. Proporcionan mecanismos para ejecutar múltiples tareas simultáneamente, aprovechando mejor los recursos del sistema. A continuación, se presenta una descripción detallada de ambas bibliotecas y sus diferencias.

	**Descripción Detallada de threading y multiprocessing**

	*Biblioteca threading*

	*threading* es una biblioteca para la programación concurrente que permite a los programas ejecutar múltiples *hilos* de ejecución al mismo tiempo. Los hilos son entidades más ligeras que los procesos, comparten el mismo espacio de memoria y son ideales para tareas que requieren poco procesamiento o que están limitadas por E/S.

	- *Uso Principal:* Ideal para tareas que no son intensivas en CPU o que esperan recursos (como E/S de red o de archivos)
	- ds
	- *Ventajas:* Bajo costo de creación y cambio de contexto, compartición eficiente de memoria y recursos entre hilos.
	- xsd
	- *Desventajas:* Limitada por el Global Interpretes Lock (GIL) en CPython, que previene la ejecución de múltiples hilos de Python al mismo tiempo en un solo proceso.

	**Biblioteca multiprocessing**

	*multiprocessing*, por otro lado, se enfoca en la creación de procesos. Cada proceso en multiprocessing tiene su propio espacio de memoria. Esto significa que pueden ejecutarse en paralelo real en sistema con múltiples núcleos de CPU, superando la limitación de GIL.

	- *Uso Principal:* Ideal para tareas intensivas en CPU que requieren paralelismo real.
	- sada
	- *Ventajas:* Capacidad de realizar cálculos intensivos en paralelo, aprovechando múltiples núcleos de CPU.
	- dsw
	- *Desventajas:* Mayor costo en recursos y complejidad en la comunicación entre procesos debido a espacios de memoria separados.

	**Diferencias Clave**

	- *Modelo de Ejecución:* *threading* ejecuta hilos en un solo proceso compartiendo el mismo espacio de memoria, mientras *multiprocessing* ejecuta múltiples procesos con memoria independiente.
	- sds
	- *Uso de CPU:* *multiprocessing* es más adecuado para tareas que requieren mucho cálculo y pueden beneficiarse de múltiples núcleos de CPU, mientras que *threading* es mejor para tareas limitadas por E/S.
	- dsd
	- *Global Interpreter Lock (GIL):* *threading* está limitado por el GIL de CPython, lo que restringe la ejecución en paralelo de hilos, mientras que *multiprocessing* no tiene esta limitación.
	- sddf
	- *Gestión de Recursos:* *threading* es más eficiente en términos de memoria y creación de hilos, pero *multiprocessing* es más eficaz para tareas aisladas y seguras en cuanto a datos.

	**Conclusión**

	Entender y utilizar adecuadamente *threading* y *multiprocessing* es crucial para optimizar aplicaciones en Python, especialmente en términos de rendimiento y eficiencia. La elección entre ambas depende de las necesidades específicas de la tarea, como el tipo de carga de trabajo (CPU-intensiva vs E/S-intensiva) y los requisitos de arquitectura de la aplicación.
	</br>
2. **Práctica**

	El uso de *hilos* puede ser muy conveniente en casos que necesitemos realizar múltiples cosas en un mismo proceso,

	Podremos construir un ejemplo donde tengamos una función con dos mensajes, donde inicia y finaliza, pero entre estos colocaremos un tiempo de espera de dos segundos, posteriormente ejecutaremos la función dos veces, pasándole como argumento el número de tarea que se está ejecutando:

	![[IMG_916.png]]

	De esta manera, las dos tareas que hemos creado se ejecutaran de forma secuencial, para que la segunda se ejecute tendrá que haber terminado la primera.

	Y esto si tenemos múltiples tareas, es un proceso que se vuelve demasiado lento y dependiente de que las tareas anteriores hayan concluido.

	Para ello tendremos en mente los hilos, ya que nos permitirán ejecutar estas múltiples tareas, dentro de un mismo proceso en paralelo.

	*Implementación de hilos*

	Para los hilos utilizaremos la librería *threading*, recordemos que para esta tenemos la clase *Thread* y a esta le pasaremos como argumentos, a la propiedad *target* a la que asignaremos la función de nuestra tarea y también la propiedad *args* donde le pasaremos los argumentos de nuestra función, estos se pasan en forma de tupla, por lo que al ser solo un elemento se le tendrá que agregar una coma al final, para que lo tome como tupla.

	![[IMG_917.png]]

	De esta manera, creamos nuestros hilos como instancias y con *start()* se inicializan a la vez.

	Finalmente, podremos imprimir un mensaje que indique que los hilos han finalizado correctamente, pero para que esto espere a que finalicen, tendremos que utilizar el método *join()* de la propia instancia de nuestro hilo. Seguido de esto ya podremos colocar lo que deseamos ejecutar como siguiente.

	![[IMG_918.png]]

	Teniendo como resultado que ambos procesos se ejecutan en simultáneo con los hilos, además de que nuestro mensaje final espera a que los hilos finalicen, al aplicar *join()* en ambas instancias.

	![[IMG_919.png]]

	De esta manera, también se ha reducido el tiempo total de ejecución de nuestro ejemplo sin aplicar hilos.

	*Multiprocesos con multiprocessing*

	Es similar a *threading*, la principal diferencia es que al ejecutar diversos procesos con *multiprocessing* estos no compartirán memoria, por lo que serán procesos totalmente separados uno del otro. Esto significa que no podrán compartir variables de la misma forma a como sucede con los hilos.

	Algo interesante es que pueden aprovechar múltiples núcleos de la CPU, lo que viene útil al implementar tareas de CPU intensivas. Además de tener una sintaxis muy similar a *threading*:

	![[IMG_920.png]]

	Aqui se aplica el mismo concepto, con una sintaxis muy similar, ahora la diferencia será que al ser dos procesos totalmente independientes, no siempre finalizaran en el mismo orden, en ocasiones será uno pero en ocasiones otro.

	![[IMG_921.png]]

	*Ejemplo práctico*

	Implementando la ayuda de la librería *requests*, crearemos una lista de diversos dominios y a estos le realizaremos una petición *GET* mediante un bucle. Además, mediante el uso de la librería *time* recogeremos el tiempo en el que se inicia y en el que finaliza para así calcular el tiempo que tardo en total el solicitar todas estas peticiones.

	![[IMG_922.png]]

	De esta manera se iría haciendo petición por petición conforme se tome cada url mediante el bucle.

	![[IMG_923.png]]

	De esta manera, para cada URL, se calcula el tamaño del contenido que esta retorna como respuesta y se muestra.

	Finalmente, gracias al tiempo inicial y final, se calcula la diferencia y es posible saber cuánto duró la ejecución de todas las peticiones en conjunto.

	*Empleando hilos*

	Lo anterior tiene este tiempo de cálculo sin emplear hilos, por lo que empleándolos debería ser mucho más rápido.

	Para emplear hilos, en este caso, la idea sería que toda la lógica de nuestro bucle, en donde itera sobre la lista y aplica la petición a cada dominio, tendríamos que colocarlo dentro de una función, a la cual llamaremos *realizar_peticion*, a esto le pasaríamos como argumento nuestro URL, ya que el bucle lo definiríamos en la parte inferior:

	![[IMG_924.png]]

	Ahora en nuestro bucle iríamos definiendo cada hilo por cada iteración. Al ser hilos temporales, antes del bucle definiríamos una lista de hilos, donde los iremos guardando luego de generar nuestro hilo e inicializarlo:

	![[IMG_925.png]]

	Recordemos que para que el resto de nuestro código se ejecute una vez los hilos hayan finalizado de ejecutarse, tendremos que utilizar el método *join()* para cada hilo, por lo que como hemos almacenado cada uno de ellos en una lista, ahora podremos iterar sobre esta y para cada hilo aplicar el *join()*, lo cual nos servirá para esperar a que todos los hilos finalicen correctamente:

	![[IMG_926.png]]

	![[IMG_927.png]]

	De esta manera, al ejecutarlo, ya notaremos una mayor rapidez. Además del cálculo del tiempo que transcurre, se nota que ha disminuido bastante.

	*Utilizando multiprocessing*

	Para utilizar la librería *multiprocessing* hemos visto que la sintaxis es prácticamente la misma, solo cambian los nombres para las referencias de la librería y clase:

	![[IMG_928.png]]

	En cuanto al tiempo de ejecución, será algo muy similar:

	![[IMG_929.png]]

	Es importante, dependiendo del caso, esperar a que finalicen los hilos, ya que si elimináramos el bucle que nos permite esperar a que finalicen todos los hilos aplicando *join()*, nos llevaría directamente a la ejecución de las siguientes líneas, antes de esperar a que estos procesos o hilos finalicen.

[[#Índice]]

## **Siguientes apuntes**

[[Desarrollo_de_aplicaciones_de_escritorio_con_Python]]