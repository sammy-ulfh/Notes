
## **Índice**

* [[#Organización del código en módulos]]
* [[#Importación y uso de módulos]]
* [[#Creación y distribución de paquetes]]
## **Organización del código en módulos**

1. **Introducción**

	La organización del código en módulos es una práctica esencial en Python para construir programas escalables y mantenibles. Los módulos son archivos de Python que contienen definiciones y declaraciones de variables, funciones, clases u otros objetos que se pueden reutilizar en diferentes partes del programa.

	*Estructura de Módulos:*

	Cada módulo en Python es un archivo *.py* que encapsula tu código para un propósito específico. Por ejemplo, puedes tener un módulo para operaciones matemáticas, otro para manejo de entradas/salidas y otro para la lógica de la interfaz de usuario. Esta estructura ayuda a mantener el código organizado, facilita la lectura y hace posible la reutilización de código.

	*Importación de Módulos:*

	Python utiliza la palabra clave *import* para utilizar módulos. Puedes importar un módulo completo como *import math*, o importar nombres específicos de un módulo utilizando *from math import sqrt*. Python tambien permite la importación de módulos con un alias para facilitar su uso dentro del código, como *import numpy as np*.

	*Paquetes:*

	Cuando los programas crecen y los módulos comienzan a acumularse, Python permite oprganizar módulos en paquetes. Un paquete es una carpeta que contiene módulos y un archivo especial llamado *\_\_init\_\_.py* , que indica a Python que esa carpeta contiene módulos que pueden ser importados.

	*Ventajas de los Módulos:*

	* *Mantenimiento:* Los módulos permiten trabajar en partes del código de manera independiente sin afectar otras partes del sistema.
	  </br>
	* *Espacio de nombres:* Los módulos definen su propio espacio de nombres, lo que significa que puedes tener funciones o clases con el mismo nombre en diferentes módulos sin conflicto.
	  </br>
	* *Reutilización:* El código escrito en módulos puede ser reutilizado en diferentes programas simplemente importándolos donde se necesiten.

	</br>
2. **Práctica**

	Un módulo será otro archivo en Python que tenga definiciones de clases, variables y funciones, los cuales podrán ser importados desde otros scripts, lo que nos ayuda a tener el código de una forma mucho más estructurada, limpia y escalable.

	Teniendo esto en cuenta, comenzaríamos creando un archivo *math_operations.py* y en este definiremos funciones con las operaciones básicas *suma*, *resta*, *multiplicacion* y *division*:

	![[IMG_444.png]]

	De esta manera lo guardamos y ahora buscaríamos reutilizar todo este *script* y sus funciones definidas desde otro script, el cual llamaremos *main.py*, esto porque sería como nuestro script principal.

	Aquí lo que tendríamos que hacer es importarlo de la siguiente manera:

	![[IMG_445.png]]

	Lo que Python hará, será buscar este archivo en el directorio actual, por lo que no haría falta colocar una ruta absoluta. Tampoco hace falta colocar él *.py*, ya que al importarlo Python automáticamente sabe que nos referimos a otro módulo, el cual también es un script en Python.

	De esta manera, ahora con referenciar al módulo que hemos importado y luego a la función que queramos ejecutar, podríamos realizar lo siguiente:

	![[IMG_446.png]]

	De esta manera, ahora el script principal nos queda mucho más limpio.

	Ahora, si quisiéramos hacer referencia directamente a la función sin referencias al módulo, lo que podríamos hacer es importar directamente estas funciones del módulo:

	![[IMG_447.png]]

	Y esto nos funcionaría como si de una función que tuviésemos definida dentro de nuestro mismo script se tratase.

	*Bibliotecas estándar en Python*

	De esta manera, ahora podremos hablar sobre las bibliotecas estándar de Python, ya que estas están divididas en módulos y las podremos utilizar, por lo que podríamos importar alguna como *math*:

	![[IMG_448.png]]

	Y algo que podríamos hacer cuando no sepamos que contiene la librería y que podríamos utilizar de esta, es aplicarle un *dir()* y esto nos retornará en pantalla la capacidad que tenemos de módulos a utilizar:

	![[IMG_449.png]]

	De esta manera tenemos algunas como *sqrt* (para raiz cuadrada), *pow* (para exponentes), *tan* (para tangente), entre otros.

	Ahora podríamos de math traernos *sqrt* y utilizarlo para sacar la raíz cuadrada de algún número:

	![[IMG_450.png]]

	En algunos casos específicos en los que lleguemos a utilizar una gran variedad de las funciones que ya tenga definida una librería, lo que podríamos hacer es importar todo.

	Lo malo es que nos traería absolutamente todos los módulos de esta librería, pero tampoco afectaría tanto en cuanto al rendimiento respecta:

	![[IMG_451.png]]

	Es importante aclarar que estos módulos no dependen como tal de un script, ya que estos ya vienen incorporados directamente con Python y traen sus propios módulos, por lo que no dependerán de un script.

	Esto podríamos verlo con un ejemplo en el que transformamos un texto a una cadena *md5* con la librería *hashlib*:

	![[IMG_452.png]]

	Esto nos transformaría un texto a md5, pero finalmente también podremos ver su archivo, ya que este módulo depende de uno para su funcionamiento.

	En cambio, en cuanto a *math*, como Python ya lo tiene incorporado, esto no dependerá de ningún archivo:

	![[IMG_453.png]]


## **Importación y uso de módulos**


1. **Introducción**

	La importación y uso de módulos es una técnica fundamental en Python que permite la modularidad y la reutilización del código. Los módulos son archivos de Python con extensión *.py* que contienen definiciones de funciones, clases y variables que se pueden utilizar en otros scripts de Python.

	*Importación de Módulos:*

	La declaración *import*  es usada para incluir un módulo en el script actual. Cuando importas un módulo, Python busca ese archivo en una lista de directorios definida por *sys.path*, la cual incluye el directorio actual, los directorios listados en al variable de entorno *PYTHONPATH*, y los directorios de instalación por defecto.

	*Uso de Módulos:*

	Una vez que un módulo es importado, puedes hacer uso de sus funciones, clases y variables, utilizando la sintaxis *nombre_del_modulo.nombre_del_elemento*. Esto es esencial para organización del código, ya que permite acceder a código reutilizable sin necesidad de duplicarlo.

	*Importación con Alias:*

	A veces, por conveniencia o para evitar conflictos de nombres, puedes querer darle a un módulo un alias al importarlo usando la palabra clave *as*: *import module as alias*

	Esto permite acceder a los componentes del módulo usando el alias en lugar del nombre completo del módulo.

	*Importación Específica:*

	Si solo necesitas una o varias funciones específicas de un módulo, puedes importarlas directamente usando *from modulo import function*. Esto permite no tener que prefijar las funciones con el nombre del módulo cada vez que se llaman. Además, puedes importar todas las definiciones de un módulo (aunque no es una práctica recomendada) usando *from modulo import \**.

	*Módulos de la Biblioteca Estándar:*

	Python viene con una biblioteca estándar extensa que ofrece módulos para realizar una variedad de tareas, desde manipulación de texto, fecha y hora, hasta acceso a internet y desarrollo web. Familiarizarse con la biblioteca estándar es crucial para ser un programador eficiente en Python.

	*Módulos de Terceros:*

	Además de las bibliotecas estándar, hay una amplia gama de módulos de terceros disponibles que puedes instalar y utilizar en tus programas. Estos módulos a menudo se instalan utilizando herramientas de gestión de paquetes como *pip*.

	</br>
2. **Práctica**

	Podríamos importar una librería en Python con un alias, lo cual nos puede servir para tener una forma más sencilla de referirnos a esta librería, para esto se utiliza *as* y podríamos hacerlo con cualquier librería:

	![[IMG_454.png]]

	De esta manera, cuando referenciamos a un módulo de la librería math, para referenciar a la misma librería, bastaría con colocar *m*, ya que fue el alias que le dimos.

	O de la misma forma podría funcionarnos para el módulo con el que sacamos la raíz cuadrada si quisiéramos traerlo directamente:

	![[IMG_455.png]]

	**Concepto de Python Library Hijacking:**

	Este concepto en ciberseguridad hace referencia al *secuestro de librerías*, teniendo en cuenta que las librerías son un conjunto de módulos que trabajan en sincronía para proporcionar una funcionalidad, por lo que una librería contendrá varios módulos y paquetes.

	Entonces tendremos que tener en cuenta que Python busca sus librerías y para ello está algo similar al PATH en Linux.

	Estas rutas podremos verlas en el intérprete de Python si utilizamos la librería *sys* y referenciamos al path:

	![[IMG_456.png]]

	Por lo que estas rutas, que están separadas por comas, son las que Python tiene en cuenta cuando queremos importar una librería, buscando en cada una de las rutas, una a una, la librería que queremos importar.

	Por lo que si importáramos la librería *hashlib* al imprimir la dirección de su archivo, esta estaría dentro de una de las direcciones contempladas por el PATH mostradas anteriormente:

	![[IMG_457.png]]

	Pero también, si observamos el PATH que tiene en cuenta Python, hay que tener cuidado porque este se puede modificar, tal como el PATH de Linux y además la primera referencia a módulos y librerías que es el *' '*, referencia al directorio de trabajo actual.

	Por lo que con base en esto, por ejemplo, de un archivo que tuviese la librería *hashlib*, pues al saber esto podríamos crearnos un script *hashlib.py* en el directorio actual, de forma que ahora nosotros podríamos definir su comportamiento.

	Antes de esto, podríamos tener en cuenta la librería *os*, ya que en Linux esta nos podría permitir ejecutar comandos de bash desde Python:

	![[IMG_458.png]]

	De esta manera, con *os.system()*, podremos ejecutar cualquier comando, en el output del comando *whoami* que ejecutamos, la primera línea es el resultado del comando y la segunda es el código que retorna la ejecución de este, en este caso es 0 porque fue exitoso.

	Por lo que ahora en nuestro archivo *main.py* vamos a importar la librería *hashlib*, si hemos creado antes el archivo *hashlib.py* en el directorio actual, la renombraremos temporalmente para que no entre en conflicto:

	![[IMG_459.png]]

	Al importar la librería luego crearemos una variable con el texto "hola":

	![[IMG_460.png]]

	Esta es una cadena de texto la cual está en UNICODE, pero le agregaremos una *b* al inicio para convertir a BYTES para que sea una representación numérica de los datos y esto lo hacemos, ya que *md5* de esta librería requiere que esto esté en bytes para poder representar la cadena en *md5* y lo haríamos de la siguiente manera:

	![[IMG_461.png]]

	¿Qué es md5?

	El md5 es un algoritmo de reducción criptográfico, usualmente es utilizado para por ejemplo transformar dos archivos o cadenas y ver si la conversión fue igual, lo cual nos puede servir para verificar si algún archivo fue modificado.

	Lo que quiere decir que mientras algo no sea modificado, la cadena resultante será estática.

	Entonces, ahora podremos ver como nuestro script en el archivo *main.py* está funcionando correctamente, pero si ahora nuestro archivo *test.py* lo renombramos a *hashlib.py*, donde tendremos como contenido:

	![[IMG_462.png]]

	Por lo que ahora si ejecutáramos nuestro archivo *main.py* con el contenido que ya tenía, ahora realmente nos estaría llamando como módulo al archivo *hashlib.py* que está en el directorio actual, por lo que nos ejecutaría el comando "whoami":

	![[IMG_463.png]]
	De esta manera, ahora vemos como primeramente se ve el output del comando y luego el error mostrado se debe a que Python no ha encontrado el módulo que queremos ejecutar para efectuar la conversión a *md5* y esto es evidente, ya que realmente no estamos importando la librería necesaria para efectuar esas operaciones.

	Entonces, con esto, como nosotros podemos crearnos nuestros propios módulos, Python buscara primeramente en el directorio actual de trabajo, lo que claramente podría suponer un riesgo de cara a la seguridad.

	Por ejemplo, si somos un usuario *pepito* sin privilegios, pero por alguna razón se nos otorga el permiso de que con *sudo*, podremos ejecutar el script con permisos de usuario con privilegios y suponiendo que estamos en un entorno controlado, pues no tendremos permisos para editar el archivo *main.py*, pero suponiendo que por alguna razón el directorio sí que tiene permisos de escritura para el usuario *pepito*, entonces al ver que desde el archivo *main.py* se utiliza la librería *hashlib*, entonces el usuario podrá crearse el script *hashlib.py*.

	Por lo que esto representa un riesgo, ya que al ser ejecutado con permisos de usuario privilegiado, este archivo en lugar de ejecutar el comando "whoami" pues podría ejecutar otro y la diferencia aquí es que ahora los comando se estarían inyectando como *root* con los permisos privilegiados, algo que ya es crítico porque se puede hacer cualquier cosa.

	Otra forma de llegar a poder realizar el *Python Library Hijacking*, sería el poder tener un permiso de escritura sobre alguna de las rutas del PATH en el que Python realiza sus búsquedas, pues aquí podríamos directamente editar *hashlib.py*, ya que la librería *hashlib* si depende de un archivo de Python.

	O por ejemplo si la librería que se solicita está en la última ruta del PATH, pero por alguna razón tenemos permisos de escritura en algún directorio que una de las rutas absolutas que en el PATH esta antes de la que tiene la librería, pues podremos en esa crear un script con el nombre de la librería y dado que Python va revisando cada ruta una a una, de izquierda a derecha, se quedará con el primero que encuentre.


## **Creación y distribución de paquetes**

1. **Introducción**

	La creación y distribución de paquetes es un proceso clave en el ecosistema de Python, que permite a los desarrolladoes compartir sus bibliotecas y módulos con la comunidad global. Un paquete en Python es una colección estructurada de módulos que pueden incluir código reutilizable, nuevos tipos de datos, o incluso aplicaciones completas.

	*Creación de Paquetes:*

	Para crearun paquete, primero se organiza el código en módulos y subpaquetes dentro de una estructura de directorios. Cada paquete en Python debe de contener un archivo especial llamado *\_\_init\_\_.py*, que puede estar vacío, pero indica que el directorio es un paquete de Python. Este archivo también puede contener código para inicializar el paquete.

	*Estructura de Directorios:*

	La estructura típica de un paquete podría incluir directorios para documentación, pruebas y el propio código, asi como archivos de configuración para la instalación y la distribución del paquete.

	*Archivos de Configuración:*

	Los archivo *setup.py* y *pyproject.toml* son fundamentales en la creación de paquetes. Contienen metadatos y configuraciones necesarias para la distribución del paquete, como el nombre del paquete, versión, descripción y dependencias.

	*Distribución de Paquetes:*

	Para distribuir un paquete se suele utilizar Python Package Index (*PyPi*), que es un repositorio de software para la comunidad de Python. Subir un paquete a PyPi lo hace accesible para otros desarroladores mediante herramientas de gestión de paquetes como *pip*.

	*Instalación Global:*

	Al distribuir un paque, los usuarios pueden instalarlo a nivel global en su entorno de Python, lo que significa que estará disponible para todos los proyectos en ese entorno. Esta es una manera eficaz de compartir código y permitir que otros se beneficien y contribuyan al trabajo que has hecho.

	*¿Por Qué Empaquetar y Distribuir?:*

	Empaquetas y distribuir software tiene varios beneficios. Permite la reutilización de código, facilita la colaboración entre desarrolladores, y ayuda a la gestión de dependencias y versiones de software. Además, contribuir a la comunidad de código abierto puede llevar al reconocimiento del trabajo del desarrollador y proporcionar oportunidades para recibir retroalimentación y mejoras colaborativas.

	En resumen, aprenderemos el proceso de empaquetado y distribución de software en Python, desde la organización inicial del código hasta su publicación en PyPI y la instalación global, brindando las habilidades necesarias para contribuir efectivamente al ecosistema de Python.

	</br>
2. **Práctica**

	Los paquetes en Python nos servirán para organizar nuestros módulos que son scripts en Python los cuales realizan diversas funcionalidades y además contiene un archivo *\_\_init\_\_.py*, para que Python entienda bien la jerarquía de directorios de nuestro paquete.

	**¿Qué es PyPi?**

	El *Python Package Index* es el repositorio de software oficial para aplicaciones de software de terceros en el lenguaje de programación Python.

	Si nosotros llegamos a instalar una librería como pwntools con pip3: *pip3 install pwntools*, al utilizar este gestor de paquetes lo estaríamos instalando directamente de PyPi.

	Por lo que si vamos a la web de [PyPi](https://pypi.org/) y buscamos por *pwntools*, aquí veríamos el proyecto de esta librería, una descripción de como funciona, los contribuidores e inclusos los releases que se le han dado.

	Incluso aquí podremos ver como instalar el paquete:

	![[IMG_464.png]]

	Entonces, para poder subir proyectos en PyPi, tendremos que crearnos una cuenta y agregar nuestro móvil por el doble factor de autenticación y una vez hecho loguearnos, de lo contrario no podremos subir nuestros propios paquetes en PyPi.


	Una vez tengamos creada nuestra cuenta de PyPi, en el directorio del usuario nos crearemos un archivo *.pypirc*, el cual tendrá como contenido:

	```
	[pypi]
		username = __token__
		password = 
	```

	La password o token es algo que aun no tenemos pero para ello nos tendemos que ir a nuestro perfil en PyPi y luego a *account setting*, ahí buscaríamos hasta API tokens y presionaríamos en *Add API tokens*:

	![[IMG_465.png]]

	De esta manera crearemos un token para todos los proyectos dándole un nombre y este será el que almacenaremos en el apartado de password.

	**Creando nuestro propio paquete en Python**

	La idea ahora será crear un paquete *Hack4u* o con cualquier otro nombre en el cual a través de algunos módulos se crearan funciones que nos permitirán en todo momento saber los cursos que están existentes en la academia *Hack4u* donde cada curso nos lo represente de la forma *Nombre* *Link* y *Duración*.

	Así mismo, luego crearemos un módulo *utils.py*, el cual luego se encargue de darnos la duración total de cada curso (la suma de las horas totales).

	Un paquete es un directorio que contiene una serie de módulos, por lo que primeramente crearemos nuestro directorio *hack4u_project* y dentro de este primeramente crearemos nuestro directorio *hack4u*, así como los archivo *setup.py* y *README.md*, donde README será para agregar la descripción de este proyectito.

	Por lo que ahora tendríamos nuestro directorio *hack4u_project* de la siguiente manera:

	![[IMG_466.png]]

	Ahora dentro del directorio *hack4u* el cual será nuestro paquete.

	Ahora estando dentro del paquete tendremos que crearnos un archivo *\_\_init\_\_.py*, en cada paquete que lleguemos a crear tendremos que colocar este archivo, por lo que si en nuestro directorio  principal *hack4u_project* tuviésemos otro paquete, este también tendría que llevar el archivo. Esto es necesario para que Python comprenda la jerarquía de los directorios.

	Ahora, en nuestro paquete *hack4u*, crearemos un módulo el cual se llamara *cursos.py*:

	![[IMG_467.png]]

	En módulo que hemos creado comenzaremos creando la clase Curso, la cual tendrá contemplado en el constructor los atributos *name*, *duration* y *link*:

	![[IMG_468.png]]

	Con esto, lo que tendremos en mente es que cada curso lo tendremos en cuenta como un objeto, por lo que crearemos una lista *courses*, que es una lista de objetos. Aquí se definirán objetos que serán instancias temporales de la clase *Cursos*. En este caso actualmente la academia cuenta con 4 cursos, por lo que pondremos estos:

	*Links*

	* *Introducción a Linux:*`https://hack4u.io/cursos/introduccion-a-linux/`
	* *Personalización de entorno en Linux:* `https://hack4u.io/cursos/personalizacion-de-entorno-en-linux/`
	* *Python ofensivo:* `https://hack4u.io/cursos/python-ofensivo/`
	* *Introducción al Hacking:* `https://hack4u.io/cursos/introduccion-al-hacking/`

	Con esto, ahora crearemos nuestro 4 objetos dentro de la lista y de esta manera al imprimir la lista veremos que es una lista de objetos:

	![[IMG_469.png]]

	Aquí podremos recordar que tenemos la capacidad de listar un objeto con algo que queramos mostrar utilizando en método especial *\_\_str\_\_*, por ende lo que haremos será recorrer la lista y listar cada objeto:

	![[IMG_470.png]]

	Con esto listo, ahora definiríamos que vamos a mostrar cuando un objeto sea listado, mediante nuestro método especial *\_\_str\_\_*:

	![[IMG_471.png]]

	De esta manera, al listar objeto a objeto recorriendo la lista, nos funcionaría correctamente.

	Pero aqui tenemos un pequeño problema, ya que solo funciona si queremos listar directamente el objeto, al hacerlo con la lista nos seguiría representando que son objetos:

	![[IMG_472.png]]

	Para solucionar esto, lo que haremos será utilizar otro método especial, este será sustituido en el lugar de *\_\_str\_\_*, ya que funciona de la misma manera, pero nos permitirá que la información de cada curso llegue a mostrarse incluso cuando listemos la lista de objetos:

	![[IMG_473.png]]

	Este es el método especial *\_\_repr\_\_* y ahora al listar el contenido de la lista si funcionaria sin ningún problema:

	![[IMG_474.png]]

	Y si volviéramos a colocar el listar cada objeto de forma individual, mientras recorremos la lista de objetos, nos funcionaría de la misma manera la que funciona como un tipo de *\_\_str\_\_*:

	![[IMG_475.png]]

	Ahora lo que haremos será colocar lo que imprime los cursos en una función, la cual llamaremos *list_courses*:

	![[IMG_476.png]]

	Con esto listo, dentro del directorio de nuestro paquete vamos a ejecutar el intérprete de Python e importaremos nuestro paquete *hack4u*, tendrá que ser dentro del mismo directorio la que de esta manera buscara primeramente aqui y lo encontrara sin problemas:

	![[IMG_477.png]]

	De esta manera, lo que estamos haciendo es que con *import hack4u.cursos*, estamos importando el módulo *cursos.py* de nuestra librería *hack4u*. Traemos directamente el módulo para poder llamar a la función con *hack4u.cursos.list_courses()* y de esta manera se nos listan los cursos.

	O podríamos importar de este módulo la función *list_courses*, de esta manera ya no tendríamos que referenciar a la librería y módulo al inicio:

	![[IMG_478.png]]

	En este caso, nos estaremos dando cuenta de que tenemos que colocar el nombre del paquete y luego el nombre del módulo al momento de importarlo (*import hack4u.cursos*), por lo que no podríamos hacer *from hack4u import list_courses*, ya que esto nos daría error. Lo cual se debe a que Python entra en conflicto, ya que no sabe en qué módulo se encuentra esta función.l

	Entonces para esto tenemos nuestro archivo *\_\_init\_\_.py*, aquí definiremos que para nuestro módulo *cursos* no importe la función o directamente todo:

	![[IMG_479.png]]

	O al definir en nuestro archivo *\_\_init\_\_.py* que nos importe todo, igual funcionaría:

	![[IMG_480.png]]

	Es importante recordar que para poder importar nuestro paquete, el directorio *hack4u* de nuestro paquete tendrá que ser un subdirectorio del directorio actual, ya que será donde Python buscará.

	De esta manera, ahora también podríamos importar directamente la función *list_courses* de nuestro paquete, ya que gracias a la definición en nuestro *\_\_init\_\_.py* ya se estará cargando el contenido del módulo *cursos* y Python sabrá de dónde tomar la función.

	![[IMG_481.png]]

	Por lo que si quisiéramos e importamos todo lo del módulo *courses* tanto en nuestro *\_\_init\_\_.py* como al intérprete, podríamos hasta jugar directamente con la lista de los objetos *courses*:

	![[IMG_482.png]]

	Así como con cualquier otro contenido que estuviese definido dentro de nuestro módulo.

	Ahora, en nuestro módulo vamos a crear una función *search_course_by_name()*, con esta vamos a recorrer la lista de objetos y nos enfocaremos en el nombre, donde nosotros podremos pasarle como argumento un nombre la función y esta comparará este nombre con cada objeto, en caso de encontrar el curso con el nombre que le pasemos, lo retornará.

	De lo contrario, al terminar el bucle  retornaría None.

	![[IMG_483.png]]

	De esta manera, ahora podríamos buscar por nombre cuando carguemos todo de nuestro paquete en el intérprete de Python:

	![[IMG_484.png]]

	Con esto ya tendríamos representado lo que nos interesaría con base en los cursos, pero ahora vamos a crear otro módulo llamado *utils.py*, este nos servirá para devolver la duración total para todos los cursos.

	![[IMG_485.png]]

	En nuestro módulo *utils.py* primeramente tendremos que darle el acceso a la lista de objetos que contiene toda la información, por ende tendremos que importarlo desde el modulo *cursos* que tenemos en el directorio actual:

	![[IMG_486.png]]

	De esta  manera estaríamos importando la lista de objetos *courses*, para tener acceso a ella. Esto nos permitirá trabajar con toda la información de los cursos y en este caso acceder a lo que nos interesa que es la duración en horas de estos.

	Entonces ahora crearemos una función *total_duration()* y en esta definiremos en una sola línea si deseamos que nos itere en toda la lista  y por cada objeto tome el atributo *duration* y todo esto lo pondremos dentro de la función *sum()* que ya trae el propio Python, que recordemos que puede funcionar para iterables y va recogiendo y sumando los valores en cada iteración, por lo que nos regresaría una suma total de las horas de todos los cursos.

	![[IMG_487.png]]

	Sabiendo que esto nos retornaría la cantidad total de horas de todos los cursos, por último tendremos que indicar que nos importe todo lo de este módulo cuando sea llamado el paquete *hack4u*, lo cual también se especifica en nuestro archivo *\_\_init\_\_.py*:

	![[IMG_488.png]]

	Finalmente, lo importaríamos de nuestro paquete dentro del intérprete de Python y ahora estaría funcionando correctamente:

	![[IMG_489.png]]

	Recordemos que dentro del intérprete de Python, cuando valores son retornados de funciones, sin importar el tipo de dato, esto se mostrara directamente, a diferencia de cuando ejecutamos un script, ya que en este caso nosotros tendremos que decidir si mostrarlo en pantalla o no con *print()*.

	Ahora, si observáramos todos los archivos que tenemos dentro de donde se encuentran nuestros módulos, se nos genera una carpeta *\_\_pycache\_\_*, esta podremos borrarla y no afectara en nada:

	![[IMG_490.png]]

	Ahora, desde el directorio principal del proyecto, todos los archivos y carpetas los veríamos de esta manera (en cuanto a que existan, lo mostrado solo es una representación de todo en forma de arbol):

	![[IMG_491.png]]

	Ahora, para poder crear nuestro paquete y subirlo a *PyPi*, tendremos que colocar cierta información en nuestro archivo setup.py, lo cual es lo siguiente:

	```
	from setuptools import setup, find_packages

	# Leer el contenido del archivo README.md
	with open("README.md", "r", encoding="utf-8") as fh:
		log_description = fh.read()

	setup(
		name="hack4u",
		version="0.1.0",
		packages=find_packages(),
		install_requires=[],
		author="Sammy-ulfh",
		description="Una biblioteca para consultar cursos de hack4u.",
		long_description=log_description,
		long_description_content_type="text/markdown",
		url="https://hack4u.io",
	)
	```

	Primeramente en *name* colocaríamos el nombre del paquete.

	En *version* la versión de nuestro paquete, al ser la primera versión, será la "0.1.0".

	En *packages* se utiliza la función *find_packages()* para encontrar o descubrir todos los paquetes que existan, es posible tener múltiples paquetes por lo que esta función en el directorio actual los busca y los muestra o representa.

	De resto colocamos el autor y la descripción.

	En *long_description* estaríamos colocando el contenido a mostrar, lo que pasa donde está el comentario es que se lee el archivo y todo su contenido se guarda en la variable *long_description*, por ello mismo se iguala a la variable y es todo el contenido del archivo de presentación del proyecto y está en formato Markdown y esto lo indicamos en *long_description_content_type*.

	Finalmente le agregamos una *url*.

	En este caso, como el mismo proyecto ha sido creado diversas veces por lo que es mejor cambiarlo para evitar errores al subirlo con twine.

	*Markdown* tiene cierta forma de configurar el contenido para una buena visualización mediante lugares que lo soporten, tales como *github*. Aquí no será explicado el uso de *Markdown* por ende lo que colocaremos en el archivo README.md, será lo siguiente:

	![[README]]

	Con todos los archivos listos, ahora para subirlo ahora tendremos que instalar *twine* con *pip3*:

	![[IMG_492.png]]

	Ahora dentro de nuestro proyecto ejecutaremos `python3 -m build`:

	![[IMG_493.png]]

	![[IMG_494.png]]

	Esto nos creará un directorio *dist* y dentro de este tendríamos todo en un archivo comprimido:

	![[IMG_495.png]]

	Con todo listo, ahora podríamos subir el proyecto, y antes verificaríamos que nuestro perfil está sin proyectos:


	![[IMG_496.png]]


	Recordemos tener el archivo .pypirc en el directorio home del usuario, con la configuracion del API TOKEN que creamos anteriormente.
	
	Ahora con twine le indicaremos que queremos subir todo lo que está en dist:

	![[IMG_498.png]]
	
	![[IMG_497.png]]

	Ahora veremos como ya tenemos un proyecto:

	![[IMG_499.png]]
	 
	 Y ya podríamos ver el README:

	![[IMG_500.png]]

	Para cualquier cambio que realicemos en nuestros proyectos de paquetes, tendremos que ir incrementando la version en nuestro *setup.py* y volver a hacer el *build* con python3 y subirlo con twine.

	Ahora podríamos perfectamente eliminar todo el paquete que tenemos como proyecto y olvidarlo:

	![[IMG_501.png]]

	De esta manera, ahora podríamos instalarlo y trabajar tal como en los ejemplos que estuvimos viendo durante su creación:

	![[IMG_502.png]]

	![[IMG_503.png]]

	![[IMG_504.png]]

	Ahora si listáramos el archivo de este paquete que nosotros creamos, veremos como se almacena dentro de las rutas que Python tiene contempladas en su PATH:

	![[IMG_505.png]]

	Si nos moviéramos a este directorio veremos como esto es todo lo que hicimos nosotros:

	![[IMG_506.png]]

	Si deseamos podremos desinstalarlo con `pip3 uninstall paquete` y después para evitar conflictos `pip3 cache purge` para limpiar la caché.

[[#Índice]]

## **Siguientes apuntes**

[[Entrada_y_salida_de_datos]]

