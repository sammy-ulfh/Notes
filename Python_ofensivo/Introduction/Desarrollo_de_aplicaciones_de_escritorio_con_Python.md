## **Índice**

- [[#Introducción a las interfaces gráficas de usuario (GUI)]]
- [[#Desarrollo de aplicaciones GUI con Tkinter (1/8)]]
- [[#Desarrollo de aplicaciones GUI con Tkinter (2/8)]]
- [[#Desarrollo de aplicaciones GUI con Tkinter (3/8)]]
- [[#Desarrollo de aplicaciones GUI con Tkinter (4/8)]]
- [[#Desarrollo de aplicaciones GUI con Tkinter (5/8)]]
- [[#Desarrollo de aplicaciones GUI con Tkinter (6/8)]]
- [[#Desarrollo de aplicaciones GUI con Tkinter (7/8)]]
- [[#Desarrollo de aplicaciones GUI con Tkinter (8/8)]]
- [[#Desarrollo de aplicaciones GUI avanzado con CustomTkinter]]
- [[#Chat Multiusuario con GUI y Cifrado E2E (1/5)]]
- [[#Chat Multiusuario con GUI y Cifrado E2E (2/5)]]
- [[#Chat Multiusuario con GUI y Cifrado E2E (3/5)]]
- [[#Chat Multiusuario con GUI y Cifrado E2E (4/5)]]
- [[#Chat Multiusuario con GUI y Cifrado E2E (5/5)]]
- [[#Siguientes apuntes]]

## **Introducción a las interfaces gráficas de usuario (GUI)**

*Tkinter* es una biblioteca estándar en Python para la creación de interfaces gráficas de usuario (GUI). Es una interfaz de programación para *Tk*, un toolkit de GUI que es parte de Tcl/Tk. Tkinter es notable por su simplicidad y eficiencia, siendo ampliamente utilizado en aplicaciones de escritorio y herramientas educativas.

*¿Por qué Tkinter?*

- *Facilidad de Uso:* Tkinter es amigable para principiantes. Su estructura sencilla y clara lo hace ideal para aprender los conceptos básicos de la programación de GUI.
  </br>
- *Portabilidad:* Las aplicaciones creadas con Tkinter pueden ejecutarse en diversos sistemas operativos sin necesidad de modificar el código.
  </br>
- *Amplia Disponibilidad:* Al ser partes de la biblioteca estándar de Python, Tkinter está disponible por defecto en la mayoría de las instalaciones de Python, lo que elimina la necesidad de instalaciones adicionales.

En esta sección nos sumergiremos con Tkinter, empezando por una introducción detallada que nos permitirá entender y utilizar múltiples funcionalidades. A través de proyectos prácticos, aplicaremos estos conocimientos para construir desde aplicaciones simples hasta interfaces más complejas, proporcionando una base sólida para cualquiera interesado en el desarrollo de GUI con Python.

## **Desarrollo de aplicaciones GUI con Tkinter (1/8)**

1. **Introducción**

	**Tkinter: Explorando Componentes Clave**

	1. *tk.label*

		- *Descripción:* *tk.Label* es un widget en Tkinter utilizado para mostrar texto o imágenes. El texto puede ser estático o actualizarse dinámicamente.
		 </br>
		- *Uso Común:* Se usa para añadir etiquetas en una GUI, como títulos, instrucciones o información de estado.
		 </br>
		- *Características Clave:*

			- *text:* Para establecer el texto que se mostrará.
			- *font:* Para personalizar la tipografía.
			- *bg y fg:* Para establecer el color de fondo (*bg*) y de texto (*fg*).
			- *image:* Para mostrar una imagen.
			- *wraplength:* Para especificar a qué ancho el texto debería envolverse.

	2. *mainloop()*

		- *Descripción:* *mainloop()* es una función especial en Tkinter que ejecuta el bucle de eventos de la aplicación. Este bucle espera eventos, como pulsaciones de teclas o clics del mouse, y los procesa.
		 </br>
		- *Importancia:* Sin *mainloop()*, aplicación GUI no responderá a eventos y parecerá congelada. Es lo que mantiene viva la aplicación.

	3. *pack()*

		- *Descripción:* *pack()* es un método de geometría para colocar widgets en una ventana.
		 </br>
		- *Funcionalidad:* Organiza los widgets en bloques antes de colocarlos en la ventana. Los widgets se "empaquetan" en el orden en que se llama a *pack()*.
		 </br>
		- *Características Clave:*

			- *side:* Para especificar el lado de la ventana donde se ubicará el widget (por ejemplo, top, bottom, left, right).
			 </br>
			- *fill:* Para determinar si el widget se expande para llenar el espacio disponible.
			 </br>
			- *expand:* Para permitir que el widget se expanda para ocupar cualquier espacio adicional en ventas.

	4. *grid()*

		- *Descripción:* *grid()* es otro método de geometría utilizado en Tkinter para colocar widgets.
		- dw
		- *Funcionalidad:* Organiza los widgets en una cuadrícula. Se especifica la fila y la columna donde debe ir cada widget.
		- ds
		- *Características Clave:* 

			- *row y column:* Para especificar la posición del widget en la cuadrícula.
			- *rowspan y columnspan:* Para permitir que un widget ocupe múltiples filas y columnas.
			- *sticky:* Para determinar cómo se alinea el widget dentro de su celda (Por ejemplo, N, S, E, W)

	*Conclusión:*

	Estos componentes de Tkinter (tk.Label, mainloop(), pack(), grid()) son fundamentales para la creación de aplicaciones GUI eficientes y atractivas. Comprender su funcionamiento y saber cómo implementarlos adecuadamente es crucial para cualquier desarrollador que busque crear insterfaces de usuario interactrivas y funcionales con Pytho y Tkinter.

2. **Práctica**

	*Instalación*

	Usualmente, *tkinter* ya viene instalado con Python, en caso de no ser así, lo podremos instalar utilizando pip:

	```python3
	pip3 install tk  
	```

	Primeramente, importaremos la librería *tkinter*, para referenciarlo de una forma más corta lo haremos como *tk*:

	![[IMG_930.png]]

	Podremos generar una ventana principal con tkinter, para ello se utiliza la clase *Tk* de la propia librería, ya en esta nosotros iremos acomodando y organizando los widgets que queramos agregar y utilizar.

	Al generar una ventana con Tkinter, usualmente en la parte superior nos saldrá el nombre de la aplicación, por ello tendríamos que utilizar sobre nuestra instancia el método *title()* y como argumento asignarle un nombre

	Finalmente, para poder lanzar nuestra aplicación, tendremos que utilizar el método *mainloop()*, lo cual sería como el bucle principal de nuestra aplicación, lo que nos permite estar capturando entradas de teclado, interacción con botones, entre otras cosas:

	![[IMG_931.png]]

	De esta manera, ahora al ejecutarlo se nos abriría una ventana, lo cual sería la ventana principal de nuestra aplicación, donde iremos acomodando y definiendo sus funcionalidades y widgets.

	![[IMG_932.png]]

	En este caso no se ve el nombre de la aplicación, debido a que se está empleando un entorno personalizado en Linux.

	*Mostrar contenido en nuestra ventana*

	Para lograrlo tendríamos que utilizar *labels*, que son widgets que nos permiten mostrar cierta información por la aplicación, de forma que podremos mostrar un texto o imagen.

	Un widget tendremos que verlo como un elemento dentro de nuestra aplicación, a través del cual un usuario podrá interactuar con nuestra aplicación o visualizar cierto contenido.

	Para nosotros mostrar un contenido, tendríamos que crear un label, lo cual almacenaríamos en una variable. Por así decirlo, lo haríamos con el método *Label()*, donde como argumentos tendremos que pasarle nuestra ventana y como segundo argumento lo que mostraremos, en este caso un texto:

	![[IMG_933.png]]

	De esta manera aún no tendremos nada dentro de nuestra ventana si la ejecutamos. Para poder representar/mostrar el contenido que deseemos en nuestro label, a nivel de posicionamiento, podremos utilizar distintas utilizades, como *pack()*, *grid()* o *place()*.

	En este caso aplicaremos *pack()* directamente en nuestro label y veremos cómo ahora sí se mostrará y estará todo el tiempo centrado en la parte superior:

	![[IMG_934.png]]

	![[IMG_935.png]]

	*Agregar un botón para definir una acción*

	Podremos definir un botón con el propio método *Button* de la librería tkinter, le pasaremos tres argumentos, el primero será la propia ventana en la que se va a colocar, el segundo será un contenido que tendrá nuestro botón asignándolo a la propiedad *text* y finalmente a la propiedad *command* tendremos que asignarle la funcionalidad que vamos a realizar, en este caso será la función *accion_de_boton()* que definiremos posteriormente, además de finalmente utilizar *pack()* para que se muestre en nuestra ventana:

	![[IMG_936.png]]

	Finalmente, definiremos nuestra función para que muestre algo en pantalla, mediante la terminal:

	![[IMG_937.png]]

	De esta manera, al ejecutarlo, tendríamos nuestra venta con nuestro botón y, si lo presionamos, veríamos lo siguiente en nuestra terminal:

	![[IMG_938.png]]

	*Fondo en un label*

	Para colocar un fondo en un label tendremos que agregarle un argumento extra, el cual será indicar un color mediante un string a la propiedad *bg*:

	![[IMG_939.png]]

	![[IMG_940.png]]

	Ahora agregaríamos más labels y los mostraríamos en nuestra ventana con *pack()*:

	![[IMG_941.png]]

	![[IMG_942.png]]

	*Posicionar un label*

	Estos label son acomodados automáticamente de la forma anterior, pero nosotros podremos cambiar su posición y colocarlo como mejor se vaya a acomodar para nuestra aplicación.

	Para este caso pensaremos en que los primeros label queden en la parte superior, enfocando su posición en el eje X, mientras que el último lo acomodaremos sobre el eje Y, en la parte izquierda de nuestra ventana (eje X).

	Para esto utilizaríamos la propiedad *fill* para como argumento indicarle algún eje para que se adapte al resize de nuestra aplicación. Para esto, en los primeros dos vamos a colocarlos para el eje X, que lo que hará será posicionarlo para que su eje horizontal se acomode al resize:

	![[IMG_943.png]]

	De esta manera, al nosotros estar cambiando el tamaño de nuestra ventana, el label siempre estará adaptándose:

	![[IMG_944.png]]

	Para el tercer label haremos lo mismo, pero lo acomodaremos para el eje Y, para poder acomodarlo del lado izquierdo, agregaremos la propiedad *side* como argumento en *pack()*, donde le asignaremos *tk.LEFT*, para que se acomode a la izquierda:

	![[IMG_945.png]]

	![[IMG_946.png]]

	Así como lo hemos colocado a la izquierda, también podremos colocarlo a la derecha con *RIGHT*:

	![[IMG_947.png]]

	![[IMG_948.png]]

	O si deseamos colocarlo en la parte superior\/inferior, tendriamos que utilizar *TOP*\/*BOTTOM*:

	
	![[IMG_949.png]]

	![[IMG_950.png]]

	Con *TOP*:

	![[IMG_951.png]]

	Y en caso de no indicar nada, pues veremos que se queda en el centro, en la parte superior.

	Esta sería la forma de acomodar el contenido de nuestra aplicación con *pack()*, pero ahora veremos cómo se hace con *grid()*.

	**Método grid()**

	El método grid sería como generar una tabla imaginaria dentro de nuestra aplicación y cada una de sus celdas podría contener uno o varios widgets.

	Sería como utilizar el método pack, la diferencia es que con *grid()* tendremos que indicar la fila y columna a nivel posicional.

	Como base, nos quedaría así:

	![[IMG_952.png]]

	Es lo mismo, pero solo cambiaríamos la forma en la que indicamos que se muestren nuestros label.

	Al no colocar ninguna posición, se representarían en la misma columna:

	![[IMG_953.png]]

	*Indicar posicionamiento:*

	Para indicar el posicionamiento, le tendremos que indicar la columna y fila correspondientes, donde queremos que se muestre.

	Para ello utilizaremos las propiedades *row* y *column* para, a nivel posicional (numérico), indicar en qué posición se muestre:

	![[IMG_954.png]]

	En este caso, con la almohadilla *#* se han comentado los label 2 y 3, de esta manera no se mostrarán. Con el label 1, estamos indicando con *row* que se coloque en la fila 0 y con column en la columna 0, por lo que estará exactamente en la parte superior izquierda del todo:

	![[IMG_955.png]]

	Teniendo esto en mente, ahora para colocar el segundo label, podríamos jugar moviéndolo cerca.

	A un lado del primer label:

	![[IMG_956.png]]

	Si quisiéramos colocarlo debajo, tendría que ser en la primera fila, manteniéndose en la columna 0:

	![[IMG_957.png]]

	O incluso colocarlo debajo del primero, en la celda de la derecha (1,1):

	![[IMG_958.png]]

	De esta manera vemos cómo podremos colocar en distintas posiciones los elementos dentro de nuestra aplicación.

	Ahora podríamos tener dos label en la parte superior y uno en la parte inferior, de la siguiente manera:

	![[IMG_959.png]]

	*Asignarle más celdas a un label:*

	Al momento de crear nuestros label y mostrarlos, como en el ejemplo anterior, podremos desear que nuestro label azul ocupe ambos espacios, quedando de alguna manera en conjunto con los dos de la parte superior, algo como lo siguiente:

	![[IMG_960.png]]

	Para esto utilizaríamos la propiedad *columnspan* a la cual le asignaremos a nivel de representación, cuántas celdas queremos que nos tome a nivel de columnas:

	![[IMG_961.png]]

	De esta manera estaría ocupando los dos espacios en cuanto a columnas respecta (horizontalmente). El tamaño del fondo no es ocupado totalmente debido a que se adapta al texto o contenido.

	Por lo que realmente nuestro label está ocupando las dos celdas, pero el contenido se centra automáticamente y el fondo que agregamos se adapta a este, por lo que si agregáramos más texto, veremos cómo el fondo se adapta al tamaño del contenido y se mantiene centrado.

	Si excediéramos el contenido en la parte inferior, lo que sucedería es que ahora la celda inferior se haría más grande, adaptando a las de arriba, por lo que ahora el contenido de los dos label superiores se vería más pequeño, pero realmente las celdas se han agrandado, mientras que el contenido se centra y mantiene su tamaño:

	![[IMG_962.png]]

## **Desarrollo de aplicaciones GUI con Tkinter (2/8)**

1. **Introducción**

	**Tkinter: Profundizando en Componentes y Gestión de Layout**

	1. **place()**

	- *Descripción*: *place()* es un método de gestión de geometría en Tkinter que permite posicionar widgets en ubicaciones específicas mediante coordenadas x-y.
	- *Características clave:*

		- *x* y *y*: Especifican la posición del widget en términos de coordenadas.
		- *width* y *height*: Definen el tamaño del widget.
		- *anchor*: Determina desde qué punto del widget se aplican las coordenadas (por ejemplo, *nw* para esquina superior izquierda).
		- *Posiciones Relativas:* Se pueden utilizar valores relativos (por ejemplo *relx*, *rely*) para posicionar widgets en relación con el tamaño de la ventana, lo que hace que la interfaz sea más adaptable al cambiar el tamaño de la ventana.
		</br>
	2. **tkinter.Entry()**

	- *Descripción:* *tkinter.Entry()* es un widget en Tkinter que permite a los usuarios introducir una línea de texto.
	- *Uso común:* Ideal para campos de entrada de texto como nombres de usuario, contraseñas, etc.
	- *Funcionalidades Clave:*

		- *get():* Para obtener el texto del campo de entrada.
		- *delete():* Para borrar el texto del campo de entrada.
		- *insert():* Para insertar texto en una posición específica.
	  </br>
	3. **tkinter.Button()**

	- *Descripción:* *tkinter.Button()* es un widget que los usuariospueden presionar para realizar una acción.
	- *Uso común:* Ejecutar una función o comando cuando se hace clic en él.
	- *Características clave:*

		- *text:* Define el texto que aparece en el botón.
		- *command:* Establece la función que se llamará cuando se haga clic en el botón.
	  </br>
	4. **geometry()**

	- *Descripción:* *geometry()* es una función que define las dimensiones y la posición inicial de la ventana principal.
	- *Funcionalidad:* Permite especificar el tamaño y la ubicación de la ventana en el formato *ancho x alto + X + Y*.
	- *Importancia:* Es fundamental para establecer el tamaño inicial de la ventana y su posición en la pantalla.
	  </br>
	5. **tk.Text()**

	- *Descripción:* *tkinter.Text()* es un widget que permite la entrada y visualización de múltiples líneas de texto.
	- *Uso Común:* Ideal para campos de texto más extensos, como áreas de comentarios, editores de texto, etc.
	- *Funcionalidades Clave:*

		- Similar a *tkinter.Entry()*, pero diseñado para manejar texto de varias líneas.
		- Permiten funciones como copiar, pegar, seleccionar texto.

	**Conclusión**

	Estos componentes y funciones (*place()*, *tkinter.Entry()*, *tkinter.Button()*, *geometry()*, *tkinter.Text()*) son esenciales en la construcción de interfaces de usuario ricas y funcionales con Tkinter. Proporcinan la flexibilidad necesaria para crear aplicaciones GUI interactivas y atractivas, adaptándose a una amplia gama de necesidades de diseño de interfaz.
	</br>
2. **Práctica**

	**Método place()**

	Place nos puede ser de ayuda para posicionar nuestros label a nivel de píxeles, podríamos posicionar un label de forma absoluta indicándole con *x* y *y* una posición a nivel de píxeles en los que esta quedara representado.

	De esta manera con *x\=20* le indicamos que quede posicionado 20 píxeles a la derecha de forma absoluta, mientras con *y\=20* indicamos que quede 20 píxeles hacia abajo. De esta manera veremos como queda posicionado y será de forma absoluta, lo que quiere decir que no habrá cambios al momento de manipular el tamaño de nuestra ventana:

	![[IMG_963.png]]

	![[IMG_964.png]]

	*Asignar una posición de forma relativa*

	Posicionar un label de forma relativa, querrá decir que este va a respetar la posición en relación con el tamaño total de la ventana. Tomaremos como total de *x* \= 1, así como el total de *y* \= 0.

	Lo que quiere decir que todo el eje X de nuestra ventana tendrá un valor total de 1, así como el eje Y. Al manipular el tamaño de nuestra ventana, el espacio de nuestros ejes asignados, siempre será el mismo.

	Si en *X* asignamos 0.8, siempre será 0.8 la distancia entre nuestro tope izquierdo y nuestro label.  

	Para asignar una posición relativa, utilizaremos *relx* y *rely*:

	![[IMG_965.png]]

	![[IMG_966.png]]

	De esta manera, considerando que el valor total de nuestra ventana en *X* y *Y* es de *1*, sin importar el tamaño que tenga la ventana *X* siempre será *0.5* e *Y* siempre será *0.2*, ya que estos fueron los asignados.

	La forma en la que podremos entender el cómo se posiciona es con los bordes izquierdo y superior, ya que el borde izquierdo siempre quedará en la posición que asignemos en el eje X, así como el borde superior siempre quedara posicionado en la posición que asignemos para el eje Y.

	Esto lo podremos visualizar mejor si colocamos ambas posiciones del segundo label exactamente a la mitad:

	![[IMG_967.png]]

	*Centrar un label*

	Al momento de posicionar un label, como vimos anteriormente, lo que queda como tal posicionado son los bordes, pero sí queremos centrar el label en esa posición exactamente, pues lo que tendremos que hacer es utilizar la propiedad *anchor* y asignarle *CENTER* de la propia librería.

	Podremos verlo de forma más clara al ponerlo exactamente al centro:

	![[IMG_968.png]]

	De esta manera ahora lo que es tomado como punto de referencia para asignar el posicionamiento es el centro de nuestro label, por ello se ve centrado.
	
	Si le quitáramos la propiedad anchor, solo se posicionaría considerando lo explicado anteriormente, los bordes izquierdo y superior:

	![[IMG_969.png]]

	*Asignar un tamaño a nuestra ventana*

	Al momento de utilizar posicionamiento relativo, cuando ejecutamos nuestro código nos puede pasar que la ventana de primeras sea pequeña y por ende no nos permita visualizar totalmente el contenido.

	Como este ejemplo:

	![[IMG_970.png]]

	*Método geometry()*

	En este caso tendríamos que asignarle un mayor tamaño para que podamos visualizarlo correctamente sin ningún problema.

	Para ello utilizaremos el método *geometry()* al cual le pasaremos como argumento en formato de texto la proporción que tendrá nuestra ventana y se aplicará directamente en la ventana, la cual estamos manejando como *root*:

	![[IMG_971.png]]

	![[IMG_972.png]]

	Ya con esta base, nosotros podremos ir asignando una proporción la cual se adapte de mejor forma a lo que estemos construyendo.

	*Widget Entry()*

	Este widget nos sirve para poder manejar la entrada de datos del usuario, por lo que al colocarlo se nos agregara a nuestra ventana un recuadro el cual nos permitirá escribir en el:

	![[IMG_973.png]]

	Para generarlo se hace de la misma forma que con un label, ya que podremos solo indicarle la ventana en la que queremos colocarlo.

	Para mostrarlo, en este caso  utilizamos pack(), por ende aquí para indicar una distancia de padding o separación en cuanto al eje *X* y *Y* se utiliza *pad* y se le agrega *x* o *y*, dependiendo de cuál nos interese modificar.

	En este caso vamos a poner que quede 5 píxeles separados del borde superior:

	![[IMG_974.png]]

	También colocaremos un padding a los lados, para que quede bien también haremos que nuestro *Entry()* se acople al resize de la ventana, que es cuando manipulamos el tamaño:

	![[IMG_975.png]]

	Con esto, ahora nosotros podríamos escribir contenido, pero para poder nosotros almacenarlo en una variable y realizar cosas con ello, lo que haremos será agregar un botón que nos permita indicar que se realice esta acción y dentro de nuestra acción, finalmente nos mostrará por terminal el contenido de la variable.

	*Recoger los datos de entrada*

	Para esto tendríamos que crear un botón debajo, al cual le agregaremos como *command* una función que definiremos, la cual nos permitirá aprovechar el widget creado con el método *get()* para recibir los datos y en este caso mostrarlos en la terminal:

	![[IMG_976.png]]

	Lo cual nos daría la siguiente funcionalidad cada que presionemos el botón:

	![[IMG_977.png]]

	El widget *Entry()* está bien, pero en cuanto a limitaciones solo nos permite introducir una línea de texto, si nosotros quisiéramos realizar cosas como saltos de línea al presionar enter, para ello tendremos que utilizar un widget distinto.

	*Widget Text()*

	En cuanto a representación visual en nuestra ventana será prácticamente lo mismo que utilizar *Entry()*, la diferencia aquí es que *Text()* por defecto tiene una mayor dimensión, por lo que tendremos que agrandar nuestra ventana con *geometry()* dándole por lo menos una resolución de *600x550*.

	Por lo que con solo realizar los cambios de *Entry()* a *Text()*, así como de la variable del widget y las dimensiones, lo tendríamos de la siguiente manera:

	![[IMG_978.png]]

	![[IMG_979.png]]

	![[IMG_980.png]]

	Al escribir y darla al botón nos daría un error. Esto se debe a que ahora tendríamos que hacer un cambio en nuestra función que se manda a llamar para recuperar los datos y es que ahora tendremos que indicar desde que línea empiece a tomar los datos y como segundo argumento hasta cuál línea los tome.

	En este caso, nosotros representamos la primera línea con "1.0", la segunda con "2.0", etc. Teniendo en cuenta como podemos representar las líneas, podríamos indicar desde que línea empiece a tomar el contenido, como segundo argumento para indicarle hasta que línea lo tome, como quisiéramos que lo haga hasta el final, pues eso lo haríamos con *tkinter.END*, que en nuestro caso al exportar la librería para hacer referencia a ella como *tk*, pues sería *tk.END*

	![[IMG_981.png]]

	![[IMG_982.png]]

	Ademas, es importante mencionar que en nuestro formato "1.0" de las lineas, con el numero antes del punto indicamos el numero de linea, pero con el numero despues del punto indicamos el caracter, como si de una cadena de texto se tratase.
	
	Con esto en mente, pues también podríamos empezar desde la tercera línea y a partir del tercer caracter, lo que nos ignoraría la primera y segunda línea al recuperar el contenido:

	![[IMG_983.png]]

	![[IMG_984.png]]
## **Desarrollo de aplicaciones GUI con Tkinter (3/8)**


1. **Introducción**

	**Tkinter: Explorando Widgets Avanzados y Funcionalidades de Diálogo**

	1. *Frame()*

	- *Descripción:* *Frame()* es un widget en tkinter utilizado como contenedor para otros widgets.
	- *Uso Común:* Organizar el layout de la aplicación, agrupando widgets relacionados.
	- *Características Clave:*

		- Actúa como un contenedor invisible que puedecontener otros widgets.
		- Útil para mejorar la organización y la gestión del layout en aplicaciones complejas.
	</br>
	2. *Canvas()*

	- *Descripción:* *Canvas()* es un widget que proporciona un área para dibujar gráficos, líneas, figuras, etc.
	- *Funciones de Dibujo:*

		- *create_oval():* Crea figuras ovales o círculos. Los parámetros especifican las coordenadas rectángulo delimitador.
		- *create_rectangle():* Dibuja rectángulos. Los parámetros definen las coordenadas de las esquinas.
		- *create_line():* Permite dibujar líneas. Se especifican las coordenadas de inicio y fin de la línea.
		- *Uso Común:* Crear gráficos, interfaces de juegos, o elementos visuales personalizados.
	</br>
	3. *Menu()*

	- *Descripción:* *Menu()* se utiliza para crear menús en una aplicación Tkinter.
	- *Uso Común:* Añadir barras de menús con opciones como *Archivo*, *Editar*, *Ayuda*, etc.
	- *Características Clave:*

		- Se pueden crear menús desplegables y menús contextuales.
		- Los menús pueden contener comandos, opciones de selección y otros submenús.
	</br>
	4. *messagebox*

	- *Descripción:* *messagebox* es un módulo en Tkinter que proporciona ventanas emergentes de diálogo.
	- *Funciones Comunes:*
		- *showinfo()*, *showwarning()*, *showerror()*: Muestran mensajes informativos, de advertencia y de error, respectivamente.
		- *Uso Común:* Informar al usuario sobre eventos, confirmaciones, errores o advertencias.
	</br>
	5. *filedialog*

	- *Descripción:* *filedialog* es un módulo que ofrece diálogos para seleccionar archivos y directorios.
	- *Funciones Clave:*
		- *askopenfilename():* Abre un cuadro de diálogo para seleccionar un archivo para abrir.
		- *asksavefilename():* Abre un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo para guardar.
		- *askdirectory():* Permite al usuario seleccionar un directorio.

	- *Uso Común:* Integrar la funcionalidad de apertura y guardado de archivos en aplicaciones.

	**Conclusión**

	El dominio de estos widgets y módulos (*Frame()*, *Canvas()*, *Menu()*, *messagebox*, *filedialog*) es crucial para desarrollar aplicaciones GUI interactivas y completas en Tkinter. Cada uno aporta funcionalidades específicas que permiten crear interfaces de usuario más ricas y dinámicas, adaptadas a una amplia variedad de necesidades.
	</br>
2. *Práctica*

	*Widget Frame()*

	En nuestra ventana, utilizar el widget *Frame()* es como agregar nuevos elementos, los cuales serán como contenedores, donde podremos representar nuestra información. Esto nos será de ayuda para tener la representación de nuestro contenido de una forma mucho más organizada, ya que podremos agregar múltiples contenedores del widget *Frame()* para representar nuestra información o contenido de la aplicación.

	Podríamos ver nuestra ventana como un contenedor principal. Al agregar contenedores dentro de esta, los elementos que agreguemos en nuestro contenedor  Frame se verán de la misma forma que en la ventana principal, como lo hemos visto hasta ahora.

	*Creación del widget*

	Para crear este widget utilizaremos *Frame()*, donde como hemos visto anteriormente le colocaremos como primer argumento la ventana, le daremos un fondo con *bg* y como nueva propiedad para aprender, utilizaremos *bd* para asignarle un valor numérico para que se le de un ancho al borde que tendrá:

	![[IMG_985.png]]

	Recordemos que al crear un widget, no se representa automáticamente. En este caso utilizaremos *place()* para colocarlo al centro de la ventana, de forma relativa y que tome como punto de enfoque el centro del frame:

	![[IMG_986.png]]

	Si ahora ejecutamos esto, tendríamos nuestra ventana de la siguiente manera:

	![[IMG_987.png]]

	En este caso no visualizamos nada debido a que nuestro frame no tiene nada de contenido, pero sí por ejemplo creáramos un *Label()*, sería de la misma manera que como lo hemos hecho, la diferencia será que ahora en lugar de pasarle como primer argumento nuestra ventana principal, será el frame que hemos creado.

	![[IMG_988.png]]

	Podríamos agregar otro label e incluso aumentar el tamaño de nuestro borde en el frame, cambiando el valor de *bd*:

	![[IMG_989.png]]

	Se puede jugar con tamaños para verlo del mismo tamaño, en este caso se ve así porque un label es más grande que otro por el contenido, pero en lugar de jugar con tamaños, en este caso podríamos poner un texto más general como "Label1" y cambiar solo el número para el segundo, teniendo un resultado mucho mejor visualmente:

	![[IMG_990.png]]

	Otra forma más correcta de afrontar el que los label no estén alineados, sería que al estar mostrándolos con *pack()* podremos utilizar la propiedad *fill* para que se adapte a todo el tamaño sobre el eje X.

	![[IMG_991.png]]

	**Widget Canvas()**

	El widget *Canvas()* nos permitirá dibujar figuras dentro de nuestra aplicación. Para utilizarlo lo crearíamos como hemos creado otros widgets y en este caso lo haremos para nuestra ventana principal. Le daremos un alto y ancho, así como un color de fondo, y al mostrarlo con *pack()* le daremos un padding para que no quede tan pegado a la parte superior:

	![[IMG_992.png]]

	![[IMG_993.png]]

	*Crear un círculo u óvalo*

	Para crear el círculo, almacenado en la variable *oval*, vamos a utilizar el método *create_oval* de nuestro canvas. Como argumentos principales tendremos 4, que podremos verlos como *w*, *x* , *y* y *z*, además de *fill* para asignarle un fondo a nuestra figura.

	Tendremos que ver *w*, *x*, *y* y *z* como los vertices de un cuadrado imaginario, donde indicaremos los puntos necesarios mediante pixeles para que cada vertice se acomode en nuestro canvas y crear nuestro óvalo, dependiendo de que tan alejado pongamos el vertical del vertical o el horizontal del horizontal, tendremos como resultado un círculo o un óvalo.

	Otra forma de verlo sería como colocar las coordenadas de dos puntos, el primero sería viendo nuestro objeto como un cuadrado imaginario, donde el punto iniciara en la esquina superior izquierda y el final será en la esquina inferior derecha, tal como trazar una línea en un plano, sobre la cual se creara nuestro óvalo o círculo.

	![[IMG_994.png]]

	![[IMG_995.png]]

	Para crear un rectángulo aplicaríamos la misma lógica anterior, pero utilizando el método *create_rectangle*, le daremos unos puntos distintos para que no colisione con el círculo que ya tenemos:

	![[IMG_996.png]]

	*Crear una línea*

	Para crear una línea, es de la misma forma que lo hemos hecho anteriormente, colocando el punto inicial y el punto final. En todas las figuras que representemos, podremos ver los primeros dos valores dados como el *x* y*y* del primer punto, así como los últimos dos valores, los puntos del punto final:

	![[IMG_997.png]]

	En este caso, la línea se ve muy delgada, por lo que podremos agregar el atributo *width* e indicarle a nivel de píxeles como queremos que se vea de grosor:

	![[IMG_998.png]]

	**Crear un Menú con Tkinter**

	Para esto, primero crearemos una ventana totalmente vacía:

	![[IMG_999.png]]

	Recordemos que el *mainloop()* para nuestra ventana, lo utilizamos para que toda la interacción en nuestra aplicación tenga su funcionalidad y el usuario pueda interactuar con cada apartado  realizar las tareas que la aplicación permite.

	Para nuestro menú, comenzaríamos creando una barra principal sobre la cual estarán las distintas opciones de nuestro menú y en cada una de estas podremos poner opciones o submenú. Para ello utilizaríamos el widget *Menu()* y le pasaríamos como argumento la ventana en la que lo mostraremos, además utilizaremos el método *config* de nuestra ventana para a nivel de propiedad indicarle como argumento nuestra barra, para que así se muestre:

	![[IMG_1000.png]]

	Para agregar nuestro primer apartado de nuestro menú, tendremos que crear un nuevo widget *Menu*, el cual para mostrarlo utilizaremos un método de nuestra propia barra de menu, el cual es *add_cascade()* y como propiedades colocaremos *label* donde indicaremos el texto que mostrara nuestra opción y con *menu* pasaremos el widget de menu que recién creamos, donde al presionarlo se mostrarán las opciones de nuestro primer menu:

	![[IMG_1001.png]]

	En este caso, al seleccionar el menú solo veremos unas líneas. Esto se debe a que aún no agregamos opciones. Para poder agregar utilizaremos el método *add_command* directamente en nuestro widget *menu1*:

	![[IMG_1002.png]]

	Las líneas sobre nuestras opciones las podremos llamar fragmentado, estas están por defecto y nos permiten que al presionarlo nos separe en una ventana distinta las opciones de nuestro primer menú.

	Es posible que no nos interese la posibilidad de fragmentarlo y separarlo de nuestra ventana principal, es por ello que al momento de crear nuestro widget del primer menú tendremos que agregar la propiedad *tearoff* y asignarle el valor de 0, de esta manera ahora lo veremos así:

	![[IMG_1003.png]]

	Además, al crear el widget del menu también agregamos que este será mostrado en nuestra barra del menú, que será la principal e incluirá todos los menús.

	Por lo que nuestro widget menu1, al crearlo con *Menu()* tendrá como primer argumento donde se mostrará *bar_menu* y como segundo argumento la propiedad *tearoff* seteada a *0*, para indicar que no queremos que nuestras opciones de cada menu se puedan fragmentar.

	Ahora crearemos un *segundo menú*, para ello lo haremos de la misma forma anterior. A este menú le llamaremos *Extras* y como opción le agregaremos *Mostrar mensaje*, ya que configuraremos una función la que efectúe mostrarnos un mensaje en pantalla mediante el módulo *messagebox* de tkinter:

	![[IMG_1004.png]]

	Para lanzar el mensaje, importaremos el módulo *messagebox* de tkinter y crearemos nuestra función *action_menu* donde, con *showinfo* del módulo *messagebox*, dándole como primer argumento el nombre de la ventana y como segundo el contenido que mostrará como mensaje, se lanzará nuestro mensaje informativo:

	![[IMG_1005.png]]

	Ahora, en nuestra primera opción de nuestro menú *Extras*, tendremos que agregar el atributo *command* para que al presionar en la primera opción indicarle que se tiene que ejecutar esta función:

	![[IMG_1006.png]]

	Por lo que ahora, al ejecutarlo y presionar en la primera opción de nuestro segundo menú, tendremos la siguiente ventana con el mensaje:

	![[IMG_1007.png]]

	De esta manera, a cada opción dentro de los menús que coloquemos  en nuestra barra de menús, podremos agregarles una funcionalidad específica que se ejecute al presionarlo.

	*Messagebox*

	El módulo *messagebox* de la librería *tkinter* nos permite mostrar mensajes al usuario en distintas formas. Es por ello que no solo podremos aplicar esto en el caso de los menús, sino que también en botones o incluso cuando el programa llegue a presentar un error inesperado.

	Para ello crearemos una ventana con un único botón que, al presionarlo, nos lance un mensaje:

	![[IMG_1008.png]]

	![[IMG_1009.png]]

	Además de *showinfo*, tenemos otras formas de lanzar mensajes como *showwarning()* y *showerror()*, que se utilizan de la misma forma, solo cambia la visualización al mostrar el mensaje.

	*filediaolog*

	En tkinter tenemos muchísimos módulos que nos permiten hacer distintas cosas, otro muy interesante es *filedialog* el cual nos permite mediante su método *askopenfilename()*, abrir una ventana para la selección de algún archivo y nos retornara la ruta absoluta de este mismo, lo cual podremos almacenar en una variable:

	![[IMG_1010.png]]

	De la forma anterior, además de guardar la ruta absoluta en la variable *ruta_absoluta*, la mostraremos en pantalla. Una vez presionado el botón, podremos seleccionar cualquier archivo en el sistema:

	![[IMG_1011.png]]

	Al seleccionar el archivo y darle a *open*, se nos almacenará la ruta absoluta en la variable y, como indicamos, se mostrará en la terminal:

	![[IMG_1012.png]]

	De la misma forma que tenemos *askopenfilename()*, también tenemos *asksaveasfilename()*, nos permite seleccionar una carpeta y escribir un nombre en la barra para darle save, esto no nos guardara el archivo, pero si nos almacenara en nuestra variable la ruta absoluta con todo y el nombre del archivo que deseamos crear o almacenar, para lo cual podríamos apoyarnos con le uso de *open()*:

	![[IMG_1013.png]]

	![[IMG_1014.png]]

	*askdirectory()*

	También tenemos *askdirectory()*, funciona exactamente igual que los anteriores y nos permitirá almacenar la ruta absoluta de algún directorio para trabajar con él en nuestro sistema.


## **Desarrollo de aplicaciones GUI con Tkinter (4/8)**


1. **Introducción**

	Se abordara un proyecto que consolidará todo lo aprendido hasta ahora con Tkinter: la creación de nuestro propio editor de texto, similar al Bloc de Notas.

	Este será un excelente ejercicio para aplicar nuestras habilidades en un contexto práctico y realista, permitiéndonos ver cómo los componentes individuales en Tkinter se unen para formar una aplicación funcional.

	Nuestro editor de texto incluirá funcionalidades básicas como:

	- Crear un nuevo archivo
	- Abrir y editar archivos existentes
	- Guardar los cambios
	- Cerrar la aplicación

	Para esto haremos uso de varios widgets y técnicas de Tkinter que hemos estudiado, como *tkinter.Text()* para el área de edición, *Menu()* para la barra de menús y *filedialog* para la gestión de archivos.

	Se adoptara un enfoque de Programación Orientada a Objetos (POO) en este proyecto. Utilizando clases para estructurar nuestro código, lo que permitirá dividir la funcionalidad de la aplicación  en bloques lógicos y reutilizables. Este método no solo facilitará la organización y gestión del código, sino que también nos proporcionará una sólida base para la escalabilidad y mantenimiento  futuro del proyecto.
	</br>
2. **Práctica**

	Para construir este proyecto iniciaremos creando un archivo *execise.py*, en el cual importaremos la librería *tkinter* y los módulos *filedialog* y *messagebox*:

	![[IMG_1015.png]]

	Con esto listo, ahora crearíamos nuestra ventana principal y al final agregaremos el *mainloop()* de nuestra ventana, para que el usuario pueda interactuar con las funcionalidades que generaremos:

	![[IMG_1016.png]]

	*Construyendo el menú*

	Comenzaremos creando nuestra barra de menú y crearemos un primer menú de opciones, *Nuevo*, *Abrir*, *Guardar* y *Salir*:

	![[IMG_1017.png]]

	Podremos observar como primeramente definimos la barra de menús y nuestro menú de opciones, luego agregamos las opciones correspondientes y finalmente indicamos a nuestro programa la configuración para que sean mostradas en nuestra ventana. Lo veríamos de la siguiente manera:

	![[IMG_1018.png]]

	Para ver un poco mejor nuestra ventana, le asignaremos una proporción que se adapte a lo que mejor consideremos, en este caso una buena proporción podría ser *700x500*, la cual se asigna directamente a la ventana con el método *geometry()*:

	![[IMG_1019.png]]

	*Comenzamos a trabajar con POO*

	Para ello vamos a crear una clase la cual se llame *SimpleTextEditor*, la cual visualizaremos, referenciando primeramente, hacia un objeto *editor* y pasándole como argumento nuestra ventana principal:

	![[IMG_1020.png]]

	Con esto en mente comenzaríamos creando nuestra clase y en nuestro constructor recibiendo la ventana para asignarla como propiedad a nuestra clase. Además, aquí mismo aprovecharemos para crear nuestro widget *Text* para la edición del archivo (no se mostrará aún, porque solo lo estamos creando, recordemos que para dibujarlo en la venta tendremos que usar los métodos *pack*, *grid* o *place*).

	![[IMG_1021.png]]

	En este caso creamos el widget *Text* para nuestra ventana y lo mostramos con *pack()*, pero podremos notar como tendremos un problema de que no se adapta a nuestra ventana y es lo que buscaremos en este caso:

	![[IMG_1022.png]]

	Al utilizar pack sabremos que al utilizar la propiedad *fill*, podremos indicarle esto a nuestro widget, en el eje X siempre se adaptara al total de la pantalla, pero cuando lo intentamos en el eje Y, veremos que existe como un límite y por ende no se adapta al total de la ventana en el eje Y:

	![[IMG_1023.png]]

	Además de *tk.X* para el eje X y *tk.Y* para el eje Y, tenemos *tk.BOTH* la cual nos sirve para indicarle a un widget que se adapte en ambos ejes, *X* y *Y*:

	![[IMG_1024.png]]

	Pero a pesar de esto seguiremos notando como en el eje Y no se adapta totalmente, para ello tendremos la propiedad *expand*, la cual colocaremos como segundo argumento después de nuestro *fill* y le asignaremos un *1*, lo que significará que se podrá adaptar más allá de los límites preestablecidos, de esta manera ahora si se adaptará al total de nuestra ventana:

	![[IMG_1025.png]]

	*Metodo quit_confirm*

	De las 4 opciones que hemos colocado en nuestro menú, comenzaremos definiendo la funcionalidad de nuestra opción *salir*.

	Para ello en nuestra clase crearemos el método *quit_confirm*, lo esperado de esto es que nos salte una ventana la cual nos permita seleccionar entre *ok* y *cancel*, lo cual es un método del módulo *messagebox* de tkinter y este es *askokcancel()*.

	Si lo utilizamos directamente nos saltará la venta, pero buscaremos imprimir lo que esta nos retorne:

	![[IMG_1026.png]]

	Para que esto funcione tendremos que indicarle a la opción *salir* que nos ejecute el método *quit_confirm* de nuestro objeto *editor*, lo cual hacemos con la propiedad *command:*

	![[IMG_1027.png]]

	Finalmente, al ejecutarlo y presionar *salir*, nos cargará la siguiente ventana:

	![[IMG_1028.png]]

	En este caso no nos muestra ningún contenido, ya que no se lo indicamos, ni le dimos nombre a la ventana.

	Pero podremos observar los dos botones, al presionarlo nos retornará algo y como hemos indicado que nos lo imprima en pantalla, lo veremos en la terminal. Primeramente, lo haremos para *ok* y después para *cancel* y esto será lo que veremos:

	![[IMG_1029.png]]

	Como observamos, cuando fue presionado *ok* nos fue retornado un *True*, pero cuando se presionó *cancel* lo que se retornó fue un *False*, por lo que con ello podremos trabajar con condicionales para saber si el usuario realmente quiere salir de la aplicación o no.

	De esta manera, ahora le asignaremos como nombre a la ventana "Salir" y como contenido del mensaje para el usuario "¿Estás seguro de que deseas salir?", finalmente de forma directa meteremos esto en un condicional, donde si nos retorna *True*, entrará directamente y este será el caso donde se presione *ok*.

	Al entrar, lo que buscaremos es destruir nuestra ventana principal para que se cierre y se termine de ejecutar nuestro programa, recordando que tenemos nuestra ventana como una propiedad de la clase, solo tendremos que referencial al método *destroy()* de nuestra propia ventana, para que se finalice la ejecución de esta misma:

	![[IMG_1030.png]]

	De esta forma, ahora lo que veremos al ejecutar nuestra venta y darle a salir será lo siguiente:

	![[IMG_1031.png]]

	Si presionamos *cancel* no pasará nada, pero si presionamos *ok*, al ser *True* entrará en el condicional y se destruirá la ventana, por lo que se cerrará nuestro programa.

	*Opción Abrir archivo*

	Ahora programaremos el funcionamiento de la opción *Abrir*, el método que crearemos para esta será *open_file*, por lo que de nuestro objeto para esta opción, agregamos el método con nuestra propiedad *command*:

	![[IMG_1032.png]]

	Ahora comenzaremos creando el método en nuestra clase, como utilizaremos el método *askopenfilename* del módulo *filedialog*, primero buscaremos imprimir en la terminal lo que nos retorna al seleccionar un archivo:

	![[IMG_1033.png]]

	De esta manera, al presionar *Abrir* y seleccionar un archivo, veremos lo siguiente:

	![[IMG_1034.png]]

	![[IMG_1035.png]]

	Como vemos, lo que nos retornara al seleccionar un archivo es su ruta absoluta del mismo. Lo que haremos será almacenar su ruta absoluta en una variable, en este caso le daremos de nombre *filename*, de esta manera utilizamos *open()* con *with* para no preocuparnos por cerrar el archivo y lo abrimos en modo de lectura, nuestra área de texto cuenta con el método *insert* donde indicaremos que desde la primera línea y el carácter 0, nos inserte el contenido del archivo que recuperaremos con *file.read()*:

	![[IMG_1036.png]]

	De esta forma, esto ya nos cargará el contenido del archivo que seleccionemos, pero puede ser que al momento de abrir un archivo ya tengamos otro cargado, por ende antes de abrir el archivo limpiaremos nuestra área de texto con el método *delete()*, donde le indicaremos que nos limpie nuestra área de texto desde la primera línea y el carácter 0 ("1.0"), hasta el final ("tkinter.END"), además en nuestro constructor agregaremos la propiedad *current_open_filename* para que después de cargar el contenido de ese archivo en esta almacenemos siempre la ruta absoluta del archivo que tengamos abierto:

	![[IMG_1037.png]]

	De esta manera ahora si podremos seleccionar y cargar el contenido de cualquier archivo y empezar a editarlo:

	![[IMG_1038.png]]

	![[IMG_1039.png]]

	Incluso podríamos hacer la prueba de verificar si nos elimina un contenido que ya tengamos, si cerramos y ejecutamos nuevamente nuestra aplicación, podríamos escribir contenido y luego cargar un archivo, de esta manera observaremos como si nos elimina el contenido que ya tenía para cargarnos el de un archivo.

## **Desarrollo de aplicaciones GUI con Tkinter (5/8)**


1. **Introducción**

	Continuaremos con el proyecto del editor de texto, con el objetivo de finalizarlo. Hasta ahora se ha logrado implementar funciones clave como la creación, edición, guardado y apertura de archivos de texto. En esta sesión, nos enfocaremos en pulir nuestra aplicación, asegurándonos de que todas las funcionalidades trabajen de manera fluida y eficiente.

	Una vez hayamos completado y perfeccionado nuestro editor de texto, daremos un paso adelante en nuestro aprendizaje con el inicio de un nuevo y fascinante proyecto: creación de una calculadora con interfaz gráfica interactiva. Este proyecto nos permitirá aplicar y expandir aún más nuestros conocimientos en Tkinter, abordando nuevos desafíos y explorando diferentes aspectos de la creación de GUIs.

	En la calculadora, implementaremos funciones básicas como:

	- Sumar
	- Restar
	- Multiplicar
	- Dividir

	Así como una interfaz de usuario intuitiva que permita a los usuarios interactuar fácilmente con la aplicación. Este proyecto no solo reforzará nuestras habilidades en tkinter y la programación orientada a objetos, sino que también nos brindará la oportunidad de abordar problemas de lógica de programación y diseño de interfaces de usuario.
	</br>
2. **Práctica**

	*Nuevo archivo*

	Ahora definiremos el funcionamiento para la opción de generar una nueva nota, esto es sencillo, ya que solo definiremos el método *new_file* y lo que haremos será limpiar todo nuestra área de texto, porque es posible que ya tenga algún texto y además como en este momento no está siendo asignado el contenido a ningún archivo, setear la propiedad *current_open_file()* como un string vacío:

	![[IMG_1040.png]]

	De esta manera, al tener ya contenido o algún archivo abierto, al presionar *Nuevo*, nos elimina el texto que se esté mostrando en nuestro widget *Text* y además seteamos nuestro *current_open_file()* a una cadena vacía.

	*Guardar*

	En el caso de guardar, la lógica podría ser un poco más compleja. En este caso tendremos que tener en cuenta primeramente si nuestra propiedad *current_open_file* tiene contenido, de tenerlo ya sabemos con qué archivo se está trabajando y solos se tendrá que guardar el contenido, de lo contrario haremos uso de *filedialog* para que con el método *asksaveasfilename* indiquemos en donde y con qué nombre lo guardaremos.

	De esta manera, a nuestra opción *Guardar* le asignaremos como función a ejecutar *save_file* del objeto *editor* y comenzaremos definiendo un condicional donde verifique la propiedad *current_open_file* no tiene contenido, de no tenerlo entrará en el condicional:

	![[IMG_1041.png]]

	De esta manera, en nuestro condicional definiremos que al no saber con qué archivo se está trabajando se utilice *asksaveasfilename()* del módulo *filedialog* para saber como guardaremos el contenido que estemos escribiendo.

	Tendremos que verificar si esto nos retorna contenido o no, porque en caso de que en la variable donde vayamos a almacenarlo este vacía, quiere decir que no se seleccionó un directorio y nombre para saber con qué archivo estemos trabajando.

	De esta manera, si tiene contenido almacenaremos el archivo con el que trabajaremos en *current_open_file*, de lo contrario no haremos nada y saldremos de la función con un *return*:

	![[IMG_1042.png]]

	Finalmente, si no hemos salido de la función, quiere decir que ya sabemos con qué archivo estamos trabajando, por lo que se abrirá en forma de escritura y almacenaremos el contenido que tenga nuestro widget *Text*, el cual podemos recuperar gracias a su propiedad *get*, indicando que nos tome encuenta desde el incio hasta el final:

	![[IMG_1043.png]]

	De esta manera ya podremos almacenar archivos y de ser un archivo nuevo, podremos almacenarlo en un directorio deseado y con el nombre que quieramos.

	Con esto ya tendremos totalmente funcional nuestro primer proyecto hecho con interfaz gráfica.

	**Calculadora**

	Comenzaremos creándonos el archivo *calculadora.py*, en este archivo principalmente tendremos en cuenta nuestra ventana y la creación de una instancia de la clase *Calculadora* que crearemos con la definición de la lógica y la interfaz de nuestro programa, por lo que le pasaremos como argumento la ventana principal:

	![[IMG_1044.png]]

	Con esto en mente, comenzaríamos a crear nuestra clase con su constructor. Aquí recibiremos la ventana principal *root* como *master* para referenciarla en todo momento, así en nuestra clase.

	Además, en una calculadora usualmente en la parte superior contamos con un display, es por ello que crearemos uno que sea un widget *Entry()* y además lo mostraremos con *grid()* en la posición (0,0), así como todo el contenido de nuestra aplicación, ya que al contar con todos los botones, conviene más mostrarlo a nivel de casillas:

	![[IMG_1045.png]]

	De esta manera, tendríamos una ventana inicial pequeña la cual solo contiene nuestro widget *Entry()*.

	Para darle forma a nuestro display, tendremos que modificarlo, para ello primeramente le indicaremos como argumento la ventana en la que se tiene que mostrar, así como darle un tamaño en píxeles, en este caso con la propiedad *width* le daremos un valor de *15*, ademas utilizaremos la propiedad *font* donde asignándole una tupla, primeramente indicamos la fuente y luego el tamaño, en este caso será *Arial, 23* y finalmente agregaremos un borde con *bd* de *10*:

	![[IMG_1046.png]]

	Esto nos daría un resultado así:

	![[IMG_1047.png]]

	Esto ya tiene una mayor forma, pero podríamos mejorarlo. Agregaríamos un fondo con *bg*, en este caso podríamos jugar con el color `#17dfff`, finalmente, como el cursor se ve bastante grueso al momento de escribir en nuestro display, utilizaremos *insertwidth* y le daremos un valor de 1, para verlo delgado:

	![[IMG_1048.png]]

	Con estos cambios, ya tendríamos nuestro display de la siguiente forma:

	![[IMG_1049.png]]

	En una calculadora siempre se suele visualizar la entrada de datos al lado derecho, es por ello que en nuestro mismo widget tendremos que utilizar la propiedad *justify* y asignarle *right* para verlo de esta manera:

	![[IMG_1050.png]]

## **Desarrollo de aplicaciones GUI con Tkinter (6/8)**

1. **Introducción**

	Se seguira construyendo la calculadora con interfaz gráfica. Nos enfocaremos en perfeccionar la funcionalidad y el diseño de la aplicación, asegurando que cada elemento opere de manera efectiva y que la interfaz sea intuitiva y atractiva.
	</br>
2. **Práctica**

	Comenzaremos teniendo en cuenta los botones que agregaremos para nuestra calculadora, por ello primeramente haremos una lista en la cual almacenemos el texto que mostrará cada uno de nuestros botones, de la siguiente manera:

	![[IMG_1051.png]]

	Ahora crearíamos dos variables, una para la fila y otra para la columna de cada botón. Estas serán *row* y *col*, que tendremos inicializadas en (1,0). Esto es debido a que nuestro display esta en la primera fila (0), por ende comenzaríamos a partir de la 1, donde mediante la iteración de un bucle vamos a ir incrementando las columnas y una vez haya pasado por todas las columnas, se pasará a la siguiente fila.

	Como vimos en los botones, tenemos en cuenta en total 4 columnas.

	![[IMG_1052.png]]

	Lo siguiente será iterar sobre cada elemento de la lista que será el contenido de cada botón. Al iterar llamaremos a un método que se encargará de construir cada botón. El método será *build_button()* y recibirá como argumentos el contenido del botón, así como fila y columna.

	Después, como para cada fila tendremos 4 columnas, bastará con un condicional para verificar cuando la columna sea mayor a 3, en ese caso la regresaremos a la columna 0, así como aumentaremos la fila, para que ahora genere los de la siguiente fila.

	![[IMG_1053.png]]

	Ahora podríamos colocar un string que nos muestre la información sobre cada botón y de en qué posición quedará representado, comentando la línea donde se manda a llamar el método, ya que por el momento no está creado:

	![[IMG_1054.png]]

	![[IMG_1055.png]]

	De esta manera veremos el contenido de cada botón y cuál será la posición de cada uno. Esto fue a manera de observar que es lo que está sucediendo, ahora podremos quitar esto y descomentar la línea que manda a llamar a nuestro método *build_button* para ahora si comenzar a generarlo.

	**Método build_button**

	Para este método tendremos en cuenta los parámetros que vamos a recibir y primeramente construiremos el botón, para este tendremos en cuenta que lo mostraremos en la ventana principal (*nuestra propiedad master*), después indicaremos el texto que mostrará cada botón, que será el parámetro *button* que recibe en cada iteración de la lista:

	![[IMG_1056.png]]

	Ahora nos faltaría mostrar cada botón, donde con grid indicaremos la fila y columna correspondientes:

	![[IMG_1057.png]]

	De esta manera, ahora al ejecutarlo veremos todo de la siguiente manera:

	![[IMG_1058.png]]

	Todo se ve descuadrado, pero es debido a que todo trata de ocupar la columna correspondiente. Es por ello que le indicaremos a nuestro display, con la propiedad *columnspan* que ocupe las 4 columnas al mostrarse con grid, que corresponde a abarcar las columnas de los botones para que tengamos una mejor adaptación de todo:

	![[IMG_1059.png]]

	Lo único que nos deja esto es un descuadramiento en cuanto al tamaño de cada botón. Esto sucede porque el tamaño del contenido es distinto en cada uno de ellos. Es por ello que les asignáramos un tamaño fijo a todos, para que se vean igual. Para ello utilizaremos la propiedad *width* en la creación de los botones, le daremos como valor 3 o 4 y dejaremos el que mejor quede a nuestra consideración:

	![[IMG_1060.png]]

	Para la definición de cada botón, cambiará el *command* que será la asignación del método a ejecutar; es por ello que jugaremos con una serie de condicionales.

	Primeramente, nos enfocaremos en el botón *C* que será para limpiar el display de nuestra calculadora. En este caso, le asignará a este botón el método *clear_display()*, de no ser este el botón, generaremos los demás sin *command*, solo para que los muestre e ir viendo la funcionalidad:

	![[IMG_1061.png]]

	Ahora definiríamos cómo se limpie nuestro display. En este caso, al ser un widget *Entry* se hace de forma similar al widget *Text*, solo cambia que se está trabajando con una sola línea y múltiples caracteres. Por ello no se utiliza "1.0", donde antes del punto se indica la línea y después del punto el carácter desde el cual considera, si no directamente el carácter número 0, hasta el final:

	![[IMG_1062.png]]

	De esta manera, ya funciona el limpiar nuestro display si tenemos caracteres escritos.

	Ahora, para el botón de *\=*, definiremos un método *calculate* para que se calcule el resultado. Por el momento solo dejaremos un print para saber si se esté ejecutando correctamente:

	![[IMG_1063.png]]

	Al ejecutarlo y presionar el *\=*, veremos cómo funciona correctamente lo que hemos definido en el método *calculate*:

	![[IMG_1064.png]]

## **Desarrollo de aplicaciones GUI con Tkinter (7/8)**

1. **Introducción**

	Se seguirá avanzando con el proyecto de la calculadora con interfaz gráfica. Nos enfocaremos en perfeccionar la funcionalidad y el diseño de la aplicación, asegurando que cada elemento opere de manera efectiva y que la interfaz sea intuitiva y atractiva.
	</br>
2. **Práctica**

	Ahora para el resto de botones agregaremos un método, el que requerirá de un argumento, lo cual se agrega al *command* de la misma manera, pero agregando el argumento, en este caso será el contenido del botón para saber con cuál se trabaja y la función imprimirá esa información:

	![[IMG_1065.png]]

	Aqui parece todo bien, pero tendremos un problema. Hasta ahora cada que en la propiedad *command* queremos agregar alguna función o método, lo hemos hecho sin paréntesis y esto es porque no han requerido de argumentos, pero el colocarle los paréntesis lo que ocasiona es que se ejecute directamente en lugar de asignarse para cada vez que sea presionado el botón.

	![[IMG_1066.png]]

	Es por ello que para a que se dé la asignación correctamente sin que se ejecute. Haremos uso de las funciones anónimas lambda, lo cual ahora sí nos permitirá tener el funcionamiento que esperamos:

	![[IMG_1067.png]]

	De esta manera se hace la asignación correctamente y cada que presionemos los botones correspondientes al método *click* nos dará su información:

	![[IMG_1068.png]]

	Ahora en el método *click* lo que haremos será insertar el valor de cada tecla que sea presionada en el display y para ello utilizaremos *insert* como se usa en el widget *Text*. Vamos a colocar que cada que se presione una tecla el carácter siempre se agregue al final, para que sea a la derecha siempre, y si escribimos primero 7 y luego 8, nos represente correctamente el 78, ya que si colocamos que se ingrese al inicio o en la posición 0, siempre lo colocara a la izquierda y en lugar de 78 veríamos un 87:

	![[IMG_1069.png]]

	Utilizar *end* o *tk.END* al insertar los datos o cualquier otra operatoria con los widgets de texto es exactamente lo mismo y no tendrá ningún efecto distinto.

	Además, al utilizar las funciones lambda en la asignación de *command* para los botones, tendremos que colocar dentro de ellas los paréntesis para cada método, aunque estos no requieran argumentos, de lo contrario no se ejecutarán al presionar los botones.

	Con lo anterior, al ejecutar la aplicación y presionar los botones, ya nos estaría colocando todo dentro del display:

	![[IMG_1070.png]]

	*Método click*

	Para nuestro método click, primeramente pensaremos en agregar dos propiedades más a nuestro constructor de la clase, será *op_validation* que será un valor booleano inicializado en *False* para validar cuando se pare de introducir números a realizar cierta operación con otro número, además de la propiedad *current* que en forma de string irá almacenando número a número, incluyendo el punto de una forma conjunta, lo cual cambiará una vez se presione uno de los botones para realizar la operación, almacenando totalmente nuestro primer número, asignando nuevamente una cadena vacía a *current* y empezando a almacenar ahora el segundo número.

	![[IMG_1071.png]]

	Ahora, en nuestro método click primeramente definiremos una validación de si el botón que se ha presionado está entre una serie de números del 0 al 9 o si es el punto, de lo contrario serán los distintos tipos de opción y para ello se utilizará *else*.

	![[IMG_1072.png]]

	La idea entonces será que, mientras solo se ingresen números y, en su respectivo caso, el punto para generar un número con decimales, iremos agregando uno a uno a nuestra propiedad *current* que será el número actual que vayamos introduciendo.

	Además, mostraremos en pantalla, al final de cada que presionemos un botón, el número que vamos generando, así como el estado de nuestra propiedad *op_verification*, que por el momento estará siempre en False:

	![[IMG_1073.png]]

	![[IMG_1074.png]]

	De esta manera vamos visualizando nuestro número. Nuestro estatus cambiará una vez que se presione cualquier tecla de alguna operación, así como almacenaremos el número que ya tenemos y regresaremos *current* a una cadena vacía para almacenar el siguiente número.

	De esta manera, primeramente deberemos agregar las propiedades *op* para almacenar el valor del botón de la operación que se quiere realizar y *total* para ahí almacenar el primer valor ya en un valor *float*, una vez que necesitemos vaciar el valor de current:

	![[IMG_1075.png]]

	Ahora nos iremos al *else* en nuestro método *click*, donde entrará una vez que presionemos el botón para realizar algún tipo de operación. Aqui vamos a validar primeramente si *current* tiene contenido, porque podremos presionar algún botón de una operación sin haber ingresado números.

	En el caso de que nuestro current ya tenga contenido, quiere decir que tenemos un número para ya almacenar, entonces aqui verificaremos si nuestra propiedad *op* está vacía, que al ser el primer dato lo estará, en este caso almacenaremos en *total* el valor de current como un dato numérico flotante y regresaremos nuestra propiedad *current* a un dato vacío para que poder almacenar el siguiente número.
	
	Finalmente, fuera de los condicionales, vamos a asignarle a *op* el valor del botón que se ha presionado para saber el tipo de operación que se realizará y le asignaremos el valor de *True* a nuestro *op_validation*:

	![[IMG_1076.png]]

	Finalmente, al inicio de nuestro método agregaremos una verificación, donde si nuestro *op_validation* es *True* lo setearemos a *False* y al final mostraremos a forma de nosotros observar el funcionamiento los datos de lo que valdrá nuestra propiedad *op* al seleccionar un tipo de operación, así como el valor de *total* una vez  que *current* regresa a ser una cadena vacía:

	![[IMG_1077.png]]

	Con esto listo, podremos observar el funcionamiento planeado hasta ahora, con los primeros dos dígitos que se ingresen con tipo de operación seleccionada de por medio:

	![[IMG_1078.png]]

## **Desarrollo de aplicaciones GUI con Tkinter (8/8)**

1. **Introducción**

	En lo siguiente se finalizará la construcción de nuestra aplicación calculadora con interfaz gráfica, además realizando una revisión de los métodos para verificar la funcionalidad final y correcta de nuestra aplicación.
	</br>
2. **Práctica**

	*Método calculate*

	Al hacer esto, cuando ya tengamos una operatoria seleccionada y los dos caracteres de los cuales se calculará esa operación, ahora pasaremos a lo que se realizará cuando presionemos el botón de igual, que se irá al método *calculate*.

	Aqui primeramente se verifica si *current* ya tiene un valor numérico, que sería nuestro segundo número y, además, si *op* ya cuenta con el tipo de operación que se va a realizar. De no tener estos dos, no abra un segundo número con el cual realizar una opción o no abra un tipo de opción a realizar.

	Luego de esta verificación, iremos verificando con condicionales qué tipo de operación se va a realizar. Comenzaremos por la división, donde dividiremos el primer valor *total* entre el segundo *current*, aplicando la conversión current a *float*:

	![[IMG_1079.png]]	

	Aplicaríamos esta misma lógica para el resto de operaciones:

	![[IMG_1080.png]]

	Luego de esto, tendríamos que limpiar nuestro display y mostrar el resultado, recordemos que el resultado tendremos que agregarlo al final, para que se nos muestre sin ningún problema a la derecha del todo:

	![[IMG_1081.png]]

	Finalmente, antes de realizar nuestra prueba de que estas operaciones funcionen, tendremos que asegurarnos de que nuestro método que se encarga de limpiar el display cuando se presiona la *C*, limpie todas las variables que se utilizan al efectuar una operación, ademas de eliminar lo que se imprime en terminal, ya que eso lo teniamos para veificar el funcionamiento, teniéndolo de la siguiente manera:

	![[IMG_1082.png]]

	Ahora, si empezamos a practicar operaciones de dos valores, veremos que todo funciona correctamente:

	![[IMG_1083.png]]

	![[IMG_1084.png]]

	![[IMG_1085.png]]

	![[IMG_1086.png]]

	Aqui, si ya efectuamos una operación antes, como 100\/2 y seguimos dándole a igual, los siguientes resultados seguirán dividiéndose entre 2, debido a que se mantienen los valores de *op* y *current*, mientras que la aplicación de la operación va manipulando el valor de *total*:

	![[IMG_1087.png]]

	Para darle un pequeño ajuste, podremos hacerlo al mostrar el resultado. Si efectuamos una división de *5\/7*, esto nos dará bastantes decimales. Para evitar esto en operaciones así, haremos que nos muestre solamente 3 decimales con *round* al momento de mostar el resultado en el display:

	![[IMG_1088.png]]

	![[IMG_1089.png]]

	Con esto aplicado, ahora, si repetimos la división *5\/7*, tendremos lo siguiente:

	![[IMG_1090.png]]

	**Entrada por teclado**

	Ahora todo funciona correctamente cuando utilizamos los botones, pero si intentamos utilizar el teclado no funciona, ya que no registra tecla por tecla, como sería utilizar los botones.

	Por ello utilizaremos un manejador de eventos especiales, que nos permitirá registrar las entradas por teclado y por cada tecla podremos asignarlo al método que ya tenemos que es *click* para enviarle tecla por tecla como lo hacemos con los botones.

	Para ello dentro de nuestro constructor utilizaremos un método especial de la propia ventana, el cual es *bind*, donde como primer argumento le daremos *\<Key\>* que es especialmente para reconocer cuando se presiona una tecla, así como segundo argumento se llamara a un método que crearemos el cual será *press_key*, dentro de este colocaremos un print que solo diga que se ha presionado una tecla y observaremos como cada que presionamos alguna tecla, entra en este método:

	![[IMG_1091.png]]

	En nuestro método, tenemos en cuenta que recibiremos un evento, por lo tanto, utilizamos *event* para recibirlo y trabajar con ello más adelante. Con esto podremos observar cómo al presionar con el mouse sobre el display y empezar a presionar teclas, nos mostrará el mensaje en la terminal:

	![[IMG_1092.png]]

	Dentro de nuestro método, al recibir el evento como *event*, es posible ver la tecla que se está presionando con la propiedad *char*; de esta manera, podremos ver las teclas normales:

	![[IMG_1093.png]]

	Nos mostrará las teclas normales, pero teclas especiales como el *Enter*, *Espacio*, entre otros. Se debe a que estos tienen una representación especial que no será visual si solo lo imprimimos en pantalla:

	![[IMG_1094.png]]

	*Representación de teclas especiales*

	Para estas teclas, tenemos una representación especial. No podremos verlas en pantalla, pero sí realizar comparaciones en nuestro código para comprobar cuál es la tecla que se ha presionado.

	Para ello podremos ver la siguiente tabla:

	![[IMG_1095.png]]

	Si deseamos visualizar esta tabla, nosotros, dentro del sistema operativo Linux bastará con utilizar el comando `man ascii`.

	Podremos ver que la tecla *Enter* se representa como *\\r* o, en su defecto, en hexadecimal, como *\\x0D*. Con esto en mente podremos comprobar estas teclas especiales y representar un mensaje cuando estas sean presionadas:

	![[IMG_1096.png]]

	De esta manera, aqui lo que podremos hacer es que para cada número que se presione, llamar a la misma función que llaman los botones que es *click* y pasarle como argumento el número que se presiona, de esta manera estaríamos teniendo el mismo funcionamiento:

	![[IMG_1097.png]]

	 Con esto listo, ahora para los caracteres especiales, le indicaremos a *Enter* que sea como el igual y llame al método *calculate* y aplicamos un *return* para que salga del método sin ejecutar nada más.

	Para el carácter especial de la tecla *Esc* indicaremos que nos ejecute el método *clear_display* para que nos limpie todo, tal como presionar *C* en los botones.

	Finalmente, para el *Space*, indicaremos que nos cierre la aplicación, en lugar de usar *destroy()* para simplemente cerrar forzadamente la ventana como en la actividad anterior, se utilizara *quit()* para cerrar la aplicación, de una forma menos agresiva.

	![[IMG_1098.png]]

	Con esto ya tendríamos todo el funcionamiento de nuestra calculadora para utilizarla con teclado y los botones, adicionalmente podremos agregarle al constructor que la ventana solo se quede en el tamaño que se le de y que no tenga la posibilidad de tener un resize, mediante `root.resizable(False, False)`. Esto nos funcionaría para que nuestra calculadora únicamente esté en el tamaño que requerimos.

	*resizable* cuenta con dos parámetros, ya que es asignarle que no se pueda hacer resize en el eje X ni en el Y.

	¡Con esto estará totalmente lista nuestra calculadora sencilla con GUI!

## **Desarrollo de aplicaciones GUI avanzado con CustomTkinter**

1. **Introducción**

	**CustomTkinter** es una extensión de la conocida biblioteca Tkinter de Python, diseñada para facilitar la creación de interfaces gráficas de usuario (GUI) con un estilo más moderno y personalizable. A continuación se detallan sus características y diferencias con respecto a tkinter tradicional:

	**Características de CustomTkinter**

	- **Estilo Moderno y Personalizable:** CustomTkinter ofrece widgets con un diseño más moderno y atractivo en comparación con los estándares de Tkinter. Estos widgets pueden personalizarse ampliamente en términos de colores, formas y efectos visuales.
	  </br>
	- **Facilidad de Uso:** Mantiene la simplicidad y facilidad de uso de Tkinter, permitiendo a los desarrolladores crear interfaces gráficas de manera intuitiva, pero con aspecto visual más atractivo y profesional.
	  </br>
	- **Compatibilidad:** Es compatible con el código Tkinter existente, lo que permite a los desarrolladores mejorar las interfaces de aplicaciones existentes sin necesidad de reescribir todo desde cero.
	  </br>
	- **Widgets Mejorados:** Incluye versiones mejoradas de los widgets estándar de Tkinter, como botones, etiquetas, campos de texto, etc. Con mejoras en la interactividad y el diseño.

	**Diferencias con Tkinter**

	- **Diseño Visual:** La diferencia más notable es el estilo visual. CustomTkinter proporciona un aspecto más moderno y elegante, mientras que Tkinter tiene un aspecto más tradicional y básico.
	  </br>
	- **Personalización de Widgets:** CustonTkinter permite una mayor personalización en la apariencia de los widgets, como temas oscuros, bordes redondeados, y efectos de animación, que no están disponibles directamente en Tkinter estándar.
	  </br>
	- **Facilidad de Transición:** Aunque CustonTkinter es una extensión, los desarrolladores familiarizados con Tkinter encontrarán la transición suave, ya que muchos de los conceptos y estructuras son similares.
	  </br>
	- **Comunidad y Soporte:** Tkinter al ser una biblioteca más antigua y establecida, tiene una comunidad más grande y una amplia gama de recursos y documentación. CustomTkinter, siendo más nuevo, está en proceso de crecimiento en términos de comunidad y recursos disponibles.

	En resumen, CustomTkinter se posiciona como una excelente opción para los desarrolladores que buscan mejorar la estética y la funcionalidad de sus interfaces gráficas en Python, manteniendo al mismo tiempo la simplicidad y la familiaridad de Tkinter.

	</br>
2. **Práctica**

	CustomTkinter cuenta con su propia [documentación](https://customtkinter.tomschimansky.com/documentation/)

	**Instalación**

	Para instalarlo tendremos que utilizar pip, instalando así CustomTkinter:

	```pip
	pip install customtkinter  
	```

	Estando en la documentación oficial, podríamos dirigirnos al tutorial y a principiante, donde se encuentra toda la documentación perfectamente explicada, si vemos el ejemplo de [grid system](https://customtkinter.tomschimansky.com/tutorial/grid-system), el cual es el primero.

	Observaremos cómo la sintaxis es muy similar a la de Tkinter:

	![[IMG_1099.png]]

	Lo cual podríamos ejecutar y observaremos que es lo mismo con una mejor estética visual:

	![[IMG_1100.png]]

	**Ejemplos**

	Para ver algunos ejemplos cloraneros el [repositorio](https://github.com/TomSchimansky/CustomTkinter) de custontkinter, una vez clonado, entramos en la carpeta e instalaremos con el parámetro **\-r** todo lo del archivo **requirements.txt**:

	**clonar repositorio**
	```git
	git clone https://github.com/TomSchimansky/CustomTkinter
	```

	**Instalar requerimientos**

	```pip
	pip install -r requirements.txt 
	```

	Para observar algunos ejemplos, podremos meternos a la carpeta **examples** y aquí primeramente ejecutaremos el archivo **scrollable_frame_example.py**. Veremos que esto nos abre una ventana con 3 espacios de scroll, con diferentes tipos de seleccionables y nos retornara la información en terminal:

	![[IMG_1101.png]]

	En el caso anterior fue necesaria una librería extra que aún no teníamos en el sistema, la cual es **pillow** por ello se instala con pip y ya funciona sin problemas.

	Podremos ver otro ejemplo como el **image_example.py**:

	![[IMG_1102.png]]

	O otro ejemplo muy interesante, el cual es un login y este será el archivo **example_background_image.py**:

	![[IMG_1103.png]]

	Y si hacemos el intento de logueo, pues la aplicación estará preparada para tomar la información, mostrarla en terminal y llevarnos a otra pantalla:

	![[IMG_1104.png]]

	Podremos ver otro ejemplo, el cual es **complex_example.py** y veremos que este ya contiene una mayor cantidad de widgets. Podremos cambiar entre el modo oscuro o claro, escribir en una caja de texto, seleccionar entre un menú, escalar la aplicación completa, etc.

	![[IMG_1105.png]]

	Incluso si nos pusiéramos a ver algún archivo, observaríamos cómo la sintaxis es muy similar a lo que se ha estado viendo de tkinter, cambiarán algunas cosas y la complejidad será un poco mayor, pero sigue la misma línea.

	Esto ha sido una visión general de las cosas que se pueden hacer con CustomTkinter. Si es algo que deseas aprender y tenerlo en cuenta más a fondo, recuerda que puedes acceder a la propia [documentación](https://customtkinter.tomschimansky.com/documentation/) y aprender muchas cosas muy interesantes por tu cuenta.

## **Chat Multiusuario con GUI y Cifrado E2E (1/5)**

1. **Introducción**

	Nos enfocaremos en construir un chat multiusuario desde cero, utilizando conceptos avanzados como threading y socket para gestionar la comunicación en tiempo real. Se empleará Tkinter para crear una interfaz gráfica intuitiva, permitiendo a varios usuarios conectarse y conversar de manera efectiva.

	Aprenderemos cómo estas herramientas pueden ser integradas para desarrollar una aplicación de chat robusta y funcional, explorando tanto la programación de back-end como de front-end para una experiencia de usuario completa.

	</br>
2. **Práctica**

	**IMPORTANTE:**
	Recordemos que para ejecutar el cliente, tendremos que tener siempre corriendo el servidor, además cada que se realicen cambios en uno u otro, se tendrá que cerrar y volver a ejecutar para que se carguen los cambios.

	Para este chat multiusuario, estaremos creando dos scripts, uno para el servidor y uno para el cliente. El servidor estará continuamente en escucha para conexiones entrantes, todo será totalmente establecido en la red local, pero si quisiéramos que funcione fuera de nuestra red local, tendríamos que alojar nuestro script del servidor en algún vps público para que cualquier cliente pudiese establecer una conexión.

	Toda la parte de nuestra interfaz gráfica estará del lado del cliente, ya que el servidor estará operando las conexiones, no requerirá realmente de una.

	En el cliente, tendremos en cuenta que cuando un cliente entre le aparece en el momento el cliente que se haya conectado al resto de clientes conectados, así como cuando este se desconecte. Además, manejaremos un campo donde se verán todos los mensajes de los distintos clientes, así como para enviar mensajes e incluso un campo donde al presionar un botón nos pueda listar los clientes.

	**server.py**

	Este será el script que se encargue de gestionar y actualizar en todo momento las conexiones de los clientes.

	Para nuestro servidor, iniciaríamos importando la librería **socket**, ya que vamos a entablar conexiones, así como la librería **threading** para la gestión de múltiples usuarios.

	Para todo el lado de nuestro servidor, definiríamos una función **server_program** la cual solo se ejecutara si el script es ejecutado directamente:

	![[IMG_1106.png]]

	Comenzaríamos creando nuestro socket, donde como primer argumento indicamos que trabajaremos con la familia de direcciones *IPv4*, mientras que, como segundo argumento, indicamos que trabajaremos mediante TCP:

	![[IMG_1107.png]]

	Además, utilizaremos la propiedad *setsockopt*, donde en el nivel **SOL_SOCKET** cambiaremos la propiedad **SO_REUSEADDR** a **1** para que nos reutilice el mismo puerto en caso de que la conexión se cierre y se abra rápidamente, ademas indicaremos el host y puerto al inicio:

	![[IMG_1108.png]]

	Ahora estaremos inicializando el servidor con **bind**, pasándole mediante una tupla el host y el puerto donde se inicializará, para después ponernos en escucha con *listen*.

	Finalmente, colocaremos un mensaje que se mostrará en la terminal, para en todo momento saber en qué parte del código vamos. Así, en caso de presentarse un error, tendremos un poco la idea de por dónde se dio:

	![[IMG_1109.png]]

	Como en todo momento deseamos gestionar a los clientes e incluso saber qué usuario es el que está conectado, para ello crearemos una lista *clients* que será una lista de sockets y un diccionario *usernames*, donde la llave será un socket de usuario y el contenido, el nombre de usuario.

	Además, mediante un bucle infinito vamos a estar recibiendo las conexiones de los clientes, donde con *accept* recibimos su socket y su address, almacenaremos el socket en la lista de clientes.

	Finalmente, mostraremos un mensaje de la conexión que se ha generado, mostrando por la terminal el addr, a manera de confirmación para nosotros (recordemos agregar la *f* para que muestre bien la variable):

	![[IMG_1110.png]]

	De esta manera, ahora visualizamos si generamos una conexión al servidor:

	![[IMG_1111.png]]

	Con esto listo, ahora crearemos un nuevo hilo, donde como argumentos le pasaremos una función como target, la cual será *client_thread* para gestionar cada cliente, como segundo argumento con la propiedad *args* asignaremos los argumentos que le pasaremos, que serán el socket del cliente, la lista de sockets de cada cliente y el diccionario de los nombres de usuario.

	Luego, antes de inicializar el hilo colocaremos la propiedad *daemon* y le asignaremos el valor de *True*, lo cual nos sirve como una forma de asegurar que una vez se finalice la ejecución principal, que sería la función *server_program* en este caso, se asegure el cierre de todos los hilos, sin que nos de problemas de que se queden en ejecución y, por lo tanto, no podamos cerrar el servidor y se nos quede en un estado de espera.

	Finalmente, inicializamos el hilo con *start()* y en nuestra función para gestionar el hilo del cliente, por lo pronto solo definiremos un mensaje para mostrar en terminal, para verificar que todo esté funcionando correctamente.

	![[IMG_1112.png]]

	![[IMG_1113.png]]

	Además, como buena práctica recordemos que tendremos que agregar el método especial *close()* para nuestro socket del servidor, el cual irá después de nuestro bucle. Es posible que no siempre lleguemos al punto que corresponda a cerrar correctamente el socket, pero como buena práctica recordemos siempre agregarlo:

	![[IMG_1114.png]]

	De esta manera, ya tendremos clientes separados donde, en nuestra función *client_thread* definiremos lo que deseamos que suceda para cada cliente de forma individual.

	Antes de empezar a definir del lado del servidor lo que sucedera para cada cliente, crearemos nuestro script para el cliente, que será donde se requerirá de la interfaz gráfica.

	**Client**

	Empezaremos definiendo que nuestra función principal *client_program* se ejecute solamente si el script es ejecutado directamente, así como colocando el host y puerto correspondientes a la dirección del servidor al que nos conectaremos y definiriamos el socket del cliente de la misma manera:

	![[IMG_1115.png]]

	Con esto listo, estableceríamos la conexión con el servidor, luego la parte donde se solicitará el nombre de usuario por consola y será lo primero que se enviará al servidor:

	![[IMG_1116.png]]

	Esto se utilizará del lado del servidor, para mostrarle a los demás usuarios conectados, el usuario que se ha conectado.

	Ahora, del lado del servidor, para cada cliente recibiremos el nombre de usuario y en el diccionario, utilizando el socket del cliente como llave, almacenaremos el nombre de usuario enviado por el usuario y mostrando finalmente el contenido del diccionario:

	![[IMG_1117.png]]

	De esta manera, al inicializar el servidor y conectarnos con el script del cliente múltiples veces, obtendremos el siguiente funcionamiento:

	![[IMG_1118.png]]

	De esta manera, del lado izquierdo en cada posición visualizamos todo el socket del cliente y del lado del valor visualizamos el nombre de usuario para ese cliente.

## **Chat Multiusuario con GUI y Cifrado E2E (2/5)**

1. **Práctica**

	Si quieramos mostrar un mensaje como el que se le mostrara a todos los usuarios una vez tengamos nuestra interfaz gráfica, del lado del servidor podríamos mostrar que cierto usuario se ha conectado:

	![[IMG_1120.png]]

	![[IMG_1119.png]]

	Del lado del cliente concluye todo al colocar el nombre de usuario, esto sucede porque aún no estamos gestionando nada del lado del cliente.

	En nuestro script para el cliente, primeramente vamos a importar todo lo necesario, en lugar de importar la librería tkinter, nos vamos a traer todo lo de la librería para referenciarlo directamente, también importaremos la librería threading para utilizar hilos y del módulo *scrolledtext* de la librería tkinter, nos traeremos la clase *ScrolledText*, que servirá para utilizar el scroll del mouse.

	![[IMG_1121.png]]

	Con esto, ahora en nuestra función para el socket del cliente, continuaríamos definiendo nuestra ventana como *window*, le asignamos un título, colocamos el mainloop para que permita la interacción dinámica de los widgets y finalmente colocamos la instrucción de finalizar el socket del cliente, para cuando se deje de utilizar la aplicación:

	![[IMG_1122.png]]

	En este caso, al utilizar el contenido de la librería tkinter ya no tendremos que referenciarlo utilizando *tkinter.Tk()* o *tk.Tk()*, lo cual se debe a que hemos importado directamente cada cosa de la librería y es como ya tenerlo dentro de nuestro documento, lo que nos permite una referenciación directa.

	Ahora utilizaremos el widget *ScrolledText* y lo almacenaremos en la variable *text_widget*, como argumento le daremos la ventana en la que se mostrara y después lo mostraremos con *pack()*:

	![[IMG_1123.png]]

	Esto nos genera y muestra un widget similar al de *Text*, con la diferencia de que cuenta con un scroll:

	![[IMG_1124.png]]

	Nos permite escribir, pero existe una propiedad que podremos cambiar, la cual es *state*, esta la podremos cambiar en un inicio al crearlo, o después de crearlo, utilizando el método *configure* sobre el widget, podremos cambiar configuraciones.

	Le podríamos dar el valor de *disable* a *state* y esto hará que el widget tenga un estado en el que no nos deje realizar cosas sobre el:

	![[IMG_1125.png]]

	De esta manera el usuario no podrá colocar contenido y siempre que se quiera representar algún contenido se tendrá que cambiar la propiedad *state* para ese widget a *normal*. Esto viene bien, si lo consideramos el apartado donde se mostraran los mensajes de todos los usuarios.

	Para no observar el contenido del scrolltext tan pegado a los margenes, generaremos un padding en ambos ejes de 5 píxeles.

	Además, agregaremos un widget *Entry* para que el usuario pueda escribir sus mensajes, lo definiremos para nuestra ventana principal. Lo mostraremos con pack y le aremos un padding de 5 píxeles en ambos ejes y agregaremos un *fill* que recordemos que nos sirve para darle un tamaño a nuestro widget con respecto a un eje, pero lo haremos para ambos con *BOTH*:

	![[IMG_1126.png]]

	Con esto tendremos nuestra aplicación con una vista similar a la siguiente:

	![[IMG_1127.png]]

	Con esto listo, ahora configuramos que al nosotros escribir algo nos lo muestre en el *Scroll Text* y se borre de nuestro *entry*, ya que es  un envío.

	Ahora asociaremos con *bind* para reconocer un evento de teclado dentro de nuestro widget Entry, a la tecla de Enter (Return). Una vez se reconozca que se ha presionado esta tecla agregaremos a la función que se llamara, pero recordemos que para que no se llame al ser asignado tendremos que utilizar una función lambda.

	Como del propio *bind* automáticamente recibimos un evento, tendremos que colocarlo el inicio para considerarlo en la función lambda, de lo contrario nos dará error. Además, lo pasaremos como argumento principal a la función *send_message()* que se ejecutara, como otros argumento que serán *client_socket*, *username*, *text_widget*, *entry_widget*, para realizar lo del mensaje de forma local, así como realizar el envío hacia el servidor.

	![[IMG_1128.png]]

	Con esto, tendríamos que generar la función con todos los parámetros que recibirá en la parte superior, a manera de comprobación haremos que en terminal nos muestre un mensaje, para verificar su funcionamiento:

	![[IMG_1129.png]]

	Vemos que funciona correctamente, con esto ahora la idea será que el mensaje se borre de nuestro entry y aparezca en el scrolltext, además de realizar el envío.

	A manera de prueba recuperaremos el mensaje de nuestro *Entry* y lo mostraremos en la terminal:

	![[IMG_1130.png]]

	![[IMG_1131.png]]

	Con la recolección del mensaje en mente, entonces lo que tendríamos que hacer es enviarlo al servidor a nivel de socket, ya que este cuenta con la lista de todos los clientes a los cuales tendrá que enviarles el mensaje.

	Enviaremos al servidor el mensaje en un formato *username > message*, así como eliminaremos el mensaje de nuestro entry:

	![[IMG_1132.png]]

	Ahora haremos que nos muestre el mensaje en nuestro mismo chat, por lo tanto, tendremos que cambiar la propiedad *state* del scrolledtext para que nos permita escribir, escribiremos el mensaje siempre al final para que se vea a como estamos acostumbrados en los chats y finalmente volveremos a colocar el *state* en *disable*:

	![[IMG_1133.png]]

	De esta manera, de forma local la estaremos mostrando el mensaje que enviemos al servidor:

	![[IMG_1134.png]]

	Ahora, del lado del servidor tenemos una forma de comunicarnos con cada uno de los clientes, por ello lo primero que haremos será enviar un mensaje a todos para indicarle a cada usuario cuando un usuario nuevo se haya conectado:

## **Chat Multiusuario con GUI y Cifrado E2E (3/5)**


1. **Práctica**

	Ahora, del lado del servidor, una vez se conecte un nuevo cliente, gestionaremos que se envíe un mensaje indicando el usuario que se ha conectado al chat.

	Este mensaje tendrá que ser enviado a todos los usuarios y recordemos que tenemos almacenados los sockets de todos en una lista, por lo que solo tendremos que definir una iteración sobre todos y que no realice nada cuando el socket sea el del mismo cliente que ha entrado, para que este nos vea el propio mensaje de que se ha conectado.

	![[IMG_1135.png]]

	Como el servidor envía este mensaje, tendremos que recibirlo del lado del usuario, para ello crearemos la función *receive_message*, con la cual utilizaremos hilos y colocaremos entre las definiciones de nuestra aplicación, para que se esté ejecutando continuamente en espera de mensajes, además de la misma manera que en servidor, asignaremos el valor de *True* a la propiedad *daemon* de nuestro hilo.

	![[IMG_1136.png]]

	Nuestra función recibe como argumentos el propio socket de cliente para recibir el mensaje y el *text_widget* para escribir el mensaje y el usuario pueda verlo.

	Por ello, en nuestra función vamos a utilizar una excepción dentro de un bucle infinito por posibles problemas de conexión, donde si se da un problema de conexión, pues se terminara la ejecución del bucle. En cuanto al *try*, recibiremos el mensaje y si este tiene contenido mostraremos el mensaje cambiando los estados del widget para el texto de los mensajes, de lo contrario terminaremos el bucle:

	![[IMG_1137.png]]

	De esta manera, al conectar distintos clientes veremos como nos salta el mensaje de los usuarios que van ingresando:

	![[IMG_1138.png]]

	Ahora, si intentamos enviar algún mensaje, veremos como estos solo se nos muestran de forma individual y no son enviados al resto de usuarios, esto es porque aún no definimos que el servidor envíe este mensaje a todos los demás clientes:

	![[IMG_1139.png]]

	Por ende, ahora lo que tendremos que definir del lado de nuestro servidor es que una vez haya enviado el mensaje de que ha ingresado un nuevo usuario, se inicie un bucle infinito que este continuamente en escucha en espera de mensajes, para enviarlo al resto de usuarios que no sean el usuario que lo ha enviado:

	![[IMG_1140.png]]

	Y como el cliente ya tiene definido el cómo recibirá los mensajes, ya funcionara todo el envío de mensajes de forma correcta:

	![[IMG_1141.png]]

## **Chat Multiusuario con GUI y Cifrado E2E (4/5)** 

1. **Práctica**
	**client.py**

	Ahora gran parte de la lógica ya se encuentra definida, por ello nos enfocaremos más en la parte del cliente para mejorar la estética de nuestra aplicación.

	Primeramente, nos enfocaremos en agregar un botón de enviar, el cual se encuentre a un lado de nuestra entrada de texto para enviar el mensaje como usuario, si simplemente agregáramos el botón, se colocaría debajo:

	![[IMG_1142.png]]

	![[IMG_1143.png]]

	De esta forma vemos como nuestro botón se coloca debajo de nuestro entry, esto se debe a que para que nos lo represente como esperamos tendremos que colocarlos dentro de un mismo frame, así como indicarle al entry que tendrá que estar colocado a la izquierda y nuestro botón a la derecha.

	Primeramente, crearemos el frame y le daremos las medidas que tenía nuestro entry, para visualizar que tome esta forma, debido a que no se muestra nada hasta que tiene contenido, le daremos un color de fondo:

	![[IMG_1144.png]]

	Con esto en la aplicación solo veríamos una línea muy delgada del color seleccionado, por ello asignaremos el entry en el frame y lo colocaremos del lado izquierdo con la propiedad *side*:

	![[IMG_1145.png]]

	En nuestro entry, lo que hacemos es colocarlo a la izquierda y permitir que el tamaño se adapte en ambos ejes, permitiendo más allá del límite propio debido a que si no lo colocamos lo veremos muy pequeño en el eje X.

	Nuestro botón lo colocamos del lado derecho, con un padding de 5 píxeles del lado izquierdo en el eje X para que no quede pegado al entry:

	![[IMG_1146.png]]

	Con esto ya lo tendríamos, solo faltaría eliminar el fondo que colocamos para el frame y agregarle el command a nuestro botón, el cual se aprovechara de la misma función que se ejecuta al presionar el *Enter*:

	Como reutilizaremos la función *send_message* y en esta realmente no utilizamos el evento que nos retorna bind, entonces recordemos que para ignorar o no tomar en cuenta un parámetro en una función lambda, tendremos que colocar un *\_* en su lugar, con lo cual podríamos quitarlo de la función y del llamado a la función, para reutilizarla en nuestro botón:

	![[IMG_1147.png]]

	De esta manera, ya tendríamos el funcionamiento esperado para el botón también y, por lo tanto, enviará el mensaje con el enter o con presionar el botón.

	*Listar usuarios*

	Ahora en la parte inferior agregaríamos un botón para listar a todos los usuarios que se encuentren en línea, para ello como command utilizaremos una función que crearemos la cual será *list_users_request*, donde como argumento pasaremos el socket, ya que con este podremos comunicarnos con el servidor, para enviarle un mensaje el cual sea *\!usuarios*:

	![[IMG_1148.png]]

	![[IMG_1149.png]]

	Con esto, del lado del servidor, al recibir específicamente el mensaje *\!usuarios*, enviaremos de regreso a ese cliente en específico un mensaje con la lista de usuarios conectados:

	![[IMG_1150.png]]

	Una vez es enviado el mensaje de los usuarios al cliente, se aplica un *continue* para que regrese a la espera de más mensajes y no proceda a enviarle el mensaje *!usuarios* al resto de clientes.

	De esta manera, ya podríamos visualizar las personas que se encuentran conectadas:

	![[IMG_1151.png]]

	Aunque, por el momento solo se almacena cuando un cliente entra, pero si alguno sale ya no es eliminado, por ende al cerrar la aplicación de un cliente y solicitar nuevamente los usuarios, veremos que siguen saliendo los mismos usuarios activos:

	![[IMG_1152.png]]

	Aquí es donde podremos aprovecharnos del *try*, ya que si un usuario sale automáticamente entraría en la excepción indicando un error de comunicación al estar en espera de un mensaje y por ende, fuera del bucle eliminaríamos a este usuario de la lista, así como del diccionario.

	Para hacer esto correctamente, primeramente crearemos un botón que nos ayude a controlar el flujo de salida, el cual será *exit_widget* y llamará a la función *exit_request* la cual recibirá como argumento el socket del cliente para con este controlar el flujo de salida, donde ademas le enviara al cliente el nombre del usuario para enviar un mensaje indicando que lo ha abandonado, asi como la ventana para aplicarle un *quir* y un *destroy* para asegurar que todos los procesos terminen correctamente:	

	![[IMG_1153.png]]

	Por lo tanto, en nuestra función *exit_request* lo que haremos será enviar un mensaje para el servidor indicando que usuario ha salido del chat, luego cerraremos nuestro socket como cliente y finalmente cerraremos correctamente la ventana, lo cual terminará con todos los procesos hijos, en este caso los hilos.

	![[IMG_1154.png]]

	Finalmente, del lado del servidor, al cerrar el socket desde el lado del cliente, pues se generara un problema de comunicación con este cliente, por ende entrara a la excepción y terminara de estar en escucha, por lo que podremos desde el lado del servidor cerrar el socket de este cliente y finalmente eliminar tanto de la lista el socket de este cliente, como del diccionario, de esta manera actualizaremos la lista de usuarios conectados, así cada que se realice esta consulta ahora si saldrán únicamente los activos:

	![[IMG_1155.png]]

	De esta manera, al entrar múltiples usuarios, platicar y salirse, todo se actualizará automáticamente y veremos como podremos consultar los usuarios activos:

	![[IMG_1156.png]]

	El único problema visual son los saltos de línea, pero esto se arregla editando como enviamos y mostramos el mensaje.

	**Visualizar el contenido más reciente del chat**

	Para visualizar el contenido más reciente del chat cada que enviemos un mensaje, para ello podremos utilizar la propiedad *text_widget.see(END)* y como vemos le asignamos como argumento que se enfoque en el final, de esta manera cada que enviemos un nuevo mensaje, se enfocará en mostrarnos lo más reciente de la conversación:

	![[IMG_1160.png]]

	De esta manera, al tener muchos mensajes en el chat, ahora podremos visualizar siempre la conversación actual al enviar nuevos mensajes:

	![[IMG_1161.png]]

	**Hilos en modo daemon**

	Si  recordamos, al momento de crear los hilos colocamos la propiedad *daemon* y la seteamos a *True*. Esta nos sirve para indicar que absolutamente todos los procesos hijos dependan totalmente de la función que los ejecuta, por ende si finaliza la ejecución, los hilos terminarán y se terminará de ejecutar completamente el programa.

	Si no colocáramos esta opción, los hilos serían como procesos independientes, por lo que al salir de la aplicación aún se quedarían en segundo plano, terminando posiblemente en un error al ya no contar con el resto de la funcionalidad:

	![[IMG_1157.png]]

	En este caso la línea que define que el hilo sea dependiente de un proceso padre (la propia función que lo ejecuta) fue comentada, por lo que ahora cada hilo será tratado como si de un proceso independiente se tratase del lado del cliente, entonces ahora al ejecutar el programa y buscar cerrarlo, veremos como a pesar de que la ventana si se cierra se queda mediante la terminal esperando, debido a que aún quedan los hilos corriendo:

	![[IMG_1158.png]]

	Y si activamos el hilo en modo *daemon*, veremos como todo se finaliza correctamente:

	![[IMG_1159.png]]

## **Chat Multiusuario con GUI y Cifrado E2E (5/5)**

1. **Introducción**

	Esta es la etapa final para nuestro chat multiusuario, por ende nos enfocaremos en la seguridad y privacidad de las conversaciones. Utilizaremos la librería SSL y herramientas como OpenSSL para implementar un cifrado robusto.

	Aprenderemos como integrar estas tecnologías en nuestro chat para asegurar que las comunicaciones entre usuarios sean seguras y privadas. Esta sesión es crucial para entender la importancia del cifrado en aplicaciones de mensajería y como aplicarlo efectivamente en aplicaciones reales.

	Lo siguiente son los comandos utilizados a lo largo de la generación del cifrado:

	- **openssl genpkey \-algorithm RSA \-out server\-key.key \-aes256**

		Esta instrucción genera una nueva clave privada RSA. La opción *\-algorithm RSA* especifica el uso del algoritmo RSA. *\-out server-key.key* indica que la clave generada se guardara en un archivo generado llamado *server-key.key*. La opción *\-aes256* significa que la clave privada será cifrada utilizando el algoritmo AES \-256, lo que añade una capa de seguridad al requerir una contraseña para acceder a la clave.

	- **openssl rew \-new \-key server-key.key -out server.csr**

		Esta línea crea una Solicitud de Firma de Cifrado (CSR) utilizando la clave privada RSA que generaste *\-new* indica que se trata de una nueva solicitud, *\-key server-key.key* especifica que se usara la clave privada almacenada en *server-key.key*, y *\-out server.csr* guarda la CSR generada en un archivo llamado *server.csr*. La CSR es necesaria para solicitar un certificado digital a una autoridad certificadora (CA).

	- **openssl x509 \-req \-days 365 \-in server.csr \-signkey server\-key.key \-out server-cert.pem**

		Este comando genera un certificado autofirmado basado en la CSR. *\-req* indica que se está procesando una CSR. *\-days 365* establece una valides de certificado por un año, *\-in server.csr* especifica la CSR de entrada, *\-signkey server\-key.key* utiliza la misma clave privada para firmar el certificado, y *\-out server\-cert.pem* guarda el certificado generado en un archivo llamado *server\-cert.pem*.

	- **openssl rsa \-in server\-key.key \-out server\-key.key**

		Este comando se utiliza para quitar la contraseña de una clave privada RSA protegida. *\-in server\-key.key* especifica el archivo de clave privada cifrada como entrada, y *\-out server\-key.key* indica que la clave privada sin cifrar se guardara en el mismo archivo. Al ejecutar este comando, se pedirá la contraseña actual de la clave privada. Una vez proporcionada, OpenSSL generara una versión sin cifrar y la guardara en el mismo archivo, sobreescribiendo la versión cifrada.

		Este paso se hace a menudo para simplificar la automatización en entornos donde ingresar una contraseña manualmente no es práctico. Sin embargo, es importante ser consciente de que al eliminar la contraseña, la clave privada se vuelve más vulnerable al acceso no autorizado.
	</br>
2. **Práctica**

	Primeramente, recordemos que alguien como intermediario puede tratar de interceptar las conversaciones, por ende nuestros mismos podríamos ponernos en escucha con *tshark* o *wireshark*, por ende si establecemos la comunicación entre dos clientes con nuestro chat multiusuario, y ejecutamos el siguiente comando en otra ventana:

	```bash
	tshark -i lo -Tfields -e data.data  
	```

	![[IMG_1162.png]]

	Con esto listo, ya tenemos tshark en escucha para interceptar los mensajes que enviemos, estos nos saldrán en hexadecimal:

	![[IMG_1163.png]]

	Por ende, al convertir este mensaje de hexadecimal a un formato legible, estaríamos viendo el mensaje que hemos enviado:

	![[IMG_1164.png]]

	Por lo tanto, es posible interceptar la comunicación de nuestra aplicación, por ahora.

	Para evitar esto tendremos que seguir una serie de pasos, para ello utilizaremos *OpenSSL*, donde tenemos que seguir una serie de pasos.

	**Crear clave privada**

	```bash
	openssl genpkey -algorithm RSA -out server-key.key -aes256
	```

	Con el comando anterior, lo que estamos haciendo es crear una clave privada, la cual se crea empleando el algoritmo RSA, la cual se almacenara como server-key.key y para crearla nos solicitara colocarle una contraseña:

	![[IMG_1165.png]]

	Aquí colocaremos la contraseña que nosotros queramos y ya la veremos creada:

	![[IMG_1166.png]]

	**Solicitud de forma de certificado (CSR)**

	Luego de crear nuestra key, la idea será generar una solicitud de forma de certificado, para lo cual utilizaremos el siguiente comando:

	```bash
	openssl req -new -key server-key.key -out server.csr
	```

	Para generar el certificado dependeremos de la clave que ya le hemos asignado y la pedirá primeramente, para el resto de información podríamos solo darle al enter hasta que termine, sin rellenar nada:

	![[IMG_1167.png]]

	Ahora mismo ya tendríamos nuestro archivo csr y la clave privada, en este punto ya podríamos crear un certificado autofirmado, que sería el que vamos a estar utilizando.

	**Certificado autofirmado**

	```bash
	openssl x509 req -days 365 -in server.csr -signkey server-key.key -out server-cert.pem
	```

	De esta forma estaríamos creando un certificado autofirmado, donde le damos una valides de un año, pasándole nuestro archivo CSR, la clave privada y almacenándolo como out en *server\-cert.pem*.

	Ahora esto dependería de la contraseña que le hemos asignado a nuestra clave privada y por ende ya tendríamos todo lo que necesitamos:

	![[IMG_1168.png]]

	Con lo que tenemos hasta ahora, el servidor podría iniciar y tendríamos que estar colocando de forma continua la contraseña, para que esto no sea necesario tendríamos que ejecutar el comando:

	```bash
	openssl rsa -in server-key.key -out server-key.key
	```

	Lo que este último comando hace es tomar la clave privada y almacenarla con el mismo nombre, por lo tanto, la sobreescribe para que ya no sea necesario estar proporcionando continuamente la contraseña en nuestro servidor, pero para realizar esto si nos pedirá la contraseña:

	![[IMG_1168.png]]

	**Encriptación de las comunicaciones**

	Ahora estos archivos o recursos siempre tendrán que estar en la misma carpeta/directorio, porque ahora tendremos que indicarle al servidor que opere por SSL, por lo que tendremos que importar la librería *ssl* en nuestro sevidor:

	![[IMG_1170.png]]

	Por ende, ahora en nuestro servidor justo después de utilizar el *bind* con nuestro socket de servidor, tendremos que utilizar la siguiente acción:

	```python
	server_socket = ssl.wrap_socket(server_socket, keyfile="server-key.key", certfile="server-cert.pem", server_side=True)
	```

	Con esto le estamos indicando a nuestro socket que queremos manejar una comunicación encriptada, donde como primer argumento pasamos el propio socket del servidor, después el archivo de nuestra clase privada, para después pasar el certificado autofirmado.

	![[IMG_1173.png]]

	Esto sería a nivel de servidor, a nivel de cliente ahora tendríamos que importar la misma librería:

	![[IMG_1171.png]]

	Por ende, ahora antes de realizar la conexión con el servidor le indicaremos a nuestro socket la misma acción para indicarle que vamos a trabajar con ssl para tener una comunicación cifrada, pasando como único argumento nuestro propio socket de cliente:

	![[IMG_1172.png]]

	Aquí se ha utilizado *ssl.wrap_socket*, pero para una mayor seguridad puede ser mucho mejor utilizar *ssl.SSLContext.wrap_socket()*.

	**Mensajear con el cifrado**

	Si ahora con todo listo ejecutamos el servidor y conectamos dos clientes para que interactúen, veremos como se reciben y envían los mensajes correctamente:

	![[IMG_1174.png]]

	Ahora si nos pusiéramos de nuevo en escucha con *tshark* con el comando:

	```bash
	tshark -i lo -Tfields -e data.data
	```

	Recordando que como usuario con privilegios *root*.

	Por ahora, al enviar mensajes y luego ver lo que recogió *tshark* veríamos lo siguiente:

	![[IMG_1175.png]]

	![[IMG_1176.png]]

	No vemos que reciba nada, pero esto puede ser porque la comunicación se esté dando, por un lado, distinto, por ende ahora utilizaremos el comando para ver en formato json por cuál es y enviaremos un mensaje largo para visualizarlo correctamente:

	```bash
	tshark -i lo -Tjson
	```

	Por ende podremos enfocarnos en *payload*, que parece ser que es donde está el mensaje, solo tendríamos que quitarle los puntos e intentar convertirlo de hexadecimal a un formato legible:

	![[IMG_1177.png]]

	![[IMG_1178.png]]

	Y resulta que ahora no es legible. Obtendríamos este mismo resultado si intentáramos visualizar el contenido de *app_data* de lo que se recogió con *tshark*.

	Así que ahora está finalizado nuestro chat multiusuario con interfaz gráfica y lo más importante, cifrado para quela conversación no pueda ser interceptada.

[[#Índice]]

## **Siguientes apuntes**

[[Creando un escáner de puertos (1-4)]]