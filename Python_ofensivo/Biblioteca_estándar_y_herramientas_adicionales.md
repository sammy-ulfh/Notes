
## **Índice**

- [[#Manejo de fechas y horas]]
- [[#Expresiones regulares]]
- [[#Manejo de archivos y directorios]]
- [[#Conexiones de red y protocolos (1/4)]]
- [[#Conexiones de red y protocolos (2/4)]]


## **Manejo de fechas y horas**

1. **Introducción**

	La biblioteca *datetime* en Python es una de las principales herramientas a trabajar con fechas y horas. Aquí hay algunos aspectos clave sobre la biblioteca.

	- *Tipos de Datos Principales:* *datetime* incluye varios tipos de datos, como *date* (para fechas), *time* (para horas), *datetime* (para fechas y horas combinadas) y *timedelta* (para representar diferencias de tiempo).
	- *Manipulación de Fechas y Horas:* Permite realizar operaciones como sumar o restar días, semanas, o meses en una fecha, comparar fechas o extraer componentes como el día, mes o año de una fecha específica.
	- *Zonas Horarias:* A través del módulo *pytz* que se integra con *datetime*, se pueden manejar fechas y horas en diferentes zonas horarias, lo que es crucial para aplicaciones que requieren precisión a nivel global.
	- *Formateo y Análisi:* *datetime* permite convertir fechas y horas a string y viceversa, utilizando códigos de formato específicos. Esto es útil para mostrar fechas y horas en formatos legibles o para parsear string que representan fechas/horas.
	- *Facilidad de Uso:* A pesa de su potencia y flexibilidad, datetime es relativamente fácil de usar, lo que la hace accesible incluso para programadores principiantes.
	- *Amplia Aplicación:* Desde registros de eventos hasta cálculos de períodos de tiempo, datetime es indispensable en una variedad de aplicaciones, como sistemas de reservas, análisis de datos temporales, y más.

	En resumen, datetime es una biblioteca integral y robusta para el manejo de fechas y horas en Python, ofreciendo una amplia gama de funcionalidades esenciales para el manejo de datos temporales en la programación.
	</br>
2. **Práctica**

	Con todo lo anterior en mente, ahora crearíamos un nuevo archivo y en este importaríamos la librería *datetime*:

	![[IMG_683.png]]

	Con esta librería ahora gracias a *.datetime.now()* podremos obtener la fecha actual y almacenarla en una variable para después mostrarla:

	![[IMG_684.png]]

	La forma en que se mostrara por convenio es año-mes-día hora:minuto:segundos

	Nosotros también podríamos crear una fecha utilizando *date()*, esta sería siguiendo el convenio anterior:

	![[IMG_685.png]]

	Así como hemos generado una fecha, también podríamos generar una hora, con *time()*:

	![[IMG_686.png]]

	Además, también es posible generar una fecha y hora en conjunto con *datetime()*:

	![[IMG_687.png]]

	Con el ejemplo, en el que extraemos la hora actual, de esta misma podremos extraer con ciertas propiedades todo de manera individual:

	![[IMG_688.png]]

	Teniendo como resultado:

	![[IMG_689.png]]

## **Expresiones regulares**

1. **Introducción**

	La librería *re* en Python proporciona un conjunto completo de herramientas para trabajar con expresiones regulares, que son patrones de cadenas diseñados para la búsqueda y manipulación de texto.

	Varios aspectos importantes de esta librería:

	- *Funciones Básicas:* *re* incluye funciones como *search* (para buscar un patrón dentro de una cadena), *match* (para verificar si una cadena comienza con un patrón específico), *findall* (para encontrar todas las ocurrencias de un patrón) y *sub* (para reemplazar partes de una cadena que coinciden con un patron).
	  </br>
	- *Compilación de Patrones:* Permite compilar expresiones regulares en objetos de patrón, lo que puede mejorar el rendimiento cuando se usan repentinamente.
	  </br>
	- *Grupos y Captura:* Ofrece una capacidad de definir grupos dentro de patrones de expresiones regulares, lo que facilita extraer partes específicas de una cadena que coinciden con subpatrones.
	  </br>
	- *Flags:* Soporta modificaciones que alteran la forma en que las expresiones regulares son interpretadas y coincididas, como ignorar mayúsculas y minúsculas o permitir el modo multilínea.
	  </br>
	- *Patrones Complejos:* Permite la creación de patrones complejos utilizando una variedad de símbolos y secuencias especiales, como cuantificadores, aserciones y clases de caracteres.
	  </br>
	- *Aplicaciones Prácticas:* Las expresiones regulares son extremadamente útiles en tareas como la validación de formatos (por ejemplo, direcciones de correo electrónico), el análisis de registros (logs), el procesamiento del lenguaje natural, y la limpieza y preparación de datos.
	  </br>
	- *Curva de Aprendizaje:* Aunque potentes, las expresiones regulares pueden ser complejas y requieren de una curva de aprendizaje. Sin embargo, una vez dominadas, se convierten en una herramienta invaluable en el arsenal de cualquier programador.

	En resumen, la librería ‘**re**‘ en Python es una herramienta esencial para cualquier tarea que implique procesamiento complejo de cadenas de texto, proporcionando una forma poderosa y flexible de buscar, analizar, y manipular datos basados en texto.
	</br>
2. **Práctica**

	La librería que estaremos utilizando para todo esto es *re*, por ende la importaremos y crearemos una cadena para, con base en esta cadena, empezar a ver cómo podríamos utilizarla:

	![[IMG_690.png]]

	Con esto, ahora con *findall* de esta librería, podríamos buscar matches de alguna secuencia de caracteres, por ejemplo si buscáramos cuantas veces aparece 'gato', a *findall* le pasaríamos como primer argumento la secuencia a buscar y como segundo argumento en donde la buscara, en este caso será nuestra variable *text* y lo que esto nos retornara son las coincidencias de nuestra cadena y en una lista lo colocara, lo que además nos hará saber cuantas veces lo encontró:

	![[IMG_691.png]]

	*Consideración de dígitos con \\d:*

	Incluso podríamos jugar con caracteres especiales para casos un poco distintos, por ejemplo, si tuviésemos un texto con dos fechas representas:

	![[IMG_692.png]]

	En este caso tendemos dos fechas, las cuales tienen exactamente el mismo formato, día-mes-año, y tiene dos elementos entre cada '/', por ende con ello lo que haremos será utilizar un carácter especial *\\d{num}*, donde con *num* le indicamos el número de caracteres a considerar.

	En este caso serían 2, ya que entre cada barra */* tenemos dos números, por lo que al realizar esto, colocaríamos la búsqueda como "\\d{2}/\\d{2}/\\d{2}", indicándole que en cada barra tendrá que considerar 2 caracteres, gracias al carácter especiales *\\d*:

	![[IMG_693.png]]

	De esta manera, con conocer solamente un patrón igual en ambas fechas, podremos extraerlas.

	Esto nos lanzará el resultado esperado, pero desde luego es recomendable que cuando indicamos nuestra barra */* que sí que está en el texto, le indiquemos antes una barra invertida *\\*, esto nos ayudará a que no interprete la barra */* como que queremos indicar otra cosa y simplemente la ignore o la considere texto. Esto es importante, ya que en expresiones regulares, dependiendo de lo que queramos realizar, la barra */* también permite realizar cosas.

	![[IMG_694.png]]

	Entonces, realmente *\\d* por sí solo lo podremos considerar como que podrá considerar un dígito en la cadena, pero gracias a las llaves podremos colocar cierta cantidad de caracteres que nos interese tomar. En este caso, al final realmente se toman 4 dígitos, ya que el año tiene 4 dígitos y se han colocado 2, por lo que realmente nos quedaría de la siguiente manera:

	![[IMG_695.png]]

	Por lo que aquí hemos jugado de igual con patrones de búsqueda, pero además empleamos caracteres especiales.

	*Patrones de búsqueda para la obtención de grupos:*

	Un ejemplo sería tener una cadena donde tengamos 2 correos electrónicos a los que los usuarios podrían contactar, pero lo que queremos con base en este texto es obtener de los correos electrónicos, de cada uno una tupla donde tomando como delimitador el *@*, nos regrese en la primera posición de la tupla lo que esta antes del *@* y como segunda posición lo que esta después, el texto sería:

	![[IMG_696.png]]

	Y esperando como resultado algo como: *\[(soporte, hack4u.io)\]*.

	Entonces, para obtener esto, tendríamos que considerar primero, buscar un match y esto lo podremos hacer con *()@()*, lo cual nos sirve para indicar que vamos a contemplar una secuencia de caracteres antes y después de un *@* el cual será nuestro delimitador.

	Dentro del primer paréntesis vamos a colocar *\\w*, esto nos sirve para indicar que en este apartado podremos tener un carácter alfanumérico, como claramente habrá más de 1, para que lo considere tendremos que agregarle un *+* luego de *\\w*, quedándonos como *\\w+*, de esta manera consideraría múltiples caracteres alfanuméricos (números y letras).

	Para nuestro segundo paréntesis indicaríamos lo mismo, pero seguido de esto tendremos que contemplar el punto *.* y este también lo escaparemos con *\\*, ya que los puntos en expresiones regulares también nos permiten indicar ciertas cosas. Una vez escapado el número, volveremos a indicar que aquí puede haber caracteres alfanuméricos, pero haciendo uso de las llaves colocaremos que después del punto todos tienen un mínimo de 2 caracteres alfanuméricos: *\\w{2,}* y la coma nos permite representar que 2 es un mínimo y no conocemos el máximo.

	De esta manera, nos quedaría lo siguiente:

	![[IMG_697.png]]

	Lo del mínimo después del punto es porque todos los correos tienen siempre mínimo dos caracteres después del punto. Con esto conseguimos obtener distintos grupos que son almacenados en una tupla y estas tuplas por cada match en una lista.

	Si nosotros colocáramos un límite de caracteres alfanuméricos, el final de nuestro correo es demasiado largo, listaría solamente hasta el límite indicado:

	![[IMG_698.png]]

	En este caso, en el primer grupo lista todo sin problemas, pero en el segundo, al tener en *technologies* 12 caracteres, solo nos mostrará hasta el límite indicado de 5, que sería *techn*.

	*Sustituciones con expresiones regulares::*

	La librería *re* cuenta con *sub()*, lo cual nos permite realizar sustituciones en texto, por ende si nosotros tuviésemos la siguiente cadena:

	![[IMG_699.png]]

	Utilizando *sub()* podríamos especificar como primer argumento algún match, por ejemplo *gato* y en caso de que este exista en el texto reemplazarlo por otra cadena como *perro* indicada como segundo argumento, y finalmente como tercer argumento el texto donde esperamos realizar la sustitución:

	![[IMG_700.png]]

	Si en ambos tuviésemos gato, al encontrar dos matches, en ambos nos cambiaría *gato* por *perro*.

	*Realizar split en textos con la librería re:*

	Podríamos imaginar que tenemos el contenido de un archivo *csv*, como el siguiente texto:

	![[IMG_702.png]]

	Y ahora, para utilizar split y separar cada campo y colocarlo en una lista, el primer argumento tendrá que ser el delimitador, en este caso la coma, y el segundo argumento tendrá que ser donde buscará este delimitador y separado almacenará todo en una lista y lo retornará:

	![[IMG_703.png]]

	**Ejercicio de validador de correo**

	Ahora crearemos un programita el cual nos sirva para validar la estructura de un correo electrónico, donde si es correcta nos retornará un *True* y si es incorrecta nos retornará un *False*.

	Para esto comenzaremos creando la función *validar_correo*, esta recibirá como argumento el correo y primeramente crearemos un patrón:

	![[IMG_704.png]]

	De esta manera estaríamos haciendo exactamente lo mismo que cuando hicimos el match con el correo anteriormente, la diferencia sería que estaríamos englobando nuestros propios caracteres haciéndolo más personalizable. De esta manera, antes de arroba, dentro de los corchetes con *A-Z* estamos haciendo referencia a todas las letras mayúsculas de la A a la Z, lo mismo aplica para las minúsculas y los números, además agregamos un punto, guion bajo, más y menos.

	Esto quiere decir que cualquiera de estos caracteres puede ser el que esté ahí, finalmente fuera de los corchetes se le agrega el *+* para indicar que cualquiera de los caracteres englobados podrá estar ahí y que puede haber múltiples.

	El *@* nuevamente lo tenemos considerándolo como nuestro delimitador y después del arroba englobamos posibles caracteres y quitamos el punto, menos, más y guion bajo, ya que en esta parte no debería de haber, nuevamente se le coloca el *+* después lo que englobamos, ya que puede haber múltiples caracteres de acuerdo a los que englobamos. Llegamos al punto y lo escapamos y luego después del punto también englobaremos los posibles caracteres que puedan estar si es un correo y nuevamente con las llaves indicaremos un mínimo de dos caracteres.

	Luego de que nuestro patrón este definido, vamos a buscar el match con la librería y *findall*, pasándole como primer argumento el patrón y como segundo argumento, donde tendrá que buscarlo:

	![[IMG_705.png]]

	Finalmente, si hay un match  regresará una lista con un elemento, pero si no hay match regresará una lista vacía. Verificar si una lista tiene contenido o no es algo que podremos verificar con un condicional, por lo que aprovechándonos de esto, cuando la lista tenga contenido nos retornará *True* y cuando no, quiere decir que no hubo match, por lo que nos retornará *False*:

	![[IMG_706.png]]

	Por ende, finalmente vamos a llamar la función y pasarle un correo correcto y haremos un print de lo que retorne:

	![[IMG_707.png]]

	Y en caso de pasarle un correo incorrecto:

	![[IMG_708.png]]

	*Concepto de búsquedas con las regex:*

	Cuando realizamos búsquedas con *findall*, se hace incluso tomando palabras que en su contenido pueden llegar a completar alguna palabra. Por ejemplo, si tuviésemos las siguientes palabras:

	![[IMG_709.png]]

	En este caso nos retorna 4 veces *car*, porque en 4 palabras se llegan a completas estos 3 caracteres.

	Pero también podremos hacer referencia a que nos llegue a hacer match solamente de aquellas que inicien con estos 3 caracteres, pero puedan contener más a la derecha, esto lo haremos con *\\b* al inicio, pero a la izquierda de la cadena que indica esto, tendremos que colocar una *r*, lo cual hace referencia a que nos tome en consideración los caracteres especiales:

	![[IMG_710.png]]

	De esta manera, nos va a considerar solo aquellas que inicien con *car*. También podremos aplicarlo si queremos aquellas que finalicen con *car* o lo tengan cerca del final, agregando el carácter especial *\\b* al final:

	![[IMG_711.png]]

	Con esto, lo que nos retorna son los matches donde las palabras contiene *car* cerca del final, por ende nos estaría retornando los matches de las palabras masticar y magicarp.

	Si quisiéramos que nos encuentre match únicamente con la palabra *car*, pues tendremos que colocar el carácter especial al inicio y al final.

	![[IMG_712.png]]

	Esto lo podríamos traducir como que inicia con *car* y finaliza con *car*, lo que nos resultaría en que si hay algo a la izquierda o derecha de esta palabra, entonces no nos lo va a considerar.

	Entonces, considerando esto para nuestro validador de correos, podremos agregar este carácter especial y nos funcionará sin problemas, siendo más preciso:

	![[IMG_713.png]]

	*Utilizando finditer:*

	Primeramente, tomaremos el ejemplo de las fechas y realizaremos la misma búsqueda, pero ahora lo que haremos será hacerlo aplicando un grupo:

	![[IMG_714.png]]

	Lo que *finditer* nos permite, es de alguna forma iterar para poder realizar cosas con esto, la forma en la que podriamos usarlo es directamente iterando ya que nos retorna un objeto que podremos iterar:

	![[IMG_715.png]]

	De esta manera le pasamos a *finditer* los argumentos del patrón y el texto donde buscara con este patrón.

	Esto lo que nos retorna realmente es un objeto el cual podremos iterar y en cada iteración guardamos el contenido en *match*, por lo que al imprimir lo que vemos son como dos objetos.

	Lo cómodo de esto, es que si quisiéramos obtener la fecha correspondiente al match, bastaría con utilizar *group* sobre este objeto y pasarle el argumento *0*:

	![[IMG_716.png]]

	Lo interesante de esto, es que directamente podríamos ir iterando entra cada match y con *group(0)* mostrar el match, pero con *start()* podríamos mostrar a partir de qué índice de la cadena de texto empieza y con *end()* donde finaliza:

	![[IMG_717.png]]

	Como ya sabemos, a una cadena de caracteres podremos acceder a sus caracteres individuales, por lo que accediendo a una posición, accederíamos a un carácter, la posición 0 por ejemplo en este caso, sería la *H*.

	Las expresiones regulares son un tema bastante extenso, por lo que se puede profundizar más, estas se suelen utilizar mucho para realizar comprobaciones y verificar que el texto está planteado como queremos.

	Es por ello que se puede profundizar más en el siguiente video: [Expresiones regulares](https://www.youtube.com/watch?v=MRKpVxn5fqI&t=59s)

## **Manejo de archivos y directorios**

1. **Introducción**

	La librería *os* y el módulo *shutil* en Python son herramientas fundamentales para interactuar con el sistema de archivos, especialmente en lo que respecta a la creación y eliminación de archivos y directorios.

	Aquí tienes una descripción detallada de ambas:

	*Librería os:*

	- *Funcionalidades Básicas:* *os* proporciona una interfaz rica y variada para interactuar con el sistema operativo subyacente. Permite realizar operaciones como la creación y eliminación de archivos y directorios, así como la manipulación de rutas y el manejo de la información del sistema de archivos.

	*Creación y Eliminación de Archivos y Directorios:*

	- *Creación de Directorios:* Utilizando *os.mkdir()* u *os.makedirs()*, se pueden crear directorios individuales o múltiples directorios (y subdirectorios) respectivamente.
	  </br>
	- *Eliminación:* *os.remove()* se usa para eliminar archivos, mientras que *os.rmdir()* y *os.removedirs()* permiten eliminar directorios y directorios con subdirectorios, respectivamente.
	  </br>
	- *Gestión de Rutas:* La sublibrería *os.path* es crucial para manipular rutas de archivos y directorios, como unir rutas, obtener nombres de archivos, verificar si un archivo o directorio existe, etc.

	*Módulo shutil:*

	- *Operaciones de Alto Nivel:* Mientras que *os* se enfoca en operaciones básicas, *shutil* proporciona funciones de nivel superior, más orientadas a tareas complejas y operaciones en lotes.
	  </br>
	- *Copiar y Mover Archivos y Directorios:* *shutil* es especialmente util para copiar y mover archivos y directorios. Funciones como *shutil.copy()*, *shutil.copytree()* y *shutil.move()* facilitan estas tareas.
	  </br>
	- *Eliminación de Directorios:* Aunque *os* puede eliminar directorios, *shutil.rmtree()* es una herramienta más poderosa para eliminar un directorio completo y todo su contenido.
	  </br>
	- *Manejo de Archivos Temporales:* *shutil* también ofrece funcionalidades para trabajar con archivos temporales, lo que es útil para operaciones que requieren almacenamiento temporal de datos.

	En resumen *os* y *shutil* en Python son bibliotecas complementarias para la gestión de archivos y directorios.
	Mientras *os* ofrece una gran flexibilidad para operaciones básicas y de bajo nivel, *shutil* brinda herramientas más potentes y de alto nivel, adecuadas para tareas complejas y operaciones en lotes. Juntas, forman un conjunto integral de herramientas para la manipulación eficaz del sistema de archivos en Python.

	</br>
2. **Práctica**

	El manejo en cuanto a directorios y archivos con estas librerías es muy importante en Python, ya que por ejemplo en cuanto a un programa que nosotros utilicemos en nuestro propio ordenador, teniendo en cuenta una carpeta o archivo que para nosotros si es existente, pero para otra persona no, entonces con *os* y *shutil*, podremos definir cierta lógica que nos ayude a trabajar de alguna manera para ya sea crear estos archivos o directorios o extraerlos de algún lado, para que también estén contemplados para esa persona.

	Con esto en mente, nosotros podríamos comprobar  si un archivo existe con *os.path.exists()* y como argumento le tendremos que pasar el nombre de este archivo, esto retornara un *True* si existe y un *False* si no existe, por ende lo podríamos gestionar con un condicional. Para esto tendremos que importar la librería *os*:

	![[IMG_718.png]]

	Si ahora creáramos el archivo, pues nos regresaría un *True* porque si existe:

	![[IMG_719.png]]

	*Crear directorios con os.mkdir()*

	De esta misma forma podríamos verificar si un directorio no existe y en caso de que no exista, podremos crearlo, para crearlo utilizaremos *os.mkdir()* y como argumento le pasaremos el nombre de este directorio que vamos a crear.

	![[IMG_720.png]]

	Además, con *os* también podremos crear directorios anidados, lo cual se refiere a crear directorios con subdirectorios gracias a *makedirs()*, de esta manera si borráramos el directorio *mi_directorio*, pues este ya no existiría, pero ahora si comprobamos si existe *mi_directorio* y a la vez su subdirectorio *mi_subdirectorio*, pues no existen, por lo que gracias a *makedirs()*, podríamos crear los dos a la vez:

	![[IMG_721.png]]

	*Listar el directorio actual con listdir():*

	Si utilizamos *listdir()* podremos listar todo el contenido del directorio actual, esto nos será dado en forma de una lista (se crearon 5 archivos de texto solo para el ejemplo):

	![[IMG_722.png]]

	Al ser una lista lo que nos es retornado, podríamos listarlo con *join*, colocando un salto de línea como separador entre cada elemento:

	![[IMG_723.png]]

	O también iterando en la lista:

	![[IMG_724.png]]

	*Eliminar archivos con remove()*

	Podremos eliminar archivos también, utilizando  *remove()* y pasándole como argumento el nombre del archivo, de esta manera primeramente podríamos verificar si un archivo existe y de ser así, eliminarlo:

	![[IMG_725.png]]

	*Eliminar directorios vacios con rmdir():*

	Si creáramos un directorio vacío, por ejemplo *prueba*, si este no tienen ningún contenido dentro podremos borrarlo, de lo contrario nos lanzaría una excepción indicando que el directorio no está vacío:

	![[IMG_726.png]]

	*Utilizando shutil para eliminar directorio que no esten vacios:*

	Realizando la misma comprobación de si un directorio existe, en caso de que este tenga contenido (en esta caso un subdirectorio), podríamos eliminarlo utilizando la librería *shutil* y de esta *rmtree()*, que le pasaríamos como argumento el nombre del directorio y lo eliminaría:

	![[IMG_727.png]]

	*Renombrar archivos con rename en os:*

	Mediante el uso de la librería *os*, podremos renombrar archivos con *rename()*, donde el primer argumento será el nombre actual del archivo y el segundo el nuevo nombre:

	![[IMG_728.png]]

	*Calcular el tamaño de un archivo en bytes:*

	Empleando la librería *os*, podríamos utilizar *path.getsize()* y pasándole un archivo nos retornaría el tamaño en byte, en este caso le pasaré un archivo propio del sistema Linux:

	![[IMG_729.png]]

	Contemplar rutas con *path.join()*, la forma en la que este funciona es que le tendremos que pasar como argumento los distintos directorios y subdirectorios , uno a uno en orden y finalmente el archivo al cual queremos llegar, por lo que el colocar de esta manera los directorios, subdirectorios y el archivo, nos retornará la representación del directorio:

	![[IMG_730.png]]

	Para representar la ruta absoluta desde el directorio actual hasta *mi_archivo.txt*, pues sería ==mi_directorio/mi_subdirectorio/mi_archivo.txt==, lo cual está bien, pero dependiendo del sistema, el Linux se representa de esta manera, pero en Windows podría llegar a dar errores porque se representan con la barra invertida *\\*, en este caso tenemos *path.join()*, al cual pasándole como argumento cada directorio de forma ordenada hasta llegar a nuestro archivo nos ayudaría a representarlo:

	![[IMG_731.png]]

	Con esto en mente, incluso podremos hacer referencia a *basename* que hace referencia al archivo y *dirname* que hace referencia al directorio:

	![[IMG_732.png]]

	De esta manera, de acuerdo a una ruta dada, el último que le pasamos es nuestro archivo y el resto será el directorio o ruta para llegar a ese archivo. Es importante contemplar este orden, ya que siempre nos tomaría como *basename* lo último que ingresamos, mientras que el resto será tomado como *dirname*:

	![[IMG_733.png]]

	De esta manera podríamos conseguir gestionar y manipular rutas dentro del sistema. Incluso aquí podría ser un ejemplo donde podríamos utilizar *split()* con la librería *os*, para separar toda la ruta, pasandola directamente como argumento y podríamos almacenar cada cosa en variables distintas:

	![[IMG_734.png]]


## **Conexiones de red y protocolos (1/4)**

1. **Introducción**

	Los protocolos *TCP* (Transmission Control Protocol) y *UDP* (User Datagram Protocol) son fundamentales en la comunicación de red, y la librería *socket* en Python proporciona las herramientas necesarias para interactuar con ellos. Aquí tienes una descripción detallada de ambos protocolos y el uso de ‘*socket*‘:

	*Protocolos TCP:*

	- *Orientado a la Conexión:* TCP es un protocolo orientado a la conexión, lo que significa que establece una conexión segura y confiable entre el emisor y el receptor antes de la transmisión de datos.
	  </br>
	- *Fiabilidad y Control de Flujo:* Garantiza la entrega de datos sin errores y en el mismo orden que se enviaron. También gestiona el control de flujo y la corrección de errores.
	  </br>
	- *Uso en Aplicaciones:* Es ampliamente utilizado en aplicaciones que requieren una entrega fiable de datos, como navegadores web, correo electrónico, y transferencia de archivos.

	*Protocolo UDP:*

	- *No Orientado a la Conexión:* A diferencia de TCP, UDP es un protocolo no orientado a la conexión. Envía datagramas (paquetes de datos) sin establecer una conexión previa.
	  </br>
	- *Rápido y Ligero:* UDP es más rápido y tiene menos sobrecarga que TCP, ya que no verifica la llegada de paquetes ni mantiene en orden los mismos.
	  </br>
	- *Uso en Aplicaciones:* Ideal para aplicaciones donde la velocidad es crucial y se pueden tolerar algunas pérdidas de datos, como en juegos en línea, streaming de video y voz sobre IP (VoIP).

	*Librería 'socket' en Python:*

	La librería *socket* en Python es una herramienta esencial para la programación de comunicaciones en red. Permite a los desarrolladores crear aplicaciones que pueden enviar y recibir datos a través de la red, ya sea una red local o a través de internet. Aquí tienes una visión general de la librería *socket*:

	- *Creación de sockets:* La librería *socket* proporciona clases y funciones para crear sockets, que son puntos finales de comunicación. Puedes crear sockets tanto para el protocolo TCP (Transmission Control Protocol) como para UDP (User Datagram Protocol).
	- sd
	- *Conexiones TCP:* Puedes utilizar *socket* para establecer conexiones TCP, que son conexiones confiables y orientadas a la conexión. Esto es útil para aplicaciones que requieren transferencia de datos confiable, como la transmisió de archivo o la comunicación cliente-servidor.
	- sddsd
	- *Comunicación UDP:* La librería *socket* también admite la comunicación mediante UDP, que es un protocolo de envío de mensajes sin conexión. Es adecuado para aplicaciones que necesitan una comunicación rápida y eficiente, como juegos en línea o aplicaciones de transmisión de video en tiempo real.
	- sds
	- *Funciones de envío y recepción:* Puedes utilizar métodos como *send()* y *recv()* para enviar y recibir datos a través de sockets. Esto permite tranferir información entre dispositivos de manera eficiente.
	- sds
	- *Gestión de conexiones:* La librería *socket* incluye métodos como *bind()* para asociar un socket a una dirección y puertos específicos, y *listen()* para poner un socket en modo de escucha, lo que permite aceptar conexiones entrantes.
	- dsd
	- *Conexiones cliente-servidor:* Con *socket*, puedes crear aplicaciones cliente-servidor, donde un programa actúa como servidor esperando conexiones entrantes y otro actúa como cliente para conectarse al servidor.

	En resumen, la librería *socket* en Python proporciona las herramientas necesarias para desarrollar aplicaciones de red, permitiendo la comunicación entre dispositivos a través de diferentes protocolos y ofreciendo control sobre la tranferencia de datos. Es una parte fundamental  de la programación de redes en Pytho y se utiliza en una amplia variedad de aplicaciones, desde servidores web hasta aplicaciones de chat y juegos en línea.
	</br>
2. **Práctica**

	En Python es común crear exploits y al saber que diversos servicios operan en un puerto dado, al nosotros saberlo y querer explotar este servicio tendremos que entablar la conexión o comunicación desde nuestro script con este servicio. Por ende utilizaremos la librería *socket*, la cual nos permitirá entablar las conexiones tanto por TCP como por UDP, que a nivel de protocolo sería orientado a conexión y no orientado a conexión.

	De esta manera, un socket lo podremos considerar como una asignación o designación de un concepto abstracto, el cual nos permitirá intercambiar cualquier flujo de datos, generalmente de una forma fiable y ordenada. Lo que además nos permite que dos máquinas se comuniquen entre ellas.

	Algo que vamos a estar creando es prácticamente un servidor que se ponga en escucha en un puerto dado y en otro realizar la conexión y enviar algo, como lo siguiente con netcat:

	![[IMG_735.png]]

	De esta manera, la parte superior es la que está en escucha en *localhost* mediante el puerto 123, mientras que la parte inferior realiza una conexión al *localhost* al puerto dado, por lo que si nosotros enviamos el *Hola, esto es una prueba* desde nuestra conexión, nuestra parte superior que está en escucha lo recibe.

	Con esto en mente, vamos a crear un nuevo archivo en Python, colocaremos nuestro *shebang* e importaremos la librería *socket*:

	![[IMG_736.png]]

	Lo primero que tendríamos que hacer, es crear el socket del servidor. Donde ahora *server_socket* nos permitirá aceptar conexiones entrantes y por ende establecer este servicio en escucha para que otros clientes se conecten:

	![[IMG_737.png]]

	De esta manera, con el método *socket()*, nuestro primer argumento *socket.AF_INET* hace referencia a la familia de direcciones que acepta, que en este caso estamos tratando con IPv4, por ende con *socket.AF_INET* estamos indicándolo. Con *socket.SOCK_STREAM*, estamos indicando que vamos a trabajar con conexiones *TCP* (Transmission Control Protocol).

	Por ende esta sería la primera línea, pero para estar nosotros en escucha, en este caso definiremos que será en el equipo local (*localhost*) por el puerto *1234*, por lo tanto, tendríamos que definir *server_address*, donde estaremos indicando que estará por escucha en el localhost y por el puerto 1234:

	![[IMG_738.png]]

	De esta manera, al utilizar *bind()* sobre nuestro socket y pasarle como argumento en donde se pondrá en escucha, ahora estaríamos poniéndonos en escucha en *localhost* por el puerto *1234*.

	![[IMG_739.png]]

	Con esto, ahora la idea es que para nosotros aceptar conexiones de múltiples clientes y en paralelo comunicarnos con todos, lo conveniente sería jugar con hilos.

	En este caso, primeramente estaríamos trabajando con un único cliente y lo que estaríamos definiendo es como una cola de espera donde si ya esta entablada una conexión con un cliente, el resto de conexiones que se intenten estarán como en una cola de espera, de forma que mientras que no se cierre una conexión que ya esta entablada con un cliente, no va a llegar la información o mensaje del siguiente. Por lo que para efectuar esto podríamos utilizar directamente con nuestro socket *listen()* y como argumento pasarle el número de conexiones a las que vamos a limitarlo.

	![[IMG_740.png]]

	Ahora, mediante un bucle infinito, podremos definir otro socket, pero este será un socket que recibiremos del cliente que se conecte, de forma que ahora nosotros también podríamos comunicarnos con él y enviar información, este lo recibiremos con la propiedad *accept()*  y nos retornara dos valores, uno que será el propio socket y otro que será la información desde donde se esta conectando y el otro que sea el puerto:

	![[IMG_741.png]]

	Por ende, ahora la idea aquí es que el cliente se conecta y primeramente recibimos su socket y address para también nosotros poder comunicarnos con él. Entonces, como también el cliente nos enviara datos, lo que haremos será que mediante el socket del cliente vamos a recibir esos datos, información o mensaje con *recv()* y como argumento le pasaremos el número de bytes que queremos recuperar de esa información enviada por el cliente, de tal manera que esa información en bytes la almacenaremos en una variable *data*:

	![[IMG_742.png]]

	Como esta información esta en bytes, a la hora de representarla de una forma legible para nosotros, tendríamos que utilizar *decode()*, para transformarlo a una cadena legible (tengamos en cuenta que cuando nosotros seamos el cliente, también tendremos que convertir estos bytes a una cadena antes de enviarlo), de esta manera al mostrarlo por pantalla, que sería la variable *data*, tendríamos que aplicar el *decode()*:

	![[IMG_743.png]]

	También podríamos representar la información del cliente con la conexión que se ha realizado, por lo que podríamos mostrar *client_address* con un mensaje. Además, utilizar *sendall()* para automáticamente enviarle un mensaje al cliente una vez nos envíe uno, jugaremos con *f* strings para que interprete el salto de línea y al final de la cadena colocaremos *.encode()* para que la cadena sea enviada en bytes al cliente.

	![[IMG_744.png]]

	Finalmente con *close()*, vamos a indicar que nos cierre esa conexión con el cliente una vez se haya acontecido todo lo anterior, de forma que solo estaríamos permitiendo recibir un mensaje y una vez recibido, le retronaríamos al cliente "Un saludo, crack!", y una vez esto suceda se cerrara la conexión:

	![[IMG_745.png]]

	De esta forma ya tendríamos montado un pequeño servidor, el cual pondremos a correr. Primeramente, estableceríamos la conexión utilizando *netcat* y después vamos a montanos el script para que, siendo un cliente, conectarnos con Python.

	![[IMG_746.png]]

	Si estamos en Linux y movemos algunas cosas en el script por curiosidad, o forzamos el cierre de este, puede ser que el puerto no se llegue a cerrar correctamente y al ejecutar el script de nuevo nos diga que este puerto esta ocupado, para este caso podremos utilizar el comando `sudo ufw deny PORT` (cambia PORT por el puerto correspondiente).

	De esta forma, vemos como cuando un cliente se conecta, esta conexión abre un puerto aleatorio al cual mismamente nosotros podremos enviarle información que proporcionamos en el script.

	Por lo que si una vez se cierra ese socket nos volviéramos a conectar, funcionaria correctamente:

	![[IMG_747.png]]

	Ahora, si viéramos lo de las múltiples conexiones con respecto a la cola de usuarios por usuario de acuerdo en el orden que se conecten, si ahora hiciéramos 3 conexiones, enviamos en mensaje de la primera, pero luego un mensaje de la tercera, el mensaje de la tercera no se vería reflejado:

	![[IMG_748.png]]

	De esta forma, hasta que el cliente que en orden se conectó como segundo envíe algo, no se enviara nada del tercero, y una vez el segundo envíe un mensaje, la representación de todo se efectuara en el orden que se conectaron:

	![[IMG_749.png]]

	*Conexión de un cliente:*

	Ahora, si quisiéramos generar un script para realizar una conexión desde el lado del cliente, el concepto sería el mismo. Crearíamos un script *client.py* y en este vamos a aplicar el mismo principio para crear el socket del cliente y en cuanto a la conexión que realizara, para nuestro *server_address*, aquí colocaríamos la dirección de a donde se va a conectar el cliente:

	![[IMG_750.png]]

	De esta manera, le estamos indicando al crear el socket del cliente que con *socket.AF_INET* estamos creando un socket para conexión utilizando IPv4 y con *socket.SOCK_STREAM* que es una conexión TCP (Transmission Control Protocol).

	Luego en *server_addres*, estamos indicando la dirección de a donde nos conectaremos.

	Aquí, tomando directamente el socket de cliente vamos a indicar que nos vamos a conectar a la dirección dada, en el caso del servidor para abrirlo se utiliza *bind()*, pero cuando se trata de un cliente para conectarse, se utiliza *connect()* y de igual manera le pasaremos el *address* del servidor:

	![[IMG_751.png]]

	Finalmente, como lo de limitar la cantidad de conexiones a la vez  se gestiona del lado del servidor, aquí lo que nosotros haremos será efectuar un *try*, pero no utilizaremos excepciones, ya que realmente no se suelen dar errores del lado del cliente, más bien utilizaremos luego del *try* un *finally* que sabremos que si o si se ejecutara después del *try* y en nuestro *finally* lo que haremos será cerrar nuestro propio socket, ya que esto siempre es una buena práctica para evitar que quede por ahí abierto y tener fugas de información:

	![[IMG_752.png]]

	Ahora escribiremos un mensaje el cual enviaremos en forma de bytes con *sendall()*, así como también recibiremos lo que el servidor nos retorne con *recv()* y lo mostraremos aplicándole un *decode*, ya que recordemos que los datos son siempre enviados en formato de bytes.

	![[IMG_753.png]]

	De esta manera, al ejecutarlo tendríamos lo siguiente:

	![[IMG_754.png]]

	Aquí en nuestro script del servidor estamos cerrando solamente el socket del cliente, pero realmente aún nos faltaría cerrar el socket del servidor, de la forma en que podríamos gestionarlo es que una vez presionemos *ctrl + c*  (*KeyboardInterrupt*) para terminar el programa, nuestro programa detecte esto y sería como la forma de capturar el flujo de salida de nuestro script y aquí ya cerraríamos el programa.

## **Conexiones de red y protocolos (2/4)**

1. **Introducción**

	*Manejadores de contexto con conexiones:*

	Los manejadores de contexto (*with* en Python) se utilizan para garantizar que los recursos se gestionen de manera adecuada. En el contexto de las conexiones de socket, un manejador de contexto se encarga de abrir y cerrar el socket de manera segura. Esto evita que los recursos del sistema queden en uso indefinidamente y asegura una gestión adecuada de las conexiones.

	*Diferencias entre send y sendall:*

	- *send(data):* El método *send()* se utiliza para enviar una cantidad específica de datos a través del socket. Puede no enviar todos los datos en una sola llamada y puede ser necesario llamarlo múltiples veces para enviar todos los datos.
	- sd
	- *sendall(data):* El método *sendall()* se utiliza para enviar todos los datos especificados a través del socket. Realiza llamadas repetidas a *send()* internamente para garantizar que todos los datos se envíen por completo sin pérdidas.

	La elección entre *send* y *sendall* depende de si se necesita garantizar la entrega completa de los datos o si se permite que los datos se envíen en fragmentos. send puede enviar datos fragmentos, mientras que sendall garantiza que todos los datos se envíen sin pérdida.
	</br>
2. **Práctica**

	Utilizando *with* podremos optimizar de mejor manera todo el servidor que hemos montado anteriormente, ya que al colocarlo lo que conseguimos es que automáticamente se cierren los sockets tanto de servidor y cliente sin ningún problema, evitando que quede información colgada y sería mucho más eficiente.

	![[IMG_755.png]]

	Aquí, de una forma mucho más organizada, estaríamos creando una función que nos permitiría inicializar el servidor, estaríamos definiendo de forma separada el *host* y el *puerto*, luego con *with* estaríamos realizando exactamente la misma definición de un socket y finalmente al socket del servidor lo vamos a referencias con *s*, esto es algo mucho mejor, ya que se asegurara de que se cierre correctamente, evitando que se quede abierto.

	Luego de esto inicializaríamos el server pasando la información por una tupla como lo hacíamos anteriormente, utilizando *bind()*, así como también definiríamos que aceptara en escucha de 1 a uno. Luego recibiremos el socket del cliente y su address:

	![[IMG_756.png]]

	Luego de esto también utilizaríamos *with* con el socket del cliente que es *conn*, para asegurar que se cierre correctamente una vez lo terminemos de utilizar.

	En este primeramente definiremos el poder recibir 1024 bytes con *recv()* y lo almacenaremos en *data* y lo que haremos en esta ocasión será enviarlo de vuelta al mismo cliente. Esto será gestionado dentro de un bucle infinito, por lo que en caso de que recibamos una entrada vacía del cliente, la conexión se cerrara automáticamente al salir del bucle infinito con *break*:

	![[IMG_757.png]]

	Finalmente, mandaríamos a llamar a la función *start_server()*, para iniciar el servidor al ejecutar el script:

	![[IMG_758.png]]

	Ahora, al ejecutar nuestro script, inicializaríamos nuestro servidor y nuestra conexión la veríamos así:

	![[IMG_759.png]]

	Y si enviáramos una cadena vacía o interrumpiéramos la conexión, también se cerraría todo correctamente del lado del servidor:

	![[IMG_760.png]]

	*Conexión del lado del cliente con esta estructura:*

	Para el cliente definiremos todo dentro de una función *start_client()* y en esta definiremos mismamente el host y el puerto para realizar la conexión, así como con *with* nuestro socket para una conexión con IPv4 mediante TCP al cual haremos referencia con *s* y aquí en lugar de jugar con *bind*, utilizaremos *connect()* debido a que del lado del cliente lo que se busca es conectarse al servidor.

	![[IMG_761.png]]

	Con este hecho, enviaremos un mensaje al servidor en formato bytes con *sendall()* y como el servidor nos responderá, este lo recibiremos en una variable *data*, gracias a *recv()*, indicándole que esperamos recibir como máximo 1024 bytes y al final mostrar ese mensaje aplicandole un *decode*.

	![[IMG_762.png]]

	Por último, ejecutaremos la funcion *start_client()*:

	![[IMG_763.png]]

	Ahora, antes de ejecutar el servidor, en el script del servidor agregaremos que nos muestre mensajes de en donde y en que puerto se pone en escucha y de las conexiones que se realicen (recordemos agregar la *f* para representar correctamente el F-string):

	![[IMG_764.png]]

	Finalmente, al ejecutar ambos script, primeramente abriendo el servidor y luego la conexión del cliente, tendríamos lo siguiente:

	![[IMG_765.png]]


[[#Índice]]


