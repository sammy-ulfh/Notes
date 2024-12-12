 ## **Índice**

- [[#Listas]]
- [[#Tuplas]]
- [[#Conjuntos]]
- [[#Diccionarios]]
- [[#Proyecto de videojuegos]]
- [[#Siguientes Apuntes]]


## **Listas**

1. **Introducción:**

	Las listas son estructuras de datos que nos permiten almacenar secuencias ordenadas de elementos. Son mutables, lo que significa que podemos modificarlas después de su creación, y son dinámicas, permitiéndonos añadir o quitar elementos en ellas.

	**Características de las Listas**

	Vamos a explorar las características clave de las listas en Python, que incluyen su capacidad para:

	- Almacenar datos heterogéneo, es decir, pueden contener elementos de diferentes tipos (enteros, cadenas, flotantes y más) dentro de la misma lista.
	- Ser indecadar y cortadas, lo que permite acceder a elementos específicos de la lista directamente a través de su índice.
	- Ser anidadas, es decir, una lista puede contener otras listas como elementos, lo que permite crear estructuras de datos completas como matrices.

	**Operaciones con listas:**

	También cubriremos las operaciones fundamentales que se pueden realizar con listas, como:

	- Añadir elementos con métodos como *append()* y *extend()*
	- Eliminar elementos con métodos como *remove()* y *pop()*
	- Ordenar listas con el método *sort()* o la función incorporada *sorted()*
	- Invertir los elementos con el método *reverse()* o la sintaxis de corte \[::-1\]
	- Comprender las comprensiones de listas, una forma "pythonica" de crear y manipular listas de manera concisa y eficiente.

	**Métodos de Listas:**

	Profundirzaremos en la rica gama de métodos que Python ofrece para trabajar con listas y cómo estos métodos pueden ser utilizados para manipular listas de acuerdo a nuestras necesidades.

	**Buenas Prácticas:**

	Se darán las mejores prácticas en el manejo de listas, incluyendo cómo y cuándo usar listas en comparación con otros tipos de colecciones en Python, como tuplas, conjuntos y diccionarios.
	</br>
2. **Práctica**

	Empezaremos retomando la creación de una lista en Python:

	![[IMG_155.png]]

	De esta manera, crearíamos la lista y mostraríamos su contenido.

	**len():**
	
	También, es importante recordar que podremos usar el método *len()* para saber cuantos índices o datos contiene nuestra lista:

	![[IMG_156.png]]

	**append() y extend():**

	La forma de agregar un solo elemento a la lista con *append()* o agregar múltiples elementos con *extend()*:

	![[IMG_157.png]]

	**Iterar en una lista:**
	
	Iterar individualmente sobre cada elemento de una lista para trabajar con ellos:

	![[IMG_158.png]]

	**remove() y pop()**

	Eliminar elementos específicos con *remove()*, el ejemplo que se mostrará será una lista de vulnerabilidades en cuanto ciberseguridad respecta, y veremos como podremos eliminar cualquiera de las que tengamos con indicar el nombre o contenido específico de esta:

	![[IMG_159.png]]

	![[IMG_160.png]]

	Si llegamos a tener elementos repetidos, solo eliminará el primero con el que se encuentre de inicio a fin, ya que podríamos pensarlo como si lo recorriese de esta manera.

	O bien eliminar el último elemento de una lista con *pop()*:

	![[IMG_161.png]]

	Con pop también podremos eliminar posiciones específicas, indicándole el índice como argumento:

	![[IMG_178.png]]

	Además de eliminar el elemento, es posible que al momento de que se elimine se almacene en una variable, por ende podríamos lanzar un mensaje de que una persona ha sido eliminada de la lista, de la siguiente manera:

	![[IMG_179.png]]

	**Ordenar listas numéricas con sort():**

	![[IMG_162.png]]

	O también haciéndolo de forma directa, pasando la lista como argumento:

	![[IMG_163.png]]

	De esta manera sería lo mismo; la diferencia sería que, cuando pasamos la lista como argumento, la nueva lista ordenada no se almacena en *numbers*, por lo que alterará la lista, pero fuera de ella, por así decirlo.

	Teniendo exactamente la misma lista desordenada, lo podremos ver si en la siguiente línea imprimimos nuevamente la lista *numbers*.

	**Voltear listar con reverse():**

	Esto nos ayudaría a prácticamente voltear toda la lista, donde el primer elemento ahora será el último, el ultimo el primero, el penultimo el segundo, etc...

	![[IMG_164.png]]

	**Acceder a posiciones especificas:**

	Cuando queremos acceder a índices específicos en una lista, debemos tener en cuenta que en Python siempre se empezará a contar desde el número cero, por ende el último índice siempre será 1 menos al total de elementos.

	Si una lista tiene 50 elementos, su último elemento estará en el índice 49.

	![[IMG_165.png]]

	Podremos acceder al último elemento de una lista con *-1*, pero no solo eso. Una lista en Python puede ser recorrida de forma inversa, donde -1 es el último elemento, -2 el penúltimo y así sucesivamente.


	**Crear sublista de la lista principal:**

	Es posible mostrar elementos de una lista mediante rangos, es por ello que si quisiéramos crear una sublista con elementos desde el primero hasta n elementos, podríamos hacerlo de la siguiente manera:

	![[IMG_166.png]]

	Aquí con *\[:3\]* generamos una sublista donde almacenamos los valores en un rango desde el primer elemento de la lista hasta el tercero.

	Nos mostrará hasta el índice 2, debido a que tenemos que tener en consideración que los índices en las listas comienzan desde el cero y siempre nos mostrará un índice menor al indicado.

	También es posible hacerlo de forma un poco distinta, donde lo haríamos inversamente por así decirlo.

	Indicándole que no nos muestre los últimos elementos, colocando un signo *-* antes del número o índice.

	![[IMG_167.png]]

	Nos muestra lo mismo, pero no se está realizando lo mismo.

	Aquí lo que le indicamos con *\[:-2\]* es que no nos muestren los últimos dos elementos de esa lista.

	Otra forma sería indicándole desde el inicio, de cuál índice debería iniciar y acabar en el último índice de la lista:

	![[IMG_168.png]]

	Con *\[2:\]*, estamos indicándole que comience en el índice 2, que sería el tercer elemento de la lista y sería un rango desde ese elemento hasta el último de la lista.

	Ahora, si quisiéramos trabajar específicamente con rangos, donde le indicamos ambas partes, debemos tener en cuenta que a la izquierda deberá ir el índice desde el cual iniciará el rango, mientras que a la derecha tendremos que indicar el índice donde finalizará más 1.

	![[IMG_169.png]]

	De esta manera, le estamos indicando que nos dé un rango para crear una sublista, que vaya desde el índice 1, hasta el índice 2, pero indicándolo con un número más, o visto de otra forma, desde el índice 1 hasta el elemento 3 de la lista.

	**Recorrer listas con bucles:**

	*for:*

	Recorrer una lista elemento a elemento con for es sencillo, se puede hacer iterando en un rango de números y por ende acceder elemento a elemento, tal como lo haríamos con while.
	
	Una forma sencilla es indicarle al for que itere sobre la lista (que es un tipo de objeto) elemento a elemento. Como lo hemos visto anteriormente, for puede iterar sobre objetos.

	Entonces quedaría que de la siguiente manera:

	![[IMG_170.png]]

	De esta manera, *attack* va tomando el valor de cada uno de los elementos de forma individual, recorriendo toda la lista.

	*while:*

	Con while podremos recorrer la lista elemento a elemento, accediendo a ellos de forma individual gracias a una variable que iremos incrementando. Sabremos dónde detener el incremento de la variable, ya que con *len()* podremos saber el número total de elementos de la lista.

	Como una lista siempre empieza desde el índice cero, nuestra variable que incrementa siempre tendrá que ser menor al número total de elementos, ya que el último elemento tendrá como índice el número total de elementos menos uno.

	Por lo tanto, quedaría de la siguiente manera:

	![[IMG_171.png]]

	El texto seguido de '#', son comentarios de una sola línea y Python no tendrá en consideración esto como si de código se tratase. Será como algo que ignore al momento de ejecutar el programa, pero que a la hora de ver el código puede ayudar a que cualquier persona lo entienda.

	Crear un objeto iterable de la lista que retorne, por un lado, el índice y, por el otro, el valor almacenado en ese índice es posible con *enumerate()*.

	Como ya mencionamos con for es posible iterar sobre objetos, por ende podremos iterar sobre el objeto de enumerate y tomar del lado izquierdo el índice, así como del lado derecho el valor almacenado y  trabajar con ellos, en este caso imprimirlos en pantalla:

	![[IMG_172.png]]

	**Acceder a los índices de una lista sin bucles:**

	Anteriormente se vieron métodos como *map()* y funciones *lambda anónimas*. Realizando una aplicación de estas para finalmente convertirlas en una lista, nos ayudaría a generar una lista de los índices de la lista principal, de la siguiente manera:

	![[IMG_173.png]]

	Aquí lo que pasa es que map itera sobre el objeto que crea enumerate, con la función lambda lo que hacemos es que en cada iteración la tupla creada por enumerate la pasamos a la variable *x* y queda almacenada en ella, finalmente tomamos el primer valor (índice 0) que es donde se almacena el índice de nuestra lista principal, de acuerdo a la iteración en la que va.

	Una vez *map()* termina de realizar esto y nos da todos los índices, recordemos que nos los da como valores individuales en cada iteración, por ello con *list()* hacemos que todo se transforme en una lista y de esta manera tenemos todos los índices representados en una lista.

	**upper() y lower():**

	Generar listas de los mismos datos mediante listas de comprensión solo en mayúsculas o solo en minúsculas es posible gracias al método *upper()* y *lower()*:

	![[IMG_174.png]]

	Aqui lo que pasa es que se itera sobre toda la lista principal con *for* y recordemos que en una lista de comprensión la acción u operatoria al iterar en un bucle se coloca antes de este, por lo que utilizamos *upper()* y *lower()* para que se almacene en mayúsculas o minúsculas todo el texto en cada posición.

	**Iterar dos litas a la vez mediante el uso de zip():**

	Recordemos que con *zip()* podremos combinar listas, lo cual sería muy similar a utilizar enumerate. Pero en el primer (0) índice estaría el valor de la primera lista que le pasemos y en el segundo (1) estaría el valor de la segunda lista que le pasemos, ambas del mismo índice en su misma lista.

	Si tenemos las listas:

	numeros = \[1, 2, 3\]  
	nombres = \["Andrés", "Jaime", "Pedro"\]
	
	si utilizamos zip: zip(numeros, nombres), se crea un objeto tal como lo hace *enumerate()*, una forma de visualizar esto sería:
	
	(1, "Andrés")
	(2, "Jaime")
	(3, "Pedro")

	Estas serían tuplas, tal como lo hace enumerate, por ende podríamos acceder de la misma manera a estos:

	![[IMG_175.png]]

	**Eliminar índices específicos de una lista con del:**

	*del* nos ayuda para eliminar índices en específicos en una lista, de la siguiente manera:

	![[IMG_176.png]]

	**Limpiar una lista:**

	Es posible limpiar una lista con *clear()*. Esto lo que haría sería dejar vacía nuestra lista y, por ende, una vez limpia, ya no contendrá ningún dato:

	![[IMG_177.png]]

	**Alterar o modificar valores en posiciones específicas:**

	Así como podemos acceder a los valores para mostrarlos, es posible que conociendo el índice específico modifiquemos el valor en esa posición, reemplazándolo por otro:

	![[IMG_180.png]]

	**Añadir un valor en una posición específica con insert() sin eliminar ninguno:**

	Es posible añadir un nuevo valor en una posición donde ya existe un dato. Lo que pasaría luego de esto es que todos los datos ya existentes se recorrían una posición hacia adelante a partir de donde nosotros insertemos el dato:

	![[IMG_181.png]]

## **Tuplas**

Las tuplas son una estructura de datos fundamental en Python, esta comparte algunas similitudes con las listas, per se distinguen por su inmutabilidad.

Las tuplas son colecciones ordenadas de elementos que no pueden modificarse una vez creadas. Esta característica las hace ideales para asegurar que ciertos datos permanezcan constantes a lo largo del ciclo de vida de un programa.

1. **Introducción**

	**Características de las tuplas:**

	- *Inmutabilidad:* Una vez que se crea una tupla, no puedes cambiar, añadir o eliminar elementos. Esta inmutabilidad garantiza la integridad de los datos que desea mantener constantes.
	- *Indexación y Slicing:* Al igual que las listas, puedes acceder a los elementos de la tupla mediante índices y también puedes realizar las operaciones de slicing para obtener subsecuencias de la tupla.
	- *Heterogeneidad:* Las tuplas pueden contener elementos de diferentes tipos, incluyendo otras tuplas, lo que las hace muy versátiles.

	**Operaciones con tuplas:**

	Aunque no puedes modificar una tupla, hay varias operaciones que se pueden realizas:

	- *Empaquetado y Desempaquetado de tuplas:* Las tuplas permiten asignar y designar sus elementos a múltiples variables de forma simultánea.
	- *Concatenación y Repetición:* Similar a las listas, puedes combinar tuplas usando el operador *+* y repetir los elementos de una tupla un número determinado de veces con el operador *\**.
	- *Métodos de Búsqueda:* Puedes usar métodos como *index()* para encontrar la posición de un elementos y *count()* para contar cuántas veces aparece un elemento en la tupla.

	**Uso de tuplas en Python:**

	- *Funciones y asignaciones múltiples:* Las tuplas son muy útiles cuando una función necesita devolver múltiples valores o cuando se realizan asignaciones múltiples en una sola línea.
	- *Estructuras de datos fijas:* Se usan para crear estructuras de datos que no deben cambiar, como los días de la semana o las coordenadas de un punto en el espacio.
	</br>
2. **Práctica:**

	La definición de una tupla  en Python es muy similar a la de la lista, la única diferencia es que en lugar de corchetes usaremos paréntesis:

	![[IMG_182.png]]

	![[IMG_183.png]]

	**Índices:**

	Acceder a los elementos de una tupla para mostrarlos es exactamente de la misma manera que en la una lista:

	![[IMG_184.png]]

	**Modificar valores de una tupla:**

	Una vez creada una tupla no es posible modificar valores que ya contenga, por ende si intentamos cambiar el valor de alguna posición, lo que pasaría es que nos arrojaría un error:

	![[IMG_185.png]]

	**Soporte de distintos tipos de datos:**

	 En una tupla, al igual que en alguna lista, podremos almacenar distintos tipos de datos y no tendrán que ser necesariamente de un mismo valor todos los datos almacenados:

	![[IMG_186.png]]

	Podríamos visualizarlo mejor iterando sobre cada una de las posiciones de la tupla, de la misma forma en la que la lista lo permite:

	![[IMG_187.png]]

	**Inmutabilidad:**

	La inmutabilidad quiere decir que no se pueden modificar valores una vez se define la tupla, esto quiere decir que tampoco podremos utilizar métodos que modifiquen la tupla directamente, tales como *insert()*, *extend()*, *remove()*, *append()*, entre otras formas en las que podríamos modificar una lista gracias a su mutabilidad.

	Si intentáramos utilizar cualquiera de estos, en cualquier caso nos lanzaría una excepción mostrándonos el tipo de error y es que las tuplas no contienen o aceptan estos métodos:

	![[IMG_188.png]]

	**Asignación de los valores de una tupla a variables:**

	Es posible asignarle los valores de una tupla de forma individual a distintas variables colocadas en una sola línea, de la siguiente manera:

	![[IMG_189.png]]

	También es posible ver la longitud de una tupla o ver el número de valores totales en ella, de la misma manera que lo hacemos en una lista:

	![[IMG_190.png]]

	**Modificar de forma indirecta una tupla:**

	Si bien no es posible modificar de forma directa, es posible hacerlo de forma indirecta creando otra tupla como auxiliar para ello.

	![[IMG_191.png]]

	**Operaciones con tuplas:**

	Funcionarían de la misma forma que en las listas, por ejemplo, al utilizar el operador *\** nos repetiría n veces la tupla:

	![[IMG_192.png]]

	O incluso verificar qué números son pares y almacenarlos en nueva tupla con una lista de comprensión, lo cual finalmente forzaríamos su conversión a tupla:

	![[IMG_193.png]]

	Este tipo de sintaxis es de las listas de comprensión, por lo que itera en toda la tupla y almacenara cada elemento conforme vaya iterándola, ahora para que solo se almacenen los elementos pares, el condicional realiza la verificación de sí la división de ese número entre 2 da como restante 0, entonces almacenara el número.

	Finalmente, realiza su conversión a tupla y ahora tendríamos una tupla con los números pares.

	O si quisiéramos hacerlo para impares, bastaría con cambiar la parte que verifica si es par y esta es el condicional.

	Ya que si el restante es distinto a cero, esto significará que el número es impar:

	![[IMG_194.png]]

	**Mutabilidad de listas dentro de una tupla:**

	A pesar de que una tupla no es mutable, su inmutabilidad no es hereditaria como tal a todos los tipos de datos que puede almacenar.

	Es por ello que si contiene una lista dentro, a pesar de que es una tupla, el contenido específico de la lista sí puede ser modificado:

	![[IMG_199.png]]

	**¿Qué caso práctico podría existir para el uso de tuplas al ser inmutables?**

	Si bien son inmutables, pueden tener diversos usos dependiendo de lo que queramos conseguir.

	Un caso práctico para una buena implementación sería manejar con tuplas las credenciales de unas bases de datos y, por ende, estas no podrán ser modificadas.

	En caso de que se quiera intentar esto, pues con el conocimiento de lanzar excepciones podríamos manejarlo.

	![[IMG_195.png]]

	Esto nos indica el tipo de excepción que se está manejando para este error, por ende podríamos manejarlo con una excepción nosotros, recordando que podríamos ponerla de forma general para que funcione con cualquier error:

	![[IMG_196.png]]

	O indicándole la excepción específica para que funcione correctamente (yo agregaré la librería pwntools para utilizarlos y se muestre con un colorcito el mensaje, funcionaría correctamente con solo utilizar el print):

	![[IMG_197.png]]

	Además, log cuenta con otras opciones para lanzar mensajes:

	![[IMG_198.png]]


## **Conjuntos**

Los conjuntos son conocidos en Python como *sets*. Son una colección de elementos sin orden y sin elementos repetidos, inspirados en la teoría de conjuntos de las matemáticas. Son ideales para la gestión  de colecciones de elementos únicos y operaciones que se requieren eliminar duplicados o realizar comparaciones de conjuntos.

1. **Introducción:**

	**Características de los Conjuntos:**

	- *Unicidad:* Los conjuntos automáticamente descartan elementos duplicados, lo que los hace perfectos para recolectar elementos únicos.
	- *Desordenados:* A diferencia de las listas y las tuplas, los conjuntos no mantienen los elementos en ningún orden específico.
	- *Mutabilidad:* Los elementos de un conjunto pueden ser agregados o eliminados, pero los elementos mismo deben ser inmutables (por ejemplo, no puedes tener un conjunto de listas, ya que estas listas se pueden modificar).

	**Operaciones con conjuntos:**

	Exploraremos las operaciones básicas de conjuntos que Python facilita, como:

	- *Adición y Eliminación:* Añadir elementos con *Add()* y eliminar elementos con *remove()* o *discard()*.
	- *Operaciones de conjuntos:* Realizar uniones, intersecciones, diferencias y diferencias simétricas utilizando métodos o operadores respectivos.
	- *Prueba de pertenencia:* Comprobar rápidamente si un elementos es miembro de un conjunto.
	- *Inmutabilidad opcional:* Usar el tipo *frozenset* para crear conjuntos que no se pueden modificar después de su creación.

	**Uso de conjuntos en Python:**
	</br>
	- *Eliminación de Duplicados:* Son útiles cuando necesitas asegurarte que una colección no tenga elementos repetidos.
	- *Relaciones entre colecciones:* Facilitan la comprensión y el manejo de relaciones matemáticas entre colecciones, como subconjuntos y superconjuntos.
	- *Rendimiento de Búsqueda:* Proporciona una búsqueda de elementos más rápida que las listas o las tuplas, lo que es útil para grandes volúmenes de datos.

	

2. **Práctica:**

	Los conjuntos los definiremos con llaves *{}*, a diferencia de las listas o tuplas estos no están enumerados. Esto se refiere a que sus datos no son marcados de forma posicional o general, un índice para ellos como en las listas.

	Recordemos que en las listas y tuplas podremos acceder a los datos indicando posiciones, por ende a los datos se le asigna una numeración:

	![[IMG_200.png]]

	Esto no se puede realizar en los conjuntos debido a que no se les da una enumeración y, por lo tanto, no cuenta con posiciones o índices para sus datos.

	Además, es importante mencionar que en los conjuntos no podremos tener datos repetidos, ya sea repetir un mismo número o una misma cadena de texto, por ejemplo.

	La definición o creación de un conjunto se hace de forma sencilla, prácticamente de la misma manera que con las listas o tuplas:

	![[IMG_201.png]]

	![[IMG_202.png]]

	**Capacidad de agregar nuevos elementos con  add() y update():**

	Los conjuntos o los tipos de datos *set* nos permiten agregar nuevos elementos en ellos, ya que son mutables, esto lo haríamos de la siguiente manera:

	![[IMG_203.png]]

	En este caso el 4 se nos almacena de forma ordenada, pero es importante tener en mente que en el caso de los conjuntos no funciona así al ser una estructura de datos no ordenada, por ende nunca debemos dar por hecho que el último valor que agreguemos estará al final.

	Esto se debe a que Python internamente realiza una organización de los datos de una forma más óptima, por lo que luego se dan casos como el siguiente:

	![[IMG_204.png]]

	Para agregar una mayor cantidad de elementos y no solo uno, podremos utilizar *update()*, lo cual es muy similar al extend en las listas:

	![[IMG_205.png]]

	**Remover o eliminar elementos en los conjuntos con remove():**

	En los conjuntos podremos eliminar elementos específicos empleando *remove()* y pasándole como argumento el dato específico que queremos eliminar:

	![[IMG_206.png]]

	**Remover elementos que no sabemos si existen con discard():**

	Podremos emplear *remove()* en múltiples ocasiones, pero además una cosa interesante es que los conjuntos permiten emplear el uso de un método, el cual puede ser utilizado sin dar ningún error en caso de que el dato no exista.

	Recordemos que en los conjuntos los datos son únicos y por ende no se repiten.  El emplear remove para un elemento que no sabemos si existe, se vería de la siguiente manera:

	![[IMG_207.png]]

	Esto nos dará error al no existir el elemento, pero al no estar seguros de si el elemento existe o no, para evitar que esto nos diera error podríamos emplear con mayor seguridad *discard()*:

	![[IMG_208.png]]

	Por ende, cuando existe lo eliminara como si de *remove()* se tratase, pero, si este no existe, no pasaría nada.

	**Intersecciones entre conjuntos con intersection():**

	Al generar una intersección entre dos conjuntos, esta podríamos almacenarla en un nuevo conjunto. El resultado de esta serán los datos que son iguales en ambos conjuntos, creando un nuevo conjunto con esos elementos.

	De esta manera podríamos saber que elementos contienen iguales dos conjuntos distintos:

	![[IMG_209.png]]

	**Generar uniones en conjuntos con union():**

	Es posible mezclar o unir dos conjuntos distintos, estos dos se unirán eliminando las repeticiones, dejando únicamente elementos únicos. Recordemos que los conjuntos contienen solamente elementos únicos:

	![[IMG_210.png]]

	**Subconjuntos y comprobación con issubset():**

	En Python decimos que un conjunto es un subconjunto de otro, cuando todos los elementos de este aparecen en otro conjunto.  
  
	Es por ello que en el siguiente ejemplo nuestro primer conjunto sería considerado subconjunto de nuestro segundo conjunto:

	![[IMG_211.png]]

	Ahora una forma de asegurarnos que todos los elementos de un conjunto aparecen en otro y por ende es considera subconjunto, sería aplicar una comprobación con *issubset()*, esto retornara un valor booleano, indicando si es verdadero o falso.

	True (verdadero) cuando si aparezcan todos sus elementos en el conjunto que es pasado como argumento o False (falso) cuando no y por ende no sea considerado subconjunto:

	![[IMG_212.png]]

	Aqui hacemos la comprobación de si los datos de nuestro primer conjunto, aparecen en el segundo conjunto y por ende nuestro primer conjunto será considerado subconjunto.

	En este caso retorna True porque, en efecto, es un subconjunto del segundo conjunto. 
	
	Es importante recordar que en los conjuntos no importa el orden, por más que parezca que se ordenan cuando insertamos datos, no debemos confiarnos de ello porque esto no es así, simplemente Python hará una organización del conjunto de la forma más óptima y no es la más ordenada.
	
	Usualmente puede notarse así, pero el creerlo de esta manera podría llevarnos a errores en nuestros programas.

	Si un solo elemento del primer conjunto no se encuentra en el segundo conjunto, ya no sería considerado subconjunto y por ende nos daría False ahora:

	![[IMG_213.png]]

	![[IMG_214.png]]

	Lo mismo pasaría para cualquier otro dato como las cadenas de texto:

	![[IMG_215.png]]

	![[IMG_216.png]]


	**Formas prácticas de utilizar los conjuntos set():**

	Podríamos emplearlo para de una lista que contenga múltiples repeticiones, crear o generar una que elimine completamente las repeticiones, esto lo logramos con *set()* que es el tipo de dato de los conjuntos y no contienen repeticiones:

	![[IMG_217.png]]

	Aqui finalmente lo tendríamos en otra variable almacenada sin ninguna repetición, ahora nosotros esperamos generar una lista, pero como realizamos una conversión a conjunto, actualmente tenemos un conjunto, por lo que tendremos que transformarlo nuevamente a lista para que tengamos una lista sin repeticiones:

	![[IMG_218.png]]

	Con esto listo, es importante que en los conjuntos los datos no están ordenados y nunca debemos esperar que sea así, es por ello que si queremos asegurar que nuestra lista esté ordenada tendremos que aplicarle un sort:

	![[IMG_219.png]]

	*Búsquedas eficientes:*

	Los conjuntos pueden ser una vía mucho más rápida o eficiente de verificar si un dato existe, ya que en una lista podría ser menos eficiente.

	Un ejemplo sería el siguiente:

	Primeramente, generaríamos una secuencia o un rango de números de 10 mil números en total, pero esta llegará hasta el 9,999 porque recordemos que Python empieza a contar desde el cero.

	Si intentamos imprimirla, no nos mostrará los números como tal, pero podremos iterar sobre este:

	![[IMG_220.png]]

	![[IMG_221.png]]

	Se muestran todos los números, pero en este caso con un comando de bash solo mostramos los últimos elementos.

	Entonces todos estos números podríamos almacenarlos en un conjunto:

	![[IMG_222.png]]

	Al estar almacenado como un conjunto ahora si vemos todos los datos como números almacenados.

	Finalmente, para realizar una búsqueda, es sencillo y solo será verificar si en este caso un número está dentro de nuestro conjunto, de existir nos retornará el dato booleano True y de no existir retornara False:

	![[IMG_223.png]]

	Esto desde luego es más eficiente que verificar si un dato existe empleando el uso de una lista.

	Si intentáramos con un dato que sabemos que no estará en el conjunto, retornara False:

	![[IMG_224.png]]

	![[IMG_225.png]]

	*Caso práctico con inserciones y uniones:*

	Un caso hipotético en el que tengamos usuarios de dos plataformas distintas, podríamos primeramente mostrar aquellos que se encuentran en ambas plataformas y posteriormente todos los usuarios de ambas plataformas, evitando las repeticiones gracias a este tipo de dato:\

	![[IMG_226.png]]

	![[IMG_227.png]]

	**Comparaciones entre conjuntos:**

	También podremos realizar comparaciones en conjuntos gracias a *difference()*, este nos ayudará para verificar de los datos que tenemos en nuestro primer conjunto, cuáles datos no aparecen en el segundo conjunto, que es el que se le pasa como argumento a difference:

	![[IMG_228.png]]

	![[IMG_229.png]]


## **Diccionarios**

1. **Introducción:**

	Los diccionarios son una de las estructuras de datos más poderosas y flexibles de Python. Los diccionarios en Python son coleeciones desordenadas de pares clave-valor. A diferencia de las secuencias que se indexan mediante un rango numérico, los diccionarios de indexan con claves únicas, que pueden ser cualquier tipo inmutable, como cadenas o números.

	**Características de los Diccionarios:**

	- *Desordenados:* Los elementos de un diccionario no están ordenados y no se accede a ellos mediante un índice numérico, sino a través de claves únicas.
	- *Dinámicos:* Se pueden agregar, modificar y eliminar pares clave-valor.
	- *Claves únicas:* Cada clave en un diccionario es única, lo que previene duplicaciones y sobrescrituras accidentales.
	- *Valores accesibles:* Los valores no necesitan ser únicos y pueden ser de cualquier tipo de dato.

	**Operaciones con diccionarios:**

	- *Agregar y modificar:* Agregar nuevos pares clave-valor y modificar valores existentes.
	- *Eliminar:* Eliminar pares clave-valor usando *del* o el método *pop()*.
	- *Métodos de diccionario:* Utilizar métodos como *keys()*, *values()* y *items()*, para acceder a las claves, valores o ambos en forma de pares.
	- *Comprensiones de diccionarios:* Una forma elegante y consisa de construir diccionarios basados en secuencias o rangos.

	**Uso de diccionarios en Python:**

	- *Almacenamiento de datos estructurados:* Ideales para almacenar y organizar datos que están relacionados de manera lógica, como una base de datos en memoria.
	- *Búsqueda eficiente:* Los diccionarios son altamente optimizados para recuperar valores cuando se conoce la clave, proporcionando tiempos de búsqueda muy rápidos.
	- *Flexibilidad:* Pueden ser anidados, lo que significa que los valores dentro de un diccionario pueden ser otros diccionarios, listas o cualquier otro tipo de dato.


2. **Práctica:**

	Los diccionarios son otra estructura de datos no ordenada de pares clave-valor,  no tienen enumeración como en las listas, lo que lo haría un poco similar a los conjuntos, también son mutables y su principal diferencia frente a todas las demás estructuras de datos es su peculiaridad de almacenar valores en formato clave-valor.

	Ahora podríamos definir un diccionario e imprimir su tipo de dato, así como el contenido de este, y lo veríamos de la siguiente manera:

	![[IMG_230.png]]

	Podremos acceder a los valores de un diccionario de forma similar a como lo hacemos en una lista, la diferencia es que en lugar de colocar índices, colocaremos las llaves o claves, que son las que colocamos a la izquierda de los  *:* en cada valor:

	![[IMG_231.png]]

	**Mutabilidad:**
	
	Como los diccionarios son mutables, podremos modificar los valores ya almacenados, casi de la misma manera en la que lo haríamos para una lista:

	![[IMG_232.png]]

	**Agregar nuevos valores:**

	Para agregar nuevos valores, como tambien tendremos que agregar una clave para este nuevo valor, se haría de la misma forma como si fuésemos a modificar alguno:

	![[IMG_233.png]]

	**Eliminar datos:**

	Podremos utilizar *del* para eliminar una llave y valor indicados, indicando entre corchetes la clave o llave para ese valor en concreto:

	![[IMG_234.png]]

	**Búsquedas por clave:**

	Para verificar si una clave existe en nuestro diccionario, sería similar a la condición que establecimos para verificar si un dato existía en un conjunto, donde si lo que retorna es True quiere decir que si existe esta clave y por ende tendrá algún dato almacenado:

	![[IMG_235.png]]

	De esta forma, podríamos verificar si existen diversas claves y con base en ello realizar una toma de decisiones en nuestros programas.

	**Recorrer diccionarios:**

	Para iterar en diccionarios, sería como si empleáramos enumerate en una lista e iteráramos sobre él, ya que al final de cuentas nuestra clave sería como el índice y para que esto funcione tendríamos que hacer uso de nuestro método *items()*:

	![[IMG_236.png]]

	**clear() y len()**

	En los diccionarios tambien podremos emplear los métodos *clear()* y *len()*, donde con len podremos calcular el número de elementos que contiene nuestro diccionario y con clear limpiar nuestro diccionario, lo cual funciona tal como en una lista:

	![[IMG_237.png]]

	![[IMG_238.png]]

	**Diccionarios de comprensión:**

	Así como las listas comprensión, tambien podremos emplear diccionarios de comprensión, los cuales solo se diferencian porque al inicio tendriamos que indicarle la clave de cada valor:

	![[IMG_239.png]]

	Esto nos generaría un diccionario donde se almacene el cuadrado de una serie de números.

	Podríamos verlo más claramente si iteramos sobre cada par de clave-valor:

	![[IMG_240.png]]

	**Listar las claves y los valores de un diccionario por separado:**

	Podremos listar las claves de un diccionario fácilmente gracias al método *keys()*:

	![[IMG_241.png]]

	De la misma manera para los valores, con el método *values()*:

	![[IMG_242.png]]

	**Verificar si una clave existe con el método get():**

	Podremos utilizar el método* get()* pasándole dos argumentos, el primero será la clave que buscaremos y el segundo será un string, ya que será un mensaje que podremos manejar en caso de que esa clave no exista:

	![[IMG_243.png]]

	![[IMG_244.png]]

	Este método es de mucha ayuda, ya que no rompe el flujo del programa y por ende continúa funcionando, los datos que retorna, ya sea el valor o el mensaje en caso de que esa clave no existe, se pueden manejar, ya sea almacenándolo en otras variables y esto no mostrara nada en pantalla, en este caso lo hace porque lo pasamos por un *print()*.

	**Agregar múltiples datos de clave-valor a un diccionario con update():**

	Podremos agregar múltiples valores de clave-valor a un diccionario con *update()*, esto podemos hacerlo de forma directa pasándole un diccionario como argumento, tal como funcionaria *extend()* en las listas, o bien otro diccionario, que al final sería lo mismo.

	![[IMG_245.png]]

	**Diccionarios anidados:**

	Así como existen bucles y condicionales anidados, tambien tenemos diccionarios anidados y estos al final podrían ser similar al formato *json*.

	El uso de diccionario anidados podría ayudarnos a representar múltiples valores dentro de un valor cuando sea necesario, como lo siguiente:

	![[IMG_246.png]]

	El diccionario anidado y su contenido serian elementos individuales tomados como valores de una clave, por lo que al final de cuentas nuestro diccionario realmente tiene 4 valores, así que cuidado con eso.

	![[IMG_247.png]]

	Con esto, podríamos acceder al diccionario en nuestro apartado de hobbies o a cada dato de forma individual:

	![[IMG_248.png]]

	**Formas de iterar en un diccionario:**

	Existen distintas formas de iterar sobre un diccionario, si lo hiciéramos como lo hacemos para una lista, iteraríamos sobre las claves de este diccionario, que tambien existe la forma de iterar solo sobre las claves del diccionario, que estas dos serian lo mismo:

	![[IMG_249.png]]

	![[IMG_250.png]]

	Como tambien tenemos el método *values*, podríamos iterar solamente sobre los valores:

	![[IMG_251.png]]

	Además, como vimos el método *items()*, podremos saber que accedemos a dos valores separados porque funciona de la misma manera que enumerate, ya que si tomáramos el output de este con una sola variable nos retornaría tuplas con ambos valores:

	![[IMG_252.png]]

	Por ello podemos tomarlo con dos variables y separarlo automáticamente, tal como lo hacemos cuando empleamos el uso de enumerate en las listas:

	![[IMG_253.png]]

## **Proyecto de videojuegos**

Con base en todo lo anterior, se realizará un proyecto de gestión de videojuegos en Python. Este proyecto servirá para consolidar nuestras habilidades de programación, abordando administración de ventas, la gestión del stock y la actualización de datos en un sistema de control central.

Este proyecto será guiado paso a paso, mostrando cómo se puede aplicar cada estructura de datos en situaciones concretas de manejo de información. Se creará un programa que no solo administre eficientemente los datos de videojuegos, sino que también sea capaz de interactuar con el usuario para realizar consultas y actualizar el inventario.

Para todo el proyecto haremos como una versión simple y una un poco más compleja.

**Shebang**

Desde luego, inicialmente tendremos que agregar el *shebang*, el cual ya sabemos que nos ayudará a indicarle al sistema con que interprete ejecutarse, en este caso, python3:


```shebang
#!/usr/bin/env python3
```

**Representación**

Vamos a tratar de representar nuestro proyecto en partes, de esta manera podríamos empezar creando un tipo de separadores mediante el uso de comentarios:

![[IMG_254.png]]

**Apartado Géneros**

En este apartado comenzaríamos creando un diccionario en el cual almacenaremos nuestros juegos. Aquí, como se trabajará, será que la clave es el nombre del juego y el valor viene siendo la categoría del juego.

Por ejemplo, teniendo el juego "Super Mario Bros" donde su categoría es "Aventura", quedándonos varios juegos representados de la siguiente manera:

![[IMG_255.png]]

**Apartado ventas y stock**

Ahora, para  nuestro apartado de ventas y stock, crearíamos un diccionario tomando como clave los mismos juegos, pero como valor le agregaremos una tupla que contendrá dos valores, como primer valor el total de juegos que se han vendido y como segundo valor el total de juegos disponibles en stock:

![[IMG_256.png]]

**Apartado clientes**

Ahora, en el apartado de clientes, vamos a generar un diccionario en el cual la clave seguirá siendo el juego, pero en el valor agregaremos un conjunto, el que indicará los nombres de los clientes.

Para efectos prácticos agregaremos una serie de pocos clientes y consideraremos que entre ellos compraron un total del número de ventas que tenemos para cada juego, ya que el colocar 924 como lo es en el caso del *Final Fantasy VII*, sería más tedioso y además para efectos más prácticos en sistemas ya complejos los clientes se van agregando conforme los clientes van realizando sus compras.

Por ello quedaría representado de la siguiente manera:

![[IMG_257.png]]

**Sumario**

Para el sumario antes tendremos una variable donde tendremos un juego y luego imprimiremos o mostraremos información sobre este dentro del apartado de sumario.

![[IMG_258.png]]

Hasta aquí, lo que estamos definiendo es que nos vaya a empezar a mostrar un resumen del juego que tenemos en la variable "mi_juego".

Los corchetes y las cosas sobre estos son para representar de una mejor forma el output de lo que vayamos a mostrar, y los símbolos especiales como "\n" nos sirve para realizar un salto de línea y no mostrar las cosas en líneas pegadas, dándole una mejor vista.

El otro símbolo especial "\t" nos sirve para efectuar un tabulado en nuestro output. Tengamos en cuenta que, como tabulado, querría decir prácticamente separar 4 espacios donde sea colocado, en este caso al inicio.

De esta manera, hasta ahora tendríamos un output así:

![[IMG_259.png]]

Ahora agregaríamos el mostrar total de ventas para el juego en cuestión, recordando que en la tupla podremos acceder a los valores como en una lista y el primer valor (índice 0) es el que corresponde a las ventas, mientras que el segundo valor corresponde al stock.

![[IMG_260.png]]

Realizaríamos lo mismo para mostrar el total de unidades de ese juego que quedan existentes en el stock:

![[IMG_261.png]]

Ahora faltaría mostrar los clientes que han comprado este juego, para ello podríamos mostrarlo accediendo de la misma manera, pero al realizarlo observaremos que la representación de este se nos haría en el tipo de dato del conjunto, por lo que para representar los nombres así directamente se vería un poco feo:

![[IMG_262.png]]

Para corregir esto o mostrarlo de una mejor manera, tendríamos la posibilidad de utilizar *' '.join()*, el cual nos ayuda a indicarle de qué manera representarnos el contenido y qué colocar entre cada elemento del conjunto:

![[IMG_263.png]]

De esta manera, dentro de las comillas del join tendremos que indicarle cómo queremos representar los elementos del conjunto y qué colocar entre cada elemento. En este caso, le indicamos que nos coloque una coma y un espacio, para una representación más limpia de cada cliente.

Hasta aquí ya tendríamos un programa sencillo, el cual nos listaría la información de los juegos que tengamos registrados. Ahora, con cambiar el juego en nuestra variable *mi_juego*, que en programas más complejos sería un input del usuario, nos mostraría la informacion para ese juego.

![[IMG_264.png]]

Con esto ya tendríamos un pequeño programa que nos permite listar la información de los juegos, pero aún podemos hacerlo más interesante.

**Haciendo nuestro programa más completo**

Ahora, al inicio de nuestro programa, crearíamos una lista en la cual ingresaríamos los juegos que tenemos disponibles:

![[IMG_265.png]]

De esta manera, ahora podríamos eliminar nuestra variable *mi_juego* y colocar nuestro sumario en una función. A esta le pasaremos como argumento elemento a elemento el contenido de la lista para que nos dé un resumen de todos los juegos.

Por ende, tendríamos que definir el parámetro *juego* en nuestra función y a este se le pasaría como argumento el juego correspondiente cuando iteremos nuestra lista. Por lo que, también tendríamos que cambiar la llave por la que se buscará en cada diccionario debido a que ahora la variable *mi_juego* ya no existe. En su lugar utilizaremos el parámetro definido *juego*, el cual recibirá el contenido y será prácticamente una variable dentro de la función:

![[IMG_266.png]]

Ahora iteraríamos en la lista y le pasaríamos el nombre de cada juego para que nos liste toda la información:

![[IMG_267.png]]

Aquí entra en juego la reutilización del código, ya que mandamos a llamar múltiples veces nuestra  función.

Así como también en las variables, entraría en juego el ámbito de las variables, por lo que no habría conflicto si le pasamos una variable con el mismo nombre del parámetro de nuestra función. Esto lo podríamos ver como si fuesen dos variables distintas, una existente en nuestro bucle y otra en nuestra función, y es como si le pasáramos a la variable de la función el contenido de la variable del bucle.

Por lo que no nos generaría ningún conflicto, ya que el ámbito de cada variable está en su respectivo bloque, una en el bucle y una en la función, como si de dos variables distintas se tratase.

Ahora, si ejecutáramos nuestro programa, nos mostraría un resumen de todos los juegos:

![[IMG_268.png]]

Teniendo esto, podríamos jugar con distintas cosas. Un ejemplo sería el querer que nos muestre los datos de solamente aquellos juegos que hayan tenido más de 500 ventas, en este caso tendríamos que agregar un condicional que verifique las ventas para los juegos:

![[IMG_269.png]]

De esta manera se nos mostrarían solamente aquellos que hayan tenido más de 500 ventas:

![[IMG_270.png]]

Y además, con lo que hemos hecho, podremos tener múltiples formas que se nos ocurran de agregar como característica para mostrar la información, así como lo es la de mostrar solamente aquellas que hayan tenido cierto numero de ventas.

Al final del todo, podríamos considerar agregar algo que nos retornara el total de unidades que han sido vendidas considerando todos los juegos. Para esto podríamos emplear una función lambda e iterar sobre todos los valores del diccionario que almacena las ventas y el stock:

![[IMG_271.png]]

La definición de nuestra función lambda es sencilla de comprender, al iterar sobre los valores de nuestro diccionario gracias a *.value()*, accedemos a las tuplas que, por un lado, contienen las ventas y por otro el stock. Con esto sabemos que podemos acceder a ambos mediante un bucle y almacenarlo en dos variables, en este caos almacenamos el dato de ventas en la variable ventas y para el valor del stock colocamos un guion bajo *_*, esto quiere decir que queremos ignorar o eliminar ese valor, ya que no lo tomaremos en cuenta para lo que realizaremos.

Con el recorrido listo, a la izquierda del bucle tendremos que indicar que hacer, como queremos que retorne el valor de ventas, pues colocamos la variable, como conforme se vaya ejecutando, queremos que se vaya sumando para tener un total de las unidades vendidas, por lo que agregamos el método *sum()* para esto y finalmente almacenar el valor total de unidades vendidas.

Como podremos observar, el total de ventas que nos representa es de todos los productos, pero nosotros solo estamos mostrando los productos con ventas arriba de las 500 unidades, por lo que para arreglarlo haríamos lo siguiente:

![[IMG_272.png]]

![[IMG_273.png]]

De esta manera, lo que estamos haciendo es que además de recuperar los valores, también recuperamos las claves en cada iteración del diccionario, por lo que ahora tendríamos cada uno de los nombres.

Con esto, podríamos agregar la misma condición que agregamos en el primer bucle, asegurando que solo nos realice la suma de las ventas cuando el total de ventas sea mayor al tope que hayamos definido, para ello se crea una variable global *tope*, para poder considerarla en ambas.

Por lo que ahora nuestro output quedaría de la siguiente manera:

![[IMG_274.png]]

Si llegáramos a cambiar el tope de unidades vendidas para que nos muestre más, con un tope de 100 quedaría de la siguiente manera:

![[IMG_275.png]]

Con esto hemos concluido el proyecto, finalmente con una herramienta la cual está completa debido a que dependiendo de características que modifiquemos, en este caso como lo es el tope, nos mostrara distinta información.

[[#Índice]]

## **Siguientes Apuntes**

[[Programación_Orientada_a_Objetos_en_Python_(POO)]]

