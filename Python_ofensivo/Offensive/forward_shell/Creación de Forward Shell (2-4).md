# Práctica

Cuando jugamos con **mkfifo** y utilizamos el comando:

```shell
mkfifo input; tail -f input | /bin/sh 2>&1 > output
```

Lo que estamos haciendo es que cada comando que entre en el archivo input se lea y se ejecute de forma automática por una sh, almacenando el resultado en el archivo output, del cual nosotros podremos recuperar el contenido al leer dicho archivo. 

Un ejemplo práctico de esto, podría ser ir agregando comandos y observando el contenido de output, viendo así que la ejecución de cada comando ahora si que tiene que ver con los anteriores, manteniendo así algo similar a una sesión de una terminal:

![[Offensive/forward_shell/images/031.PNG]]

De esta manera vemos cómo todo se maneja en una especie de sesión y todo ya es más cercano a tener una terminal interactiva. Además, aquí si llegamos a ejecutar cosas como una Shell interactiva con php, si que la tendríamos:

![[Offensive/forward_shell/images/032.PNG]]

En php una forma de crear y mostrar variables es con lo siguiente:

```php
$variable = "valor";
echo $variable;
```

Como hemos solicitado una Shell php interactiva y en teoría ahora la tenemos, este código php debería interpretarnoslo correctamente:

![[Offensive/forward_shell/images/033.PNG]]

Si vemos que nos interpreta correctamente el código php, de esta Shell php interactiva podremos salirnos con solo escribir **quit**. Y si volvemos a los comandos tradicionales de la **sh**, veremos que ahora hemos vuelto a la sh.

![[Offensive/forward_shell/images/034.PNG]]

Además, algo importante a tener en cuenta es que cuando ejecutado comando podremos a llegar a colocar muchísimos caracteres especiales los cuales pueden llegar a corromper una cadena como la que estamos colocando entre las comillas simples, cuando colocamos múltiples veces los mismos tipos de comillas dentro de una cadena de texto.

Por ende, si esto sucediera, aplicaremos un tratado en base64 en nuestro script para evitarlo. Con este concepto claro, ahora pasaremos al script.
## Script

Mencionando lo de evitar romper nuestro comando con los posibles caracteres especiales que pueda llevar, lo convertiremos en base64. Para ello, traeremos b64encode de la librería base64. Lo que pasemos a la función necesitará estar en formato bytes y lo que nos retorne estará en formato bytes, pero nosotros lo buscaremos en string, por lo que le aplicaremos un decode:

![[035.PNG]]

De esta forma, estamos enviando el comando en base64 y lo decodificamos en nuestro propio contenedor, para ejecutarlo con una sh. Con esto en mente, con esta función lo único que haremos será ejecutar el comando con **mkfifo** que nos crearía tanto los archivos **input** y **output** para manejar un tipo de sesión. 

Tenemos la ruta **/tmp** la cual es muy usual para trabajar con archivos temporales; sin embargo, en este caso vamos a trabajar con la ruta **/dev/shm** que es lo mismo que la ruta **/tmp**. 

Para evitar conflictos con que se nos llegue a cerrar nuestro script y se queden creados estos archivos y que al volvernos a conectar retome los mismos archivos de una sesión anterior, utilizaremos la librería random para generar un número aleatorio para la sesión y así evitar estos problemas.

Aquí lo que haremos será crear el número aleatorio para así almacenar nuestros archivos en esta ruta con el nombre **{num}.input/{num}.output**. Para posteriormente trabajar con estos para la ejecución de los comandos. 

Además, recordando que en nuestra terminal se nos quedaba totalmente en espera al ejecutarlo, le pondremos un timeout de 5 segundo a la petición y como sabremos que dará error, la manejaremos con un try para evitar que de error, pero por detrás se quedarán corriendo los archivos con mkfifo funcionando de forma correcta:

![[036.PNG]]

De esta manera generamos el número de nuestra sesión y generamos la ruta completa de cada uno de los archivos respetando la misma sesión.

![[037.PNG]]

De esta manera ya estaríamos creando los archivos con nuestra función **set_setup()** y esto es algo que podríamos verificar si obtenemos una Shell interactiva de nuestro contenedor:

![[038.PNG]]

En este caso, a pesar de estar como root, el único usuario que podrá utilizar este archivo para que funcione como un tipo de sesión será con el que nos conectamos en nuestra webshell. 

Con lo anterior en mente, ahora crearíamos una función distinta para enviar todos los comandos con los que vamos a manejar una sesión, en este caso, lo que se hará es ir introduciendo estos comandos en el archivo **input**:

![[039.PNG]]

![[040.PNG]]

De esta manera, estamos viendo cómo llega correctamente el comando que enviamos al archivo input. 

Además, podremos hacer que cuando nosotros presionemos **CTRL + C** en busca de cerrar el programa, automáticamente nos mande a llamar una función que elimine estos archivos:

![[041.PNG]]
## Extra

Como dato extra, en cuanto a organización en nuestro código podremos llegar a utilizar lo siguiente si lo deseamos:

![[042.PNG]]

Esto nos sirve para de una forma visual observar que es lo que nosotros esperaríamos recibir como tipo de dato y, por el lado de la flecha, sería lo que esperamos retornar. Esto está más enfocado a la organización visual, ya que, no habrá problema si al final no se retornan o reciben estos tipos de datos. Es meramente conceptual de una forma en la que podría ayudarnos a llevar de forma más organizada la estructura y construcción del código. En este caso no lo usaré, pero desde luego es un concepto interesante.

## Siguientes apuntes

[[Creación de Forward Shell (3-4)]]
