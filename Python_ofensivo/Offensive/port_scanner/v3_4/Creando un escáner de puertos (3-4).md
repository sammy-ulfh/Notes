## Realizando una modificacion en el menu

En este caso nosotros hacemos la comprobación de que los elementos del menú no están vacíos, pero esto podría ser fastidioso al tener ya una serie muy grande de elementos en el menú.

Por ello, en el caso de requerir algunos de forma obligatoria, bastaría con quitar la comprobación que nosotros tenemos y agregar el atributo **required** en la definición de cada argumento y setearlo a **True**:

![[Offensive/port_scanner/v3_4/images/001.png]]

De esta manera, automáticamente al ejecutar el script, nos indicará todos los argumentos que son necesarios para su funcionamiento y si falta alguno, nos dirá cuál es el que falta:

![[Offensive/port_scanner/v3_4/images/002.png]]

## Mejorar la velocidad con hilos

En este caso, como ya no utilizamos la librería **sys** podríamos quitarla y ahora agregar la librería **threading** para trabajar con hilos y acelerar el proceso de nuestro escaneo. 

De esta manera, vamos a agregar los hilos en la función **scan_ports**. Crearemos una lista para almacenar todos los hilos que se vayan generando en cada iteración. 

Le pasaremos como target la función a ejecutar y como **args** los argumentos que le pasaremos a la función. Después iniciaremos, almacenaremos el hilo en la lista y lo iniciaremos:

![[Offensive/port_scanner/v3_4/images/003.png]]

Finalmente, vamos a iterar sobre la lista de los hilos y agregaremos el método **join** para que no cierre el programa hasta que finalicen todos los hilos de ejecutarse.

![[Offensive/port_scanner/v3_4/images/004.png]]

Esto ya nos haría el escaneo de una forma muchísimo más rápida.

## Gestionar hilos

Esto funciona correctamente; sin embargo, podemos llegar a tener errores al realizar escaneos más robustos, ya que, la librería thread al tener muchísimos hilos llega a dar errores, además de que incluso una cantidad muy grande de hilos puede saturar nuestro sistema y volver todo más lento en lugar de rápido. 

Por ello, gestionaremos la cantidad de hilos que deseamos tener simultáneamente activos, para evitar este tipo de errores. 

Esto se puede gestionar directamente con threading, pero esto nos dejaría un código mucho más robusto al ir haciéndolo en tandas de ciertos hilos. 

Por ende, lo que haremos será utilizar **ThreadPoolExecutor** el cual importamos desde **concurrent.futures**. Para ello, podremos utilizarlo con un alias para mantener todo asegurando que se cierre correctamente, utilizando **with**:

![[Offensive/port_scanner/v3_4/images/005.png]]
A **ThreadPoolExecutor** le podemos agregar el atributo **max_workers** para asignarle el total de hilos que deseamos que estén trabajando de forma simultánea. 

**ThreadPoolExecutor** nos permite utilizar **map**, de tal manera que podemos extraer uno a uno los elementos de un iterable y automáticamente pasárselo como argumento a una función:ion:

![[Offensive/port_scanner/v3_4/images/006.png]]

Esta sería la forma en la que debería de funcionar con base en la lógica, sin embargo, al tener dos argumentos, entonces podríamos aprovechar la lógica de las funciones lambda, para recuperar con ella cada puerto y ejecutar nuestra función, pasándole tanto el target como el puerto:

![[Offensive/port_scanner/v3_4/images/007.png]]

Ahora tendríamos una nueva versión del escáner de puertos lista y podríamos escanear puertos con una rapidez buenísima.

## Siguientes apuntes

[[Creando un escáner de puertos (4-4)]]

