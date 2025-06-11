## Introduccion

En este caso nos olvidaremos de la libreria **sys** para trabajar con los argumentos directamente. Tenemos la libreria **argparse** que nos ayuda a poder crear menues para manejar todo incluso con opciones dentro de nuestro script, tales como **-h** para un panel de ayuda.

## Practica

Iniciaremos considerando la siguiente estructura para esta version del escaner de puertos:

![[001.png]]

Iniciaremos generando una variable target, la cual almacenara el contenido que nos retorne nuestra funcion **get_arguments** y esto lo consideraremos como nuestro host:

![[002.png]]

En nuestra funcion **get_arguments** vamos a crear una instancia de la clase **ArgumentParser** de nuestra libreria **argparse** y le agregaremos el parametro **description**, en este caso sera **Fast TCP Port Scanner**:

![[003.png]]

Para ir agregando las opciones o argumentos, utilizaremos el metodo **add_argument** y de lo podremos indicar de distintas maneras, en este caso **-t** o **--target**, finalmente le agregaremos el parametro especifico **dest** el cual hace a referencia a destino y colocaremos entre comillas el nombre de la variable en la cual queremos que nos almacene el valor que le sea pasado, esta variable no tiene que estar creada previamente.

Finalmente, tenemos el parametro especifico **help** al cual podremos darle una descripcion de ayuda para el propio argumento que estamos considerando agregar:

![[004.png]]

Ahora, podremos recopilar todos los argumentos con su contenido con el metodo **parse_args()**, lo que nos permitira acceder a estos y verificar si tienen contenido cada una de las cosas necesarias y de lo contrario indicar que faltan argumentos saliendo con un codigo de estado no exitoso con la libreria sys:

![[005.png]]

De la misma forma, podriamos agregar el **first_port** y **last_port**, eliminando de esta forma las variables globales que utilizabamos:

![[006.png]]

Finalmente transformamos y verificamos que los puertos sean datos numericos y retornamos todas las opciones para recibir el rango de puertos y el host desde la funcion principal **main**:

![[007.png]]

Y en nuestra funcion main, al recibir todo en la variable **target**, ya podriamos utilizarlo:

![[008.png]]

De esta manera, ahora al ejecutar al script, si agregamos la opcion **-h** nos muestra un panel de ayuda para ver que opciones tenemos, asi como la descripcion de nuestro programa:

![[009.png]]

![[010.png]]

Al tener una serie de opciones que son obligatorias, ya lo que podriamos hacer es colocar todo en un solo condicional con AND y que imprima el panel de ayuda, lo cual se hace con el metodo **print_help**:

![[011.png]]

Hasta este punto esta bien, pero podremos trabajarlo de otra manera. Podremos tener un solo argumento para los puertos, para poder trabajarlo en un rango **100-500** o tomando en consideracion puertos especificos **22,80,90**, lo cual nos ayuda para aplicar un split y hacerlo facilmente, entonces utilizariamos solamente el argumento **-p**:

![[012.png]]

En este caso, retornamos de forma individual tanto el target como el puerto, por lo que en nuestra funcion main tambien lo recibiremos de esta manera y verificando si en nuestros puertos tenemos **-** o **,** haremos un split y lo trabajaremos de forma distinta, si es guion sera con un bucle for en un rango, mientras que si son separados por coma haremos el split e iteraremos sobre esa lista:

![[013.png]]

## Refactorizar el codigo

Lo ideal siempre es tener la logica del codigo lo mejor estructurada posible, asi como que la logica no se manege directamente en main.

Para ello, en este caso como estamos trabajando con un objeto iterable en ambos casos, podremos mover esta logica a una funcion, donde retornemos solamente el iterable y lo iteremos en una funcion distinta.

Podremos crear la funcion **parse_ports** para trabajar la logica para retornar los iterables:

![[014.png]]

De esta manera, hemos hecho que al obtener la lista de nuestro puerto en ambas partes, teniendo coma o guion, se aplique directamente a cada elemento un TypeCast para convertir los puertos a un dato numerico y finalmente retornar directamente el iterable sobre el cual nuestro bucle iterara para mandar a llamar al escaneo con su puerto y target especificos.

Esto funciona correctamente, pero aun nos falta el caso en el que le pasemos directamente un puerto especifico, que en este caso retornaremos una tupla sobre la que tambien pueda iterar nuestro bucle de **scan_ports** para realizar el escaneo:

![[015.png]]
