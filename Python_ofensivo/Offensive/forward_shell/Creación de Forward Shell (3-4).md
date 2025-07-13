# Práctica

Después de almacenar el comando en el archivo **input**, iremos leyendo el archivo **output** y será lo que retornaremos para el usuario como output del comando. Para ello crearemos la función **read_output**:

![[043.PNG]]

Además, al momento de enviar el mando al archivo **input** le agregaremos un salto de línea para que simule el presionar el **Enter** y así esto sea como la ejecución del comando, de lo contrario no recibiremos output. 

Si vamos ejecutando comandos, veremos cómo nos arrastra el output de los comandos anteriores:

![[044.PNG]]

Para evitar esto, bastaría que, cada vez que agreguemos un nuevo comando al archivo **input**, limpiemos el contenido del comando **output**. De esta manera recibiríamos únicamente el output del comando recién ejecutado.

![[045.PNG]]

De esta manera, veremos cómo ya tenemos realmente una Shell interactiva:

![[046.PNG]]

Ahora solo vemos un problema y es que cuando llegamos a ejecutar una Shell interactiva o incluso cuando vayamos a tener outputs grandes, estos no los recibiremos completos debido a que no alcanzamos a leerlos cuando realizamos el **cat**. Para evitar esto, nos aseguraremos de repetir el leer el comando al menos 5 veces y entre cada vez que lo lea le aplicaremos una espera de **0.2** segundos. De esta manera, ahora sí recibiremos bien el output, ya que nos aseguramos de esperar el tiempo suficiente para poder leer todo el output:

![[048.PNG]]

La desventaja que podríamos ver es que ahora para recibir el output de cada comando esperaremos 1 segundo, pero es algo válido para asegurar recibir correctamente el output de este comando. 

Ahora podríamos tener este problema, al momento en el que ejecutamos un comando cuando corrimos una bash con **script /dev/null -c bash**. Al ejecutar comandos como el **whoami** veremos el output de la siguiente manera:

![[049.PNG]]

Primeramente, nos repetirá el comando, después nos pondrá el output y finalmente la traza de que estamos en una Shell **bash**. Nosotros, como mejor lo buscaremos representar, es primeramente mostrar la traza de la terminal y seguido de esto el output del comando. 

Para ello, primero que nada, reorganizaremos todo nuestro código para que manejarlo como una clase y después utilizaremos un archivo **main.py** donde lo correremos.

![[050.PNG]]

![[051.PNG]]

![[052.PNG]]

De esta manera, ya lo tendríamos todo listo para, en un archivo main.py, empezar a correr nuestra **Forward Shell** creando una instancia de la clase y ejecutando el método **run()**. Además manejaremos la salida del programa desde el archivo principal **main.py**:

![[053.PNG]]

Ahora, nosotros para lanzar una pseudo terminal bash, utilizamos el comando **script /dev/null -c bash**, por lo que podremos agregar un atributo **is_pseudo_terminal** el cual en un principio esté en **False**, pero si se introduce este comando, se cambie su valor a **True**. De esta manera podremos validarlo para manejar el output para que nos lo muestre como quisiéramos dejarlo:

![[054.PNG]]

Para manejar el output recordemos cómo teníamos la salida. Primeramente nos mostraba el comando que ejecutábamos, después el output y finalmente la traza de la pseudo terminal. Como sabemos que entre cada uno existe un salto de línea, entonces crearemos una lista de cada parte que se nos muestra considerando como delimitador el salto de línea:

![[055.PNG]]

![[056.PNG]]
Como podremos observar, el último elemento siempre es la traza de la pseudo terminal, por lo que podremos mostrar primeramente esto y después la penúltima posición, que es el output del comando.

Si agregamos que imprima el número de caracteres que tiene cuando inicia y cuando ya estás ejecutando comandos, veremos que cuando iniciamos la pseudo terminal, la lista contiene 2 o 3 elementos y, cuando ya ejecutamos comandos, tiene 4, pero puede ser mayor dependiendo del comando ejecutado. Con esto en mente, lo que haremos será mostrar con un salto de línea el último elemento de la misma cuando sea equivalente a 2 o 3:

![[057.PNG]]

Con esto, ya estaremos mostrando correctamente el output de la pseudo terminal cuando recién la ejecutamos.

## Siguientes apuntes

[[Creación de Forward Shell (4-4)]]