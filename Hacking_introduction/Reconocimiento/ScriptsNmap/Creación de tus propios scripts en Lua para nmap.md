# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Siguientes apuntes]]
# Introducción

Nmap permite a los profesionales de seguridad personalizar y extender sus capacidades mediante la creación de scripts personalizados en el lenguaje de programación Lua. Lua es un lenguaje de scripting simple, flexible y poderoso que es fácil de aprender y de usar para cualquier persona interesada en crear scripts personalizados para Nmap. 

Para utilizar Lua como un script personalizado en Nmap, es necesario tener conocimientos básicos del lenguaje de programación Lua y comprender su estructura básica que debe tener un script. La estructura básica de un script en Lua en Nmap incluye la definición de una tabla, que contiene diferentes campos y valores que describen la funcionalidad del script.

Los campos más comunes que se definen en la tabla de un script de Lua en Nmap incluyen:

- **description:** Este campo se utiliza para proporcionar una descripción corta del script y su funcionalidad.
- **categories:** Este campo se utiliza para especificar las categorías a las que pertenece el script, como descubrimiento, explotación, enumeración, etc.
- **author:** Este campo se utiliza para identificar al autor del script.
- **license:** Este campo se utiliza para especificar los términos de la licencia bajo la cual se distribuye el script.
- **dependencies:** Este campo se utiliza para especificar cualquier campo de bibliotecas o software que requiere el script para funcionar correctamente.
- **actions:** Este campo se utiliza para definir la funcionalidad específica del script, como la realización de un escaneo de puertos, la detección de vulnerabilidades, etc.

Una vez que el script con Lua esté creado, se puede invocar con Nmap mediante el parámetro **--script** y el nombre del archivo del script. Con la creación de scripts personalizados en Lua es posible personalizar aún más las capacidades de Nmap y obtener información valiosa sobre los sistemas y servicios de la red.
# Práctica

Creamos un archivo **example.nse** y abriremos una sección **HEAD** para aquí colocar nuestro campo de descripción, el cual lleva su contenido entre doble corchetes:

![[021.PNG]]

Como siguiente paso utilizaremos las secciones **RULE** y **ACTION**. 

En nuestra sección **RULE** vamos a definir lo siguiente:

![[022.PNG]]

De esta manera, se verifica que el puerto tenga el protocolo TCP y que además se encuentre abierto. 

Si esta condición se cumple, ahora en nuestro ACTION vamos a mostrar que el puerto en concreto está abierto. Nuestro action estará definido casi de la misma forma que nuestro **portrule** y le agregaremos a ambos un **end** al final; si no, nos dará problemas.

![[023.PNG]]

Recordemos que los puertos los recibimos gracias a que nmap permite que le sean pasados los puertos a enumerar con su parámetro **-p**. Con ello ya tendremos un script sencillo que nos permitirá enumerar puertos TCP abiertos. 

Podremos utilizarlo con **--script** y colocando su ruta absoluta:

```shell
nmap --script [path] -p[ports] [host]
```

![[024.PNG]]

Con ello ya nos habremos montado un script sencillo en Lua y sabremos que tenemos la posibilidad de personalizar scripts para Nmap con Lua.

# Siguientes apuntes

[[Alternativas para la enumeración de puertos usando descriptores de archivo]]