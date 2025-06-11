
## **Índice**

- [[#El intérprete de Python]]
- [[#Shebang y convenios en Python]]
- [[#Variables y tipos de datos]]
- [[#Operadores básicos en Python]]
- [[#String Formatting]]
- [[#Control de flujo (Condicionales y Bucles)]]
- [[#Funciones y ámbito de las variables]]
- [[#Funciones lambda anónimas]]
- [[#Manejo de errores y excepciones]]
- [[#Siguientes apuntes]]

##  **El intérprete de Python**

El intérprete de Python es el corazón del lenguaje de programación Python; es el motor que ejecuta el código que escriben los programadores. Cuando hablamos de *intérprete de Python*, nos referimos al programa que lee y ejecuta el código Python en tiempo real.

*Funciones Clave del Intérprete de Python:*

- *Ejecución de Código:* El intérprete ejecuta el código escrito en Python línea por línea, lo que facilita la depuración y permite a los desarrolladores probar fragmentos de código de forma interactiva.
  </br>
-  *Modo interactivo*: El intérprete puede usarse en un modo interactivo que permite a los usuarios ejecutar comandos de Python uno a uno y ver los resultados de inmediato, lo cual es excelente para el aprendizaje y la experimentación.

   ![[IMG_005.png]]

	Además, es posible ejecutar cosas en una sola línea con el parámetro -c, sin necesidad de abrir como tal el intérprete de comandos.
	
	![[IMG_006.png]]
   </br>
-  *Modo de script:* Además del modo interactivo, el intérprete puede ejecutar programas completos o scripts que se escriben en archivos con la extensión ==.py==.
   </br>
-  *Compilación a Bytecode:* Aunque Python es un lenguaje interpretado, internamente, el intérprete compila el código a bytecode antes de ejecutarlo, lo que mejora el rendimiento.
   </br>
- *Máquina Virtual de Python:* El bytecode compilado se ejecuta en la Máquina Virtual de Python (Python Virtual Machine – PVM), que es una abstracción que hace que el código de Python sea portable y se pueda ejecutar en cualquier sistema operativo donde el intérprete esté disponible.

**Ventajas del Intérprete de Python:**

- *Facilidad de uso:* La capacidad de ejecutar código inmediatamente y de manera interactiva hace de Python, una herramienta excelente para principiantes y para el desarrollo rápido de aplicaciones. 
  </br>
-  *Portabilidad:* El intérprete de Python está disponible en múltiples plataformas, lo que significa que los programas de Python pueden ejecutarse en casi cualquier sistema sin modificaciones.
   </br>
-  *Extensibilidad:* El intérprete de Python permite la extensión con módulos escritos en lenguajes como C o C++, lo que puede ser utilizado para optimizar el rendimiento.

El intérprete de Python es una herramienta poderosa y flexible que hace que el lenguaje sea accesible y eficiente para una amplia variedad de aplicaciones de programación. Comprender cómo funciona el intérprete es fundamental para cualquier programador que desee dominar Python.

## **Shebang y convenios en Python**

En el desarrollo con Python, el shebang y los convenios de codificación son aspectos importantes que facilitan la escritura de scripts claros y portables.

*Shebang en Python:*

El shebang es una linea que se incluye al principio de un script ejecutable para indicar al sistema operativo con qué intérprete debe ejecutarse el archivo. En los scripts de Python, el shebang común es:

```
#!/usr/bin/env python3
```

Esta línea le dice al sistema que utilice el entorno (*env*) para encontrar el intérprete de Python 3 y ejecutar el script con él. Es fundamental para asegurar que el script se ejecute con Python 3 en sistemas donde Python 2 todavía está presente.

En Linux, el ejecutar */usr/bin/env* nos mostrará todas las variables de entorno en nuestro sistema. Y en este caso, al ejecutar */usr/bin/env python3*, nos ejecutaría el intérprete de comandos de python3.

Es por ello que al colocarlo de la manera indicada en nuestro script estaríamos asegurando que se ejecute con el intérprete indicado, ya que lo busca entre las rutas que están almacenadas en el *PATH*, en dado caso que su ruta sea distinta a */usr/bin/python3*. 

Más que nada es para evitar errores de cara a una persona que tenga almacenado el binario de *Python 3* en otra ruta.

De esta manera si tuviésemos un script para imprimir el inigualable Hello, World!, al agregar el shebang podríamos simplemente darle permisos de ejecución y ejecutarlo como un archivo y sin problemas se ejecutaría con Python 3.

```
#!/usr/bin/env python3

print("Hello, World!")
```

*Sin shebang:*

![[IMG_007.png]]

*Con shebang:*

![[IMG_008.png]]


*Convenios en Python:*

Los convenios de codificación son un conjunto de recomendaciones que guían a los desarrolladores de Python para escribir código claro y consistente. El más conocido es ==PEP 8==, que abarca:

- *Nombres de variables:* Utilizar '*lower_case_with_underscores*' para nombres de variables y funciones, '*UPPER_CASE_WITH_UNDERSCORES*' para constantes y '*CamelCase*' para clases.
  </br>
- *Longitud de Línea:* Limitar las líneas a 79 caracteres para código y 72 para comentarios y docstrings.
  </br>
- *Indentación:* Usar 4 espacios por nivel de indentación.
  </br>
- *Espacios en blanco:* Seguir las prácticas recomendadas sobre el uso de espacios en blanco, no incluir espacios adicionales en listas, funciones y argumentos de funciones.
  </br>
- *Importaciones:* Las importaciones deben estar en líneas separadas y agrupadas en sl siguiente orden: módulos de la biblioteca estándar, módulos de terceros y luego módulos locales.
  </br>
-  *Compatibilidad entre Python 2 y 3:*  Aunque Python 2 ha llegado al final de su vida útil, algunos convenios pueden seguirse para mantener la compatibilidad.

El cumplimiento de estos convenios no solo mejora la legibilidad del código, sino que también facilita la colaboración entre desarrolladores y el mantenimiento a largo plazo del software.

El uso adecuado del shebang y la adhesión a los convenios de Python son señales de un desarrollo cuidadoso y profesional. Integrar estos aspectos en tus prácticas de codificación es crucial para el desarrollo de software efectivo y eficiente en Python.

*Representación de los convenios:*

![[IMG_011.png]]

Además, es importante saber que en cuanto a posibles confusiones deberíamos tener cuidado con las letras **l (ele minúscula)**, **O (o mayúscula)** y **I (i mayúscula)**.

Esto es debido a que dependiendo de la fuente de texto con la que cuenta el sistema podrían ser confundidas fácilmente, o la **O** confundida con el número **0**.

Además, existe también una forma recomendada para crear variables protegidas, que se utilizaran en cuanto a la implementación de clases:

![[IMG_012.png]]

O de otra forma, las variables o métodos privados:

![[IMG_013.png]]


*Scripts como módulos:*

En *Python 3* a los **scripts** les podremos considerar *módulos*, por ende cuando ejecutemos un script, este automáticamente será considerado el módulo principal, a diferencia de  los scripts agregados o importados a este.

Además, tenemos una forma de validarlo:

![[IMG_009.png]]

De esta forma, el contenido del condicional solo se ejecutará si el script es ejecutado directamente, considerándose así el módulo principal o main, y no como un tercero.

Entonces, para realizar una validación de como sería, al no considerarse un módulo principal importándolo desde otro script, sería de la siguiente manera:

![[IMG_010.png]]

Como vemos, al cada script ser considerado directamente un módulo se importa de forma sencilla. En este caso solo agregamos el nombre, ya que *script.py* se encuentra en el mismo directorio del script *test.py* el cual ejecutamos directamente.

De esta manera, basándonos en necesidades propias, podríamos crear script para ejecutar tanto como módulo principal y como módulo importado. Dándonos una mayor cantidad de posibilidades  en proyectos que realicemos.


## **Variables y tipos de datos**

Las variables en Python son como nombres que se le asignan a los datos que manejamos. Piensa en una variable como un nombre que le asignas a un valor, para poder referirte a él y utilizarlo en distintas partes de tu código.

Ahora, vamos a enfocarnos en comprender las variables y algunos de los tipos de datos fundamentales en Python, Estos conceptos son esenciales, ya que nos permiten almacenar y manipular la información en nuestros programas.

**Variables:**

Una variable en Python es como un nombre que se le asigna a un dato. No es necesario declarar el tipo de dato, ya que Python es inteligente para inferirlo.

**Cadenas (Strings):**

Las cadenas son secuencias de caracteres que se utilizan para manejar texto. Son inmutables, lo que significa que una vez creadas, no puedes cambiar sus *caracteres individuales*.

Teniendo esto en cuenta, podríamos definir variables de la siguiente manera y aunque contengan valores numéricos, estos se manejarían como texto, debido a la forma en la que lo estamos declarando:

![[IMG_014.png]]

De esta manera generamos y mostramos por pantalla nuestras cadenas de texto.

En la parte de la *ip_address*, mostramos entre llaves la variable para mostrarla con más texto en conjunto. Para que esto funcione y nos tome nuestra variable es importante agregar la *f* antes de nuestras comillas, de lo contrario lo tomaría como texto.

Cuando en un script queramos mostrar algo en pantalla, será importante colocarle siempre el print, de lo contrario no se mostrará en pantalla.

Tenido esto en cuenta podríamos ver el tipo de dato de la variable y veremos que aunque tengamos una con un número, es reconocida como cadena de texto debido a la forma en la que la estamos declarando.

Además, es posible realizarlo de ambas maneras que mostramos:

![[IMG_015.png]]


**Números:**

Python maneja varios tipos numéricos, pero nos enfocaremos principalmente en:

- *Enteros (Integers):* Números sin parte decimal.

	Ahora para declarar nuestras variables numéricas, quitándole el detalle de las comillas, hace la diferencia, ya que si se las quitamos ahora si el tipo de dato sería numérico:

	![[IMG_016.png]]

	Así como lo mostramos anteriormente, también es posible mostrarlo junto con otro texto, en caso de querer agregar algún mensaje antes de nuestro dato entero:

	![[IMG_017.png]]
	</br>
- *Flotantes (Floats):* Números que incluyen decimales.

	Y para nuestras variables de tipo numérico float, sería de la siguiente manera:

	![[IMG_018.png]]
	


*Type Casting:*

En Python podremos referirnos a forzar o cambiar un tipo de dato como Type Casting.

Un ejemplo de como podríamos hacer esto es convirtiendo una variable de dato numérico a flotante:

![[IMG_019.png]]

Como podremos agregamos un dato número entero, pero lo forzamos a ser float.

Podríamos realizarlo de la misma manera para convertir de float a entero:

![[IMG_020.png]]

Así como también es posible convertir a Sting:

![[IMG_021.png]]

**Listas:**

Las listas son colecciones ordenadas y mutables que pueden contener elementos de diferentes tipos. Son ideales para almacenar y acceder a secuencias de datos.

Y para trabajar con estas listas, así como con cadenas y rangos de números, utilizaremos los bucles *for*, que nos permiten iterar sobre cada elemento de una secuencia de manera eficiente.

Tendremos una forma sencilla de declarar una lista, la cual sería de la siguiente manera:

![[IMG_022.png]]

Esta sería una declaración de una variable con datos ya preestablecidos.

¿Pero qué pasa si queremos meterle datos sobre la marcha y declarar la lista vacía?

Pues para ello tendremos *append* que lo que hace es almacenar un dato en la última posición de la lista, lo que quiere decir que siempre irá agregando el dato a su vez que una nueva posición, por decirlo de alguna forma.

![[IMG_023.png]]

En Python es posible acceder a los datos de una lista de forma individual, por lo que en lugar de mostrar toda la lista podríamos mostrar posiciones específicas de la lista.

La forma en la que trabajaremos con los índices en Python será empezando desde el número 0, siendo de esta manera que el 0 corresponde a la última posición y n-1 será el número de nuestra última posición.

Un ejemplo para ello sería tener la lista [1,2,3,4], si queramos imprimir nuestro número 4, sería imprimiendo la posición 3 de este, ya que siempre empezamos a contar desde el 0.

![[IMG_024.png]]

Si quisiéramos acceder al índice 4, nos daría error, ya que simplemente este no existe:

![[IMG_025.png]]

Además, en Python tenemos una forma de referencias a nuestro índice final en nuestra lista, podríamos tener una lista muy larga y por ende no saber cuantos datos tiene en total, pero querer acceder al dato final, entonces lo podríamos hacer referenciando *-1* como nuestro índice:

![[IMG_026.png]]

Ahora bien, si lo que haremos será recorrer prácticamente índice a índice toda la lista, esta sería una mala forma de hacerlo.

En lugar de eso, lo mejor sería hacerlo mediante un bucle:

![[IMG_027.png]]

La forma de la imagen anterior, lo que hace es iterar posición por posición de toda la lista, asignándole en cada iteración el valor a port y por ende la acción que hace al recibir el valor es la que le indicamos que es que imprima la variable port.

Ahora, para la siguiente forma de hacerlo, es haciendo que el bucle for nos itere en un rango de números, generando una sumatoria en una variable en cada iteración hasta llegar al número indicado, en este caso del 0 al 8 para acceder hasta la posicion 7, debido a que en el bucle for cuando se indica un numero hasta el cual iterar, siempre llegara hasta un numero antes del indicado y aumentara el valor uno a uno.

Además, indicándole como acción en cada iteración que acceda a la posición en la que vaya:

![[IMG_028.png]]

Una forma más compleja de explicarlo sería que realmente lo que hace por atrás el bucle sería que:

- Tenemos nuestra variable i, la cual es inicializada en 0, por defecto nuestro bucle irá aumentando esta variable 1 a 1 hasta llegar un valor antes del indicado, pero esto es así porque realmente la condición aplicada es que sé detiene una vez que nuestra variable i llega a un valor menor al que nosotros indicamos, de esta manera.

  Si i < 8, esto será verdad y el bucle hará su última acción y se detendrá, ya que para la próxima valdrá 8 y la condición no será verdad.

En cuanto a la escalabilidad de nuestro código, utilizar bucles representa un mejor manejo.

Cuando nosotros agregamos código o indicaciones para nuestro programa dentro de funciones, clases o bucles, es muy importante que este contenido esté tabulado (4 espacios hacia adentro de nuestra declaración del bucle, clase o función)

De esta manera podremos diferencias entre lo que ejecutará nuestra declaración y lo que no, por ende si hacemos lo siguiente, veremos cómo el primer texto se repite en bucle, mientras que el segundo no.

![[IMG_029.png]]

En Python es posible saber cuantos datos está almacenando una lista con la función *len()*, pasándole la lista como argumento.

Además, como *append()* solo nos permite agregar un solo elemento a la lista, tenemos una alternativa que permite agregar múltiples elementos y esta es *extend()*.

Ambas se utilizarían de la siguiente manera:

![[IMG_030.png]]

También es importante notar que en las listas podremos repetir elementos y estos también serán contados al utilizar *len()*, por lo que en las listas se contemplan repeticiones de elementos anteriores.

También, es posible agregar elementos como si estuviésemos sumando lista con lista, de la siguiente manera:

![[IMG_031.png]]

La forma anterior será una forma más corta de representarlo, pero es lo mismo que realizar lo siguiente:

![[IMG_032.png]]

*Ordenamiento en listas:*

En Python, al tener una lista totalmente ordenada, podremos ordenarla con el uso de la función *sorted()*, de la siguiente manera:

![[IMG_033.png]]

*Eliminar elementos en una lista:*

Para eliminar valores en una lista, podríamos utilizar *del* y podríamos borrar el elemento almacenado en un índice específico. Por ejemplo, el índice 0, eliminaría el valor almacenado y recorría a todos los que están delante de él.

De esta manera, ahora el elemento en el índice 0, sería el que anteriormente se encontraba en el índice 1:

**Sin aplicar la eliminación:**

![[IMG_034.png]]

**Aplicando la eliminación:**

![[IMG_035.png]]

**Probando cosas con la consola interactiva:**

En nuestra consola interactiva probaremos lo siguiente, de esta manera podremos observar como podremos mostrar múltiples elementos desde el inicio de la lista hasta donde deseemos:

![[IMG_036.png]]

De esta manera, al agregar en el índice *:*, seguidamente le podremos indicar el número de elementos que queremos que nos muestre, en este caso si sería del primer valor de la lista en adelante.

Además, si llegamos a colocar más números de los existentes que tiene la lista, esto no nos daría error, pero realmente solo podría mostrarnos los existentes.

Pero ahora, si quisiéramos trabajar sobre rangos, ahí sí sería con base en el índice, teniendo la posibilidad de indicar que te muestre desde el índice 1 al 4 [*1:4]*, y nos mostrará desde el primer índice indicado hasta uno antes del colocado después de los *:*

![[IMG_037.png]]

Otra forma de realizarlo, es colocar los elementos a la izquierda en lugar de la derecha.

Esto lo que haría sería evitar mostrarnos el número de elementos indicados, desde el principio, y mostrarnos elementos partiendo del siguiente al que le indicamos, de la siguiente manera:

![[IMG_038.png]]

Además, lo mencionado anteriormente, para acceder al último elemento con el índice *-1*, realmente nos funcionaría para recorrer la lista de forma inversa, tomando como penúltimo elemento el índice *-2* y así sucesivamente.

![[IMG_039.png]]

Ya si indicáramos un índice *-7*, nos pasaría lo mismo que al tratar de acceder a un índice que no existe, dándonos error.

*Insertar datos en una posición específica:*

Para poder insertar datos en una posición específica, podríamos utilizar la función *insert()*, recibiendo dos argumentos, donde el primero es el índice y el segundo el dato a ingresar.

De esta manera, el dato que estaba en ese índice y  los siguientes, se recorrerán una posición hacia adelante, para permitir a este ingresar en esta posición.

Además, es posible que nuestras listas contengan distintos tipos de datos, por lo que podríamos mezclar entre enteros y strings, pero aquí, al querer utilizar por ejemplo un ordenamiento, ya no funcionaría y tiene todo el sentido del mundo.

![[IMG_040.png]]

*Eliminar contenido de una lista:*

Para eliminar el último elemento de una lista, vamos a contemplar la lista anterior.

Lo que nos ayudaría para ello sería *pop()*, usándolo de la misma forma que utilizamos append, extend, etc.

![[IMG_041.png]]

También podremos *saber el índice de un dato en concreto*, si llegamos a tener una lista muy grande. Sabemos que tenemos un dato, pero, sin embargo, no tenemos su índice. Para esto realizaríamos lo siguiente.  
  
Además, lo que haríamos primeramente sería una reasignación de la lista. De esta manera eliminaríamos el contenido anterior de la variable y agregaríamos contenido nuevo, sin que permanezca el anterior.

Para ello utilizaríamos *index()*:

![[IMG_042.png]]

*Pero, ¿qué pasa si tenemos elementos repetidos?*

En este caso, si utilizamos indexa, no funcionaría para listar los índices de todos los elementos repetidos, ya que en este caso se podría considerar que index revisa la lista uno a uno desde el índice inicial.

Por ende, a la primera coincidencia con el dato que se está buscando, ese será el índice que nos retorne:

![[IMG_043.png]]

Por lo tanto, si quisiéramos tener todos los índices de este dato, existe una forma de hacerlo.

Para ello, una forma de hacerlo sería creando una nueva lista, la cual contenga como elementos los índices de ese elemento en la lista principal.

Antes de esto, tenemos la función *enumerate()* a la cual, si le pasamos nuestra lista esta nos devolverá que es un objeto, y si iteramos en ella por un lado, el índice y, por otro lado, el valor que almacena:

![[IMG_044.png]]

Aquí la variable x almacenaría el valor del índice, mientras que y almacenaría el valor o dato en ese índice.

Ahora, teniendo esto en consideración, podríamos aplicar lo siguiente:

![[IMG_045.png]]

De esta manera, lo que se hace dentro de nuestra declaración dentro la lista es indicarle que:

- *La X al inicio:* Nos almacena o "muestre" el contenido de la variable x cuando el bucle esté iterando sobre cada posición.

- *El bucle:* Con enumerate obtendrá el índice y el valor, iterando en cada posición de la lista.

- *El condicional:* Se aplica una condición en la que si *y* (el valor en las posiciones) es igual al número que estamos buscando, entonces si se cumplirá el hecho de que nos almacene el contenido de x, como posición individual en la lista dentro de cada iteración.

  Si no indicáramos este condicional, lo que pasaría sería que nos almacenaría todos los índices.


*Contar el número de veces que sale un elemento:*

Para esto podremos utilizar *count()*, pasándole como argumento el número del cual queremos saber cuántas veces se repite:

![[IMG_046.png]]

*Forzar el no tener repeticiones en una lista:*

Para esto, realmente lo que tendríamos que hacer es convertir nuestra lista a un tipo de dato *set*. Este lo que tiene es que, por defecto, no contempla repeticiones de datos y además de ello podremos convertirlo o forzar su conversión nuevamente a una lista:

![[IMG_047.png]]

Como podremos ver, lo que hacemos es forzar las conversiones entre *set* y *list*. Al convertir nuestra lista a set, vemos que queda desordenada, por lo que, por último, la ordenamos y nos queda nuestra lista sin ningún dato repetido.

Además, en el set, si en algún momento intentamos meter algún dato repetido, hasta podría llegar a darnos algún tipo de error.

Ahora lo siguiente es exactamente lo mismo, pero representado de una mejor manera:

![[IMG_048.png]]

*Encontrar el número más grande y más pequeño en una lista:*

Para esto utilizamos *max()* y *min()* y funcionará este o no ordenada la lista:

![[IMG_049.png]]

*Sumar todos los valores de una lista:*

Para ello podremos utilizar *sum()*:

![[IMG_050.png]]

Entonces, ahora, si quisiéramos, hasta, podríamos sacar la media o promedio implementando el uso de *len()* para dividir entre el número total de datos en la lista:

![[IMG_051.png]]

Además, como por ejemplo, si contamos con 7 elementos, al dividir entre 7 suele darnos muchos decimales, por ello tenemos *round()* y este nos ayuda a mostrar la cantidad de elementos decimales que deseemos. Es importante considerar que aplicará redondeos.

Mientras no le indiquemos el número de decimales que deseamos mostrar, como segundo argumento, solo nos mostrará el número entero redondeándolo.

![[IMG_052.png]]


Estas son solo algunas de las estructuras de datos con las que trabajaremos por el momento, a medida que avancemos exploraremos más tipos de datos y estructuras más complejas, ampliando nuestras herramientas para resolver problemas y contruir programas más sofisticados.


## **Operadores básicos en Python**

1. *Introducción:*

	Los operadores aritméticos son símbolos que Python utiliza para realizar cálculos matemáticos.

- **Los fundamentales son:**

	- *Suma (+):* No solo suma números, sino que también une secuencias como cadenas y listas, creando una nueva secuencia que es la combinación de ambas.
	  </br>
	- *Resta (-):* Se utiliza para restar un número de otro. Con listas, su uso es menos directo y generalmente no se aplica como operador directo.
	  </br>
	- *Multiplicación (\*):* Cuando se multiplica un número por otro, obtendremos el producto. Con cadenas y listas, este operador repite los elementos la cantidad de veces especificada.
	  </br>
	- *División (/):* Divide un número entre otro y el resultado es siempre un número flotante, incluso si los números son enteros.
	  </br>
	- *Exponente (\*\*):* Eleva un número a la potencia de otro. Por ejemplo, ‘2 \*\* 3‘ resultará en 8. Este operador es menos común en operaciones con cadenas o listas.

-  **Operaciones con cadenas:**

	En Python, las cadenas son objetos que representan secuencias de caracteres y se pueden manupilar usando operadores aritméticos:

	- *Concatenación (+):* Une varias cadenas en una sola. Por ejemplo, 'Hola ' + 'Mundo' se convierte en 'Hola Mundo'.
	  </br>
	- *Repetición (\*):* Crea repeticiones de la misma cadena. 'Hola' \* 3 generará 'HolaHolaHola'.

- **Operaciones con listas:**

	Las listas son colecciones ordenadas y mutables de elementos:

	- *Concatenación (+):* Similar a las cadenas, unir dos listas las combina en una nueva lista.
	 </br>
	- *Repetición (\*):* Repite todos los elementos de la lista un número determinado de veces.

- **Funciones especiales para listas:**

	- *Zip:* Toma dos o más listas y las empareja, creando una lista de tuplas. Cada tupla contiene elementos de las listas originales que ocupan la misma posición.
     </br>
	- *Map:* Aplica una función específica a cada elemento de un iterable, lo que resulta útil para transformas los datos contenidos.

	Asi mismo, otro de los conceptos mencionados es el de *TypeCast*. El TypeCast o conversión de tipos, es el proceso mediante el cual se cambia una variable de un tipo de dato a otro.

	En Python, esto se realiza de forma muy directa, utilizando el nombre del tipo de dato con una función para realizar la conversión. Por ejemplo, convertir una cadena a un entero se hace pasando la cadena como argumento a la función *int()*, y transformar un número a una cadena se hace con la función *str()*. Esta capacidad de cambiar el tipo de dato es especialmente útil cuando se necesita estandarizar los tipos de datos para operaciones especificas o para cumplir con los requisitos de las estructuras de datos.

	A medida del progreso, se ampliara incluiremos operaciones más complejas y exploraremos otros tipos de datos y estructuras en Python.

2. *Práctica:*

	- *Sumas:*

		En Python es posible realizar operaciones directamente en un *print*, o asignarle el valor de esta operación a una variable:

		![[IMG_054.png]]

		![[IMG_055.png]]

	- *Restas:*

		![[IMG_056.png]]

	 - *Multiplicación:*

		![[IMG_057.png]]

	- *Exponente:*

		![[IMG_058.png]]

		![[IMG_059.png]]

	Además, nosotros podremos formatear los resultados y, con *formatear los resultados* nos referimos a convertir datos en una representación específica o estructura.

	 Esto quiere decir que les daremos un formato específico siguiendo una serie de reglas

	Con esto en mente, a nivel de string podríamos aplicar un formateo a nuestra última respuesta de los exponentes, al ser bastante grande:

	![[IMG_060.png]]

	De esta manera lo que estamos haciendo es formatear la respuesta, donde con los *:* le estaríamos indicando que, a partir de ahí, vamos a indicar nuestras reglas y con la *,* le estaríamos indicando que queremos que nos separe los miles con comas.

	Aquí, si intentáramos separarlos con punto en lugar de coma, nos daría error, pero es posible hacerlo, solo que tendríamos que remplazar la coma por el punto utilizando *replace()*:

	![[IMG_061.png]]

	![[IMG_062.png]]

	De esta manera le estaríamos indicando que queremos que nos reemplace la coma por el punto, y funcionaria correctamente.


	- *Módulo o restante:*

		En Python podremos sacar el módulo o restante de las divisiones con *%*:

		![[IMG_063.png]]

		Esto suele ser muy utilizado cuando aplicamos comprobaciones para saber si un número es par o impar, ya que al utilizar el módulo de un número entre dos, si nos regresa 0 quiere decir que el número es par.


   **Cadenas:**
     </br>
	- **Sumas:**
		La suma de cadenas de texto o strings, la podríamos considerar como una concatenación de estos, ya que podríamos utilizarlo de la siguiente manera:

		![[IMG_064.png]]

	- *Multiplicaciones:*

		Con las multiplicaciones, lo que hace es repetir o multiplicar el contenido, el número de veces por el que se está multiplicando.

		![[IMG_065.png]]

		Además, en nuestras cadenas de texto podremos acceder a los caracteres de forma individual, como si de una lista se tratase. Permitiéndonos utilizar rangos también:

		![[IMG_066.png]]

	**Suma de elementos de dos listas en las mismas posiciones:**

	Cuando deseamos sumar elementos, podríamos automáticamente pensar en simplemente agregar '+' entre ambas listas para obtener el resultado esperado, pero realmente esto lo que haría, sería concatenar ambas listas:

	![[IMG_067.png]]

	Es por ello que para esto tendremos la función *zip()*, donde le pasaríamos nuestras listas como argumentos:

	![[IMG_068.png]]

	Esto lo que hace es crearnos un objeto sobre el cual podremos iterar, lo cual es muy similar a cuando utilizamos *enumerate()* para poder sacar tanto el índice como el valor en esa posición.

	Con esto, al iterar sobre el objeto podremos observar como lo que hace es emparejarnos todas las posiciones o índices similares de ambas listas en una tupla que es otro tipo de dato en Python, lo cual se ve de la siguiente manera:

	![[IMG_069.png]]

	*\n* representa un salto de línea. 

	Ahora con esto, en lugar de aplicar un bucle, tenemos una cosa muy interesante, la cual es la función *map()*. Esta itera sobre todo el objeto y pasa sobre cada una de las tuplas y además nos permite indicarle si queremos realizar algo, por lo que podríamos indicarle como primer argumento que queremos que nos sume todos los elementos que se encuentre dentro de la tupla, cuando itere sobre cada una de ellas:

	![[IMG_070.png]]

	Además, por último podríamos indicar que esto nos lo genere como una lista y finalmente, pues en result se nos almacenaría una lista:

	![[IMG_072.png]]

	La diferencia es que al hacerlo sin map, pues tendríamos que aplicar una conversión de cada tupla a una lista y luego sumarlo:

	![[IMG_071.png]]

	Para tenerlo como lista, bastaría con crear una antes del bucle y almacenar cada resultado:

	![[IMG_073.png]]

    Esto es un poco el cómo funcionan ciertas cosas y si por ahora es algo complicado no hay que preocuparse, con el paso de los temas todo se irá explicando y quedará más claro.

## **String Formatting**

1. **Introducción:**

	Python proporciona variar formas de formatear cadenas, permitiendo insertar variables en ellas, así como controlar el espaciado, alineación y precisión de los datos mostrados. Estas son las técnicas de formateo de cadenas que exploraremos:

	- *Operador % (Porcentaje):*  También conocido como *interpolación de cadenas*, este método clásico utiliza marcadores de posición como *%s* para cadenas, *%d* para enteros, o *%f*  para números de punto flotantes.
	  </br>
	- *Método format():* Introducido en Python 2.6, permite una mayor flexibilidad y claridad. Utiliza llaves *{}* como marcadores de posición dentro de la cadena y puede incluir detalles sobre el formato de la salida.
	  </br>
	- *F-Strings (Literal String Interpolation):* Disponible desde Python 3.6, los F-strings ofrecen una forma concisa y legible para incrustar expresiones dentro de literales de cadena usando la letra *f* antes de las comillas de apertura y llaves para indicar dónde se insertarán las variables o expresiones.
 
2.  **Práctica:**

	El *string formatting* nos puede ser de mucha ayuda al momento de trabajar con variables y texto. Para esto podríamos contemplar lo siguiente:

	![[IMG_074.png]]

	En este caso no nos da ningún tipo de error, porque al final lo que estamos haciendo es unir dos cadenas de texto. Pero si cambiamos el tipo de dato nos dará error y por ello debemos aplicar el *string formatting*.

	- *Operador % (Porcentaje):* 
       Con el operador  *%*, lo que podremos hacer es colocarlo dentro de la cadena de texto indicando el tipo de variable que vamos a colocar, después nuevamente seguido de las comillas de cierre colocaremos el operador *%* y finalmente la variable. Esto tendrá que ser de forma posicional, lo que quiere decir es que tendrán que ir en el orden en el que las colocamos en nuestra cadena de texto.
	
	   Siendo así de la siguiente manera:

	   ![[IMG_075.png]]

		Considerando que tendremos que utilizar:

		*%s* para strings, *%d* para enteros y *%f* para flotantes.

		![[IMG_076.png]]

		Como podremos observar, por defecto con los flotantes nos muestra muchísimos decimales, para evitar esto tendríamos que indicarle a nuestro operador del flotante cuantos decimales queremos que nos muestre.
		
        Esto se puede realizar colocando *.* y el número de decimales que deseamos mostrar entre el operador *%* y la letra *f*:

		![[IMG_077.png]]

		Como lo vimos, al tener más de una variable agregada en nuestro *string formatting*,  es importante que las agreguemos separadas por comas y entre paréntesis: 
		*"cadena %s, cadena  %s, cadena %d" % (variable 1, variable 2, variable 3)*.

		En Python al aplicar esta forma de *string formatting*, si por ejemplo tuviéramos un número entero y lo aplicamos como si fuese un Sting.

        Podría no dar ningún error, pero esto es porque realmente Python internamente  aplica o fuerza la conversión del número entero a una cadena de texto con *str()*. Sin embargo, lo más recomendable siempre es indicar el tipo de dato correcto, ya que con esto podríamos evitarnos errores.
        </br>
	- *Método format():*

		El *método format* se utiliza de forma similar, la diferencia es que tiene ciertas mejoras.
		
        Al utilizar format, para poner una variable dentro en nuestro texto tendríamos que colocar llaves *{}*, y en nuestro format poner las variables como argumentos, todas separadas por comas:

	    ![[IMG_078.png]]

		Lo bueno de esto es que toma las variables de acuerdo en el orden en el que nosotros las coloquemos y además, ahora Python se encargara del tipo de dato que sea, por lo que ya no tendremos que indicárselo y no daría ningún tipo de error.

		También es interesante que con format podremos trabajar con las variables que coloquemos como si de una lista se tratase y por ende referenciarnos a ellas como el índice de una lista:

		![[IMG_079.png]]

	- *F-strings:*

		Los F-string son una forma aún más sencilla y cómoda de implementar, ya que directamente colocaríamos una *f* antes de nuestra llave de apertura y con esto, dentro del texto solo tendríamos que colocar la variable dentro de llaves *{}*:

		![[IMG_080.png]]


## **Control de flujo (Condicionales y Bucles)**

Estos conceptos son fundamentales para entender cómo crear programas en Python que puedan tomar decisiones y repetir aciones hasta cumplir ciertos criterios. Aquí es donde nuestros programas obtienen la capacidad de responder a diferentes situaciones y datos.

1. **Introducción:**

	Los condicionales son estructuras de control que permiten ejecutar diferentes bloques de código dependiendo de si una o más condiciones son verdaderas o falsas, En Python las declaraciones condicionales más comunes son *if*, *elif* y *else*.

	- *if:* Evalúa si una condición es verdadera y, de ser así, ejecuta un bloque de código.
	- *elif:* Abreviatura de *else if*, se utiliza para verificar múltiples expresiones sólo si las anteriores no son verdaderas.
	- *else:* Captura cualquier caso que no haya sido capturado por las declaraciones *if* y *elif* anteriores.

	**Bucles:**

	Los bucles permiten ejecutar un bloque de código repetidamente mientras una condición sea verdadera o para cada elemento en una secuencia. Los dos bucles principales que utilizamos en Python son *for* y *while*.

	- *for:* Se usa para iterar sobre una secuencia (Como una lista, un diccionario, una tupla o un conjunto) y ejecutar un bloque de código para cada elemento de la secuencia.
	- *while:* Ejecuta un bloque de código repetidamente mientras una condición específica se mantiene verdadera.

	**Control de flujo en bucles:**

	Existen declaraciones de control de flujo que permiten modificar el comportamiento de los bucles, como *break*, *continue* y *pass*.

	- *break:* Termina el bucle y pasa el control a la siguiente declaración fuera del bucle.
	- *continue:* Omite el resto de código dentro del bucle y continúa con la siguiente iteración.
	- *pass:* No hace nada, se utiliza como una declaración de relleno donde el código eventualmente irá, pero no ha sido escrito todavía.

	Con esto se profundizará cada uno de los ejemplos de forma más detallada. Aprendiendo como tomar decisiones dentro de nuestros programas y como automatizar tareas repetitivas. Esto nos dará la base para escribir programas que puedan manejar tareas complejas y responder dinámicamente a los datos de entrada.


2. **Práctica:**

	- **Bucle for:**
		![[IMG_081.png]]

		Aquí vemos una forma de como utilizar el bucle for.

        Como podremos notar, lo que está sucediendo es que nos genera una secuencia la cual irá desde el número cero hasta uno antes del indicado en *range()*.

        Además, en cada iteración lo que sucede es que se le asigna a *i* el valor de la iteración en la que va y por ende cuando imprimimos su valor, en este caso imprimir la secuencia de esta manera.

		Es por ello que se dice que for nos ayuda a iterar sobre secuencias, pero además nos permite iterar sobre listas, un ejemplo utilizando variables descriptivas para un mayor entendimiento sería el siguiente:

		![[IMG_082.png]]

		Con esto, también podremos observar que la variable donde se almacenan los contenidos de cada iteración, en este caso, es una declaración temporal y además, como podremos observar, ya sea *i* o *name*, realmente este es un nombre que nosotros podremos cambiar por el que nos parezca oportuno.

		Ahora, si antes de nuestra secuencia llegamos a declarar exactamente la misma variable que iterara con un valor distinto a cero, este no le afectara al bucle, ya que automáticamente le asignara el 0, pero una vez termine el bucle la variable quedara con el valor de la última iteración almacenado:

		![[IMG_085.png]]
    
		Además, como sabremos que podremos iterar con for tanto en listas como objetos. Recordemos la funcion *enumerate()*, ya que esta nos transformaba una lista en un objeto y podríamos iterar sobre él.

		Esto lo que nos retorna son distintas tuplas donde el índice 0 contiene el índice de ese valor de la lista y el índice 1, contiene el valor que almacena la lista en ese índice.

		![[IMG_086.png]]

		Como vemos, esto funciona correctamente, pero la representación del nombre en cuanto al número se ve un poco raro que comience desde el cero, esto es así porque recordemos que los índices en las listas comienzan a partir del número 0.

        Pero para tener una mejor vista de ello, al momento de mostrar i podríamos sumarle uno, esto no afectaría ni modificaría nada, simplemente cambiaria el output o la salida que ve el usuario en pantalla.

		![[IMG_087.png]]
	  
	  **Iterar sobre un diccionario:**
		
		En Python tenemos un tipo de estructura a la cual se le llama diccionario, está como tal en cada posición en lugar de índice, se le considera llave, un ejemplo sería tener:

		*frutas = { "manzanas": 3, "plátanos": 2 }*
		
		En este caso, la fruta sería nuestra llave y tiene que ser única para poder acceder al contenido, el contenido como tal sería el número de frutas. Con un bucle for podremos iterar sobre un diccionario y extraer ambas.

		![[IMG_088.png]]
	  </br>
	- **While:**

		Con while también podremos generar secuencias, pero aquí se aplica de forma un poco distinta.
		
        Esto se debe a que while se enfoca principalmente en verificar si una condición es verdadera, y si se cumple ejecutará el bucle de código siempre, como ejemplo antes de implementar una secuencia:

		![[IMG_083.png]]

		Inicializamos la variable en 0 y despues verificamos que esta sea menor a 5, de esta manera generaríamos una secuencia de 0 a 4. Sin embargo, lo anterior resulta en un bucle que infinitamente nos mostrara el 0, es por ello que tendremos que aumentar en uno la variable i para cada iteración.

		![[IMG_084.png]]


	- **Bucles anidados:**

		Los bucles anidados es una forma de hacer un tipo de *multitarea*, ya que estos nos ayudan a hacer cosas como recorrer una lista en la que cada índice de ella es una lista, conocido como lista de listas.

		Para recorrer cada elemento en la lista de listas tendremos que usar bucles anidados, para así recorrer ambas listas, la lista principal y la lista que se encuentre en cada posición de la lista principal.

		Ya que, al hacerlo con un solo bucle, quedaría de la siguiente manera:

		![[IMG_089.png]]

		Y al aplicar los dos, de la siguiente manera (adjunto un mensaje en cada iteración del primer bucle para que sea más fácil visualizarlo):

		![[IMG_090.png]]

		Aqui la variable *i* toma cada posición de la lista principal y como cada una de ellas es una lista, pues podremos iterar sobre esa lista, por lo que con el segundo bucle lo hacemos y finalmente los valores individuales los tiene la variable number, ya que itera sobre cada lista que almacena la variable *i*.

	- **Listas de comprensión con for:**

		Algo interesante en Python es que  si queremos trabajar sobre una lista y con base en esta crear otra, es que es posible definir esto en una sola línea mediante la iteración de la lista original.

		Un ejemplo seria tener la lista principal y crear una secundaria donde estén los números de la anterior, pero elevados al cuadrado, entonces podríamos definir un bucle for y que por cada iteración saque el cuadrado del dato en esa posición y lo almacene en la posición correspondiente en nuestra nueva lista:

		![[IMG_091.png]]

		De esta manera, dentro de  la definición de la lista estamos indicando que se itere sobre la lista numbers y en cada posición donde number valdrá al número en el índice correspondiente, lo eleve al cuadrado, que seria la asignación del lado izquierdo.
		
        Al elevar al cuadrado ese número, automáticamente se almacenaría en el índice correspondiente de acuerdo a la iteración de la lista principal.

	- **break:**

		En los bucles nosotros podremos utilizar 3 operadores muy importantes que pueden ser de mucha utilidad dependiendo del contexto en el que nos encontremos con nuestro código.
		
        Uno de ellos es *break*, este es muy importante y podremos indicar a nuestro código que se detenga sin completar la condición principal, en el caso de un *for*, se hace una iteración en un total de números, en caso de querer detener el bucle si se da una condición específica.

		Primeramente, podremos observar nuestro bucle como se comportaría de forma normal:

		![[IMG_092.png]]

		Con esto en mente, podríamos tener un programa donde justo en un bucle, si se llegase a dar el número 6, se tenga que detener el bucle para evitar errores.

        De esta manera, aplicaríamos una condición donde si *i* es igual a 6, entonces nos detenga por completo el bucle mediante el uso de *break*:

		![[IMG_093.png]]

		Ahora bien, si nuestro bucle pasa por el número 6 no se imprime.

        Esto se debe a que el orden del código importa y por ende si la declaración donde se realiza la comparación es primero, primero se detendrá el bucle antes de poder imprimir el 6, es por ello que se tendría que cambiar el orden y ya no tendríamos problema con ello:

		![[IMG_094.png]]


	- **continue:**

		Ahora, podremos tener un caso similar al anterior con el break, pero en lugar de querer que el bucle se detenga, simplemente queremos que no realice nada para esa iteración, pero sí para las anteriores y las próximas, ignorando una iteración en específico.

		Para ello tenemos *continue*:

		![[IMG_095.png]]

		De esta manera todo nuestro bucle funciona correctamente, pero cuando nuestro número es exactamente igual a 6, lo que hará será ignorar el bloque de código dentro del bucle después del condicional y saltará a la siguiente iteración.

        Viéndolo de otra manera, una vez pasa por el continue, el bucle simplemente realiza un salto u omite ese paso en específico en el que se encuentre, pasando al siguiente.

        Es por ello que se imprimen todos los números menos el 6, ya que al pasar por el continue es ignorado el print y pasa automáticamente a la siguiente iteración.i

	- *if-else en un bucle:*

		Los condicionales son una de las formas más utilizadas para realizar toma de decisiones en nuestros programas, es por ello que utilizarlos en bucles también es importante.

		Un condicional *if-else*, técnicamente con if verificará que una condición sea verdadera y else será para de lo contrario, también poder ejecutar un bloque de código.

		Tendríamos el siguiente ejemplo, donde solo entrara al if si la condición es verdadera, pero de ser lo contrario entrará a ejecutar el bloque de código en el else:

		![[IMG_096.png]]

		De esta forma podremos realizar verificaciones y con base en eso ejecutar o no bloques de código específicos.

	- *else en bucles:*

		Aunque hay gente que no lo sabe, los bucles también cuentan con una definición del else, a la que el bucle solo entrara si su ejecución es exitosa y no es interrumpida, lo cual se utiliza de la siguiente manera:

		![[IMG_097.png]]

		En este caso, el bucle nos permite entrar al else, ya que finaliza su ejecución correctamente.

		Aquí no es interrumpido en ningún momento, ya que, recordemos que el bucle siempre llega un número antes del que le hemos indicado, es por ello que en este caso nunca llega al 10 y por ende el break no interrumpe su ejecución.

		Un caso donde si lo haría, es donde *i* si llegue a valer 10:

		![[IMG_098.png]]

		Teniendo esto en cuenta, es importante siempre recordar que todo el código que este, después de la declaración del bucle, se le considerara aparte, por lo que sin importar que pase dentro del bucle, esto se ejecutara sin problemas, al ser indicaciones independientes de lo que suceda en este:

		![[IMG_099.png]]

		Esto funcionará de la misma manera para los bucles while:

		![[IMG_100.png]]

		Incluso él continúe no le afectará para marcar como exitosa la ejecución, la que solo hace que se salte una iteración o las requeridas.

		Y es considerada exitosa, ya que sí se realiza toda la ejecución de nuestro bucle. Además, siempre será importante el orden del código, ya que en el bucle *while* si nuestro incremento para *i* estuviese después del condicional, entraríamos en un bucle infinito, ya que una vez valga 6, siempre valdrá 6, ya que el condicional no permitirá que pase hacia la siguiente instrucción, porque el if siempre será verdadero.

		Por ello, primero se coloca primero el incremento para i, en for no sucede lo mismo, ya que por defecto realiza el incremento para i.

		![[IMG_101.png]]


	- **Condicionales:**

		La estructura de los condicionales es sencilla, primero tendremos una forma de verificar si una condición es verdadera, de serlo, se ejecutará un bloque de código el cual se identificara que es específicamente para la condición, ya que tendrá una indentación o separación hacia adentro por 4 espacios:


		![[IMG_102.png]]

		En este caso, al ser la edad mayor o igual a 18, imprimiremos que es mayor de edad.

		Pero en caso de no cumplirse la condición no pasará nada.

		![[IMG_103.png]]

		Si queremos que en caso de que la edad sea menor a 18 se muestre que la persona es menor de edad, entonces tendremos que utilizar *else*:

		![[IMG_104.png]]

		Además, es importante mencionar que no pasara nada si nuestro código está compactado y no tiene tantos saltos de línea como se muestra en las imágenes.

		Simplemente, es mostrado así para que se vea de mejor forma y se de un mayor entendimiento de lo que se realiza.

		Tendremos varias formas de definir las condiciones en nuestros condicionales, para realizar validaciones dependiendo de la necesidad:

		- *\=\=*: Este se utiliza para indicar una comparación en donde solo se considerara verdadera donde si el primer valor es exactamente igual al segundo.
		- *>=*: Este se utiliza, para definir que una condición solo será verdadera si el primer valor es mayor o igual al segundo valor.
		-  *<=*: Este se utiliza, para definir que una condición solo será verdadera si el primer valor es menor o igual al segundo valor.
		-  *<*: Este se utiliza, para definir que una condición solo será verdadera si el primer valor es menor al segundo valor.
		- *>*: Este se utiliza, para definir que una condición solo será verdadera si el primer valor es mayor al segundo valor.

		**Múltiples condiciones:**

		Con los condicionales, una peculiaridad es que puedes hacer que tus datos pasen por una serie de validaciones para realizar cosas dependiendo de lo esperado o requerido, para ello se utiliza *elif*.

		![[IMG_105.png]]

		Esto a final de cuentas lo que hace es hacer las validaciones una a una, pero en el momento que una es correcta se mete en ella y ya no tiene por qué realizar las siguientes.

		Es por ello que si la primera llega a ser falsa, se salta a la segunda validación, donde estamos indicando que si edad está entre un rango de 13 a 17 años de edad, entonces esa condición será verdadera:

		![[IMG_106.png]]

		Finalmente, el *else*, lo que quiere decir es que si ninguna de las condiciones aplicadas es correcta, directamente entrará ahí y ejecutará el código indicado.

		Es por ello que va verificando las condiciones una a una.

		![[IMG_107.png]]


	- **Ternarias con condicionales:**

		Las ternarias con los condicionales es una forma de poder definir un condicional en una misma línea y almacenarlo en una variable, de esta manera se aplicaría automáticamente la validación y al imprimir la variable nos quedaría un solo mensaje:

		![[IMG_108.png]]

		De esta manera, si la condición es verdadera, se cumplirá la instrucción colocada antes del condicional y si es falsa, la que sigue del esle:

		![[IMG_109.png]]

	- **Operadores lógicos:**

		Los operadores lógicos nos permiten efectuar múltiples comprobaciones en una misma condición, para verificar que se cumpla una o más condiciones para ejecutar un solo bloque de código.

		- *or:* OR lo utilizamos para verificar que se cumpla una u otra condición para que se considere verdadera una instancia.
		- *and:* AND lo que nos permite es colocar dos o más condiciones, de las cuales absolutamente todas tendrán que ser verdaderas para que la condición lo considere verdadero.
		- *not:* NOT nos permite invertir el resultado de una condición, donde cuando el resultado de una condición es verdadero, lo convertirá a falso y viceversa.

		![[IMG_110.png]]

		En este caso solo se mostrará el mensaje cuando edad sea mayor o igual a 20 y que también nacionalidad sea "mexicana". De lo contrario, no mostrará nada en pantalla.

		Una forma de que muestre el mensaje sería utilizando or, de manera que si se cumple una u otra, se muestre el mensaje:

		![[IMG_111.png]]

		En este caso no se cumple la edad, pero como se cumple que nacionalidad es "mexicana", la condición será verdadera e imprimirá el mensaje.

		Retomando el ejemplo con and, hagamos que la condición sea falsa a propósito.

		![[IMG_112.png]]

		De esta manera no nos muestra el mensaje, ya que es falsa, si bien el mensaje que queremos mostrar solo tendría sentido mostrarlo si la condición es falsa; sin embargo, no se muestra, ya que esto tendríamos que agregarlo para un *else*.

		Precisamente aquí es donde entra *not*, ya que dependiendo de lo requerido puede ahorrarnos el utilizar un else al invertir la condición, por lo que aplicando not conseguiríamos lo que queremos, sin necesidad de agregar un else:

		![[IMG_113.png]]

		Esto puede ser conveniente si no queremos realizar nada en caso de que la condición sea verdadera, ya que si quitamos el not y hacemos todo de la forma convencional, al no mostrar alguna indicación para que se realice en caso de que la condición sea verdadera, automáticamente nos daría error:

		![[IMG_114.png]]

		Pero si queremos tenerlo de esta manera, existe algo que hará que no nos dé ningún error y eso es *pass*, esto sería similar al continue en bucles, por así decirlo, simplemente nos permitiría tener de alguna forma vacía una validación en un condicional, para que el código no de error.

		![[IMG_118.png]]
		

		Otra forma de usar not, sería directamente en una comparación, por ejemplo, si queremos validar si nacionalidad no es igual a "mexicana", lo utilizaríamos cómo *!=*:

		![[IMG_115.png]]

		Además, algo interesante que podremos hacer con los condicionales es realizar validaciones en listas, verificando por ejemplo si un número está en una lista:

	- *Condicionales anidados:*

		Otra forma de realizar una comparación doble, por así decirlo, al utilizar and verificamos que se cumplan dos condiciones, pero también podríamos hacerlo con condicionales anidados, que sería colocar un condicional dentro de otro, al final cumpliría la misma función que el and:

		![[IMG_117.png]]

	
	**Verificar si un número es par o no:**

	Recordando el operador del módulo o resto de una división *%*, si cualquier número lo dividimos entre 2, este recuperara el restante, y si el número es par, si restante siempre será igual a 0, es por ello que podremos aplicar esto de la siguiente manera:

	![[IMG_119.png]]

	**Ejemplo de todo lo visto anteriormente:**

	![[IMG_120.png]]

	En lo anterior lo que hicimos es la posibilidad de verificar que todos los números de una lista sean pares.

	El bucle recorrerá la lista validando si cada uno de los números es par, y si en algún momento se encuentra con un número impar, la variable que indica que los números son pares cambiara a *False* el cual es un tipo de dato booleano y el bucle se romperá o se detendrá, ya que si se encontró un impar no tendría sentido seguir iterando en la lista porque ya sabemos que ahora no podremos decir que todos son pares.

	Finalmente en el condicional, al pasarle una variable de tipo booleano no será necesario verificar si es *True* utilizando el operador *\=\=*, al ser un tipo de dato booleano con poner la variable el condicional podrá verificar si este es *True*, en caso de que no, se va para el *else*.

	Además, otra forma de hacerlo sería empleando una lista de comprensión e incluso uso del operador lógico not:

	![[IMG_121.png]]

	Una cosa que podría ser negativa si el rendimiento es importante y esperamos detener el programa una vez encuentre un número impar, es que en la lista de comprensión no es posible manejar el flujo del bucle for, por lo que no se puede utilizar ni break ni continue y se iterara sobre toda la lista.

	Nuestro if verifica si se encuentra False en la lista de comprensión, en caso de ser verdadero, pues quisiéramos que nos arroje el mensaje de que no todos los números son pares, es por ello que revertirnos la condición con not, para que así nos envíe al else, de ser el caso.


## **Funciones y ámbito de las variables**


1. **Introducción:**

	**Funciones:**

	Las funciones son bloques de código reutilizables diseñados para realizar una tarea específica. En Python se definen utilizando la palabra clave *def* seguida de un nombre descriptivo, paréntesis que puede contener parámetros y dos puntos. Los parámetros son *variables de entrada* que pueden cambiar cada vez que se llama a la función. Esto permite a las funciones operar con diferentes datos y producir resultados correspondientes.

	Las funciones pueden devolver valores al programa principal o a otras funciones mediante la palabra clave *return*. Esto las hace increíblemente versátiles, ya que pueden procesar datos y luego pasar esos datos modificados a otras partes del programa.

	**Ámbito de las Variables (Scope):**

	El ámbito de una variable se refiere a la región de un programa donde esa variable es accesible. En Python hay dos tipos principales de ámbitos:

	- *Local:* Las variables definidas dentro de una función tenen un ámbito local, lo que significa que solo se pueden acceder y modificar dentro de la función donde fueron creadas.
	- *Global:* Las variables definidas fuera de todas las funciones tienen un ámbito global, lo que significa que se puede acceder a ellas desde cualquier parte del programa. Sin embargo, para modificar una variable global dentro de una función, de debe declarar como global.

	Estos conceptos son esenciales para escribir programas claros, eficientes y mantenibles en Python.
	 </br>
2. **Práctica:**

	**Funciones:**
	
	Para definir nuestras funciones en Python utilizaremos *def* el cual proviene de *define* y el bloque de código a ejecutar por esta función tendrá que estar identado/tabulado (por 4 espacios, ya que es lo más recomendable).

	![[IMG_122.png]]

	En este caso realizamos solamente la definición de la variable, pero no sucede nada al ejecutar el programa.

	Esto sucede debido a que en Python las funciones son como bloques de código reutilizables, es por ello que podremos programar alguna tarea que pueda llegar a ser repetitiva y utilizarla múltiples ocasiones en nuestro programa, por lo tanto, para que esto funcione se tendrá que llamar o ejecutar la función, puede ser directamente para iniciar el flujo del programa o incluso dentro de una función:

	![[IMG_123.png]]

	De esta manera, mandamos a llamar la función, para que el código dentro de esta se ejecute.

	Ahora, una cosa interesante en las funciones es que podremos trabajar con los parámetros, esto quiere decir que podremos pasarle datos para que sean manipulados o usados dentro de esa función, siendo únicamente ámbito de esa función, o de otra forma, variable local.

	![[IMG_124.png]]

	De esta manera, definimos un argumento que  le tendremos que pasar a la función una vez que se llame. Este será como una variable definida dentro de la función, siendo así una variable local que como contenido tendrá lo que le pasemos como argumento.

	Es por ello que dentro de la función podremos utilizarla y, en este caso, imprimir el nombre que le hemos pasado.

	Además, algo interesante en las funciones es que pueden retornar valores. De esta manera, una forma de mostrarlo sería realizando una función de suma. El valor de una función es retornado justo al lugar de donde fue llamada, por lo que puede directamente imprimirse o ser almacenado en una función.

	![[IMG_125.png]]

	O al almacenar el dato en una función para imprimirlo después:

	![[IMG_126.png]]

	Además, por el entendimiento de variable temporal, que en este caso sería *result*.

	Quiere decir que será una variable que solo existirá mientras se esté ejecutando la función y, una vez se termine de ejecutar, estos datos o variables ya no existirán en el resto del flujo del programa. Esto lo podríamos ver si intentamos acceder a result fuera de la función:

	![[IMG_127.png]]

	**Ámbito de las variables:**

	Retomando un poco lo anterior, si generamos una función con una función dentro, esta sería considerada variable local, permitiendo modificarse y realizar cosas con ella solo dentro de la función donde fue creada.

	![[IMG_128.png]]

	De esta manera, si quisiéramos hacer algo con una variable local, fuera de la función donde fue declarada, no sería posible, ya que nos daría error.

	Podríamos considerar una variable local, como una variable temporal que solo existirá durante la ejecución de la función:

	![[IMG_129.png]]

	Es por ello que da el error de que la variable no está declarada, porque al ser un tipo de variable temporal, esta deja de existir una vez que la función termina su ejecución.

	Y a esta se le conoce como variable local.

	Si quisiéramos poder manipularla, aunque la función haya terminado de ejecutarse, tendríamos que declararla como variable global:

	![[IMG_130.png]]

	Esta definición está bien, pero una mejor forma de realizar declaraciones de variables globales sería antes de empezar a generar nuestras funciones:

	![[IMG_131.png]]

	En este caso, declarar una variable "global", de esta manera, nos permitiría trabajar con ella, pero los valores modificados dentro de una función no se tomarían en cuenta una vez se termine de ejecutar.

	Es por ello que lo mejor en Python a la hora de declarar variables globales es indicarle que será global, mediante el uso de la palabra clave *global*:

	En sí, al realizar esto por decirlo de alguna forma, lo que Python hace es traerse la variable a la función para permitir la modificación en el ámbito global, y no solo de forma local.

	Lo que haría que ahora sí se consideren los cambios realizados una vez que nuestra función se termine de ejecutar:

	![[IMG_132.png]]

## **Funciones lambda anónimas**


1. **Introducción:**

	**Funciones lambda:**
	
	Las funciones lambda son también conocidas como funciones anónimas debido a que no se les asigna un nombre explícito al definirlas. Se utilizan para crear pequeñas funciones en el lugar donde se necesitan, generalmente para una operación específica y breve. En Python, una función lambda se define con la palabra clave *lambda*, seguida de una lista de argumentos, dos puntos y la expresión que se desea evaluar y devolver.

	Una de las ventajas de las funciones lambda es su simplicidad sintáctica, lo que las hace ideal para su uso en operaciones que requieren una función por un breve momento y para casos donde la definición de una función tradicional completa sería excesivamente verbosa.

	**Usos comunes de las funciones lambda:**

	- *Con funciones de orden superior:* Como aquellas que requieren otra función como argumento, por ejemplo, *map()*, *filter()* y *sorted()*.
	- *Operaciones simples:* Para realizar cálculos o acciones rápidas donde una función completa sería innecesariamente larga.
	- *Funcionalidad en línea:* Cuando se necesita una funcionalidad simple sin la necesidad de reutilizarla en otro lugar del código.

	Con esto prenderemos cómo y cuándo utilizar las funciones lambda de manera efectiva, además de entender cómo pueden ayudarnos a escribir código más limpio y eficiente. Aunque su utilidad es amplia, también discutiremos las limitaciones de las funciones lambda y cómo el abuso de estas puede llevar a un código menos legible.

2. **Práctica:**

	![[IMG_133.png]]

	Este sería un ejemplo, aplicando la misma definición de cuando creamos esto con una función normal, haciéndolo más sencillo con una función lambda.

	Ahora también, podríamos crear el ejemplo de elevar un número al cuadrado, lo cual con una función lambda quedaría en una sola línea, pasándole un argumento:

	![[IMG_134.png]]

	De esta forma, para cosas sencillas, podremos simplemente crearlo con lambda, pero si quisiéramos hacer lo de la suma, sería generarlo para poder pasarle los 2 argumentos para la suma:

	![[IMG_135.png]]

	De esta forma podremos notar que antes de los dos puntos se tendrán que declarar los argumentos necesarios para lo que la función vaya a realizar, mientras que del lado derecho la operación o acción que realizara y además esto será lo que retornará, como si de un *return* de una función normal se tratase.

	Una forma de emplearlo con un ejemplo más realista o con el que podríamos toparnos con mayor facilidad, es mediante el uso de *map()*.

	De esta forma, recordando que *map()* nos permite pasarle dos argumentos, donde el primero será una función y el segundo el objeto a iterar.

	Lo cual resulta en un objeto y con ello podremos recordar que es posible iteraro:

	![[IMG_136.png]]

	![[IMG_137.png]]

	De esta forma, también es importante que para finalizar y tenerlo de una forma en la que podamos mostrarlo como lista, es que lo que se retorna por map, podremos transformarlo en lista y finalmente tendríamos la lista de los números al cuadrado:

	![[IMG_138.png]]

	Otra forma de utilizarlo, sería aplicando *filter()*, debido a que podremos agregar condiciones en nuestras funciones lambda y estas retornarán True o False.

	Un ejemplo sería para verificar si un número es par en una lista. En caso de que este sea par, filter lo que hará será retornarnos el número. En caso de ser impar, no nos lo retornara, por lo que no se almacenará en nuestra nueva lista.

	![[IMG_139.png]]


	O de otra forma, para que nos regresara los impares, podríamos utilizar en lugar de comparar para que sea exactamente igual a cero, diferente a cero, ya que cuando sea impar, el módulo de una división entre 2 siempre será distinto de 0.

	![[IMG_140.png]]

	Otra forma muy interesante de aplicar lambda sería importando librerías o módulos, en este caso *reduce*.

	Como esto puede ser un poco más complejo, más adelante se explicará de mejor manera el cómo importar módulos y librerías a nuestros programas.

	En este caso, con reduce, primeramente lo traeremos de una librería.

	Luego de esto, haremos una declaración similar que con map y filter. Lo que nos permitirá esto es hacer una operatoria elemento a elementos, por ejemplo, multiplicar todos los elementos de la lista. El primero por el segundo y después el resultado de ambos por el tercero y así sucesivamente:

	![[IMG_141.png]]


## **Manejo de errores y excepciones**


El manejo de errores y excepciones son un aspecto crítico para la creación de programas robustos y confiables en Python. Los errores son inevitables en la programación, pero manejarlos correctamente es lo que diferencia a un buen programa de uno que falla constantemente.


1. **Introducción:**

	**Manejo de errores:**

	Los errores pueden ocurrir por muchas razones: errores de código, datos de entrada incorrectos, problemas de conectividad, entre otros. En lugar de permitir que un programa falle con un error, Python nos proporciona una herramienta para 'atrapar' estos errores y manejarlos de manera controlada, evitando así que el programa se detenga inesperadamente y permitiendo reaccionar de manera adecuada.

	**Excepciones:**

	Una excepción en Python es un evento que ocurre durante la ejecución de un programa que interrumple el flujo normal de las instrucciones del programa. Cuando el intérprete se encuentra con una situación que no puede manejar, 'levanta' o 'arroja' una excepción.

	**Bloques try y except:**

	Para manejar las excepciones, utilizamos los bloques *try* y *except*. Un bloque *try* contienen código que puede producir una excepción, mientras que un bloque *except* captura la excepción y contiene el código que se ejecuta cuando se produce una.

	**Otras palabras clave de manejo de excepciones:**

	- *else:* Se puede usar después de los bloques *except* para ejecutar código si el bloque *try* no generó una excepción.
	- *finally:* Se utiliza para ejecutar código que debe correr inependientemente de si se genero un excepción o no, como cerrar un archivo o una conexión de red.

	**Levantar excepciones:**

	También es posible ‘levantar’ una excepción intencionalmente con la palabra clave *raise*, lo que permite forzar que se produzca una excepción bajo condiciones específicas.

	En esta clase, aprenderemos a identificar diferentes tipos de excepciones y cómo manejarlas de manera específica.
	También exploraremos cómo utilizar la declaración *raise* para crear excepciones que ayuden a controlar el flujo del programa y evitar estados erróneos o datos corruptos.

	Con esto tendrás las habilidades para escribir programas que manejen situaciones inesperadas de manera elegante y mantengan una ejecución limpia y controlada, incluso cuando se encuentren con problemas imprevistos.

2. **Práctica:**

	Los manejos de excepciones nos permitirán dar una serie de instrucciones a nuestro programa, para que al momento en el que se dé un error, el programa no se cierre de forma inesperada y rápida.

	De esta forma, podríamos controlar el flujo de salida del programa y, por ejemplo, en aplicaciones de escritorio, mostrar ventanas con mensajes sobre el error, para que no se cierre repentinamente.

	Una forma de realizarlo sería, por ejemplo, manejar una excepción cuando se intente realizar una división entre cero.

	Primeramente, tendremos que visualizar qué pasa si solo hacemos la división:

	![[IMG_142.png]]

	Aquí podremos observar que nos da un error. Este mensaje que nos muestra al final de cuentas es una excepción que lo que hace es mostrarnos dónde surgió el error y qué tipo de excepción se produjo.

	Entonces, para nosotros poder manejar una excepción cualquiera, lo haríamos de la siguiente manera:

	![[IMG_143.png]]

	De esta manera, *try* lo que hace es ejecutar un bloque de código y, en este caso, except tomaría cualquier tipo de error que se produzca y nos mostrará el mensaje.

	Sin embargo, la excepción puede ser mucho más específica, ya que puede que se dé algo inesperado, pero que no queremos realizar una instrucción en concreto para ello. Aquí es donde entran los tipos de excepciones.

	Por ello, si vemos el mensaje que nos arrojó el error cuando no utilizamos el try, veremos que la excepción en este caso es *ZeroDivisionError*, entonces, si queremos manejar solamente esta excepción en específico, tendremos que colocarlo después del except:

	![[IMG_144.png]]

	Es por ello que si ahora generáramos un error con un tipo de excepción distinta, al estar definida una específica, para alguna distinta no mostraría el mensaje que colocamos:

	![[IMG_145.png]]

	Por ello, nos muestra la excepción definida en el propio Python; por ello, si quisiéramos que se considere esta excepción, tendríamos que colocar como excepción específica *IndexError* que es lo que muestra el error.

	O bien, dejarlo sin especificar una  para que para cualquier tipo de excepción realice lo indicado.

	![[IMG_146.png]]

	![[IMG_147.png]]


	Además, es posible tratar múltiples excepciones en un mismo *try*:

	![[IMG_148.png]]

	![[IMG_149.png]]

	Además, algo interesante es que, ya considerando el apartado de librerías, podríamos importar *log* de la librería *pwn* y esto con una instrucción específica directamente nos ayudará a representar un error de una mejor manera e incluso con colorcitos.

	![[IMG_150.png]]

	**Problema con las librerías:**

	Es posible que al importar la librería de errores e incluso al querer instalar librerías, para esto la solución será crear un entorno específico para nuestras librerías y tendremos que cargarlo cada vez que lo vayamos a utilizar. Primeramente crearemos un entorno:

	```
	python3 -m venv nombre_del_entorno
	```

	Debemos asegurarnos de tener esto en una ruta absoluta en que no vayamos a manipular tanto, esto debido a que una vez hayamos creado el entorno deberemos cargar la ruta absoluta con un *source*, lo que quiere decir que le indicaremos al sistema donde deberá almacenar las librerías que queremos instalar o utilizar.

	```
	source /ruta/nombre_del_entorno/bin/activate
	```

	Después de esto, podremos utilizar *pip3* para instalar la librería pwntools o cargar el entorno para ejecutar algún programa si llega a dar error con alguna librería que ya tengamos instalada ahí.

	```
	pip3 install pwntools
	```

	**else con try:**

	Es posible utilizar *else* para un *try*, lo cual se utilizará en caso de que ninguno de los errores esperados se dé, quiere decir que todo ha salido bien y por ende podremos decidir qué hacer en nuestro programa:

	![[IMG_151.png]]

	Además, en *try* tenemos *finally* en el cual podremos defini un bloque de código que siempre se va a ejecutar, de error o no.

	Como su nombre lo indica, es importante siempre colocarlo al final del todo para evitar errores:

	![[IMG_152.png]]

	Por lo que si da error, de igual forma se ejecutará el *finally*:

	![[IMG_153.png]]

	**Lanzar excepciones:**

	También es posible lanzar las excepciones. Un ejemplo sería tener un dato numérico, pero que si este es menor a cero, nos lance una excepción. Esto se hace con *raise* indicándole que queremos lanzar una excepción::

	![[IMG_154.png]]

	De esta manera, lo que vemos al final es la excepcion que hemos lanzado y, por ende, se ha detenido el flujo del programa.

	Y lo que observamos antes de nuestra excepcion es conocido como *stack trace* y es una indicación de exactamente qué ha pasado y dónde.

	¡Intenta ocasionar distintos tipos de errores y utilizar excepciones con ello para controlar el flujo de salida de tu programa!

## **Siguientes apuntes**

[[Colecciones_y_estructuras_de_datos_en_Python]]