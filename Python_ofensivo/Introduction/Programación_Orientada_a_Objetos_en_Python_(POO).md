
## **Índice**

- [[#Clases y objetos (1/2)]]
- [[#Clases y objetos (2/2)]]
- [[#Métodos estáticos y métodos de clase]]
- [[#Comprendiendo mejor el uso de self]]
- [[#Herencia y polimorfismo]]
- [[#Encapsulamiento y métodos especiales]]
- [[#Decoradores y popiedades]]
- [[#Siguientes apuntes]]


### **Clases y objetos (1/2)**

1. **Introducción**
	La Programación Orientada a Objetos (POO) es un paradigma de programación que utiliza objetos y clases en su enfoque central. Es una manera de estructurar y organizar el código que refleja cómo los desarrolladores piensan sobre el mundo real y las entidades dentro de él.
	
	*Clases:*
	
	Las clases son fundamentos de la POO. Actúan como plantillas para la creación de objetos y definen atributos y comportamientos que los objetos creados a partir de ellas tendrán. En Python una clase se define con la palabra clave *class* y proporciona la estructura inicial para todo objeto que se derive de ella.
	
	*Instancias de Clase y Objetos:*
	
	Un objeto es una instancia de una clase. Cada ves que se crea objeto, se está creando una instancia que tiene su propio espacio de memoria y conjunto de valores para los atributos definidos por su clase. Los objetos encapsulan datos y funciones juntos en una entidad discreta.
	
	*Métodos de Clase:*

	Los métodos de clase son funciones que se definen dentro de una clase y solo pueden ser llamados por las instancias de esa clase. Estos métodos son el mecanismo principal para interactuar con los objetos, permitiéndoles realizar operaciones o acciones, modificar su estado o incluso interactuar con otros objetos.


2. **Práctica**

	Comenzaremos creando una clase *persona*, buscando un entendimiento más sencillo de esto, una definición o creación para una clase quedaría de la siguiente manera:

	![[IMG_276.png]]

	Al definir nuestra clase, tendremos que definir también un constructor, este se define con ciertos parámetros los cuales serán asignados a los atributos de un objeto:

	![[IMG_277.png]]

	Nuestro constructor es un método de la propia clase y nos permitirá asignar los atributos mediante el uso de self, *self* se utiliza, ya que al asignar valores a nuestros atributos lo haremos llamando al mismo objeto y es como la forma de llamarse a sí mismo, de la misma manera al utilizar self podremos recuperar lo almacenado en los atributos:

	![[IMG_278.png]]

	De esta manera, estamos asignando a nuestros atributos los valores que son pasados a la definición de la clase cuando se crea un objeto.

	Con esto podríamos definir un método para que nos retorne o haga algo, esto lo podríamos definir como si de una función dentro de una clase se tratase, pero se le llaman métodos:

	![[IMG_279.png]]

	De esta manera, estaríamos definiendo que nuestro método nos retorne la información del nombre y la edad mediante un mensaje seteado con un *f-string* y una vez recuperado este mensaje podríamos imprimirlo por pantalla.

	Para poder realizar esto, primero tendríamos que crear una instancia la cual sería nuestro objeto.

	![[IMG_280.png]]

	Esto nos crearía un objeto y podríamos llamar la información de la misma manera que lo hace el self, pero para hacerlo fuera de la clase tendríamos que mandar llamar nuestro objeto creado, de la siguiente manera:

	![[IMG_281.png]]

	De esta manera, nuestro *objeto* creado de la clase *Persona*, lo llamamos y accedemos a los atributos indicando un *.* antes de ellos.

	Para ejecutar o efectuar lo que tenemos en nuestro método, sería como ejecutar una función y esto haría que nos retorne el string anteriormente programado en nuestro método:

	![[IMG_282.png]]

	Con esto podremos tener en cuenta de la definición de una instancia u objeto se realizan como si de una variable se tratase, pero en esta llamamos a la clase que hemos creado y le pasamos los datos necesarios colocados en nuestro constructor, que sería el inicializador de los atributos, asignándoles los datos que le pasemos a la clase al llamarla.

	*self*, explicado de una mejor forma lo que hace es hacer referencia al objeto que se está creando o se creo, es por ello que en el constructor o en el método también se le pasó como parámetro *self*, porque es una forma de referencias a la instancia creada.

	**Método:**
	
	Entonces, una forma de entenderlo es que cuando nosotros hacemos un *sammy.saludo()*, lo que se hace por detrás es que para la clase *Persona* ejecutamos nuestro método *saludo* y le pasamos nuestro objeto *sammy*, lo cual se puede ver como: *Persona.saludo(sammy)*.

	De esta manera en nuestro método es donde tenemos que pasar *self*, ya que involucra al objeto y mediante este accedemos a los atributos, sería prácticamente lo mismo que hicimos para imprimir el nombre por fuera de la clase, pero dentro de la clase se hace referencia al objeto con *self*.

	**Constructor:**

	Cuando  creamos la instancia(objeto) de nuestra clase, lo que estamos haciendo es pasarle dos argumentos, los cuales son el nombre y la edad. ¿Pero de qué objeto o a qué objeto se le están asignando estos atributos?
	
	En este caos al objeto *sammy* y esto lo maneja ya Python para saber qué instancia fue creada, lo que podríamos ver como: *Persona.__init__(sammy, nombre, edad)*.

	Es por ello que *self* se maneja mucho en las clases, ya que nos permite manejar los atributos para una instancia(objeto) dada.

	**Variables de clase:**
	
	Existen variables de clases, por lo que los atributos que tenemos creados son solamente para los objetos conforme los vayamos creando.
	
	Un ejemplo es que podremos asignar los atributos propios de cada objeto creado, los atributos serán únicos de cada objeto, pero todos los objetos de una clase que hayan sido creados compartirán las variables de clase.

	Con esto en mente podríamos crear más instancias de nuestra clase, donde al crearla tendremos que pasar los argumentos de nombre y edad para que sean asignador por nuestro constructor a los atributos correspondientes. Después llamaremos al método *saludo* de cada instancia creada y esto nos retornaría el string, por lo que lo imprimiremos en pantalla:

	![[IMG_283.png]]

	**Ejemplo de clase de animales:**

	Con base en lo anterior, ahora crearemos una clase *Animales*, en nuestro constructor buscaremos iniciar nuestros atributos para un nombre animal, así para un tipo de animal.

	Después crearemos un constructor el cual nos dé una descripción del nombre y animal de nuestro objeto dado.

	![[IMG_284.png]]

	De esta manera, al crear un objeto, mediante nuestro constructor se asignan los valores a los atributos para ese objeto. Luego, mediante nuestro método descripción, recibe el objeto con *self* para poder acceder a los datos y mostrarlos con el string, el cual es retornado y mostrado en pantalla por el print.

	Lo que hace Python, por detrás, por así decirlo, es llamar la clase y pasarle los argumentos que nosotros le hemos pasado y el objeto creado.

	Lo cual es equivalente a lo que está comentado en el código después de los *#*, por lo que si intentáramos usar el constructor o el método llamando directamente a la clase, también funcionaria, pero tendría que estar creado el objeto desde antes o daría error:

	![[IMG_285.png]]

	La forma usual desde luego es como se vio primero, llamando al objeto y aplicando el uso de  los métodos en este.

	Además, nosotros hemos estado jugando con *return* para que nos regrese el string y nosotros podamos mostrarlo, almacenarlo o jugar con él, pero si directamente quisiéramos realizar el print en nuestro método podríamos hacerlo y nos ahorraríamos el print fuera de este al llamar al método mediante cada objeto, ya que recordemos que cada objeto es independiente y en sus atributos contendrá sus datos propios:
	
	![[IMG_286.png]]

	**Ejemplo con clase CuentaBancaria:**

	Para esta clase lo haremos un poco más complejo y crearemos métodos que operen con los valores que indiquemos para un cliente, donde el cliente será nuestra instancia(objeto).

	La definición de nuestra clase podremos empezar a plantearla viendo cuantos y cuáles argumentos le pasáremos al crear el objeto:

	![[IMG_287.png]]

	De esta manera podremos tener en cuenta que para nuestro constructor tendremos en cuenta un ID o número de cuenta, un nombre de un cliente y su cantidad de dinero. Creando nuestro constructor de la siguiente manera:


	![[IMG_288.png]]

	Aquí podríamos jugar con un concepto nuevo, si intentáramos evitar mandar el argumento de dinero esto nos ocasionaría un error, pero en nuestro constructor en la definición de los parámetros podríamos directamente setear el dinero en *0*.  

	Esto lo que nos permite es que en caso de no se coloque como argumento el contenido para el parámetro dinero, este automáticamente será 0, y si lo agregamos tomará el valor que nosotros coloquemos, por ende esto podría verse de las siguientes dos maneras:

	*Donde no le mandemos una cantidad de dinero y por defecto sea 0:*

	![[IMG_289.png]]

	![[IMG_291.png]]

	*Donde le mandemos una cantidad de dinero como argumento y por ende la cantidad que nosotros coloquemos será la que se almacenara en el atributo:*

	![[IMG_290.png]]

	![[IMG_292.png]]

	Con esto, crearemos dos métodos de los cuales uno nos permitirá agregar dinero y el otro retirarlo.

	**Método para depositar dinero:**

	Para nuestro método de depositar dinero, lo que tendremos que hacer es pasarle como argumento una cantidad de dinero y en nuestros parámetros del método tendremos que agregarlo, así como la referencia a nuestro objeto que es *self* para poder trabajar con los atributos.
	
	Ya dentro de nuestro método definiríamos el incremento del dinero con la cantidad que se le ingrese como argumento y nos quedaría de la siguiente manera:

	![[IMG_293.png]]

	Finalmente, podríamos definir que nuestro método nos retorne un string con la información de lo realizado y mediante un print imprimir el texto al llamar al método:

	![[IMG_294.png]]

	Es importante aclarar que el atributo o variable del objeto a la que se accede con *self* es totalmente independiente de nuestro parámetro de nombre *dinero*, colocado después de *self*. Este podría tener perfectamente otro nombre y no afectaría en nada al funcionamiento de nuestro programa:

	![[IMG_295.png]]

	**Método para retirar dinero:**


	Este va a ser de una forma muy similar al de depositar dinero, pero tendrá una diferencia que es fundamental. Al retirar dinero tendremos que tener cuidado con que la cantidad que queremos retirar sea menor a la cantidad que tenemos disponible de dinero.

	Es por ello que agregaremos un condicional el cual nos retornara un string con información, si la cantidad de dinero que se quiere retirar supera nuestro dinero disponible, es importante recordar que cuando utilizamos return indicamos que nos regrese una información a la función (método en este caso) y por ende se termina de ejecutar en esa línea de código y no ejecuta las siguientes:

	![[IMG_296.png]]

	Ahora tendremos lo mismo que al depositar, pero lo que haría sería restar el dinero y, en caso de superar el dinero disponible, retornaría un mensaje el cual te indicaría que tus fondos son insuficientes.

	Esto además se puede ver con algunos ejemplos aplicados de depósito y retiro de dinero.

	En un caso realista, también tendríamos que tener cuidado con que una persona no intente depositar o retirar valores negativos, ya sea mediante el programa o simplemente evitando que donde lo ingresen no se pueda colocar el caracter *-*.

	Además, es importante tener muy en cuenta que cada objeto que creemos tendrá los mismos atributos, ya que pertenecen a la misma clase, pero serán totalmente independientes uno del otro, por lo que si modificamos algo en un objeto el cambio solamente se hará en ese y otro será totalmente independiente:

	![[IMG_297.png]]

	Primero modifiqué los métodos para que al imprimir el contenido también esté el nombre y sea más fácil visualizarlo.

	Después cree otro objeto para otra persona y deposité dinero para esta, de esta manera podremos  ver cómo es totalmente independiente un objeto de otro.

	![[IMG_298.png]]

	En la llamada a la función para depositar dinero hay un error, el cual se soluciona llamando al método con el nombre correcto. Finalmente tendríamos como output de nuestro programa lo siguiente:

	![[IMG_299.png]]

	Aquí inicializamos los objetos ya con $1000 cada uno y después depositamos o retiramos dinero.

## **Clases y objetos (2/2)**

1. **Introducción**

	Dentro del paradigma de la Programación Orientada a Objetos en Python, existen conceptos avanzados como los decoradores, métodos de clase y métodos estáticos que enriquecen y expanden las posibilidades de cómo insteractuamos con las clases y sus instancias.

	*Decoradores:*

	Los decoradores son una herramienta poderosa en Python que permiten modificar el comportamiento de una función o método. Funcionan como "envoltorios", que agregan funcionalidad antes y después del método o función decorada sin cambiar su código fuente. En POO, los decoradores son frecuentemente utilizados para agregar funcionalidades de manera dinámica a los métodos, como la sincronización de hilos, la memorización de resultados o la verificación de permisos.

	*Métodos de Clase:*

	Un método de clase es un método que está ligado a la clase y no a una instancia de la clase. Esto significa que el método puede ser llamado sobre la clase misma, en lugar de sobre un objeto de la clase. Se definen utilizando el decorador *@classmethod* y su primer argumento es siempre una referencia a la clase, convencionalmente llamada *cls*. Los métodos de la clase son utilizados a menudo para definir métodos "factory" que pueden crear instancias de la clase de diferentes maneras.

	*Métodos Estáticos:*

	Los métodos estáticos, definidos con el decorador *@staticmethod*, no reciben una referencia implícita ni a la instancia (self) ni a la clase (cls). Son básicamente como funciones regulares, pero pertenecen al espacio de nombres de la clase. Son útiles cuando queremos realizar alguna funcionalidad que está relacionada con la clase, pero no requiere acceder a la instancia o a los atributos de clase.
	</br>
2. **Práctica**

	Ahora crearemos una clase *Rectangulo*, donde a ese objeto correspondiente se le van a asignar los atributos *ancho* y *alto*, los cuales le pasaremos al crear una instancia.

	Esto lo podremos necesitar, por ejemplo, para realizar un cálculo como el área de un rectángulo.

	![[IMG_300.png]]

	Con esto, podríamos crear un método simple para nuestro cálculo del área y que este sea retornado para mostrarlo en pantalla:

	![[IMG_301.png]]

	Teniendo los métodos de esta forma se llaman como si de una función se tratase, ya que se le agregan los paréntesis, ya que recordemos que a la clase se le pasa el objeto y se recibe mediante el uso de *self*.

	Recordemos que podremos acceder a los atributos del objeto simplemente colocándolo después del punto. Para nuestro método podríamos llegar a hacer exactamente lo mismo gracias al decorador *@property*, que se utiliza de la siguiente manera:

	![[IMG_302.png]]

	Esto nos permitiría llamarlo como si de un atributo se tratase.

	**Imprimiendo un objeto y modificando el output:**

	Es posible imprimir un objeto pasándolo simplemente por un print. Esto nos mostrará en pantalla la información de que es un objeto:

	![[IMG_303.png]]

	Este es un output que se nos da al querer imprimir un objeto, pero podremos cambiar o manejar lo que se muestre gracias a un método especial, el cual es *\_\_str\_\_*:

	![[IMG_304.png]]

	De esta forma retornamos un mensaje que nosotros definamos y con esto ahora, en lugar de mostrar cierta información del objeto, mostrara la información deseada.

	Por lo que con esto podríamos mostrar las propiedades del rectángulo y después calcular su área:

	![[IMG_305.png]]

	**Comparaciones entre objetos con el método especial \_\_eq\_\_:**

	Nosotros podremos hacemos comparaciones entre objetos con el operador *\=\=*:

	![[IMG_306.png]]

	Esto a simple vista parecerá que funciona, pero incluso al tener los mismos datos, esto nos retornará *Flase*. Esto es porque aún no definimos nuestro método especial para manejar este y lo definiríamos con *\_\_eq\_\_*:

	![[IMG_307.png]]

	De esta manera, al realizar la comparativa entre dos objetos, se manda llamar directamente el método especial *\_\_eq\_\_* y nos regresará *True* o *False* de acuerdo con la comprobación que estamos realizando, ya que comparamos si los atributos de ambos objetos son iguales.

	Lo que hace el hecho de colocar una igualdad entre ambos objetos, es mandarlos a ambos como argumentos a nuestro método especial y, por ende, *self* y *otro*, son nuestros dos objetos de rectángulo.

	**Para otro ejemplo, creando la clase Libro:**

	Empezaremos definiendo nuestra clase, así como nuestro constructor para asignar el título, autor y precio.

	![[IMG_308.png]]

	Con esto ahora podríamos ver un ejemplo en el cual no es necesario pasar nuestro objeto, ya que no vamos a referenciar a nuestros atributos, sabemos que cuando tenemos un método al llamarlo, es como llamar a la clase con el método y pasándole el objeto, seguido de los argumentos requeridos para que vaya a funcionar lo cual se vería como  *Libro.metodo(objeto)*, es por ello que utilizamos *self* para referenciarlo.

	Un ejemplo donde no requeriríamos de este para el funcionamiento del método sería simplemente con un valor booleano calcular si nuestro libro se puede considerar *bestseller*, lo cual quiere decir que ha tenido éxito con sus ventas después de un cierto número de ventas, en este caso como delimitador tomaremos 5000 ventas, nosotros le pasaremos las ventas como argumento:

	![[IMG_309.png]]

	De esta manera, al ejecutarlo, nos imprimirá True debido a que el argumento para el total de ventas que le hemos pasado sí es mayor a 5000.

	Con ello podremos notar que realmente no estamos utilizando *self* para hacer referencia al propio objeto y acceder a sus atributos.

	Para esto nos vienen bien los métodos estáticos, los cuales no requieren del propio objeto y trabajarán únicamente con los argumentos que se le han pasado o con las variables de clase.

	Podremos declarar el método estático gracias al decorador *@staticmethod*:

	![[IMG_310.png]]

	De esta manera ya no fue necesario colocar el *self* y trabajo únicamente con los argumentos que le fueron pasados.

	Como esté un método de la propia clase que ya no requiere tampoco que se le pase el objeto, entonces referenciaríamos a este de mejor manera, haciéndolo directamente con la clase y no con un objeto en específico, donde podríamos hacerlo así:

	![[IMG_311.png]]

	Como mencionamos que los métodos estáticos pueden trabajar con las variables de clase, nuestro delimitador 5000 para verificar si el total de ventas se consideraría *bestseller*, podríamos almacenarlo en una variable de clase y acceder a este referenciando a la clase para realizar la verificación, que al final sería lo mismo que ya tenemos:

	![[IMG_312.png]]

	El método estático no quiere decir que no le podamos pasar objetos a nuestro método, realmente sí se podría, que sería hacer lo mismo que referencias al método mediante el objeto, ya que:

	*objeto.es_bestseller(5000)* es exactamente lo mismo que *clase.es_bestseller(objeto, 5000)*, por lo que de la segunda manera podríamos hacerlo para un método estático y sería lo mismo que hacerlo de la primera manera.

	Por lo que podríamos hacerlo aplicándolo de esta manera si nuestro *bestseller_value* lo definiéramos en nuestro constructor para asignarlo como atributo al objeto:

	![[IMG_313.png]]

	**Método para calcular el precio, incluyendo el IVA:**
	
	Ahora podríamos crear un método que nos calcule el precio de nuestro libro,  incluyendo el IVA. Primero lo haremos empleando un método estático:

	![[IMG_314.png]]

	Aquí, en lugar de pasar el objeto, se para directamente el precio que contiene el atributo del objeto, pero haciéndolo con un método normal para trabajar con el objeto, sería así:

	![[IMG_315.png]]

	para la posibilidad de trabajar con cualquier atributo.

	**Decorador para método de clase: @classmethod**

	Esto sería una forma de referenciar a nuestra clase utilizando *cls*, que sería prácticamente lo mismo a cuando utilizamos el método referenciándolo con nuestro objeto, en este caso es para cuando lo referenciamos con nuestra clase, pues esta es pasada como argumento y la mostraríamos con el parámetro *cls*:

	![[IMG_316.png]]

	Esto podría parecer que no tiene mucha utilidad ahora, ya que con poner el nombre de la clase sin aplicar ningún decorador nos funcionaría perfectamente, pero cuando hacemos uso de la herencia y polimorfismo en Python, esto cobra más sentido.

	**Herencia en clases**

	La herencia en clases quiere decir que podremos pasar de una clase a otra, todos sus métodos y atributos, creando un tipo de subclase, que contendrá todo lo de la clase principal, así como atributos y métodos nuevos que se le agreguen.

	Si hiciéramos una herencia de una clase a otra, para, por ejemplo, tener una definición del libro y una definición para el mismo libro de forma digital, donde cambiar el IVA que se aplique al momento de realizar su compra, aquí tendríamos un problema si efectuamos un método estático:

	![[IMG_317.png]]

	En este caso, nuestra clase LibroDigital es una clase con herencia de la clase Libro, lo cual se indica con los paréntesis.

	Esto quiere decir que la nueva clase tendra todo lo que tiene la anterior, pero modificamos el IVA para que el digital tenga un IVA menor.

	Pero al momento de imprimir el resultado, tenemos un problema, y es que en nuestra clase Libro referenciamos a la misma clase y, por ende, en ambos nos retorna el mismo precio final, ya que en ambos casos está tomando el IVA de la clase *Libro*.

	Entonces, si quisiéramos intentar solucionarlo referenciando a la clase *LibroDigital*, tampoco se solucionaría, ya que ahora ambos casos nos mostrarían un resultado tomando en consideración el IVA del 0.10:

	![[IMG_318.png]]

	Como vemos ahora toma para ambos el IVA del 0.10, entonces en estos casos es donde viene bien utilizar el decorador *@classmethod*, ya que por sí mismo pasa la clase desde la cual se hace referencia al método y por ende sabe cuál utilizar para mostrar los valores indicados, quedando de la siguiente manera:

	![[IMG_319.png]]

	Y ahora, como se manda a llamar de cada una de las clases, retorna los valores correctos esperados para cada caso.

## **Métodos estáticos y métodos de clase**

1. **Introducción**

	Los métodos estáticos y los métodos de clase son dos herramientas poderosas en la programación orientada a objetos en Python, que ofrecen flexibilidad en cómo se pueden acceder y utilizar la funcionalidad asociada con una clase.

	*Métodos de Clase:*

	Se define con el decorador *@classmethod*, lo que le permite tomar la clase como primer argumento, generalmente nombrada *cls*. Este acceso a la clase permite que los métodos de clase interactúen con la estructura de la clase en si, como modificar atributos de clase que afectarán a todas las instancias. Se utilizan para tareas que requieren conocimiento del estado global de la clase, como la construcción de instancias de maneras específicas, también conocidos como métodos factory.

	*Métodos Estáticos:*

	Se definen con el decorador *@staticmethod*, y no reciben un argumento implícito de referencia a la clase o instancia. Son similares a las funciones regulares dentro del cuerpo de una clase. Se utilizan como funciones que, aunque conceptualmente pertenecen a una clase debido a la relevancia temática, no necesitan acceder a ningún dato específico de la clase o instancia. Proporcionan una manera de encapsular la funcionalidad dentro de una clase, manteniendo la cohesión y la organización del código.

	Ambos métodos contribuyen a un diseño de software más limpio y modular, permitiendo una clara separación entre la funcionalidad que opera con respecto a la clase en su totalidad y la funcionalidad que es independiente de las instancias de clase y de la clase misma. La elección entre utilizar un método de clase o un método estático a menudo depende del requisito específico de acceso o no a la clase o a sus instancias.
	</br>
2. **Práctica**

	*Empleando métodos estáticos con una clase Calculadora que nos permita realizar operaciones directamente sin tener que crear instancias de esta misma:*

	Para empezar, realizaremos la definición de nuestra clase con un método estático que nos permita realizar la suma de dos números, lo cual podremos efectuar llamando a la clase con ese método y pasándole los dos número a sumar:

	![[IMG_320.png]]

	Aplicando el mismo principio, definiríamos un método para resta y otro para multiplicación:

	![[IMG_321.png]]

	Ahora crearíamos uno para la división, en el cual tendríamos que emplear una lógica donde, si el segundo número es cero, nos retorne un mensaje para indicar que no es posible dividir entre cero y evitar que el programa nos dé errores.

	![[IMG_322.png]]

	De esta manera, estamos definiendo que si nuestra variable num2 es diferente de cero, entonces nos retornará el resultado de la división, pero si este no es distinto de cero (que será igual a cero), entonces entrará al else y nos retornará el mensaje, el cual imprimiremos también:

	![[IMG_323.png]]

	**Métodos de clases con el decorador @classmethod**

	Comenzaremos creando una clase *Automovil* a la cual le pasaremos tanto marca como modelo para inicializar en el constructor.

	![[IMG_324.png]]

	Podremos crear un objeto de la forma que lo hemos hecho anteriormente:

	![[IMG_325.png]]

	Pero podríamos experimentar con una forma más interesante, donde este se cree con un método de clase:

	![[IMG_326.png]]

	Aquí sucede exactamente lo mismo que hicimos anteriormente para crear el objeto, solo que de una forma un tanto más en partes, primeramente llamamos a nuestro método de clase donde le pasamos la marca de nuestro automóvil, este con *cls* hace referencia a la misma clase, lo que es equivalente a utilizar *Automovil()*, como lo hicimos anteriormente.

	Esto, al pasarle los atributos de marca y modelo, pues nos crearía el objeto, ya que lo hace exactamente de la misma manera en la que lo haríamos sin este método de clase. Pero nosotros le pasamos solamente la marca y este ya le asigna que es un modelo deportivo.

	Finalmente, con el return no retorna el objeto, por lo que ahora nuestra variable *deportivo* será un objeto, tal como si lo creáramos como lo hicimos anteriormente.

	Por último, para comprobar que realmente el objeto se haya creado sin ningún problema, utilizamos nuestro método especial *\_\_str\_\_*, donde podremos manejar el output si queremos imprimir nuestro objeto.

	Con esto en mente, ahora podríamos crear un método que nos ayude a definir objetos de esta clase, para definir automóviles Sedán.

	![[IMG_327.png]]

	![[IMG_328.png]]

	**Variables de clase**

	Las variables de clase son las variables de la propia clase que comparten todos los objetos de una clase, teniendo esto en cuenta podríamos hacer un ejemplo donde no se creen objetos directamente, sino con un método estático y uno de clase, utilizaremos nuestro constructor para agregar contenido a una variable de clase.

	Lo que haríamos sería crear una clase donde vamos a tener una variable de clase donde vayamos a almacenar estudiantes, esto lo haremos con un método de clase para mandar a llamar a nuestro constructor, pero solo lo haremos si la edad del estudiante es mayor o igual a 18 años, por lo que haremos uso de un método estático para realizar esta comprobación.

	Primeramente, definimos nuestra clase y nuestro método de clase que nos ayudará a almacenar nuevos estudiantes:

	![[IMG_329.png]]

	Aquí primeramente tenemos nuestra clase, y con nuestro método de clase primeramente comprobamos si la edad que nos llegó para agregar un nuevo estudiante es mayor o igual a 18, para esto empleamos un método estático que solo recibirá la variable edad y verificara si es mayor o igual a 18, por lo que retornara un valor booleano (True o False) y con base en esto nuestro condicional entrará en el if si recibe True.

	![[IMG_330.png]]

	Aquí lo que estamos definiendo es que cuando nuestro constructor sea llamado, creará un objeto al cual le asignará el nombre y la edad indicados, finalmente el objeto lo almacenará en la lista, por lo que de forma indirecta estaríamos creando objetos de esta clase, que serían almacenados en una misma variable de clase, que en este caso es una lista.
	
	Por lo que nos faltaría que, si el estudiante es mayor a 18, se haga la llamada a la clase  para con el constructor crear el objeto y este se almacene, de no ser mayor de edad, entonces se imprimiría un mensaje indicando que el estudiante es menor de edad..

	![[IMG_331.png]]

	Con esto definido, finalmente solo nos faltaría llamar al método de clase, pasándole el nombre y edad de estudiantes a agregar:

	![[IMG_332.png]]

	Ahora, si lo ejecutáramos, gracias a nuestro print, veríamos a los estudiantes que son menores de edad y, por ende, su objeto no se crea ni se almacena en la variable de clase.

	![[IMG_333.png]]

	Ahora podríamos crear otro método estático, el que nos ayude a representar o mostrar por pantalla todos los estudiantes que sí fueron almacenados con éxito.

	![[IMG_334.png]]

	De esta manera, en nuestro método jugamos con enumerate para listar a nuestros estudiantes. Recordemos que enumerate nos crea un objeto iterable donde el primer elemento es el índice y el segundo lo almacenado en la lista.

	En este caso, utilizamos el argument *start* en enumerate, ya que Python comenzaría a contar desde el índice 0, pero *start* nos permite que, como se vaya mostrando en la variable i, sea a partir del número indicado.

	Para nuestro objeto, tendremos que llamarlo mediante la llamada de la clase, apuntando a su variable, por así decirlo. Al hacerlo así, al ir iterando, ahora el índice se almacenaría en *i* y el objeto en *estudiante*. Finalmente, para mostrar al estudiante, mostramos el número y el nombre del objeto.
	
	Finalmente, llamamos al método para listar a los estudiantes almacenados correctamente y al ejecutar el programa tendríamos lo siguiente:

	![[IMG_335.png]]

	Con esto vemos un claro ejemplo de una variable de clase, en donde vamos modificándola por cada objeto que vayamos creando y finalmente vemos cómo es una variable que comparten todos los objetos creados a partir de esta clase.

## **Comprendiendo mejor el uso de self**

1. **Introducción**

	El uso de self es uno de los aspectos más fundamentales y a la vez confusos para quienes se adentran en la Programación Orientada a Objetos (POO) en Python. Este identificador es crucial para entender cómo Python maneja los métodos y atributos dentro de sus clases y objetos.

	*Definición de self:*

	A nivel conceptual, *self* es una referencia al objeto actual dentro de la clase. Es el primer parámetro que pasa a cualquier método de una clase en Python. A través de *self* un método puede acceder y manipular los atributos del objeto y llamar a otros métodos dentro del mismo objeto.

	*Uso de self:*

	Cuando se crea una nueva instancia de una clase, Python pasa automáticamente la instancia recién creada como el primer argumento al método *\_\_init\_\_* y a otros métodos definidos en la clase que tienen *self* como su primer parámetro. Esto es lo que permite que un método opere con datos específicos del objeto y no con datos de la clase en general o de otras instancias de la clase/

	*Importancia de self:*

	El concepto de *self* es importante en la POO ya que asegura que los métodos y atributos se apliquen al objeto correcto. Sin self, no poriamos diferenciar entre las operaciones y datos de diferentes instancias de una clase.
	</br>
2. **Práctica**

	Comenzaremos creando una clase, donde vayamos inicializando su constructor y una instancia de esta:

	![[IMG_336.png]]

	Para esto, estamos creando una instancia *Marcelo* de la clase *Persona* y, por lo tanto, le pasaremos las propiedades o atributos del nombre y la edad.

	![[IMG_337.png]]

	Por lo tanto, aquí estaríamos creando este objeto y tendríamos que construirlo de alguna forma. Es por ello que tenemos nuestro método especial *\_\_init\_\_* que es nuestro constructor y aquí es donde como parámetro tendremos que pasarle *self*.

	Este, aunque no se lo pasemos nosotros, de forma directa, Python por detrás pasa el objeto y, por ende, mediante un parámetro *self* tendremos que recibirlo para poder trabajar con él y mediante el constructor asignar los atributos.

	Por ende, en este caso tendríamos nuestro self y otros dos parámetros, que serían el nombre y edad que pasaríamos como argumentos:

	![[IMG_338.png]]

	La forma en que podríamos verlo, es como si referenciáramos a la clase y de esta a nuestro método especial *\_\_init\_\_*, el cual es nuestro constructor, y como argumentos le estuviésemos pasando el objeto, el nombre y la edad:

	Persona.\_\_init\_\_(marcelo, nombre, edad)

	De esta manera, realmente al emplear *self*, lo que estamos haciendo es hacer referencia al objeto *marcelo* y un self.nombre, es exactamente lo mismo que marcelo.nombre

	Es por ello que podemos asignar y trabajar con los atributos empleando self:

	![[IMG_339.png]]

	Es por esto que al pasarlo, realmente en lugar de llamarlo *self*, podríamos llamarlo como deseemos y hacer referencia al objeto de la manera que mejor se nos acomode, pero por convenio y para que nuestro código tenga una mejor legibilidad, es recomendable como buena práctica utilizar *self*.

	Un ejemplo en donde además creemos un método donde se presente la persona, por así decirlo, haciendo ciertos cambios, sería lo mismo de lo que hemos visto hasta ahora:

	![[IMG_340.png]]

	![[IMG_341.png]]

	De esta manera, cada vez que utilizamos un método, pasamos indirectamente al objeto. La cosa cambia si utilizamos decoradores, ya que el decorador *@staticmethod* es independiente del objeto, pero el *@classmethod* es exactamente lo mismo que el que estamos viendo con *self*, la diferencia es que aquí hacemos referencia con *cls* y esto hace referencia directamente a la clase de la que está siendo llamada por así decirlo.

	Con el decorador *@staticmethod* podríamos trabajar también con objetos, pero es importante recordar que para poder utilizarlo se tendrá que definir el parámetro para ser pasado ahora, sí de forma directa.

	**Ejemplo con clase calculadora:**

	Ahora crearemos una clase calculadora, donde empezaremos definiendo su constructor y para hacerlo más entendible con la inicialización de una instancia (objeto).

	![[IMG_342.png]]

	De esta manera, se está pasando la referencia a nuestro objeto, la cual identificamos dentro de la clase empleando *self* como primer parámetro y el dato que le estamos pasando (el número 5) con el parámetro *num*.

	Es importante saber que, al crear funciones o métodos, las definiciones de variables dentro de los paréntesis se le llaman parámetros y argumentos a los datos que le pasamos al llamar a la función.

	En este caso, *self* y *num* son nuestros parámetros y  los argumentos serían el objeto y el número que se le vaya a pasar, en este caso *calc* y *5*. Visto de otra forma, la declaración de las variables dentro de los paréntesis son los parámetros y los datos que le pasamos para asignarle a esos parámetros serían los argumentos.

	Por último, completaríamos nuestro constructor para que le asigne el número a un atributo del objeto:

	![[IMG_343.png]]

	Ahora crearemos otro método el cual nos permita sumar un número al atributo *numero* que ya tenemos:

	![[IMG_344.png]]

	De esta manera se hace algo similar que con el constructor, pero los métodos normales no se utilizan para inicializar los atributos, sino para trabajar con ellos y modificarlos.

	Es por ello que inicializamos con nuestro constructor el atributo *numero* en 5, después con el método *suma* le sumamos el 10 que le pasamos como argumento y finalmente al imprimir nuestro atributo *numero* nos retorna la suma de estos dos:

	![[IMG_345.png]]

	**Método de doble suma:**

	Ahora creamos un método *doble_suma*. En este lo que haremos será permitir el paso de dos números y de esta manera aprovechar el método *suma* que ya está creado para realizar una suma con el número que ya está de forma individua para cada uno de los números que le pasemos, por lo que en lugar de modificar la variable directamente, solo imprimiremos el valor sin modificarla en el método *suma*:

	![[IMG_346.png]]

	![[IMG_347.png]]

	De esta manera, es como aprovechar el uso de *self*, pasando entre métodos la referencia de nuestro objeto *calc* todo el tiempo para manejar los atributos de este.

	Recordemos que lo que está seguido de la almohadilla son comentarios en Python, lo que quiere decir que será contenido que no tomará en cuenta al ejecutar el programa.

	De esta manera, entendiendo el concepto, ahora sí realizaríamos la doble suma, ya que sumariamos el resultado de estas dos sumas individuales y lo imprimiríamos en pantalla.

	Para que esto funcione, recordemos que tendremos que recuperar los valores y no imprimirlos en pantalla. Es por ello que los resultados de las sumas individuales los recuperaremos con *return* y ahora sí podremos sumar ambos para tener un resultado final, que en este caso sería "7+15":

	![[IMG_348.png]]


## **Herencia y polimorfismo**

1. **Introducción**

	La herencia y polimorfismo son conceptos fundamentales en la programación orientada a objetos, que permiten la creación de una estructura de clases flexible y reutilizable.

	*Herencia:*

	Es un principio de la POO que permite a una clase heredar atributos y métodos de una clase, conocida como su clase base o superclase. La herencia facilita la reutilización de código y creación de una jerarquía de clases. Las subclases heredan las características de la superclase, lo que permite que se especialicen o modifiquen comportamientos existentes.

	*Polimorfismo:*

	Este concepto se refiere a la habilidad de objetos de diferentes clases de ser tratados como instancias de una clase común. El polimorfismo permite que una función o método interactúe con objetos de diferentes clases y los trate como si fueran del mismo tipo, siempre y cuando compartan la misma interfaz o método. Esto significa que el mismo método puede comportarse de manera diferentes en distintas clases, un concepto conocido como sobrecarga de métodos.

	Ambos, herencia y polimorfismo, son piedras angulares en la POO y son ampliamente utilizados para diseñar sistemas que son fácilmente extensibles y mantenibles.
	</br>
2. **Práctica:**

	*Herencia:*

	La herencia es la forma que tenemos de crear subclase de una clase base o superclase, lo que podríamos traducirlo a crear una copia directa de una clase base, la cual podremos modificar.

	Para tener más claro este concepto, empezaremos creando una clase *Animal*, donde su constructor definirá el atributo del nombre:

	![[IMG_349.png]]

	De esta manera, estaríamos creando la clase Animal con su atributo *nombre*, donde  estamos creando dos objetos, *gato* y *perro* con un  nombre propio.

	Ahora crearíamos un método de hablar, pensando para que el gato diga "¡Miau!":

	![[IMG_350.png]]

	Aquí, al utilizar el método para *gato* y *perro* notaríamos un problema y es que para ambos se imprime MIAU, pero un gato dice GUAU.

	Teniendo esto, no sería algo escalable para, basándonos en el tipo de animal que estemos creando, el sonido que este haga sea distinto. Aquí es donde entra la herencia y, en lugar de tener creada de esta forma nuestro método *hablar*, lo que haríamos sería colocar *pass*:

	![[IMG_351.png]]

	De esta manera, sería como una indicación de que tendríamos que crear este método para subclases, definiendo así qué hará. Recordemos que *pass* nos permite generar una definición sin que esta haga nada para que no dé error.

	Entonces, el crearla sería como una definición de qué se tiene que crear en subclases con las indicaciones correspondientes.

	El decorador utilizado *@property*. Recordemos que lo utilizamos simplemente para poder llamar a un método como si de una propiedad o atributo se tratara, que sería sin utilizar los *()* ya que no le estamos pasando argumentos por el momento.

	*Aplicando la herencia:*

	Teniendo esto en cuenta, lo que haríamos sería crear dos clases que hereden los atributos y métodos de la clase base *Animal*:

	![[IMG_352.png]]

	De esta manera, la clase *Gato* y *Perro* ahora serían subclases de la clase *Animal* y tendrían exactamente los mismos atributos y métodos.

	Aquí lo que podremos hacer sería "modificar" un método creado. Esto solo lo modificaría para la subclase, pero el método en la clase principal seguiría siendo el mismo que contiene únicamente *pass*.

	![[IMG_353.png]]

	Ahora, la forma de crear el objeto también cambiará, ya que ahora en lugar de llamar directamente a la clase principal, llamaríamos a la subclase indicada y se podría decir que está de forma indirecta llama a la clase principal para crear el objeto, pero todos los métodos y atributos modificados o agregados en la subclase serán los que se aplicarán:

	![[IMG_354.png]]

	De esta manera, al llamar al método *hablar*, como la instancia se creó con la subclase correspondiente, retornarán lo esperado.

	Aquí podríamos jugar con *raise* para lanzar un error en caso de que se intente acceder al método *hablar* desde la clase principal, donde nos muestre un mensaje:

	![[IMG_355.png]]

	De esta manera, al crear una instancia *nutria* de la clase principal, al acceder al método, vemos que nos lanza el error que generamos con el output indicado.

	*Polimorfismo:*

	Para implementar el polimorfismo tendremos que hacerlo de una forma un tanto distinta.

	Podríamos generar una función fuera de las clases, la cual reciba un objeto y, por ejemplo, en este caso, ejecutar el método *hablar* desde esta misma.

	![[IMG_356.png]]

	Aquí modificamos el método *hablar* para que solo tenga lo que queremos que el animal vaya a decir, por ello mediante nuestra función *hacer_hablar* definimos que nos imprima en pantalla un texto donde basándose en el objeto que le fue pasado acceda al nombre y a este método, teniendo así el mismo output pero accediendo a la información del objeto desde una función. Lo cual sería emplear polimorfismo.

	Entonces, teniendo esto en cuenta, nuestra función puede acceder y trabajar con la información de estas clases.

	*Ejemplo con clase Automovil:*

	![[IMG_357.png]]

	De esta manera, estamos creando la clase *Automovil* en la que como atributos tenemos la marca y el modelo. En nuestro método *describir* buscamos mostrar una descripción del vehículo, pero al ser un coche y una moto, podría gustarnos que se mostrara qué tipo de automóvil es.

	¡Entonces aquí sería un buen caso de aplicar herencia y polimorfismo!

	![[IMG_358.png]]

	De esta forma creamos dos subclases que son heredadas de la clase base *Automovil* y modificamos para cada una de la forma correspondientes el método *describir*.

	Por ende, al crear los objetos, tendremos que referenciar a la subclase correspondiente:

	![[IMG_359.png]]

	![[IMG_360.png]]

	Si quisiéramos hacerlo empleando polimorfismo, tendríamos que crear una función a la que le pasemos el objeto para acceder a las propiedades de estos y con estas imprimir lo que queremos:

	![[IMG_361.png]]

	De esta manera, estaríamos haciendo lo mismo, pero ahora empleando el polimorfismo gracias a la función accediendo a los valores mediante esta al recibir el objeto.

	*Ejemplo con clase Dispositivo:*

	Creamos nuestra clase principal *Dispositivo* con su constructor y un método *abstracto*, lo cual quiere decir que crearemos un método que no tendrá un contenido en la clase principal, podremos dejarlo definido con *pass* o agregar un error con *raise* para que nos retorne el mensaje de que tiene que ser definido en las subclases.

	![[IMG_362.png]]

	De esta forma, *escanear_vulnerabilidades*, sería un método abstracto.

	De esta forma, ahora podríamos crear subclases donde retornaríamos resultados de casos hipotéticos donde se haya escaneado un tipo de dispositivo en busca de vulnerabilidades:

	![[IMG_363.png]]

	Con esto listo, podríamos empezar a crear nuestros objetos, donde, basándonos en el dispositivo, crearemos la instancia con la subclase correspondiente:

	Empezaremos creando un objetos para cada subclase y jugando con polimorfismo crearemos una función que, con base en el objeto que le pasemos, nos liste la información correspondiente en pantalla:

	![[IMG_364.png]]

	De esta manera podríamos para cada dispositivo acceder a su "escaneo de vulnerabilidades" y listarlo, listando el modelo antes.

	Lo cual, al efectuarlo para cada objeto, sería de la siguiente manera:

	![[IMG_365.png]]

	Recordemos agregar la *f* en el string para setearlo correctamente con variables, métodos, funciones...

	De esta forma tendríamos todo de una forma mucho más organizada y que nos permitiría reutilizarlo para crear múltiples instancias de una misma subclase.

	*Pasar por el método de la clase base y subclase:*

	Cuando nosotros utilizamos la herencia, modificamos algunos métodos y, por ende, ya no se tiene en cuenta el que fue definido en la clase base, sino el nuevo que ahora está definido en la subclase.

	Esto lo podríamos ver mejor con el siguiente ejemplo:

	![[IMG_366.png]]

	De esta manera, estamos inicializando primeramente un objeto de la clase A con el constructor, por ello, nos muestra el mensaje de que se está inicializando.

	Luego creamos un objeto *b* desde la subclase B y esta es una herencia de la clase A, dentro de esta se modifica el constructor y, por ende, solo tendrá en cuenta el constructor dentro de la subclase, por lo que solo nos muestra que se está inicializando B.

	Podremos toparnos con casos donde nos interese que lo que esté definido en la clase base también se aplique, pasando por ese método, teniendo de esta manera que pase por el método de la clase base y por el método modificado de la subclase.

	Para ello tendremos que hacer uso de *super()* para forzar que pase por el método que tiene el mismo nombre en la clase base, a pesar de que fue modificado para ser aplicado en la subclase de forma distinta, teniendo como resultado que pasa por ambos:

	![[IMG_367.png]]

	Como es notable, con *super()*, tendremos que hacer referencia al método que nos interesa con el nombre, y efectuará el método de la forma en la que esté definida en la clase base.

	En este caso aplica dos cosas, porque entra en nuestro método para inicializar el objeto e imprime lo indicado para la subclase, pero como luego con super definimos que también ejecute el constructor de la clase base, por ello se imprimen los dos mensajes, porque estaría pasando por ambos constructores.

	*Jugando con super() de una forma más práctica:*

	![[IMG_368.png]]

	De esta manera, nuestra clase base está programada solamente para poder trabajar con un parámetro, pero en nuestra subclase estamos definiendo que puede trabajar con dos, por ello es reutilizado el constructor de nuestra clase principal para que asigne el primer valor y en nuestra subclase asignamos el segundo de forma directa.

	No tienen porque ser los constructores, realmente esto funcionaría con cualquier método.

	![[IMG_369.png]]

	De esta forma, en nuestro método *saludo()* de la subclase, estamos definiendo que se ejecute el método *saludo()* de la clase base y que el string que es retornado lo almacene en la variable *original*.

	Por ello, después imprimiremos en pantalla este string, agregándole que también se está haciendo el saludo desde B.

	*Ejemplo más práctico:*

	![[IMG_370.png]]

	De esta manera modificamos los métodos existentes en la clase base para que sean distintos en la subclase, pero también reutilizamos los de la clase base para que nos almacene el nombre y edad, así como para recuperar el mensaje de quién es y la edad que tiene.


## **Encapsulamiento y métodos especiales**

1. **Introducción**

	El encapsulamiento en la programación orientada a objetos (POO) maneja principalmente tres niveles de visibilidad para los atributos y métodos de una clase: públicos, protegidos y privados. En Python, esta distinción se realiza mediante convenciones en la nomenclatura, más que a través de estrictas restricciones de acceso como en otros lenguajes.

	*Atributos Públicos:*

	Son accesibles desde cualquier parte del programa y, por convención, no tienen un prefijo especial. Se espera que estos atributos sean parte de la interfaz permanente de la clase.

	*Atributos Protegidos:*

	Se indica con un único guion bajo al principio del nombre (por ejemplo, *\_atributo*). Esto es solo una convención y no impide el acceso desde fuera de la clase, pero se entiende que esto atributos están protegidos y no deberían ser accesibles directamente, excepto dentro de la propia clase y en subclases.

	*Atributos Privados:*

	En Python, los atributos privados se indican con un doble guion bajo al principio del nombre (por ejemplo, *\_\_atributo*). Esto activa un mecanismo de cambio de nombre conocido como *name mangling*, donde el intérprete de Python altera internamente el nombre del atributo para hacer más difícil el acceso desde fuera de la clase.

	*Métodos Especiales:*

	Los métodos especiales en Python son también conocidos como métodos mágicos y son identificados por doble guion bajo al inicio y al final (*\_\_metodo\_\_*). Permiten a las clases en Python emular el comportamiento de los tipos incorporados y responder a operadores específicos. Por ejemplo el metodo *\_\_init\_\_* se utiliza para inicializar una nueva instancia de una clase, *\_\_str\_\_*  se invoca para una representación en forma de cadena legible del objeto y *\_\_len\_\_* devuelve la longitud del objeto.


	Algunos métodos especiales importantes en POO son:

	* *\_\_init\_\_(self, \[...\])*: Inicializa una nueva instancia de la clase.
	* *\_\_str\_\_(self):* Devuelve una representación en cadena de texto del objeto, invocado por la función *str(object)* y *print*
	* *\_\_repr\_\_(self):* Devuelve una representación del objeto que debería, en teoría, ser una expresión válida de Python, invocado por la función *repr(object)*
	* *\_\_eq\_\_(self, other):* Define un comportamiento del operador de igualdad *\=\=*
	* *\_\_lt\_\_(self, other), \_\_le\_\_(self, other), \_\_gt\_\_(self, other), \_\_ge\_\_(self, other):* Definen el comportamiento de los operadores de comparación(**<**, **<=**, **>** y **>=** respectivamente).
	* *\_\_add\_\_(self, other), \_\_sub\_\_(self, other), \_\_mul\_\_(self, other), etc.:* Definen el comportamiento de los operadores aritméticos (**+**, **–**, \*, etc.).

	El encapsulamiento y los métodos especiales son herramientas poderosas que, cuando se utilizan correctamente, pueden mejorar la seguridad, la flexibilidad y la claridad en la construcción de aplicaciones.
	</br>
2. **Práctica**

	**Encapsulamiento en Python:**

	El encapsulamiento en la POO nos permitirá restringir el acceso a ciertas partes o componentes de un objeto, sobre todo si se intenta acceder a estos desde fuera de la clase (funciones externas, por ejemplo).

	*Atributos protegidos:*
	
	Para ver esto comenzaremos creando nuestra clase *Ejemplo* y su constructor:

	![[IMG_371.png]]

	En este caso no estamos pasando ningún argumento a los parámetros de nuestro constructor, más que internamente Python el objeto cuando este es creado, por ello el uso de self.

	Dentro de nuestro constructor estamos creando un atributo protegido, este lo definimos de la misma manera que los demás, pero la diferencia es que al inicio se le colocara un guion bajo *\_* (*\_atributo*). Estos son utilizados más por convenio, indicando que no debería accederse o hacer referencia a este atributo desde fuera de la clase, aunque es posible, por convenio, no deberías hacerlo, ya que fue construido así para alguna funcionalidad de programa.

	Si hacemos referencia a este fuera de la clase, funcionaria:

	![[IMG_372.png]]

	Pero como ya se mencionó, por convenio no debe de hacerse cuando un atributo se define como protegido. Esto es considerado como buenas prácticas para generar un mejor código legible y organizado.

	*Atributos privados:*

	Para crear un atributo privado le agregaremos dos guiones bajos al inicio (*\_\_atributo\_privado*), este cambia un poco en cuanto al atributo protegido, ya que este no puede ser accedido directamente desde fuera de la clase:

	![[IMG_373.png]]

	Aquí lo que realmente sucede es que al definir un atributo privado Python, por detrás lo que hace es aplicar un concepto llamado *name mangling*, este básicamente cambia el nombre del atributo para que no sea posible acceder a este de forma tan fácil.

	Lo que hace es como hacer una reasignación del nombre, donde al inicio colocara un guion bajo seguido del nombre de la clase y después el nombre del atributo, quedando *\_Clase\_\_atributo_privado*, por lo que si intentáramos acceder a este atributo de esta manera, ahora si podríamos:

	![[IMG_374.png]]

	Entonces realmente el atributo privado existe pero Python por detrás hace un tipo de reasignación de nombre para que tenga una mayor seguridad y no se pueda acceder tan fácil fuera de la clase.

	**Ejemplos prácticos:**

	*Practicando con un atributo privado:*

	Crearemos una clase *Coche* en al cual definiremos los atributos *marca* y *modelo* y los pasaremos mediante nuestro constructor, pero también definiremos un atributo privado, el cual sea *\_\_kilometraje*:

	![[IMG_375.png]]

	Con esto crearemos un método *conducir*, al cual le pasaremos una cantidad y con base en eso el kilometraje del auto cambiará:

	![[IMG_376.png]]

	De esta manera los kilómetros cambiarán o aumentarán, siempre y cuando le ingresemos una cantidad positiva de kilómetros, ya que no tendría sentido el querer aumentar una cantidad negativa o menor a cero.

	Con esto el cambio se haría pero no lo visualizaríamos en pantalla al ejecutar el código, es por ello que ahora generaríamos un método el cual nos muestre por pantalla el kilometraje:

	![[IMG_377.png]]

	De esta manera, podremos observar que el objetivo de los atributos privados es que solo se pueda trabajar con ellos dentro de la clase y no fuera de ella, por ello el acceso a un atributo privado se hace un poco más complejo cuando se quiere hacer fuera de la clase, porque no deberías de hacerlo.

	Prácticamente, la idea de un atributo privado, es como crear un atributo que se desconoce para todo el programa fuera de la clase.

	**Métodos especiales**

	*\_\_str\_\_:*

	Empezaremos creando una clase *Libro*, donde inicialicemos un objeto con autor y  título, luego intentaremos imprimir el objeto que crearemos de la clase Libro:

	![[IMG_378.png]]

	De esta manera, al querer imprimir el objeto, lo que es retornado es la información de que en efecto estamos intentando imprimir un objeto.

	Aquí es donde entra el método especial *\_\_str\_\_*, que nos permite controlar el retornar algo específico al querer imprimir un objeto, por ende podremos retornar alguna cadena de texto específica la cual podremos imprimir:

	![[IMG_379.png]]

	De esta manera podremos controlar lo que será retornado al querer trabajar directamente con el objeto, en este caso nos retorna la cadena que hemos definido y la imprimimos para ver la información sobre este objeto en específico.

	Por ende, al trabajar con más objetos y querer imprimirlos, nos mostrará la información del objeto correspondiente:

	![[IMG_380.png]]

	**Método especial \_\_eq\_\_**

	Este método lo podemos utilizar para que directamente sea llamado en caso de querer definir comparaciones directas entre objetos, en donde se harán ciertas comparaciones de algunos atributos específicos que hayamos definido accediendo directamente a este si está definido, de lo contrario retornará algo, pero siempre será lo mismo al no estar definido.

	![[IMG_381.png]]

	De esta manera, al "igualar" ambos objetos en nuestro string a mostrar en pantalla, se manda a llamar a la función especial *\_\_eq\_\_*, donde tenemos definido que se reciben ambos objetos y esto retornara un valor booleano si el título y autor son iguales en ambos libros.

	Una forma que podría dejarnos más claro lo que se hace por detrás al comparar dos objetos *objeto1 \=\= objeto2*, es que se hace referenciando directamente a la clase y al método especial, donde como argumentos se pasan los objetos: *Clase.\_\_eq\_\_(objeto1, objeto2)*

	*Ejemplo aplicando encapsulamiento y métodos especiales:*

	Crearemos una clase *CuentaBancaria*, la cual como atributos tenga el número de cuenta, titular, como atributos públicos. El atributo saldo que se deberá inicializar en cero si no le es pasado ese argumento y lo pondremos como atributo privado.

	![[IMG_382.png]]

	Con esto ahora tendremos en mente crear los métodos *depositar_dinero*, *retirar_dinero* y *mostrar_dinero*.

	*Método depositar_dinero:*

	En este definiremos que incrementaremos el saldo actual solo si la cantidad que el usuario quiere ingresar en mayor a cero, de lo contrario imprimiremos un mensaje en pantalla de que es incorrecto.

	![[IMG_383.png]]

	*Método retirar_dinero:*

	Para tirar dinero, mantendremos el condicional que nos ayuda a verificar que la cantidad que se quiere retirar sea positiva, pero además tendremos que agregar uno donde nos retire el dinero solamente si la cantidad que vamos a retirar es menor al saldo actual en nuestra cuenta, por ende nunca podremos retirar más dinero del que tenemos en la cuenta y de intentarlo el programa nos lanzaría un mensaje.

	![[IMG_384.png]]

	*Método mostrar_dinero:*

	En este nos imprimirá el saldo actual en la cuenta mediante una cadena de texto para verlo de una mejor manera en pantalla.

	![[IMG_385.png]]

	Ahora, para verificar el funcionamiento de todo esto, crearemos un objeto de la clase y utilizaremos los métodos agregando dinero, retirando dinero e imprimiendo el saldo actual:

	![[IMG_386.png]]

	*Recibir múltiples argumentos en una sola variable:*

	Podremos recibir múltiples argumentos para un método o función de forma sencilla con un *\** y este será almacenado en una variable en forma de *tupla*, por lo que un ejemplo sería el siguiente, donde, después de inicializarlo, crearemos un método que nos muestre todas las frutas iterando en la tupla:

	![[IMG_387.png]]

	De esta manera, sin importar cuantos argumentos agreguemos, todos serán almacenados en el parámetro *items* gracias a que colocamos un asterisco antes y esto será almacenado en una tupla.

	Con base en esto, podríamos requerir de llegar a mostrar la longitud de nuestra tupla, pero claramente aquí no funcionaría hacer directamente uso del método *len()* sobre el objeto. Si bien podríamos hacerlo de forma indirecta generando un método solamente para eso, ya tenemos un método especial *\_\_len\_\_*, el cual nos puede ayudar a definir este comportamiento.

	![[IMG_388.png]]

	De esta manera, aprovechando el uso de este método especial, podremos hacer directamente *len()* sobre el objeto y esto llamará a la función *\_\_len\_\_* si está definida y retornará lo que nosotros le indiquemos, en este caso retornamos la longitud de la tupla, aplicándole directamente el método *len()* a la tupla.

	*Ejemplo con clase Pizza:*

	Crearemos una clase *Pizza* donde, como argumentos primeramente, le pasemos una longitud para la pizza en centímetros y después una serie de ingredientes que esta llevará:

	![[IMG_389.png]]

	Ahora, con un método *descripcion*, haremos que nos muestre en pantalla un mensaje con la longitud de la pizza, así como con el contenido de la tupla que son los ingredientes, pero con el uso del *' '.join()* hacemos que se nos muestre todo el contenido de la tupla separado por comas solamente.

	Recordemos que esto también lo llegamos a aplicar con los conjuntos, para tener una vista más limpia al momento de listar algún contenido.

	![[IMG_390.png]]

	*Método especial \_\_getitem\_\_:*

	Si nosotros creáramos una clase en la cual tenemos una lista, podríamos acceder a sus índices de forma individual si referenciamos a la variable y a un índice en concreto:

	![[IMG_391.png]]

	Esto mismo podríamos aplicarlo pasando directamente al objeto el índice sin referenciar a la lista de forma directa, lo cual llamaría directamente al método especial *\_\_getitem\_\_* donde recibe el objeto como cualquier otro método  y el índice como si de un argumento se tratase, después tú defines referenciando a la lista y el índice como lo visto anteriormente y retornamos el dato correspondiente:

	![[IMG_392.png]]

	*Método especial \_\_call\_\_:*

	El método especial *\_\_call\_\_* nos puede servir para pasar un argumento al objeto también, ya que una vez creado un objeto, podremos después utilizar este objeto pasándole un argumento. Esto entrará en la función especial *\_\_call\_\_* y hará lo que nosotros deseemos definir con este argumento.

	En este caso crearemos una clase *Saludo* en esta definiremos constructor donde el saludo será un *hola*, con esto al crear nuestro objeto le pasaríamos un nombre, por lo que entraría al método especial *\_\_call\_\_* donde recibiremos este nombre y con el uso de self recuperaremos el *hola* y agregaremos el nombre al final para retornarlo e imprimirlo desde donde se llamó a la función especial:

	![[IMG_393.png]]

	*Método especial \_\_add\_\_:*

	Este método especial nos puede servir, por ejemplo, suponiendo que tenemos una clase *Punto* a la cual le pasamos como argumentos *x* y *y*, donde creamos dos objetos que tengan estos valores y queremos que para ambos objetos nos realice la suma de ambos en *x* y ambos en *y*:

	![[IMG_394.png]]

	Ahora mismo solo tenemos *self* como parámetro en nuestro método especial, pero al utilizar estos métodos recordemos que se le pasan ambos objetos, por lo que también tendríamos que recibir el segundo objeto, lo dejaremos como *otro* en este caso.

	Y aquí tendremos que indicar cómo sumar *x* y *y* de ambos objetos:

	![[IMG_395.png]]

	Aquí vemos que se realiza la suma de x con x, y con y para ambos objetos, pero de una forma un tanto interesante.

	Podríamos hacerlo y retornar una lista donde simplemente el índice 0 sea la suma de *x* y el 1 la suma de *y*, pero ya que tenemos la clase, la reutilizamos para generar una nueva instancia, la cual nos almacenará la suma de los objetos.

	De esta forma, ahora al imprimir el contenido, como no estamos retornando un string, sino un objeto, podremos ver cómo aquí requerimos del método especial *\_\_str\_\_*, ya que este nos viene bien al querer listar directamente un objeto:

	![[IMG_396.png]]

	De esta manera habremos creado una forma de sumar los dos puntos de dos objetos. Es importante mencionar que el objeto que se retorna al utilizar el operador *+*, sería como un objeto temporal en este caso, esto se debe a que nos es retornado un objeto y nosotros "imprimimos su contenido", pero en ningún momento lo estamos almacenando como los objetos que solemos crear, por ende al salir del print no habría forma de volver a referenciarlo, al menos de que lo almacenemos como al crear uno con *p3 = p1 + p2* y finalmente listemos en objeto *p3*.

	*Ejemplo final:*

	Vamos a crear un objeto de una clase, donde le pasaremos un valor y estaremos considerando que lo vamos a tratar como si de un iterable se tratase:

	![[IMG_397.png]]

	Nuestro constructor lo crearíamos como anteriormente, considerando que el valor que nos es pasado será el *límite*:

	![[IMG_398.png]]

	Para poder jugar con esto, tendríamos que convertir nuestro objeto a un iterable, por lo que aquí es donde utilizamos el método especial *\_\_iter\_\_*, donde este método devolverá un iterador que sería el propio objeto.

	Dentro de nuestro método especial *\_\_iter\_\_* tendremos que definir la inicialización de un contador para generar nuestro iterador, así como ya previamente definir que retornaremos el propio objeto:

	![[IMG_399.png]]

	Luego, utilizaremos un método especial *\_\_next\_\_*, el cual nos ayudara a definir que sucederá en cada iteración que realice el bucle, por lo que aquí definiremos un condicional que hará una funcionalidad similar a cuando termina el bucle *while*, ya que nuestro condicional verificara si el atributo contador es menor al atributo límite en cada iteración:

	![[IMG_400.png]]

	De esta forma, vamos a definir que cada que el atributo contador sea menor al atributo límite, nos aumente en uno el contador y nos retorne el contador, para que la reciba la variable *i* de nuestro bucle ya definido:

	![[IMG_401.png]]

	De esta manera ya nos funcionaría correctamente y nos imprimiría los valores uno a uno, pero aún nos faltará definir qué hará el *else*, ya que si este no lo colocamos, sería como si se estuviese iterando infinitamente, solo que sin que se cumpla el condicional.

	Aquí es donde lanzamos con *raise* una forma especial de en estos casos detener el iterador, de la siguiente manera:

	![[IMG_402.png]]

	Podríamos considerar una forma de entenderlo que al efectuar el bucle *for* entra al método especial *\_\_iter\_\_*, aquí aprovechando inicializamos nuestro contador y le retorna el mismo objeto al bucle con la capacidad de iterarlo. De ahí solo faltaría definir qué hace el objeto en cada iteración con *\_\_next\_\_*, que en este caso incrementamos el contador. (Así lo entendí yo :D)

## **Decoradores y popiedades**

1. **Introducción:**

	*Decoradores:*

	Los decoradores en Python son una forma elegante de modificar las funciones o métodos. Se utilizan para extender o alterar el comportamiento de la función sin cambiar su código fuente. Un decorador en si mismo es una función que toma otra función como argumento y devuelve una nueva función que, opcionalmente, puede agregar una funcionalidad antes y después de la función original.

	*Propiedades:*

	Las propiedades son un caso especial de decoradores que permiten a los desarrolladores añadir *getter*,  *setter*  y *deleter* a los atributos de una clase de manera elegante, controlando así el acceso y modificación de los datos.

	En Python esto se logra con el decorador *@property*, que transforma un metodo para acceder a un atributo como si fuera un atributo público.

	*Getter y Setters:*

	* El *getter* obtiene un valor de un atributo manteniendo el encapsulamiento y permitiendo que se ejecute una lógica adicional durante el acceso.
	* El *setter* establece el valor de un atributo y puede incluir validación o procesamiento antes de que el cambio se refleje en el estado interno del objeto.
	* El *deleter* puede ser utilizado para definir un comportamiento cuando cuando un atributo es eliminado con *del*.

	Es importante saber cómo los decoradores pueden ser aplicados no solo para métodos y propiedades, sino también para funciones en general. También exploraremos cómo las propiedades se pueden utilizar para crear una interfaz pública para atributos privados/protegidos, mejorando la encapsulación y manteniendo la integridad de los datos de una clase.
	</br>
2. **Práctica:**

	*Decoradores:*

	Para estos ejemplos se emplearán directamente funciones y no clases, para que quede un poco más claro.

	Nosotros tenemos la posibilidad de crear decoradores para funciones. La forma en la que funcionan es que nos permiten alterar el comportamiento que vaya a tener una función o clase, sin alterar el código de esa función, si no tener la capacidad de agregar otras funcionalidades en su ejecución.

	Primeramente, crearemos una función *Saludo* que nos imprima por pantalla un mensaje:

	![[IMG_403.png]]

	De esta forma, tendríamos un código sencillo que nos imprimiría por pantalla el mensaje indicado. Pero también podremos crear un decorador propio, el cual se definirá como si de una función se tratase y se utilizara con la función *Saludo* tal como se utilizan los decoradores que hemos visto para los métodos de clases:

	Es importante mencionar que a las funciones que son decoradores se les llama *Función de orden superior*.

	![[IMG_404.png]]

	La idea es que dentro de nuestra función de orden superior va a haber un tipo de envoltura, ya que dentro de esta se creará una nueva función, la cual se puede llamar como deseemos, pero para un mayor entendimiento, le llamaremos *envoltura* y esta retornará *envoltura*, ya que así se debe definir para su funcionamiento correcto:

	![[IMG_405.png]]

	Ahora, la idea aquí es que nuestra función de orden superior debe tener un parámetro, ya que este hará directamente referencia a nuestra función a la que se esté aplicando el decorador y esta misma nos permitirá que realmente ahora nuestra función *envoltura* ahora pase a ser prácticamente la función *Saludo*, ya que será la que se ejecute en lugar de *Saludo*.

	Con esto en mente, podremos definir lo que sea que queramos que se ejecute y luego referenciar a nuestro parámetro el cual realmente es la función *Saludo* original, por lo que al efectuar *funcion()* se ejecuta directamente, lo que nos permite efectuar acciones antes y después de una funcion ya definida:

	![[IMG_406.png]]

	El retorno de la envoltura tendrá que ser dentro de la función de orden superior y no dentro de la propia envoltura o dará error.

	Por lo que con esta función *Saludo*, hemos expandido su funcionalidad gracias a un decorador que hemos creado.

	*Propiedades:*

	Cuando creamos una propiedad en Python con el decorador *@property*, tenemos algo llamado *getters y setter* lo cual es muy importante en el ámbito de las clases, ya que nos permite tener un mejor control sobre nuestros atributos.

	Para una práctica con esto, crearemos una clase *Persona* de la cual podremos crear objetos con los atributos, nombre y edad.

	Pero en la hora de realizar las asignaciones en nuestro constructor, vamos a definir estos atributos como protegidos:

	![[IMG_407.png]]

	Entonces aquí, si bien es posible poder modificar el contenido de los atributos fuera de la clase, a pesar de ser protegidos. No es una buena práctica, y con programadores que ya tengan más nivel sería un error fatal.

	Entonces, si llegáramos a querer modificar estos valores fuera de la clase, aquí es donde entran en juego las propiedades y los *getters* y *setters*.

	Estos se definen como propiedades, principalmente el *getter* el cual nos servirá para llamar desde fuera de la funcion y dentro de la funcion como un método lo que hará será acceder al atributo protegido y nos lo retornara, de esta manera ahora si estaría correcto aplicarlo porque se accede al atributo de forma directa dentro de la funcion y se retorna su valor:

	![[IMG_408.png]]

	De esta manera, estamos definiendo primero nuestro getter el cual solo nos retorna la información que contiene el atributo protegido *edad* y después se crea el setter con el decorador *\@edad.setter* y este lo que nos permite es reasignar el valor de este atributo protegido.

	En el setter lo que hacemos es verificar que el valor que se le quiere asignar como edad sea mayor a cero, de lo contraria nos lanzará una excepción de *ValueError* con el mensaje correspondiente.  
  
	De esta manera ya podríamos manejar de forma sencilla desde fuera de la clase el contenido del atributo protegido, teniendo buenas prácticas en nuestro código basándonos en el convenio de Python.

	Por lo que si ingresamos una "edad" negativa, esto nos lanzaría la excepción creada:

	![[IMG_409.png]]

	Por ende ahora sabemos de una buena práctica con base en *propiedades* para trabajar con los atributos protegidos y privados de una clase, ya que acceder a estos de forma directa desde fuera de la clase, se puede considerar una mala práctica.

	*Ejemplo con decoradores y la librería time:*

	Primeramente, importaremos la librería *time*:

	![[IMG_410.png]]

	Esta nos servirá en este caso para hacer lo mismo que en bash cuando queremos que el script espere ciertos segundos, lo cual logramos con *time.sleep(segundos)*

	Teniendo esto en cuenta, crearemos dos funciones, una que espere un tiempo corto y otra que espere más tiempo:

	![[IMG_411.png]]

	De esta manera queda en espera en total 3 segundos, ya que entre ambas funciones definimos que sean 3 segundos, 2 en una y 1 en otra.

	Solo veremos el cursor y podremos pensar que no sabemos que está sucediendo, por así decirlo. Entonces aquí podríamos aplicar decoradores.

	De esta manera, teniendo en cuenta la estructura, vamos a crear un decorador "cronometro" el cual recibirá la función a la que se esté aplicación y en nuestra envoltura será llamada, pero realizando una modificación para cambiar el comportamiento:

	![[IMG_412.png]]

	Ahora, antes de continuar. Para generar nuestro decorador cambiando el comportamiento de la función original, vamos a trabajar con la librería *time* y jugaremos con *time.time()*

	Si ejecutáramos esto en Python, nos retorna cierto tiempo representado en segundos. Este tiempo sé el tiempo que ha pasado desde cierto punto en el tiempo como referencia, lo que quiere decir que es el tiempo que ha pasado desde cierto año tomado como referencia, representado en segundos. A este punto de referencia se le conoce como *epoch* y la fecha de este es el 1 de enero de 1970.

	![[IMG_413.png]]

	De esta manera, podríamos tener el tiempo en el que se inicia el "cronometro" y almacenarlo y una vez se detiene, podremos almacenar ese tiempo final y restarle el tiempo inicial, de esta manera podríamos representar el tiempo que ha transcurrido:

	![[IMG_414.png]]

	Con esto en mente, ahora podríamos definir en nuestra envoltura  un inicio antes de ejecutar nuestra función original y un final cuando se ha terminado de ejecutar.

	Para representar el tiempo transcurrido podremos mostrar un mensaje en pantalla, además podremos referenciar directamente a la función para obtener el nombre de esta con *funcion.\_\_name\_\_*, de esta manera nos quedaría lo siguiente:

	![[IMG_415.png]]

	Como podremos observar, el tiempo transcurrido no es exactamente 1 segundo o 2 segundos, ya que siempre habrá algunos milisegundos de por medio cada vez que utilicemos un sleep y no siempre serán los mismos:

	![[IMG_416.png]]

	Ahora, ¿Qué pasaría si en lugar de que el sleep sea directamente *1*, lo definimos para que se le pueda pasar un argumento y este pueda ser el número que deseemos?

	![[IMG_417.png]]

	Si estuviésemos empleando solamente las funciones sin decoradores, esto no sería un problema. Como estamos utilizando decoradores, nuestra envoltura también tendrá que tener en cuenta este argumento para al momento de llamar la función pasárselo y funcionar correctamente, por lo que tendríamos que definirlo en nuestra envoltura (puede ser con otro nombre) y pasárselo a la llamada de nuestra función original:

	![[IMG_418.png]]

	De esta manera ahora nosotros podríamos pasarle los segundos que deseemos como argumento al momento de llamar cada función y funcionaria de la misma manera:

	![[IMG_419.png]]

	*Recibir múltiples valores de clave-valor:*

	Como ejemplo rápido, sin ninguna funcionalidad. Sabemos qué podremos pasar múltiples argumentos cuando definimos nuestro parámetro con un *\** al inicio:

	![[IMG_420.png]]

	De esta manera, aquí lo importante es fijarnos en la definición de nuestro parámetro, teniendo la capacidad de recibir múltiples argumentos y en los argumentos que le estamos pasando.

	Pero también tendremos la posibilidad de pasarle múltiples valores de *clave-valor*, tal como si fuese un diccionario y esto se representa con *\*\**:

	![[IMG_421.png]]

	De esta manera, podríamos trabajar con *\*\*kwargs* dentro de la función como si estuviésemos tratando a un diccionario.

	Ademas, es posible incluso colocar ambos y esto lo que querrá decir es que la función tiene la posibilidad de recibir múltiples argumentos o múltiples valores de clave-valor:

	![[IMG_422.png]]

	De esta manera podría funcionar si se le pasan múltiples argumentos o múltiples valores de clave-valor.

	*Ejemplo de cuando utilizar \*args:*

	![[IMG_423.png]]

	Aquí, mediante el uso de una función pasándole varios argumentos, estamos viendo como *args* se convierte en una tupla que almacena todos estos valores.

	De esta manera, ahora podríamos aprovechar el método que tiene Python *sum* para retornar la suma de todos estos valores e imprimirla:

	![[IMG_424.png]]

	De esta manera, en casos así es cuando utilizaremos los \*args para recibir múltiples argumentos.

	*Ejemplo de cuando utilizar \*\*kwargs:*

	Ahora vamos a crear una función *presentacion*, para realizar un tipo de presentacion de alguna persona, pasándole los pares de clave-valor para que con el uso de \*\*kwargs sean almacenados en un diccionario y podremos ver que es así imprimiendo el tipo de dato, así como el contenido:

	![[IMG_425.png]]

	De esta manera, al saber que es un diccionario podríamos representar de mejor forma todo este contenido, iterando en el diccionario:

	![[IMG_426.png]]

	*Ejemplo anterior con time:*

	Entonces, regresando al primer ejemplo que realizamos con time, sin pasar ningún argumento realmente podríamos tener estas definiciones e incluso sería mejor, ya que en cara a un momento en el que le queramos pasar múltiples argumentos o múltiples pares de clave-valor, estaría listo para recibir uno u otro, o simplemente no recibir ninguno y trabajar como ya está sin problema, lo cual lo haría más escalable:

	![[IMG_427.png]]

	De esta manera, un ejemplo con esto podría ser el pasarle varios argumentos e imprimir la tupla, por ejemplo:

	![[IMG_428.png]]

	De esta manera estamos agregando esta funcionalidad en el decorador, no nos da error, ya que estamos imprimiendo directamente la variable y podrá imprimirnos la tupla vacía, pero sí accediéramos a posiciones y esta no existen (en el caso de no pasar argumentos), entonces si daría un error.

	Ahora, si quisiéramos agregar diversos argumentos de pares de clave-valor, también funcionaria:

	![[IMG_429.png]]

	Ahora si quisiéramos un print de una clave específica, funcionaria si le pasamos un valor con esa clave, de lo contraria daría error:

	![[IMG_430.png]]

	En este caso, al ser un diccionario, podríamos arreglar este error fácilmente, donde indicaremos que el que nos muestre el contenido de la clave *nombre* solo lo realice si este existe:

	![[IMG_431.png]]

	*Es posible incluso recibir tanto múltiples argumentos sencillos, como múltiples argumentos que sean pares de clave-valor al mismo tiempo.*

	![[IMG_432.png]]

	De esta manera, Python automáticamente lo organizara y ordenara en su respectivo tipo de dato, tanto en la tupla como en el diccionario sin problemas, y si en nuestro decorador imprimiéramos ambos, funcionaria sin problemas:

	![[IMG_433.png]]

	Entonces, ahora, para que no nos muestre nada en caso de que amabas estén vacías, lo que podríamos hacer es una comprobación con el *if* donde le pasemos directamente la tupla o diccionario y automáticamente verificara si tiene contenido o no:

	![[IMG_434.png]]

	O de una forma más compactada:

	![[IMG_435.png]]

	Dejandonos un output mas limpio:

	![[IMG_436.png]]

	*Ejemplo final con clase Circunferencia:*

	Empezaremos creando una clase *Circunferencia*, de la cual para crear un objeto tendremos en cuenta que le pasaremos el radio de este mismo:

	![[IMG_437.png]]

	Como vamos a trabajar con getters y setters, así como también vamos a tener en cuenta que queremos saber el radio, diámetro y el área, entonces definiremos nuestro radio como atributo protegido:

	![[IMG_438.png]]

	Por ende, ahora configuraríamos el getter y setter para nuestro atributo *radio*:

	![[IMG_439.png]]

	Y ahora configuraríamos *getters* para poder recuperar el diámetro y el área:

	![[IMG_440.png]]

	De esta manera ahora podríamos solicitar cada uno de estos:

	![[IMG_441.png]]

	O incluso, gracias a *getter*, cambiar el valor de nuestro atributo protegido *radio* y volver a calcular el diámetro y el área:

	![[IMG_442.png]]

	Incluso, como vemos que nos muestra muchos decimales a la hora de calcular el *area*, para evitar esto podríamos utilizar *round()*, a este le tendremos que pasar como primer argumento el valor con los decimales y el segundo cuantos decimales deseamos mostrar (en este caso 2):

	![[IMG_443.png]]

[[#Índice]]

## **Siguientes apuntes**


[[Módulos_y_paquetes_en_Python]]
