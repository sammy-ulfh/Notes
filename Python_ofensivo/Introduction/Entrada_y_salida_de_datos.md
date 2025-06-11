
## **Índice**

- [[#Entrada por teclado y salida por pantalla]]
- [[#Lectura y escritura de archivos]]
- [[#Formateo de cadenas y manipulación de texto]]
- [[#Siguientes apuntes]]

## **Entrada por teclado y salida por pantalla**


1. **Introducción**

	La interacción del usuario a través de la consola es una habilidad esencial en Python, exploraremos las funciones que permiten la entrada y salida de datos. Utilizaremos *input()* para recoger la entrada del teclado y *print()* para mostrar mensajes en pantalla.

	En cuanto al formato de texto, veremos cómo manejar y representar la información de manera amigable. Esto incluye desde la manipulación básica de cadenas hasta técnicas más avanzadas de formateo de cadenas, que permiten la inserción de variables y la alineación del texto.

	La codificación de caracteres es un arpecto clave para garantizar que la entrada y salida manejen adecuadamente diferentes idiomas y conjuntos de caracteres, preservando la integridad de los datos y la claridad de la comunicación en la consola.

	Dominar estas funciones es crucial para crear programas que requieran interacción con el usuario, y te brindarán las herramientas necesarias para construir aplicaciones interactivas robustas y fáciles de usar.
	</br>
2. **Práctica**

	A la hora de crear programas o scripts, mediante Python podríamos solicitarle al usuario alguna entrada de datos con los cuales nuestro programa trabajara, por ejemplo si solicitamos la edad o nombre del usuario, lo recibiremos con un *input()* y podremos trabajar con ello en nuestro programa, ya sea mostrando información con ello o almacenándolo en una variable.

	Un ejemplo sencillo es que podríamos solicitar un nombre por pantalla y tendremos la posibilidad de, gracias a *input()*, colocar un mensaje que se mostrara al momento de solicitar que el usuario ingrese algo.

	![[IMG_507.png]]

	De esta manera, al momento que entra en el input se muestra el mensaje para solicitar el nombre y únicamente lo que el usuario escriba por teclado será almacenado en la variable *nombre*, al ingresar y presionar enter, después mostraremos lo almacenado en la variable con un mensaje y *print()* y veremos como es lo que ingresamos:

	![[IMG_508.png]]

	¿Qué pasa si intentamos hacer esto para solicitar la edad?

	En principio todo iría bien, pero habría un pequeño detalle y es que todo lo que sea introducido por pantalla, input lo almacenara en la variable como un tipo de dato *string* (cadena de texto), por lo que si se espera que se ingrese un número para realizar operaciones, se tendría que aplicar type casting para convertir este número a su tipo de dato *int*.

	Si solicitáramos la edad y luego en el input indicáramos la edad de esa persona el próximo año, al sumar un número a una cadena de texto nos daría error:

	![[IMG_509.png]]

	En cambio, al aplicar type casting y transformar el input al tipo de dato número, ahora sí que nos permitiría sumarle 1 a la edad para representar la del próximo año:

	![[IMG_510.png]]

	Ahora podríamos hacer un ejemplo más completo, en el cual efectuemos una excepción, ya que el usuario realmente podría ingresar texto y no números, y esto seguiría con el problema, ya que los caracteres no pueden ser convertidos a números.

	Para solucionar esto, la excepción que lanzaremos será de *ValueError*:

	![[IMG_511.png]]

	Esto está perfecto porque ya va bien sin lanzarnos un error, ahora lo único que nos faltaría sería colocar todo esto en un bucle infinito donde su condición siempre será *True* y en caso de que el usuario haya introducido bien el tipo de dato al momento de que termine de ejecutar todo sin problemas el bucle debería de terminar y lo haremos con un *break*, ya que todo ha salido bien, mientras que si todo sale mal se seguirá ejecutando hasta que el usuario ingrese bien los datos:

	![[IMG_512.png]]

	Ahora bien, no siempre le pediremos al usuario datos que quedamos mostrar sin problemas, supongamos que estamos solicitando la contraseña del usuario, pues en este caso realmente lo mejor sería que conforme vaya escribiendo el usuario no se vea lo que está escribiendo.

	Para ello vamos a utilizar *getpass*, lo cual es un módulo el cual depende de un script que está entre las rutas del PATH de Python, por lo que si deseamos incluso podremos ver su archivo:

	![[IMG_513.png]]

	Entonces ahora en nuestro archivo importaremos *getpass* desde el módulo *getpass* y similar a nuestro input utilizaremos *getpass()*.

	Funcionaria exactamente de la misma manera que un input, la diferencia sería que lo que vayamos a introducir no lo vamos a ver, a menos de que mostremos el contenido de la variable:

	![[IMG_514.png]]

	![[IMG_515.png]]

## **Lectura y escritura de archivos**

1. **Introducción**

	La lectura y escritura de archivos son operaciones fundamentales en la mayoría de los programas, y Python proporciona herramientas sencillas y poderosas para manejar archivos. Por lo que, aprenderemos cómo abrir, leer, escribir y cerrar archivos de manera eficiente y segura.

	*Manejo Básico de Archivos:*

	Se explicará cómo utilizar la función *open()*  para crear un objeto archivo y cómo los modos de apertura (*r* para lectura, *w* para escritura, *a* para añadir y *b* para modo binario) afectan la manera en que trabajamos con archivos.

	*Lectura de Archivos:*

	Detallaremos cómo leer contenido de un archivo en memoria, ya sea de una sola vez con el método *read()* o línea por línea con *readline()* o iterando sobre el objeto archivo.

	*Escritura en Archivos:*

	Examinaremos cómo escribir en un archivo usando métodos como *write()* o *writelines()*, y cómo estos métodos difieren en cuanto a su manejo de strings y secuencia de strings.

	*Manejadores de Contexto:*

	Uno de los aspectos más importantes en la lectura y escritura de archivos en Python es el uso de manejadores de contexto, proporcionados por la declaración *with*. Los manejadores de contexto garantizan que los recursos se manejen correctamente, abriendo el archivo y segurándose de que, sin importar cómo o dónde termine el bloque de código, el archivo siempre se cierre adecuadamente. Esto ayuda a prevenir errores comunes como fugas de recursos o archivos que no se cierran si ocurre una excepción.

	El uso de *with open()* no solo mejora la legibilidad del código, sino que también simplifica el manejo de excepciones al trabajar con archivos, haciendo el código más seguro y robusto.

	</br>
2. **Práctica**

	El manejo de archivos en Python nos permite trabajar con el contenido de archivos existentes o incluso crear nuevos archivos para introducir contenido en ellos, así como también es posible editar y agregar nuevas líneas en archivos ya existentes o que ya tengan contenido.

	Para un ejemplo inicial, buscaremos crear un archivo *example.txt* desde nuestro script de Python y a este a nivel de contenido esperaremos que tenga un "¡Hola mundo!".

	Existen diversas formas de hacerlo y algunas son más óptimas que otras, por lo que se explicaran las diferencias.

	Primeramente en nuestro archivo de Python, definiremos lo siguiente:

	![[IMG_516.png]]

	En este caso utilizamos el método especial *open()*, a este como primer argumento le indicamos el nombre del archivo y como segundo será la acción que realizaremos con este archivo, *w* representa que estaremos utilizando este archivo para introducir información en este.

	Para indicar que queremos abrir el documento para leerlo cambiaríamos la *w* por una *r* (read) y con ello ahora podríamos abrir un archivo para leerlo, aunque esto ya realmente daría por hecho que el archivo existe, por lo que para evitar errores es mejor aplicarlo cuando un archivo ya esté existente.

	Además, algo importante a mencionar es que cuando utilizamos *w*, esto lo que hace es borrarnos directamente todo el contenido que el archivo ya tenga y lo sobreescribe con lo que vayamos a querer escribir en él.

	En cambio, para escribir en un archivo sin afectar el contenido ya existente en él, tendríamos la *a* (append), que con esto incorporaríamos lo que queramos siempre al final del archivo.

	Entonces, ahora retomando lo de la imagen, al nosotros utilizar *open()* lo que pasa es que por detrás existe una clase *File* la cual estamos instanciando, por lo cual estaríamos asignándole a la variable *f* una instancia de la clase *File*, la cual tiene sus métodos.

	Entre ellos, esta *write()*, en el cual nosotros podríamos decirle que ahora que se ha abierto el archivo le vamos a meter "!.

	Esto funcionaria ya que con *w* (write), si el archivo no existe, este será creado:

	![[IMG_517.png]]

	Con esto estaríamos viendo como con *open()* estaríamos creando el archivo al no existir, así como abriéndolo con capacidad de escritura y con el método *write()* le asignamos como contenido un "¡Hola mundo!".

	Entonces ahora, si editamos el contenido que se le asigna al archivo y volvemos a ejecutar el código, veremos como lo que sucede es que el contenido que ya tenía el archivo desaparece, por lo que estaría siendo reescrito:

	![[IMG_518.png]]

	Entonces, para casos en los que no queramos borrar el contenido de este archivo tendremos *a* en lugar de *w*, que sería como indicarle que este archivo ya tiene contenido y que no queremos borrarlo.

	Por ende ahora el contenido que queramos agregar, nos lo agregara en la última línea del archivo que tiene contenido, como esto no efectúa directamente un salto de línea, lo veríamos en la misma línea del contenido que ya tenemos:

	![[IMG_519.png]]

	Si queramos que nuestro contenido realmente se efectúe en la línea siguiente porque nuestra última línea ya tiene contenido, bastaría con agregar el carácter especial de salto de línea al inicio de la cadena:

	![[IMG_520.png]]

	Realmente lo de que con *w* borre el contenido sucede al momento de que se abre el archivo, por lo que al cerrarse lo que si se almacena es todo lo que se le introdujo durante la ejecución del código, por lo que mientras nuestro código no se deje de ejecutar, podríamos escribir múltiple contenido en el archivo indicando *w*:

	![[IMG_521.png]]

	Ahora, al nosotros abrir un archivo, siempre una buena práctica será cerrarlo para evitar cualquier tipo de error, lo cual lo hacemos con el método *close()*.

	Esto nos cierra el archivo, por lo que automáticamente ya no hay forma de acceder a este, aunque luego tengamos otra línea que quiera escribir, como el siguiente ejemplo:

	![[IMG_522.png]]

	Como vemos esto nos cierra el archivo y ya no permite el acceso.

	Esto está bien, sin embargo, en scripts más robustos y complejos puede llegar a suceder que por cualquier motivo, ya sea que este se termine de ejecutar a medias o suceda cualquier cosa, el archivo podría quedar abierto y para evitar cualquier error o que un archivo se quede colgado abierto,  existe una manera más conveniente de hacerlo y esto es empleando *with*.

	Por lo que ahora con lo siguiente:

	![[IMG_523.png]]

	Esto realmente es algo muy similar a lo que hicimos anteriormente asignándole directamente la instancia a *f*, la diferencia es que de esta forma es más óptimo debido a que Python siempre se encargara de que el archivo se cierre, por lo que de cara a posibles errores en un programa, al aplicar esta forma más óptima nos despreocuparemos de posibles errores en cuanto al manejo de archivos.

	*Leer contenido de archivos:*

	Si quisiéramos leer el contenido de un archivo y poder tomar de una sola vez todo el contenido de este mismo, para ello tendríamos que cambiar la forma de abrir el archivo y en lugar de usar *w*, utilizaríamos *r* (read) y en cuanto al método el que nos permite recuperar todo el contenido de un archivo es *read()*, lo cual retornara el contenido del archivo y por ende tendremos que almacenarlo en una variable y luego podremos mostrarla.

	El archivo */etc/hosts* que estamos listando es un archivo existente en Linux, el cual tiene ya un contenido, que es el que estamos viendo:

	![[IMG_524.png]]

	El leer el contenido de un archivo también se puede hacer de distintas formas, en este caso extrajimos todo el contenido del archivo, pero también es posible leer un archivo línea a línea, esto es posible debido a que nuestro objeto *f*, que es como lo estamos referenciando, es iterable y el iterar sobre este con un bucle lo que nos permite es ir línea a línea y por ende podríamos mostrarlas y al final al terminar haber escrito por pantalla todas las líneas de esta, a diferencia de la otra forma, esta es iterando sobre el objeto de archivo y mostrar cada  línea del archivo:

	![[IMG_525.png]]

	Esto funciona correctamente, pero vemos cada línea muy separada debido a que por cada impresión de una línea que se realiza, al final de esta se agrega un salto de línea, si quisiéramos eliminarlo tendríamos que utilizar *strip()* y esto nos quitaría el salto de línea del final de cada línea que se imprima por pantalla:

	![[IMG_526.png]]

	Esta forma vendría siendo la más óptima de leer un archivo, ya que al leer un archivo línea a línea, lo que nos hace es que se carga menos cantidad de contenido del archivo en memoria a diferencia de cargar todo el contenido de un archivo directamente.

	El cargar todo el contenido ahora no afecta, pero en archivos demasiado grandes con mucho contenido puede ser un problema de cara a la memoria, por ende al leer línea a línea, no importará si el archivo es demasiado grande, ya que va leyendo línea a línea y no carga todo el contenido del archivo directamente en memoria, lo cual representa un mejor manejo de los recursos de memoria en un dispositivo.

	Por ende realmente esta sería la mejor forma de leer un archivo, ya que viene siendo la más óptima al empezar a leer directamente línea a línea sin cargar directamente el contenido en memoria.

	Existe otra forma de leer un archivo y es muy similar, pero la diferencia es que al objeto le agregaríamos el método *readlines()*, funcionaria prácticamente de la misma manera, pero antes de empezar a leer el archivo, carga todo su contenido en memoria y lo retorna línea a línea en una lista, por ende al iterar sobre la lista podremos leer línea a línea.

	![[IMG_527.png]]

	Con archivos cortos lo notaremos normal, pero la idea es que el código sea escalable y por ende con archivos muy grandes esto podría ser un proceso más lento, siendo más óptimo que empieza a leer directamente línea a línea sin antes cargarlo en memoria.

	En cuanto a ciberseguridad existe un archivo el cual es un diccionario que contiene muchas posibles contraseñas para realizar ataques de fuerza bruta, este es el diccionario *rockyou.txt*:

	![[IMG_528.png]]

	Es un archivito un tanto especial y podría llegar a sucedernos  que con el simple indicativo de lectura *r* nos daría error debido a que cuenta con ciertas líneas en formato *raw binary* y con esto hacemos referencia con *b*, lo cual nos permitiría poder realizar lectura sobre las líneas que estén en este formato.

	Al leerlas, algnunas serán líneas no legibles y tendran un formato peculiar (formato bytes):

	![[IMG_529.png]]

	![[IMG_530.png]]

	Para evitar esto bastaría con aplicar un *decode()* para que incluso aquellas líneas no legibles nos las muestre correctamente:

	![[IMG_531.png]]

	![[IMG_532.png]]

	Con *b* (raw binary), que son archivos binarios o archivos no legibles como imágenes, por ejemplo. Esto nos permite leer este tipo de contenido en archivos y el decode es para representarlos de forma legible.

	Aquí también podremos ver un ejemplo de una ventaja de que *readlines()* primero cargue el contenido del archivo a memoria y luego nos lo retorne en una lista para iterar en ella, ya que si solo tuviésemos el indicador *r*, de que vamos a leer el archivo e iteramos línea a línea, esto nos lanzaría el error hasta encontrarse con una línea que no puede representar a menos que se le indique que lea en *raw binary* con la letra *b*.

	![[IMG_533.png]]

	![[IMG_534.png]]

	A diferencia de *readlines()*, donde podríamos comprobar si podemos leer todo el archivo con solamente el indicador *r* sin problemas, antes de empezar a leerlo, lo cual podríamos ver como ventaja para no quedarnos a media lectura del archivo.

	*Escribir múltiples líneas en un archivo con el método writelines():*

	Este método lo podemos tener en cuenta para cuando vayamos a escribir en un archivo, si tenemos algún objeto iterable y el contenido de este queremos escribirlo en el archivo, un ejemplo sería tener una lista con distintas cadenas de caracteres y queremos escribirlas una a una en el archivo, pues esto podríamos hacerlo con *writelines()* pasándole como argumento la lista:

	![[IMG_535.png]]

	*Leer únicamente la primera línea de un archivo:*

	Una cosa es leer un archivo completo y utilizar el método *readlines()*, pero también podremos leer la primera línea de un archivo y para esto se utiliza *readline()* y para esto tomaremos de referencia el archivo que acabamos de crear y agregarle líneas:

	![[IMG_536.png]]

	*Almacenar contenido en un archivo con print:*

	El propio *print()*, como segundo argumento, le podremos pasar el objeto de archivo a *file*, asignándolo como si de una variable se tratase. Esto haría que el output de nuestro print, en lugar de mostrarlo en pantalla, lo mandaría hacia el archivo y lo escribiría en él.

	![[IMG_537.png]]

	*Trabajar con un archivo binario:*

	En un directorio específico yo tengo una imagen, la cual es el fondo de un entorno en Linux, si trato de ver el contenido de esta veremos como nos mostrara que es un archivo binario, esto se debe a que no es legible:

	![[IMG_538.png]]

	Ahora en nuestro archivo comenzaríamos abriendo esta imagen en modo de lectura, ya que buscaríamos leer el contenido de esta para crear una imagen en nuestro directorio actual:

	![[IMG_539.png]]

	De esta manera estamos indicando que abriremos un archivo para lectura y con la *b* que es un binario, lo utilizaremos como *f_in*, ya que será nuestro archivo input y en esta misma línea definiremos nuestro archivo output, el cual se abrirá como escritura y también será binario:

	![[IMG_540.png]]

	Finalmente, leeríamos todo el contenido de la imagen input y almacenaríamos todo el contenido del binario en nuestro nuevo archivo de imagen:

	![[IMG_541.png]]

	Con esto listo, ahora ejecutaríamos nuestro programa y veríamos como se genera la imagen en el directorio actual:

	![[IMG_542.png]]

	Por lo que podremos verificar que efectivamente si nos reconozca el archivo como una imagen e incluso mostrarla:

	![[IMG_543.png]]

	Entonces, si en algún punto estamos tratando con archivos que tengan caracteres especiales y no se puedan leer de forma normal, debemos tener en cuenta que deberemos indicar que estamos trabajando con un archivo binario.

	A la hora de abrir un archivo que no existe en modo escritura, este es creado, pero al hacerlo en modo escritura esto nos podrá dar un error, por ende podríamos lanzar una excepción para ello:

	![[IMG_544.png]]

	El programa nos lanza este error, el cual contiene la excepción "FileNotFoundError". Anteriormente, cuando referenciábamos a un archivo y se daba algún error al momento de abrirlo, la excepción que lanzábamos con *try* es "IOError" y funcionaria bien:

	![[IMG_545.png]]

	Funciona correctamente, pero realmente lo más óptimo es aplicar la propia excepción que nos da el mismo error por consola, el cual es "FileNotFoundError":

	![[IMG_546.png]]


## **Formateo de cadenas y manipulación de texto**

1. **Introducción**

	El formateo de cadenas y la manipulación de texto son habilidades esenciales en Python, especialmente en aplicaciones que involucran la presentación de datos al usuario o procesamiento de información textual. Nos centraremos en las técnicas y herramientas que Python ofrece para trabajar con cadenas de texto.

	*Formateo de Cadenas:*

	Aprenderemos los distintos métodos de formateo de cadenas que Python proporciona, incluyendo:

	- *Formateo Clásico:* A través del operador *%*, similar al *print* en C.
	- *Método format():* Un enfoque versátil que ofrece numerosas posibilidades para formatear y alinear texto, rellenar caracteres, trabajar con números y más.
	- *F-strings (Literal String Interpolation):* Incluido en Python 3.6, este método permite incrustar expresiones dentro de cadenas de texto de una manera concisa y legible.

	*Manipulación de Texto:*

	Exploraremos las funciones y métodos incorporados para la manipulación de cadenas, que incluyen:

	- *Métodos de Búsqueda y Reemplazo:* Como *find(), *index()*, *replace()* y métodos de expresiones regulares.
	- *Métodos de Prueba:* Para verificar el contenido de la cadena, como *isdigit(), *isalpha()*, *startswith()* y *enswith()*.
	- *Métodos de Transformación:* Que permiten cambiar el caso de una cadena, dividirla en una lista de subcadenas o unirlar, como *upper()*, *lower()*, *split()* y *join()*.

	También veremos cómo trabajar con cadenas Unicode en Python, lo que es esencial para aplicaciones modernas que necesitan soportar múltiples idiomas o caracteres especiales.

	Con esto tendrás una comprensión completa de cómo dar formato a las cadenas para la salida de datos y cómo realizar operaciones comunes de manipulación de texto. Estas habilidades son fundamentales para la creación de aplicaciones que necesitan una interfaz de usuario sofisticada y para el procesamiento de datos en aplicaciones de backend.
	<br/>
2. **Práctica**

	*Formateo de cadenas:*

	El formateo de cadenas lo hemos visto como la forma de manipular el texto que mostramos con la capacidad de implementar el uso de contenido no estático, como las variables.

	El método *format* es uno de ellos, el cual nos permite colocar las llaves y variables de forma posicional:

	![[IMG_547.png]]

	De esta manera vemos cómo, de acuerdo con cómo se colocaron las llaves y los variables como argumentos en format, serán mostradas.

	O de otra forma, en caso de no poder colocarlos en orden, colocar el índice correspondiente de la variable, teniendo en cuenta que en Python se comienza a contar desde el 0:

	![[IMG_548.png]]

	*F-strings:*

	Este método es más cómodo, al estar más completo y más sencillo de implementar, ya que con colocar la variable o función dentro de los corchetes bastaría. 

	![[IMG_549.png]]

	Además de que nos permite incluso realizar operaciones:

	![[IMG_550.png]]

	*Manipulación de cadenas de texto:*

	Para la manipulación de cadenas hemos visto hasta ahora *strip()*, este realmente lo que hace es eliminar cualquier espacio o carácter especial como saltos de línea, tabulaciones, entre otros, que se encuentren al inicio o al final del texto.

	Por ejemplo, si creáramos una cadena que al inicio tenga espacios y al final  también, al utilizar *strip()* e imprimirlo, no veríamos esto:

	![[IMG_551.png]]

	Si agregáramos caracteres especiales como tabulaciones o saltos de línea, el resultado sería el mismo al aplicar *strip()*:

	![[IMG_552.png]]

	*Colocar todo en minúsculas:*

	Si tenemos una cadena de texto y esta si o si queremos mostrarla en minúsculas, para ello tendríamos *lower()*:

	![[IMG_553.png]]

	Lo mismo sucede para convertirlo todo a mayúsculas, con *upper()*:

	![[IMG_554.png]]

	*Reemplazar caracteres:*

	Podríamos reemplazar caracteres de una cadena utilizando *replace()*, colocando como primer argumento el carácter de nuestro texto que deseamos cambiar y como segundo argumento el carácter por el que deseamos cambiarlo:

	![[IMG_555.png]]

	O incluso aplicarlo en palabras:

	![[IMG_556.png]]

	*Método split():*

	Este es un método interesante, ya que si lo utilizamos sin argumentos, esto lo que hará es que de toda la cadena nos tomará como delimitador los espacios y cada cosa que esté entre los espacios lo almacenará en una lista:

	![[IMG_557.png]]

	Si quisiéramos, podríamos cambiar el delimitador, ya que por defecto serán los espacios, pero podríamos colocar algún carácter en específico, como las comas *,*:

	![[IMG_558.png]]

	Como todo se almacena en una lista, podríamos iterar en ella, acceder a los datos con los índices y trabajar de la mejor manera que consideremos con estos datos.

	*Comprobar el inicio de una cadena:*

	Con el método *startswith()*, podríamos pasar como argumento algún carácter o palabra y verificar si una cadena inicia por esto, esto retornará un valor booleano donde si inicie la cadena de texto con esto nos retornara *True* y de no ser así retornara *False* y sabemos que a nivel de comprobaciones podremos utilizar estos valores en condicionales, ya que en estos siempre se trabaja con *True* o *False*.

	![[IMG_559.png]]

	*Verificar el final de cadenas de texto:*

	O lo anterior de la misma manera, pero aplicado para verificar el final de una cadena con el método *endswith()*:

	![[IMG_560.png]]

	El error mostrado es de un propio comando de bash, no tiene nada que ver con Python.

	*find() e index():*

	Ambas sirven exactamente para lo mismo, es importante saber que una cadena de texto podríamos tratarla accediendo a índices, donde cada uno de estos representaran un carácter de la cadena, incluyendo espacios y símbolos especiales, por lo que si tenemos la cadena "Hola", realmente podríamos acceder a cada letra de forma individual colocando sus 4 índices, del 0 al 3.

	Con esto en mente, al utilizar *find()* y buscar en la cadena "Hola Mundo" la palabra "Hola", si esta se encuentra en la cadena, lo que nos regresará será el índice donde comienza la palabra. En este caso comienza en el índice [0], ya que con eso comienza la cadena de texto. En caso de no existir una palabra que busquemos, lo que *find()* nos retornara será un valor -1.

	![[IMG_561.png]]

	En el caso del *index()*, funcionaría exactamente de la misma manera, la diferencia aquí es que cuando un valor no exista en la lista, esto nos retornará una excepción:

	![[IMG_562.png]]

	*Método count():*

	El método *count()* nos sirve perfectamente para contar el número de veces que aparece un carácter en una cadena, como el siguiente ejemplo:

	![[IMG_563.png]]

	La mayúscula no la consideraría, ya que Python es sensible a mayúsculas y minúsculas.

	*Método .join():*
	Este método podría ser de mucha ayuda cuando queramos representar todos los elementos contenidos en algún tipo de dato como diccionarios, listas, conjuntos, entre otros. Lo cual nos puede servir para, por ejemplo, de elementos que tengamos en una lista, representarlos todos separados por espacios:

	![[IMG_564.png]]

	Como vemos, las comillas antes del join indican lo que será el separador para cada elemento, en este caso un espacio.

	Por lo cual podríamos hacer un ejemplo donde separemos nombres por un espacio y coma:

	![[IMG_565.png]]

	*Método capitalize():*

	Nosotros podríamos tener una cadena de texto y si queremos asegurar que el primer carácter de esta sea representado en mayúscula, pues podremos usar *capitalize()*:

	![[IMG_566.png]]

	*Método title():*

	Si quisiéramos representar cada palabra de una cadena de caracteres que empiece con mayúscula la primera letra, entonces utilizaríamos el método *title()*:

	![[IMG_567.png]]

	*Método swapcase():*

	Podríamos utilizar el método *swapcase()*, para nosotros realizar un cambio en una cadena, donde los caracteres en mayúsculas los transformaría en minúsculas y las minúsculas en mayúsculas:

	![[IMG_568.png]]

	*Método isalpha():*

	Este método lo podremos utilizar para verificar si en una cadena de texto todo su contenido corresponde a letras del alfabeto, retornará un valor booleano donde, de ser así, será *True*, de lo contrario *False*:

	![[IMG_569.png]]

	En este caso da *False* en un inicio, porque incluso detecta el espacio y no está dentro del abecedario.

	*Método isdigit():*

	Funciona de la misma manera que el método anterior, pero en este caso es para verificar que nuestra cadena contenga solamente números:

	![[IMG_570.png]]

	*Método isspace():*

	Incluso con el método *isspace()*, podríamos verificar si nuestra cadena contiene solamente espacios:

	![[IMG_571.png]]

	*Métodos islower() y isupper():*

	Con estos dos podríamos verificar si toda una cadena está en mayúsculas o minúsculas:

	![[IMG_572.png]]

	*Método istitle():*

	Incluso podremos verificar si tenemos una cadena con cada palabra, que su inicial sea mayúscula:

	![[IMG_573.png]]

	*Eliminar caracteres con el método replace():*

	La forma en que podríamos hacer esto, es que con esto podremos reemplazar caracteres. Por ello podríamos reemplazar un carácter 'x' a nada '', lo cual veríamos cómo eliminarlo:

	![[IMG_574.png]]

	*Aplicar reemplazos de una forma más compleja con maketrans y translate():*

	Con maketrans primeramente tendríamos que definir una tabla, la cual sería como la que registraría los cambios que se van a aplicar, donde aquí, si colocamos varios caracteres, aplicará el cambio correspondiente al carácter en la posición correspondiente.

	Por ejemplo, si en la definición de la tabla coloco 'abc', y a lo que se va a cambiar coloco 'dfg', lo que haría sería cambiarme todas las letras 'a' por 'd', todas las 'b' por 'f', y así sucesivamente.

	La definición de nuestra tabla la hacemos de la siguiente manera con maketrans:

	![[IMG_575.png]]

	Y finalmente, aplicándole el método *translate()* a nuestra cadena y pasándole como argumento, la tabla, nos haría el reemplazo correspondiente:

	![[IMG_576.png]]

[[#Índice]]

## **Siguientes apuntes**

[[Proyectos_de_POO]]