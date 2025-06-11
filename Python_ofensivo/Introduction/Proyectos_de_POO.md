
## **Índice**

- [[#Proyecto de gestión de biblioteca de libros (1/2)]]
- [[#Proyecto de gestión de biblioteca de libros (2/2)]]
- [[#Proyecto de gestión de animales en tienda]]
- [[#Proyecto de administración de flota de vehículos]]
- [[#Proyecto de gestión de notas (1/2)]]
- [[#Proyecto de gestión de notas (2/2)]]
- [[#Siguientes apuntes]]


## **Proyecto de gestión de biblioteca de libros (1/2)**

1. **Introducción**

	En este proyecto inicial, se desarrollara un sistema de gestión para una biblioteca.

	Este sistema nos permitirá agregar nuevos libros a la biblioteca y gestionar el préstamo de estos. A través de la creación de este sistema, aplicaremos de manera práctica los fundamentos de la Programación Orientada a Objetos (POO), haciendo especial énfasis en conceptos clave como herencia y polimorfismo. Diseñaremos clases para representar diferentes aspectos de una biblioteca, como libros, miembros y transacciones de préstamo.
	</br>
2. **Práctica**

	*Shebang:*

	Primero comenzaremos creando un archivo y colocando nuestro shebang para que en todo momento el propio script indique con qué lenguaje debe ejecutarse en caso de que no se indique directamente al ejecutarse:

	![[IMG_577.png]]

	*Comprobación del módulo y contemplación del objeto:*

	Recordemos que con la variable que ya nuestro módulo tiene contemplada *\_\_name\_\_*, podremos comprobar si el script o módulo se está ejecutando directamente, y aquí definiremos las cosas que haremos, porque de no ser el script que se ejecute directamente no debería efectuarse nada.

	Entonces aquí, además, contemplaremos nuestra instancia de la clase *Libro* que estaremos creando y a esta tendremos contemplado pasarle como argumentos id (identificador del libro), autor (nombre del autor) y título (título del libro). Trataremos que, conforme se creen instancia, el identificador sea incremental, por lo que deberá ir aumentando en uno.

	![[IMG_578.png]]

	*Creación de la clase:*

	Con esto en mente crearíamos nuestra clase *Libro*, así como su constructor, que deberá tener los parámetros *id_libro*, *autor*, *nombre_libro* y, al estar en el constructor, deberemos asignarle los atributos a nuestro objeto.

	Además, pensando en la posibilidad de prestar libros que le asignaremos, más que asignarlo como parámetro en nuestro constructor, directamente vamos a crear el atributo y asignarle un valor booleano *False*, ya que al inicio ningún libro estará prestado.

	![[IMG_579.png]]

	*Método \_\_str\_\_:*

	A nivel de representación de nuestro objeto para una cadena de texto, utilizaremos este método especial, para al querer mostrarlo directamente con un *print()*, nos dé la información correspondiente:

	![[IMG_580.png]]

	De esta manera, nos regresaría la información en forma de una cadena de texto que hemos seteado de esta manera, para que se muestre como cuando creamos un objeto.

	*Clase Biblioteca:*

	Ahora, los libros son almacenados o están en una biblioteca, por lo que debajo de nuestra clase *Libro*, crearemos nuestra clase *Biblioteca*, de la que en su constructor definiremos un diccionario el cual almacenara todos los libros que estén disponibles en la biblioteca, por lo que no deberán de estar prestados.

	Nuestro constructor no recibirá ningún argumento e inicializaremos un diccionario vacío, en el cual tendremos en mente que le meteremos un identificador  como clave y el propio libro (objeto) como valor.

	Además, tendremos en mente la creación de nuestra instancia de la clase *Biblioteca*, antes de crear los libros:

	![[IMG_581.png]]

	Teniendo en cuenta la estructura que tendremos para el almacenamiento de los libros, consideraremos el método *agregar_libro*, por lo que tendremos que crearlo.

	Por lo que lo definiremos de la siguiente forma:

	![[IMG_582.png]]

	De esta manera, tengamos en cuenta que con *self* hacemos referencia al propio objeto *biblioteca*, el cual es una instancia de nuestra clase *Biblioteca* y por ello como argumento le pasamos nuestra instancia de la clase *Libro*.

	Para agregar un nuevo libro, lo que haremos será primeramente definir una condición, ya que solo agregaremos el libro si este no se encuentra en nuestra librería, por ende verificaremos si nuestro libro no se encuentra en la biblioteca, con el identificador del mismo libro:

	![[IMG_583.png]]

	De esta manera, una vez verifiquemos que este libro no esté en la biblioteca, quiere decir que podremos almacenarlo y, por ende lo almacenaremos.
	En caso de no poder almacenar el libro porque ya esté existente, retornaremos un mensaje por pantalla.

	![[IMG_584.png]]

	Ahora, para poder ver en algún momento los libros que se encuentran en la biblioteca, entonces definiremos un método que nos los mostrará, pero en este utilizaremos el decorador *@property* para no utilizar los paréntesis al llamarlo.

	Para realizar esto, vamos a hacerlo con una lista de comprensión, en la cual cuál iteraremos sobre todos los valores del diccionario (donde están los objetos de cada libro) y vamos a retornar el objeto solamente si el atributo *esta_prestado* es falso, ya que esto querrá decir que el libro no está prestado y por ende está físicamente en la biblioteca:

	![[IMG_585.png]]

	Con esto definido podremos ejecutar nuestro método:

	![[IMG_586.png]]

	Aquí nos muestra la información del objeto. Recordemos que esto sucede, ya que a nivel de representación cuando un objeto está dentro de otros tipos de datos, para que nos represente información tenemos el método especial *\_\_repr\_\_*, por lo que tendremos que definirlo en nuestra clase *Libro*.

	Aquí aprovechando que ya tendríamos una forma de mostrar la información con *\_\_str\_\_*, pues llamaríamos a la función para reutilizarla y tendría el mismo efecto, pero ahora para representarlo para listarlo de esta manera:

	![[IMG_587.png]]

	Finalmente, como código y resultado tendríamos:

	![[IMG_588.png]]

	![[IMG_589.png]]

## **Proyecto de gestión de biblioteca de libros (2/2)**

Continuamos avanzando en nuestro emocionante primer proyecto en Python, el desarrollo de un sistema de gestión de biblioteca. Esta fase del proyecto nos permitirá profundizar en las funcionalidades que hemos comenzado a construir. Nos enfocaremos en perfeccionar las características existentes y en añadir nuevas funcionalidades.


1. **Práctica**

	*Método prestar_libros:*

	Para prestar libros, lo que haremos es pasarle como argumento a nuestro método de la instancia de nuestra clase *Biblioteca* el id del libro que queremos prestar.

	La lógica de nuestro método sería realizar 2 validaciones, una donde verifiquemos si el id del libro está existente y a su vez verificar que este no haya sido prestado. De ser el caso, el atributo *esta_prestado* lo colocaremos en *True*. De lo contrario, lanzaremos un mensaje de que el libro no se puede prestar. Esto se debe a que esta ya se encuentre prestado o simplemente no exista, gracias a las validaciones que realizamos.

	![[IMG_590.png]]

	Por ende, al colocar que nos muestre los libros existentes y que no han sido prestados, luego prestar uno y volver a mostrarlos, veríamos lo siguiente:

	![[IMG_591.png]]

	*Listar libros prestados:*

	Para listar los libros prestados, nos aprovecharemos del método con el decorador *@property* que ya generamos y  lo modificaremos para que nos muestre todos los libros que en su atributo *esta_prestado* tengan *True*:

	![[IMG_592.png]]

	![[IMG_593.png]]

	*Clase BibliotecaInfantil:*

	Ahora implementaremos la posibilidad de tener una biblioteca infantil, por lo que crearemos la clase *BibliotecaInfantil*. Esta funcionaria en conjunto con nuestra clase *Biblioteca* al ser una herencia de esta misma.

	Vamos a sobreescribir el constructor para crear un nuevo diccionario donde, con base en el libro, con su ID, almacenaremos como valor un *True* si es un libro infantil o un *False*, si no es un libro infantil. Pero desde luego requerimos de que  en esta clase esté funcionando correctamente el almacenamiento de los libros, por lo que con el uso de *super()* llamaremos al mismo método de la clase base.

	![[IMG_594.png]]

	Hasta aquí tendríamos todo bien, pero tendríamos que modificar algunos métodos para, por ejemplo, primeramente recibir si el libro es infantil o no al momento en el que se almacena.

	Definiremos para la clase *BibliotecaInfantil* el método *agregar_libro*. En este, además de recibir como argumento el libro, también recibiremos un estado que será *True* o *False*, dependiendo si es para niños o no. Llamaremos al método *agregar_libro* de la clase base, para que esta se encargue de agregar este libro y lo siguiente que haremos será en el diccionario que nuestro constructor crea para esta clase agregar como llave el ID del libro y como valor el *True* o *False* que indica si es un libro para niños o no.

	![[IMG_595.png]]

	Ahora sobreescribiríamos todo el método *prestar_libro*, que realmente tendría todo el contenido, pero le agregaríamos una tercera verificación en el *if*, ya que comprobaríamos el libro con el ID correspondiente y un segundo argumento que recibirá el método *True* si es niño y *False* si no es niño, donde si ambos concuerdan, entonces el libro se puede prestar. Esto al final nos deja que solo los niños pueden pedir prestados libros para niños, mientras que solo los adultos pueden pedir prestados libros para adultos.

	![[IMG_596.png]]

	![[IMG_597.png]]

	Si quisiera un adulto solicitar prestado el libro con ID 2, que es un libro para niños, en este caso no podría:

	![[IMG_598.png]]

	Finalmente por curiosear, podríamos agregar una propiedad la cual solo pertenecerá a nuestra clase *BibliotecaInfantil*, esta nos podrá servir para mostrar el contenido de nuestro atributo *libros_para_ninos*, que lo podremos considerar como estar mostrando el estado de los libros para saber los libros con que ID son para niños.

	![[IMG_599.png]]

	![[IMG_600.png]]

	![[IMG_601.png]]

	Así vemos cómo esto concuerda a cómo almacenamos los libros cuando referenciamos si era un libro para niño o no.


## **Proyecto de gestión de animales en tienda**

1. **Introducción**

	En este proyecto se continua explorando la Programación Orientada a Objetos (POO), esta vez con un enfoque distinto. Sin emplear herencia ni polimorfismo, nos centramos en la creación de un sistema de gestión de animales en una tienda.

	El proyecto involucrará el diseño y la implementación de dos clases principales que trabajarán de manera sinérgica. Estas dos clases nos permitirán realizar una variedad de operaciones esenciales en la gestión de una tienda de animales.
	Entre las funcionalidades que desarrollaremos, se incluyen métodos para agregar nuevos animales al inventario, mostrar los animales disponibles, alimentar a los animales y gestionar su venta.

	A través de este proyecto, no solo afianzaremos nuestras habilidades en POO, sino que también demostraremos cómo diferentes clases pueden colaborar de forma efectiva para lograr objetivos comunes. Este sistema nos dará una perspectiva práctica y realista sobre cómo la POO puede ser utilizada para resolver problemas y gestionar información en un contexto de negocios.
	</br>
2. **Práctica**

	Agregaremos nuestro *shebang* y luego haremos la comprobación de que el programa se esté ejecutando directamente, lo cual nos servirá para colocar la funcionalidad de nuestro programa.

	Aquí comenzaremos teniendo en cuenta ya las definiciones de un objeto *perro* y otro *grato*. Estos serán instancias de la clase *Animal* y para crearlos tendremos que pensar en el constructor, para el cual les pasaremos los argumentos, el nombre del animal y el tipo de animal.

	![[IMG_602.png]]

	*Clase Animal:*

	Contemplando esto para nuestro constructor, comenzaremos creando nuestra clase *Animal* y asignándole los atributos que ya son pasados al crear un nuevo animal, tanto *animal* como *especie*. Además, internamente asignaremos el atributo *alimentado*, el cual será un valor booleano para saber si el animal correspondiente ha sido alimentado. El atributo no estará ni protegido, ni privado.

	Primeramente, colocaremos a cada animal como que no está alimentando y ya, en función de si son alimentados o no, esto cambiará.

	![[IMG_603.png]]

	*Clase TiendaAnimales:*

	Empezaremos teniendo en cuenta que crearemos un objeto *tienda* el cual será una instancia de la clase *TiendaAnimales* y como argumento le pasaremos un nombre, este será el nombre de la propia tienda.

	Por lo que esto lo definiremos en nuestro constructor también.

	![[IMG_604.png]]

	Ahora, con base en estas dos clases que tenemos ahora, lo interesante sería agregar o meter los animales que tengamos en esta tienda, por lo que de alguna manera tendríamos que tenerlos dentro de la propia clase *TiendaAnimales*.

	Por ende, para la clase *TiendaAnimales* definiríamos un método *agregar_animales*, para tener la posibilidad de agregarlos. Por lo tanto, lo que le pasaremos como argumento será el objeto que tengamos del animal.

	![[IMG_605.png]]

	*Agregar animales:*

	Primeramente, vamos a agregar de una vez el atributo *animales* a nuestra clase, el cual nos servirá para almacenar en todo momento el total de animales que tengamos.

	Con esto, ahora definiríamos el método *agregar_animal* en la clase *TiendaAnimales* y lo que hará es que con append nos almacenará el objeto dentro del atributo *animales*, que es una lista. Por ende, aquí tendremos almacenados todos los animales.

	![[IMG_606.png]]

	*mostrar_animales*

	Hasta aquí tendríamos todo correctamente definido, pero al ejecutarlo no veríamos nada y esto se debe a que no estamos mostrando nada.

	Por ello generaríamos un método *mostrar_animales*, en este iteraremos sobre la lista y listaremos cada animal con un *print()*, lo cual veremos de la siguiente manera:

	![[IMG_607.png]]

	Si esto lo ejecutamos ahora, veremos cómo solo se nos muestra información de qué son objetos:

	![[IMG_608.png]]

	*Método especial \_\_str\_\_:*

	En nuestro método especial *\_\_str\_\_* definiremos una estética, donde nos muestre la información del objeto de manera que sea: "Tijuana (Gato) - Alimentado" o "Púrpura (Perro) - Hambriento"

	![[IMG_609.png]]

	De esta manera, lo que puede resultar un poco más interesante es el condicional, ya que este retornara 'Alimentado' si el contenido del atributo *alimentado* es *True*, de lo contrario retornara 'Hambriento' y por ende con base en eso, será lo que se mostrará:

	![[IMG_610.png]]

	Como por defecto consideramos que un animal recién ingresado, no está alimentado, nos retorna que ambos están hambrientos.

	*Alimentar animales:*

	En nuestra clase *TiendaAnimales*, crearemos un método *alimentar_animales* con el cual la idea será alimentar a todos los animales, para después volver a mostrarlos y por ende ya veremos que todos están alimentados.

	Dentro de nuestro método *alimentar_animales*, recorríamos la lista donde tenemos a todos los animales y por cada animal mandaríamos a llamar a un método, el cual se encargue de directamente cambiar el atributo *alimentado* a *True*, para que de esta manera ya estén alimentados.

	![[IMG_611.png]]

	![[IMG_612.png]]

	De esta manera, finalmente solo mandaríamos a llamar el método *alimentar_animales* de la clase *TiendaAnimales* y volveriamos a mostrar los animales para verificar que ya están alimentados:

	![[IMG_613.png]]

	Una vez lo ejecutemos, veríamos lo siguiente:

	![[IMG_614.png]]

	*Vender animal:*

	La idea ahora es crear un método para vender un animal. Este será el método *vender_animal* y este será un método de la clase *TiendaAnimales*.

	Para esto, antes de definir el método de la tienda, la idea es que venderemos estos animales sin que estén alimentados, por lo que en nuestra clase *Animal*, definiremos el método *vender* donde cambiará el estatus de que el animal esté alimentado a *False*:

	![[IMG_615.png]]

	Con esto,  en nuestra clase *TiendaAnimales* definiremos el método *vender_animal*, donde como argumento será recibido el nombre de este para comprobar en la lista si existe un animal con este nombre y, de ser el caso, venderlo, por ende eliminarlo de la lista con *remove()*.

	Entonces, en nuestro método *vender_animal* primeramente iteraríamos sobre la lista que contiene todos los animales y con esto comprobaríamos el nombre de cada objeto con el argumento que le pasemos el cual también será el nombre de un animal, una vez lo encuentre mandaría a llamar el método vender de ese mismo animal para que ya no esté alimentado y después para la lista de animales con *remove()* le pasaría como argumento al propio animal para que sea eliminado y una vez haya encontrado al animal y eliminado a este de la lista, finalizara el bucle y a su vez la ejecución del método con *return*, ya que no tendría sentido seguir iterando la lista.

	Al finalizar la función aquí, nos permite definir fuera del bucle algo que solo se ejecutara si nunca se encuentra un animal con ese nombre. Lo que se ejecutará aquí será un mensaje indicando que el animal con el nombre indicado no ha sido encontrado.

	![[IMG_616.png]]

	De esta manera, ahora venderíamos a un animal y con esto volveriamos a mostrar a los animales:

	![[IMG_618.png]]


## **Proyecto de administración de flota de vehículos**

1. **Introducción**

	En este proyecto se creara un sistema de administración para una flota de vehículos, aplicando nuevamente los principios de la Programación Orientada a Objetos. Este proyecto se centrará en el diseño y la implementación de dos clases interactivas, que trabajarán en conjunto para gestionar eficientemente una flota de vehículos.

	Dentro de las capacidades de nuestro sistema, incluiremos métodos para generar nuevos vehículos a la flota, lo que nos permitirá expandir y diversificar nuestras opciones de alquiler. Además, desarrollaremos funcionalidades para el alquiler de vehículos, brindando a los clientes la posibilidad de elegir entre diferentes tipos de vehículos según sus necesidades.

	Otra característica clave será la gestión de la devolución de vehículos. Este método facilitará el proceso de retorno de los vehículos alquilados, asegurando un control eficiente y organizando la flota.

	Este proyecto no solo fortalecerá nuestra comprensión y habilidad en POO, sino que también nos proporcionará valiosas lecciones sobre cómo las clases pueden interactuar para administrar operaciones complejas en un entorno empresarial real.

2. **Práctica**

	Con este proyecto buscaremos facilitar la posibilidad de alquilar coches que tengamos disponibles, teniendo también la posibilidad de tenerlos o no disponibles con base en si alguno se encuentra alquilado o no, por lo que alguien puede alquilarlo y devolverlo tiempo después.

	Comenzaremos creando nuestra clase *Vehiculo*, donde para su constructor contemplaremos *matricula* y *modelo* como argumentos que pasaremos y serán asignados como atributos, además internamente asignaremos el atributo *disponible*, donde por defecto lo consideraremos en *True*, ya que inicialmente todos los coches que se generen, pues van a estar disponibles.

	![[IMG_619.png]]

	*Clase Flota:*

	Una cosa sería los vehículos que vayamos generando con la clase anterior, pero cada uno de estos se irá almacenando en una *Flota* de vehículos, la cual será esta clase.

	A la hora de crear nuestra clase *Flota*, nuestro constructor no contemplará ningún argumento que le vayamos a pasar, pero sí iniciará un atributo *vehiculos* el cual será una lista que almacenará a todos los vehiculos de nuestra flota.

	![[IMG_620.png]]

	Ahora, realizando la comprobación de que este script se está ejecutando directamente, vamos a crear una instancia de nuestra clase flota y ya estaremos contemplando el método *agregar_vehiculo*:

	![[IMG_621.png]]

	De esta manera, ahora definiríamos en nuestro método *agregar_vehiculo* que le podremos pasar como argumento un atributo y este atributo será el propio objeto de un vehiculo el que se almacenará en la lista:

	![[IMG_622.png]]

	Con esto ya estaríamos almacenando dos objetos.

	*Listar la flota inicial:*

	Para listar la flota inicial, jugaremos listando directamente nuestra instancia de la clase *Flota*, en esta haremos algo similar al proyecto anterior, donde utilizamos un método para mostrar el contenido mediante su iteración, realmente estaríamos efectuando lo mismo, pero ahora directamente en el método especial *\_\_str\_\_* y lo haremos con un *join()*, donde representaremos la información con un salto de línea:

	![[IMG_623.png]]

	La idea es que esto nos va a representar cada objeto con un salto de línea. Esto de primeras daría error, ya que en ningún momento estamos realizando directamente un print al objeto para acceder a su método *\_\_str\_\_*, por lo que tendremos que aplicárselo directamente para que nos retorne la forma que vamos a definir en nuestro método especial de la clase Vehiculo:

	![[IMG_624.png]]

	![[IMG_625.png]]

	Al funcionar correctamente, solo nos quedaría definir el método especial *\_\_str\_\_* que representaría a cada vehiculo por individual. La forma en la que representaremos la información será: *Vehiculo(matriculo=X, modelo=Y, disponible=True/False)*

	![[IMG_626.png]]

	![[IMG_627.png]]

	![[IMG_628.png]]

	Con esto ya veríamos la información, tal como lo esperamos.

	*Alquilar un vehículo:*

	Ahora, para alquilar un vehículo, crearíamos el método *alquilar_vehiculo* para nuestra clase *Flota*, al cual le pasaremos como argumento el número de matrícula y mediante la iteración de la lista tendremos que verificar si está disponible un coche con la matrícula que indicamos:

	![[IMG_629.png]]

	Ahora de aquí, para ese vehículo, cuando se haya verificado que si existe uno con esa matrícula, ahora para nuestro objeto mandaremos llamar a un método *alquilar()* propio de la clase *Vehiculo*, este se encargará de que si nuestro vehiculo sé en cuenta como un vehiculo disponible nos cambiará su estatus a *False* o no disponible, de no ser así nos mostraría un mensaje por pantalla indicando que este vehiculo no se puede alquilar:

	![[IMG_630.png]]

	![[IMG_631.png]]

	En nuestro método *alquilar_vehiculo*, asegúrenos de que la comparación que se realiza entre matrículas sea con \=\=. De esta manera evitariamos el error que da.

	 Finalmente, volveremos a ver la flota, para verificar que, en este caso, el automóvil Toyota ha sido colocado en "False":

	![[IMG_632.png]]

	Ahora tendremos en cuenta un método *devolver_vehiculo*. Este no tendrá en cuenta la matrícula para volver a colocarla en *True*, de que este vuelve a estar disponible porque ha sido regresado. Para ello utilizaremos el contenido del método *alquilar_vehiculo*, ya que este sera muy similar. La diferencia será que, en lugar de llamar a *alquilar*, tendría que llamar a *devolver*, donde regresará el valor booleano a *True:*

	![[IMG_633.png]]

	Finalmente, la forma en la que mandamos al método e imprimiremos nuevamente la flota para ver cómo regresamos a un estado donde ha sido devuelto:

	![[IMG_634.png]]

	De esta manera, en el último ejemplo, realmente en caso de que un vehiculo esté en *True*, quiere decir que el vehículo ya está en la flota y aún no ha sido alquilado a nadie.

## **Proyecto de gestión de notas (1/2)**

1. **Introducción**

	En este proyecto se realizará la construcción de un gestor de notas avanzado, aprovechando las técnicas de la Programación Orientada a Objetos (POO). Nuestro objetivo es crear un sistema interactivo que nos permita manejar eficientemente una variedad de notas.

	El corazón de nuestro proyecto será un menú interactivo desde el cual podremos realizar múltiples acciones. Entre estas, incluiremos la capacidad de crear nuevas notas que serán almacenadas en disco, virtualizar todas las notas existentes, buscar notas específicas por ciertos criterios y eliminar notas que ya no sean necesarias.

	Para lograr esto, definiremos varias clases y métodos que colaborarán para manejar las diferentres operaciones relacionadas con las notas. Una parte crucial de nuestro proyecto será la implementación de módulos múltiples, lo que nos permitirá organizar mejor nuestro código y hacerlo más mantenible.

	Además, exploraremos los conceptos de serialización y deserialización de datos utilizando Pickle. Esto nos permitirá guardar y recuperar eficientemente el estado de nuestras notas desde y hacia el disco, facilitando la persistencia de los datos a través de las sesiones de uso del gestor.

	Este proyecto no solo fortalecerá nuestras habilidades en POO y manejo de datos, sino que también nos proporcionará experiencia práctica en la creación de aplicaciones Python que interactúan con el sistema de archivos y gestionan la información de manera eficiente.
	</br>
2. **Práctica:**

	Esta será un proyecto para trabajar con una gestión de notas y además le agregaremos la serialización y deserializacion de datos con Pickle, lo que nos permitirá serializar objetos (un proceso el cual nos permite que este se almacene a nivel de disco o transmitido a nivel de red) y también aplicar una deserializacion (un proceso en el cual se trata de recuperar un objeto para poder acceder a sus datos).

	Por lo tanto, hasta ahora entendemos un objeto como una instancia de una clase, pero en el concepto de la serialización y deserializacion de datos, un objeto abarca algo más amplio, ya que se pueden considerar desde *listas*, *tuplas*, *diccionarios*, *numeros*, *cadenas*, entre otros.

	Esto le añade un nivel más de complejidad, pero desde luego nos permitirá manejar todo de una forma mucho más cómoda.

	*main.py*

	Comenzaríamos definiendo un archivo *main.py*, en este vamos a colocar el shebang y después la comprobación de que este script o módulo, se esté ejecutando de forma directa y si es así se realizarán las acciones correspondientes:

	![[IMG_635.png]]

	En esta ocasión lo cambiaremos un poco y es una de las formas que incluso yo consideraría mejor, ya que lo que haríamos sería crear una función principal donde se encuentre nuestro menú principal y esta función la llamaremos desde nuestra comprobación del archivo.

	La función principal suele ser llama *main()*, en esta nosotros definiremos todo nuestro menú principal, el cual se repetirá de forma infinita a menos que el usuario desee salir de este, lo cual también estará en una de las opciones.

	![[IMG_636.png]]

	Esto mostraría nuestro pequeño menú de forma infinita, por lo que una vez se termine de ejecutar la acción que efectuemos, regresaremos al menú.

	Lo siguiente sería almacenar en una variable la opción seleccionada, como con *input()* al convertirlo a entero para asegurar que sea un número puede darnos algún error, pues lo haremos efectuando un *try* y lanzaremos una excepción de *ValueError*, donde lanzaremos un mensaje y luego colocaremos un *continue* para asegurar que no entre de ninguna manera a nuestro condicional en esa ocasión, a menos que el usuario ingrese correctamente un dato numérico:

	![[IMG_637.png]]

	Comenzaremos contemplando las opciones, primeramente definiremos la *1*, donde al agregarse una nota le pediremos al usuario que la ingrese para almacenarla. Contemplando la opción final *5*, colocaríamos un *break* para salir del bucle y finalmente, en el peor de los casos donde la opción ingresada sea un número mayor 5 o menor a 1, imprimiremos un mensaje en pantalla de que es una opción incorrecta:

	![[IMG_638.png]]

	Nuestro condicional lo iremos completando conforme vayamos creando la funcionalidad del programa. Por ahora, seguido del condicional, colocaremos un input sin almacenar nada, solo será para mostrar una pausa, donde solo avanzara el programa una vez el usuario le dé *\<Enter\>*.

	Además, cada que lleguemos a este punto, como ya se han terminado de efectuar ciertas cosas, pues buscaremos limpiar la pantalla y esto lo podremos hacer con la librería *os*. La forma en la que podremos hacer es utilizar primeramente *os.name*, nos servirá para comprobar si el sistema es *Linux* o *Windows*, este nos retorna 'posix' para Linux y 'nt' para Windows, el comando para limpiar la pantalla en *Linux* es *clear*, mientras que en *Windows* es *cls*.

	Con base en la comprobación le pasaremos como argumento el comando a *os.system()* y esto se encargará de ejecutarlo.

	![[IMG_639.png]]

	Recordemos que para que funcione tendremos que importar la librería *os*, debajo del shebang:

	![[IMG_640.png]]

	*Librería pickle:*

	Si vamos al intérprete de Python, la librería *pickle* deberíamos poder importarla sin problemas porque ya debería venir el módulo en Python, ya que esta dependerá de un archivo en el PATH que Python contempla.

	En cado de que al importarla nos dé error, esto quiere decir que no la tenemos instalada, pero es sencillo de instalar con:

	```pip3
	pip3 install pickle-mixin  
	```

	Yo aplico un *source* al inicio porque cargo un entorno donde se  me instalan las librerías:

	![[IMG_641.png]]

	Ahora, en el intérprete de Python vamos  a importar la librería *pickle*, con esto vamos a pensar en que ya tenemos un objeto, pero este objeto es pensado en el ámbito de la serialización y deserializacion, lo que quiere decir que puede ser cualquier cosa que almacene un tipo de dato, como listas, diccionarios, cadenas de texto, etc.

	Estos serán los que convertiremos a formato bytes, lo que será una secuencia de bytes que almacenaremos en disco o transmitirlo a nivel de red, en función de lo que deseemos realizar.

	Con esto en mente, crearemos una lista de diccionarios que almacenará las notas, donde cada nota será un diccionario con dos pares de clave-valor, donde se almacenara el nombre de la nota y el contenido de esta.

	![[IMG_642.png]]

	Si nosotros quisiéramos almacenar esto en un archivo, manteniendo incluso el tipo de dato, sería algo complejo de realizar, pero con *pickle* esto se puede hacer de una forma mucho más cómoda serializando objetos a un formato de bytes o incluso para volver a transformar esa secuencia de bytes a un objeto para interpretarlo e ingresar a su contenido. Por lo que es más conveniente.

	Con esto en mente, de la forma que podríamos realizarlo es primeramente creando o abriendo un archivo *notas.pkl* y recordemos que almacenara en contenido en bytes, por lo que aparte de abrir para escritura con *w*, también tendremos que agregar la *b* para que nos lo interprete correctamente, por lo tanto, quedaría *wb*.

	Además, con *pickle*, utilizaremos *dump()*, donde como primer argumento le pasaremos el objeto que deseamos almacenar y como segundo argumento el archivo donde lo almacenará:

	![[IMG_643.png]]

	Si observáramos nuestro directorio actual observaríamos como este archivo ya está existente y se considerará un binario, si listamos su contenido se vería de la siguiente forma:

	![[IMG_644.png]]

	Como vemos, el contenido es almacenado de una forma un tanto peculiar y es complicado que sea legible.

	Pero con esto lo interesante viene a la hora de volver a abrir el archivo pero ahora con posibilidad de lectura, ya que aquí ahora podremos definir que con *load()*, pasándole como argumento el archivo nos recupere el objeto, de esta manera podríamos guardarlo en una variable *mis_notas* y con esto ahora al ver el contenido dela variable, observaríamos como tenemos la lista que almacenamos con *dump()*:

	![[IMG_645.png]]

	Por lo tanto, esta seria la idea con *pickle* para almacenar en un archivo binario nuestras notas y recuperarlas para tenerlas legibles en nuestro propio programa.

	*Gestor de notas:*

	Con esto en mente, ahora crearíamos un nuevo módulo *gestor_notar.py*, en el cual definiremos la clase *GestorNotas* en la cual para nuestro constructor contemplaremos como argumento *archivo_notas*, esté lo contemplaremos para que por defecto se cree un archivo con nombre "notas.pkl", pero sí deseamos cambiar el nombre bastaría con pasarle otro al instanciar la clase.

	![[IMG_646.png]]

	Con esto ahora en nuestro archivo *main.py*, importaríamos directamente la clase *GestorNotas* del módulo *gestor_notas.py* y crearíamos una instancia *gestor* de la misma:

	![[IMG_647.png]]

	Ahora en nuestro módulo *gestor_notas.py* vamos a manejar una excepción donde intentaremos abrir el archivo en modo de lectura, tú esto es posible quiere decir que el archivo existe y por ende cargaremos al atributo *notas* el contenido del archivo "notas.pkl", lo cual lo tendremos en mente como si fuese una lista, por la forma en que almacenaremos todo el contenido.

	En caso de que el archivo no exista, tendremos que lanzar la excepción *FileNotFoundError* y definiremos el atributo *notas* como una lista vacía:

	![[IMG_648.png]]

	De esta manera, en caso de que el archivo no exista, las notas que iremos agregando se irán almacenando en la lista de nuestro atributo *notas*, por ende al cargar el contenido al archivo será la lista y al recuperarlo también.

	*Método agregar_notas:*

	Con todo lo anterior definido, ahora definiríamos en nuestra clase *GestorNotas* un método el cual se encargue de agregar las notas a nuestra lista de nuestro atributo *notas*, donde como argumento recibirá el contenido de la nota:

	![[IMG_649.png]]

	Esto está bien, pero realmente para no tener solamente una lista con cadenas de texto, lo mejor sería representar esto a nivel de objeto, el cual tenga sus atributos y métodos.

	Por ende aquí inicializaríamos una instancia temporal de la clase *Nota*, donde le pasaremos como argumento el contenido de la nota y esto hará que nos almacene en nuestra lista un objeto.

	![[IMG_650.png]]

	Entonces, en nuestro módulo *gestor_notas*, estamos utilizando *pickle* para el manejo del archivo binario y la clase *Nota*, esta la definiremos en un módulo *notas*, por ende tendremos que importar tanto la clase como pickle al módulo *gestor_notas*:

	![[IMG_651.png]]

	*Módulo notas y clase Nota:*

	Con esto, definiríamos nuestro módulo *notas* en el directorio actual y en este crearíamos la clase *Nota*, donde su constructor contemplara el atributo *contenido* para almacenarlo como atributo:

	![[IMG_652.png]]

	*Método guarar_notas:*

	Ahora tendremos que definir un método que se mandara a llamar desde nuestro método *agregar_nota*, en nuestro módulo *gestor_notas*, este será el método *guardar_notas* y en este definiremos que mediante serialización nos almacene la lista que contiene todas las notas en nuestro archivo 'notas.pkl':

	![[IMG_653.png]]

	Finalmente, tendremos que llamar a nuestro método *agregar_nota* desde nuestro archivo principal *main.py*, donde la primera opción es la que nos permitirá agregar una nueva nota:

	![[IMG_654.png]]

	De esta manera, ahora al ejecutar nuestro *main.py*, podremos agregar una nueva nota:

	![[IMG_655.png]]

	![[IMG_656.png]]

	Ahora veremos como el archivo se ha creado y almacenado el contenido:

	![[IMG_657.png]]

	Por lo tanto, si quisiéramos verificar que el contenido del archivo, si sea lo que nosotros colocamos, podríamos hacerlo desde el intérprete de Python:

	![[IMG_658.png]]

	Como es un objeto lo que hemos almacenado, es mostrado de esta manera porque aún no definimos el método especial *\_\_repr\_\_*, para que a nivel de representación lo veamos como deseemos mostrarlo.

	Por ende accedemos directamente al objeto que está en la primera posición y recordemos que la nota que agregamos es almacenada en el atributo *contenido*, por ende hacemos referencia a él y ya esto nos retornaría el contenido que nosotros hemos almacenado en este objeto que es una instancia de la clase *Nota*.

## **Proyecto de gestión de notas (2/2)**

1. **Introducción**

	Ahora concluiremos el proyecto de gestor de nostas en Pytho utilizando Pickle. Tras haber sentado las bases es momento de integrar y finalizar todos los componentes de nuestro sistema. Vamos a revisar y perfeccionar las clases principales, asegurándonos de que todas las funcionalidades clave, como crear, visualizar, buscar  y eliminar notas, funcionen de manera fluida.

	Un enfoque importante sera la serialización y deserialización con Pickle. Esta técnica es cricual para la persistencia de las notas en el disco, permitiendo que se guarden de forma segura y se recuperen en futuras sesiones del programa.

	Al concluir habremos completado un gestor de notas funcional y eficiente. Este proyecto no solo refuerza las habilidades en programación orientada a objetos y manejo de datos, sino que también nos proporciona experiencia práctica en la creación de aplicaciones Python interactivas y robustas.

2. **Práctica**

	Ahora, en nuestro archivo principal *main.py*, pasaríamos a nuestra opción *2*, la cual sería para leer todas las notas, entonces lo que tendremos que hacer será llamar un método *leer_notas* de nuestra clase *GestorNotas*, recordando que tenemos la instancia *gestor*.

	![[IMG_659.png]]

	Con ello ahora en nuestra clase *GestorNotas* definiríamos el método *leer_notas*, el cual no recibe ningún argumento y lo que este hará será retornar la lista de las notas, ya no se tendría que aplicar deserializacion debido a que esto se aplica en el momento en el que se crea la instancia de la clase, dentro del propio constructor.

	![[IMG_660.png]]

	Recordemos que la definición de cualquier método normal tendrá que tener siempre como parámetro el propio objeto referenciado con *self*, así que también se tiene que agregar en nuestro método: *leer_notas(self)*.

	Con esto, ahora en nuestro archivo *main.py*, en la opción de leer notas, pues recibiremos la lista de objetos, lo que haremos con esto será jugar con enumerate, iniciando en 1, para que puedamos tomar el número de objetos que se le da con enumerate a partir del 1 y como segundo valor tomar el argumento y por cada iteración mostrarlo:

	![[IMG_661.png]]

	De esta manera, al ejecutarlo veríamos lo siguiente:

	![[IMG_662.png]]

	Configuraríamos enumerate para que inicie en 1:

	![[IMG_663.png]]

	De esta manera, ahora, al agregar más notas y mostrarlas, las veríamos así:

	![[IMG_664.png]]

	![[IMG_665.png]]

	Ahora, vemos los objetos de las notas representados como tal, para que su representación sea dando la información tendremos que definir en método especial *\_\_str\_\_* en nuestra clase *Nota* la cual está en nuestro módulo *notas*.

	Buscaremos retornar directamente la nota, lo cual es una cadena, y finalmente quedaría el método especial así:

	![[IMG_666.png]]

	Y al mostrar las notas ahora lo veríamos correctamente:

	![[IMG_667.png]]

	*Opción 3: buscar por una nota*

	Comenzaríamos definiendo nuestra tercera opción de nuestro panel principal, para cuando selecciones 3, entre en este. Aquí definiremos la variable *texto_busqueda*, donde mediante un input almacenaremos texto que ingresara el usuario, donde se espera que el usuario ingrese cierta cantidad de texto de una nota, para internamente realizar una validación de si internamente existe una nota que contenga ese texto.

	De una forma sencilla haríamos referencia a un método *buscar_nota*, a este le pasaremos como argumento el texto que el usuario ingrese y lo que el método retorne lo almacenaremos en *nota*, lo cual luego mostraremos con un *print()*:

	![[IMG_668.png]]

	*Método buscar_nota:*

	Este método lo definiríamos en nuestra clase *GestorNotas*, donde recibirá el argumento del texto de búsqueda, aquí lo que haremos será iterar en toda la lista que tiene las notas y por cada nota tendremos que hacer una validación donde si el *texto_busqueda* se encuentra dentro del atributo *contenido* de alguno de los objetos, esta validación la podremos realizar verificando si algún texto o palabra está dentro de una cadena, con *if "Hola" in "Hola mundo"*, esto devolvería *True*, ya que "Hola" si está dentro de la cadena "Hola mundo".

	De esta manera almacenaremos cada match en una lista y al final retornaremos la lista:

	![[IMG_669.png]]

	Esto funcionaria, pero nos mostraría la lista, lo cual podríamos llegar a cambiar utilizando *.join()*, pero en este caso ahora veremos como realizarlo con una lista de comprensión.

	![[IMG_670.png]]

	De esta manera estamos haciendo exactamente lo mismo, pero para tenerlo mejor estructurado, para cada instancia de la clase *Nota*, crearemos el método *coincide* al que estamos haciendo referencia, de esta manera exactamente la misma validación la aplicaríamos con un método propio de la clase y solo retornaríamos *True* o *False*.

	![[IMG_671.png]]

	Que al final sería lo mismo que:

	![[IMG_672.png]]

	Ahora, para el mostrar el contenido, podríamos hacerlo de la misma que en nuestra opción 2, ya que nos es regresada una lista la cual se puede iterar.

	![[IMG_673.png]]

	Es importante agregar los ':' en el bucle for, ya que en la imagen no está agregado.
	Teniendo como resultado para nuestras búsquedas:

	![[IMG_674.png]]

	*Eliminar una nota*

	Ahora tendríamos que agregar la opción de eliminar una, la cual sería el '4' dentro de nuestro condicional, lo que tendremos pensado aquí será que el usuario nos ingrese el índice del objeto y con ello eliminar esa nota.

	En nuestro condicional para la condición, cuando nuestra opción sea igual a 4, solicitaremos un input del usuario, cuál será un número, este será una entrada numérica, pero aquí también aplicaremos un *try* para lanzar una excepción en caso de que algo salga mal y lo colocaremos dentro de un bucle para que continue hasta que el usuario ingrese un número:

	![[IMG_675.png]]

	Aquí lo que estamos haciendo es realizar una validación doble, primeramente manejamos una excepción en caso de que el usuario ingrese un tipo de dato que no sea numérico, pero una vez se ingrese un número, este podría ser menor a cero, por la forma en que lo verificaremos requeriremos que sea como se muestran las notas, que es del 1 hacia arriba y ya internamente nos encargaremos de restarle un número para que sea el índice correspondiente.

	Por ende, si el número es cero o menor a cero, se aplicará un continue para que vuelva a regresar al inicio del bucle y lanzará un mensaje donde indique que el número se tiene que ingresar mayor a 0.

	Luego haremos referencia a nuestro método *eliminar_nota* de nuestra instancia *gestor* al cual le pasaremos como argumento el número correspondiente que el usuario indico y le restaremos 1 para que corresponda al índice.

	![[IMG_676.png]]

	Y crearemos el método *eliminar_nota* en nuestra clase *GestorNota*:

	![[IMG_677.png]]

	Esta sería la forma de aplicarlo con una excepción, pero también podríamos aplicarlo donde se calcule el número total de elementos que contiene la lista y a este restarle 1 para que sea el último índice, si el índice dado por el usuario es mayor al calculado con *len()*, entonces no se podrá eliminar, ya que daría un *IndexError*:

	![[IMG_678.png]]

	Esto parece estar bien, pero aún nos falta guardar los cambios en nuestro archivo al momento en el que se borran las notas de la lista, por ende reutilizaremos nuestro método *guardar_notas*:

	![[IMG_679.png]]

	Finalmente tendríamos lo siguiente:

	![[IMG_680.png]]

	![[IMG_681.png]]

	![[IMG_682.png]]

	Con esto ya estará finalizado el último proyecto de POO.

[[#Índice]]

## **Siguientes apuntes**

[[Biblioteca_estándar_y_herramientas_adicionales]]