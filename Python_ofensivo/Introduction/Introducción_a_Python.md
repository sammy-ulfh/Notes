
## **Índice**

- [[#Historia y filosofía de Python]]
- [[#Características y ventajas de Python]]
- [[#Diferencias entre Python2, Python3, PIP2 y PIP3]]
- [[#Siguientes apuntes]]


## **Historia y filosofía de Python**

*Python* es un lenguaje de programación de alto nivel, interpretado y con una filosofía que enfatiza una sintaxis que favorece un código legible. Fue creado por **Guido van Rossum** y su lanzamiento inicial fue en 1991. Van Rossum modeló Python con la idea de superar las limitaciones del lenguaje ABC, buscando crear un lenguaje que pudiera hacer todo lo que ABC hacia, pero con una sintaxis clara que fuera fácil de aprender y usar.

Desde su concepción, Python ha estado enfocado en el principio de legibilidad y simplicidad. Esto no solo hace que sea más fácil de aprender, sino que también permite a los programadores expresar conceptos complejos en menos líneas de código en comparación con otros lenguajes de programación.

Python se ha desarrollado bajo una licencia de código abierto, lo que significa que cualquiera puede contribuir al desarrollo del lenguaje. Esta filosofía colaborativa ha ayudado a Python a crecer y adaptarse rápidamente a las cambiantes necesidades de la industria tecnológica.

Uno de los documentos más importantes de la comunidad de Python es el *PEP 20* conocido como *El Zen de Python*. Este documento contiene 19 aforismos que capturan la esencia de la filosofía de Python. Algunos ejemplos notables incluyen ==Lo bello es mejor que lo feo==, ==Explícito es mejor que implícito== y ==Si la implementación es difícil de explicar, es una mala idea==.

La filosofía de Python también enfatiza la importancia de la eficiencia y la practicidad. Python se ha diseñado para ser altamente extensible, lo que permite a los programadores escribir nuevos módulos y extensiones en C o C++ para realizar operaciones criticas rápidamente.

En resumen, Python es más que un lenguaje de programación; es una comunidad y una filosofía de diseño que continúa guiando su desarrollo. Con su énfasis en la claridad, la colaboración y eficiencia, Python se ha solidificado como uno de los lenguajes de programación más populares y queridos del mundo.

## **Características y ventajas de Python**

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general que se ha popularizado por su sintaxis legible y clara. Es un lenguaje versátil que permite a los programadores trabajar rápidamente e integrar sistemas de manera más efectiva.

**Características Principales:**

- *Sintaxis simple y fácil de aprender*: Python es famoso por su legibilidad, lo que facilita el aprendizaje para los principiantes y permite a los desarrolladores expresar conceptos complejos en menos líneas de código que serían que serian necesarias en otros lenguajes.
  </br>
- *Interpretado:* Python es procesado en tiempo de  ejecución por el intérprete. Puedes ejecutar el programa tan pronto como termines de escribir los comandos, sin necesidad de compilar.
  </br>
- *Tipado dinámico:*  Python sigue las variables en tiempo de ejecución, lo que significa que puedes cambiar el tipo de datos de una variable en tus programas.
  </br>
- *Multiplataforma:* Python se puede ejecutar en una variedad de sistemas operativos como Window, Linux y MacOs.
  </br>
- *Bibliotecas extensas:* Python cuenta con una gran biblioteca  estándar que está disponible sin cargo alguno para todos los usuarios.
  </br>
- *Soporte para múltiples paradigmas de programación:*  Python soporta varios estilos de programación, incluyendo programación orientada a objetos, imperativa y funcional.


**Ventajas de usar Python:**

- *Productividad mejorada:* La simplicidad de Python aumenta la productividad de los desarrolladores ya que les permite enfocarse en resolver el problema en lugar de la complejidad del lenguaje.
  </br>
- *Amplia comunidad:* Una comunidad grande y activa significa que es  fácil encontrar ayuda, colaboración y contribuciones de terceros.
  </br>
- *Aplicabilidad en múltiples dominios:*  Python se utiliza en una variedad de aplicaciones, desde el desarrollo web hasta la inteligencia artificial, ciencia de datos y automatización.
  </br>
- *Compatibilidad y colaboración:* Python se integra fácilmente con otros lenguajes y herramientas, y es una excelente opción para equipos de desarrollo colaborativo.


Con estas características y ventajas, Python se ha establecido como un lenguaje clave en el desarrollo de software moderno. Su facilidad de uso y su amplia aplicabilidad lo hacen una elección excelente tanto para programadores principiantes como expertos.


## **Diferencias entre Python2, Python3, PIP2 y PIP3**

*Python 2*  y *Python 3* son dos versiones del lenguaje de programación Python, cada una con sus propias características y diferencias clave. *PIP2*  y *PIP3* son herramientas de gestión de paquetes correspondientes a cada versión, utilizadas para instalar y administrar bibliotecas y dependencias.

**Python2 vs Python 3:**

Para instalar Python 2, si tenemos problemas, simplemente agregamos el repositorio de Debian:

```
deb http://deb.debian.org/debian/ bullseye main contrib non-free  
```

A nuestra lista de repositorios, normalmente suele estar en /etc/apt/sources.list, podrá cambiar dependiendo de la distribución y siempre lo indican en este archivo.

Una vez hecho esto, realizamos un update e intentamos instalar Python 2:

```
sudo apt update
sudo apt install python2
```

Para la instalación de pip2 tendremos problemas, pero se soluciona ejecutando lo siguiente:

```python
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py
```

Finalmente, tendremos que agregar al PATH la ruta que nos dé, ya que nos menciona que la ruta donde se instaló no está contemplada dentro del PATH, en este caso a mí me dio la siguiente:

```
/home/user/.local/bin
```

Si quieres que te funcione para usuario root, tendrás que ejecutar el script de Python descargado para root, con eso quedaría.


- *Sintaxis de print:* En Python 2, ==print== es una declaración, mientras que en Python 3, ==print()== es una función, lo que requiere el uso de paréntesis.

	![[IMG_001.png]]

	![[IMG_002.png]]
  </br>
- *División de enteros:* Python 2 realiza una  división entera por defecto, mientras que en Python 3 se realiza una división real (flotante) por defecto.

	![[IMG_003.png]]

	![[IMG_004.png]]
  </br>
- *Unicode:* Python 3 usa Unicode (texto) como tipo de dato por defecto para representar cadenas, mientras que Python 2 utiliza ASCII.
  </br>
- *Librerías:*  Muchas librerías populares de Python 2 han sido actualizadas o reescritas para Python 3, con mejoras y nuevas funcionalidades.
  </br>
- *Soporte:* Python 2  llegó al final de su vida útil en 2020, lo que significa que ya no recibe actualizaciones, ni siquiera para correcciones de seguridad.

**PIP2 vs PIP3:**

- *Gestión de paquetes:* PIP2 y PIP3 son herramientas que permiten instalar paquetes para Python 2 y Python 3, respectivamente. Es importante usar la versión correcta para garantizar la compatibilidad con la versión de Python que estés utilizando.
  </br>
-  *Comandos de instalación:* El uso de pip2 o pip3 antes de un comando determina si el paquete se instalará en Python 2 o Python 3. Algunos sistemas operativos pueden requerir especificar pip2 o pip3 explícitamente para evitar ambigüedades.
   </br>
-  *Ambientes virtuales:* Es una buena práctica usar ambientes virtuales para mantener separadas las dependencias de proyectos específicos y evitar conflictos entre versiones de paquetes para Python2 y Python 3.

	Además, en sistemas como parrot actualmente incluso puede darnos problemas y forzarnos a tener que crear ambientes virtuales, de esta manera podríamos crearlo:

	```
	python3 -m venv nombre_del_entorno
	```

	Finalmente, para que nos funcione tendríamos que cargar este entorno, para que aquí almacene pip las dependencias. Esto lo podríamos hacer con un source y la ruta absoluta:

	```
	source /ruta/absoluta/nombre_del_entorno/bin/activate
	```

	Quedando de la siguiente manera:

	![[IMG_053.png]]


La transición de Python 2 a Python 3 ha sido significativa en la comunidad de desarrolladores de Python, y es fundamental que los programadores comprendan las diferencias y sepan cómo trabajar con ambas versiones del lenguaje y sus herramientas asociadas.

## **Siguientes apuntes**

[[Conceptos_básicos_de_Python]]
