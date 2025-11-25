- **grep**

	El comando **grep** será uno de los que más utilizaremos debido a que nos permitirá realizar filtrados en los outputs que generemos, ya sea de comandos o de archivos. Podremos manejar de cierta manera que información mostrar mediante un filtrado.

	Para utilizar grep con filtrado base, verificando si algo esta entre cada linea. Podremos hacerlo sin agregar ningún parámetro, solamente el contenido a filtrar entre comillas:

	![[Temario/images/10.PNG]]

	Como vemos, las verificaciones nos las reporta con base en cada línea si se encuentra una palabra que contenga, ya sea de forma individual la palabra que hemos escrito o dentro de una palabra completa.  

	Es notable cómo la filtración es sensible a mayúsculas y minúsculas, por lo que aquí es donde entran en juego los parámetros.

	**Parámetros**
	- **\-i**

		El parámetro **\-i** nos permite evitar la sensibilidad a letras mayúsculas y minúsculas, por lo que podremos realizar las filtraciones de forma efectiva sin preocuparnos si alguna letra encaja exactamente de la misma manera a como este escrito:

		![[Temario/images/11.PNG]]

	- **\-w**

		El parámetro **\-w** es muy importante debido a que este nos permite seleccionar únicamente aquellas líneas que tengan esa palabra de forma totalmente separada, sin que sea contenido que complemente a otra palabra o texto.

		![[Temario/images/12.PNG]]

		- **\-n**

		Nos retorna como información adicional la línea en la que se encuentra nuestra filtración.

		![[Temario/images/13.PNG]]

