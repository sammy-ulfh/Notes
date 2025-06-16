
Nuestra tarjeta de red tiene un identificador único, el cual está compuesto por el OUI (identificador del fabricante) que corresponde a los primeros 3 bytes y el OUA (Identificador único de la tarjeta asignada por el fabricante). 

En este caso realizaremos una herramienta para cambiar este identificador único, por el que quisiéramos cambiarlo.

## Macchanger

En este caso, para nuestro programa vamos a requerir de los argumentos del nombre de la interfaz de red, así como de la nueva dirección MAC que queremos asignar. 

Una de las interfaces de red que se encuentren en la computadora será la que estará conectada a internet. Usualmente, vienen con nombres típicos como **ens33, eno1, wlan0, eth0**, pero el nombre podría ser distinto. 

Para ello, primeramente vamos a generar nuestras funciones para manejar el menú y la salida correcta del programa en caso de que sea presionado **CTRL + C**:|

![[Offensive/macchanger/images/001.png]]

En este caso está hecho el menú con argparse para recuperar **-i** (interface) y **-m** (nueva dirección Mac) y ambos son argumentos obligatorios o requeridos. 

Después realizaremos nuestra función principal **main**, en esta vamos a recuperar los argumentos y mandaremos a llamar a nuestra función que realizará el cambio de la dirección Mac:

![[./images/002.png]]

En nuestra función **change_mac_address** vamos a verificar primeramente que los datos ingresados sean correctos, comparando la interfaz con la que tenemos en la computadora activa, y la dirección Mac con una regex:

![[Offensive/macchanger/images/003.png]]

Primero con la librería os, utilizando **os.getuid()** obtenemos el UID del usuario que se encuentra ejecutando el script, ya que solamente el usuario administrador puede cambiar la Mac Address, en caso de no ser el usuario root imprimirá el mensaje y saldrá con un código de estado incorrecto mediante la librería **sys**. 

Si el usuario root ejecuta el script, entonces ahora verificará que la interfaz de red ingresada por el usuario sea correcta. Por ello utilizamos la librería socket, ya que con **socket.if_nameindex()** obtenemos un iterable que convertimos a string en cada posición utilizando **map**. 

Iteramos cada línea del objeto **map** y como cada iteración se recibe un string similar a una tupla, se realiza un filtrado dividiendo en una lista con **split**, hasta finalmente obtener solamente el nombre de cada interfaz y almacenarlo dentro de una lista de comprensión.

Después removemos de la lista la interfaz **loopback**, ya que es como la local. 

Con la interfaz que dio el usuario, se verifica si se encuentra en todas las interfaces que se encuentran en nuestro ordenador. 

Para la dirección Mac, se busca un match con una regex, donde se crea un grupo que verifica que se cumpla la estructura **0b:** 5 veces y al final solo los primeros son sin los dos puntos. Cada carácter puede tener un número del 0-9, o una letra de la A-F en mayúsculas o minúsculas.

Si existe un match, la variable almacenará contenido y, si no existe, no almacenará nada. 

Por ello, al final se comparan ambas variables y esto nos retornará un valor **True** si ambos son correctos o **False** si alguno o ambos son incorrectos. 

Finalmente, si esto es verdadero, entrará en el condicional de nuestra función **change_mac_address**:

![[Offensive/macchanger/images/004.png]]

Aquí se utiliza la librería **subprocess** para ejecutar comandos Linux en nuestra computadora. Los comandos que ejecutaremos son los siguientes:

```shell
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:00:00:00:00:00
ifconfig wlan0 up
```

En este caso, **wlan0** representa a la interfaz de red. Primero se da de baja la interfaz, después se cambia la dirección Mac donde la que se encuentra después de **ether** representaría una nueva y finalmente se vuelve a dar de alta la interfaz. 

Se busca tener una respuesta de cada ejecución de comandos, ya que si se obtiene, quiere decir que se dio un error al ejecutar alguno de los comandos.

Esto es importante como para la dirección MAC, ya que si la dirección Mac no es válida, da error. 

Podremos listar **OUI** de direcciones Mac En Linux podremos utilizar el comando:

```shell
macchanger -l
```

Para listar una gran cantidad de OUI's que serían los primeros 3 bytes de una dirección Mac.

Finalmente, si todo se cambia correctamente, se nos imprime el mensaje y podremos ver la Mac Address que hemos colocado con:

```shell
macchanger -s wlan0
```