- **pwd**

	El comando **pwd** nos permite visualizar en qué directorio nos encontramos actualmente, retornando la ruta absoluta del directorio:

	![[Temario/images/14.PNG]]

 - **ls**

	El comando **ls** nos permite listar el contenido de nuestro directorio actual, permitiendo la vista de archivos y carpetas dentro de la actual:

	![[Temario/images/15.PNG]]

	No solo permite listar el contenido del directorio actual, sino que también nos permite realizarlo para directorios específicos, pasándoselo como si de un argumento se tratase:

	![[Temario/images/17.PNG]]

	**Parámetros:**

	- **\-l**

		El parámetro **\-l** nos permite listar lo mismo, pero en una forma en la que toda la información sea representada, de tal manera que podremos observar los permisos, propietario y grupo asignado a cualquier directorio o archivo, así como el peso de estos.

	- **\-a**

		![[Temario/images/16.PNG]]

		Muestra todos los directorios y archivos, considerando también los ocultos. Los archivos y directorio ocultos son todos aquello que inicial por un punto.

		**.** -> Siempre será el directorio actual en el que nos encontramos.

		**..** -> Siempre será el directorio que está detrás del actual. Por ejemplo, si estamos en el directorio **\/home\/sammy**, el directorio **..** sería el directorio **\/home\/**.

- **cd**

	El comando **cd** viene de change directory, que como su nombre lo indica, nos permite cambiar entre directorios, lo que nos permite el movernos fácilmente entre el sistema mediante el uso de la terminal.

	Al utilizarlo tendremos que pasarle como argumento el directorio al cual deseamos movernos. Si el directorio se encuentra dentro del directorio actual, bastará con colocar únicamente las sub carpetas, sin colocar la ruta absoluta:

	![[Temario/images/18.PNG]]

	Si intentamos movernos a una ruta que no está dentro de la carpeta Fondos que es en la que estamos, esto nos daría error:

	![[Temario/images/19.PNG]]

	Esto sucede debido a que busca el directorio dentro del directorio actual. Para que esto realmente nos funcione, tendremos que colocar toda la ruta absoluta, tal cual como la vemos con **pwd**. De la siguiente manera:

	![[Temario/images/20.PNG]]

- **clear**

	El comando **clear** nos permite directamente limpiar todo lo que tenemos en nuestra terminal:

	![[Temario/images/21.PNG]]

	![[Temario/images/22.PNG]]

	Esto funcionará perfectamente sin problemas si en lugar del comando empleamos la combinación de teclas **ctrl + l**.

- **touch**

	El comando **touch** nos permite crear archivos dentro de algún directorio, donde como argumento le tendremos que pasar el nombre:

	![[Temario/images/23.PNG]]

	Incluso podremos crear un archivo dentro de otro directorio:

	![[Temario/images/24.PNG]]

- **mkdir**

	El comando **mkdir** nos permite crear directorios:

	![[Temario/images/25.PNG]]

	Este directorio se crea vacío.

- **rmdir**

	El comando **rmdir** nos permite eliminar sin problemas directorios totalmente vacíos:

	![[Temario/images/26.PNG]]

	Sin embargo, si intentamos eliminar un directorio que tiene contenido, no nos lo permitirá:

	![[Temario/images/27.PNG]]

- **rm**

	El comando **rm** por sí solo nos permite eliminar archivos:

	![[Temario/images/28.PNG]]

	Pero además, este comando es el que nos permitirá eliminar directorios que no se encuentren vacíos, gracias a utilizar el parámetro **\-r** que sería como indicarle que elimine todo de forma recursiva, eliminando archivo por archivo dentro de los subdirectorios:

	![[Temario/images/29.PNG]]

- **head**

	El comando **head** nos permite seleccionar el contenido de un output por líneas, considerando un enfoque desde la parte superior hasta la inferior.

	Para indicarlo siempre utilizaremos el parámetro **\-n**, donde podremos indicarle que desde arriba a abajo nos tome el número de líneas que indiquemos, en este caso las primeras 2:

	![[Temario/images/30.PNG]]

	Sin embargo, esto también lo podremos trabajar con signos, por lo que si en lugar de solo agregar el número le agregamos un signo negativo antes de este, lo que hará será tomarnos todas las líneas superiores, evitando el número de líneas indicadas considerando el final:

	![[Temario/images/31.PNG]]

	De esta manera, lo que hace es imprimir todas las líneas, evitando o eliminando las últimas dos líneas.

- **tail**

	El comando **tail** funciona igual que head, con la diferencia de que este inicia desde la parte inferior del output (las últimas líneas):

	![[Temario/images/32.PNG]]

	De esta manera muestra las últimas dos líneas. De la misma manera que con head, también podremos trabajar agregándole un signo positivo, sucedera lo mismo, evitando una linea antes de las líneas superiores que indiquemos, imprimiendo el resto:

	![[Temario/images/33.PNG]]

- **awk**

	El comando **awk** tiene una similitud con el comando **grep**, ya que en ciertos casos nos puede ayudar a realizar filtraciones como las hace dicho comando; sin embargo, el enfoque será en la capacidad de realizar un filtrado por parámetros, donde por defecto toma los espacios como separación y realizará lo indicado para cada línea:

	![[34.PNG]]

	En este caso, imprime el primer argumento de cada línea, considerando que el separador es un espacio. El separador se puede indicar si así lo deseamos, mediante el parámetro **\-F** donde de forma continua colocamos dos comillas y dentro de ellas el separador que consideraremos.

	![[35.PNG]]

	En este caso en las líneas centrales fueron reemplazados los espacios por una barra, por ende seleccionamos este como la consideración para cada parámetro y por ende tiene el mismo funcionamiento en esas líneas, excepto en la final, ya que no existe ninguna barra y todo lo considera como un mismo argumento.

- **wget**

	El comando **wget** nos permite extraer cualquier tipo de documento hacia nuestro ordenador para tenerlo disponible de forma local.

	Nos permite realizar una solicitud hacia cualquier lugar en internet. Donde si tenemos el link directo a la descarga de un archivo, lo que recibiremos será el archivo. Si hacemos una petición directa a una página,  recibiremos el código de la misma.

	- **Descargar Discord:**

		Link de [descarga](https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64):
		```
		https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64
		```
		![[36.PNG]]

	- **Descargar archivo de un servidor abierto con Python:**

		Con Python se pueden llegar a abrir servidores que usualmente son para funcionamiento de forma local:

		![[37.PNG]]

- :(){ :|:& };:

	A esto se le conoce como **Fork Bomb**, representan un riesgo en el sistema, ya que buscan saturar el sistema. Principalmente, son aplicados en ataque de denegación de servicios (DoS), explotando los recursos del sistema, ocasionando que servicios como **SSH** dejen de operar.

	¿Cómo puedo aplicar una medida de seguridad para esto?

	Para evitar que comandos como este afecten a nuestro sistema de forma que lo sature, tendríamos que limitar los procesos que se puedan correr en simultáneo. Para ello, tenemos el archivo de configuración **\/etc\/security\/limits.conf** donde se almacena esta configuración, pero para modificarlo podremos utilizar el comando **ulimit -u numero_de_procesos**.

	Esto permitiría colocar un límite de procesos para el usuario dado.

	![[38.PNG]]
## Siguientes apuntes

[[Control de flujo, operadores y procesos en segundo plano]]
## Material de Apoyo

[Chuleta de comandos básicos](https://ciberninjas.com/chuleta-comandos-linux/)
[Comandos básicos de Linux](https://www.bonaval.com/kb/cheats-chuletas/comandos-basicos-linux)

![[basic_commands.pdf]]