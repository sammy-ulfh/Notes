# Índice

# Introducción

Veremos cómo se pueden utilizar distintos parámetros de **wfuzz** para ajustar el alcance y la profundidad del reconocimiento en aplicaciones web. Algunos de los parámetros cubiertos incluyen el parámetro **-sl**, para filtrar por un número de líneas determinado, el parámetro **-hl** para ocultar un número de líneas determinado y por último el parámetro **-z** para indicar que tipo de dato queremos utilizar de cara al reconocimiento que nos interese aplicar, abarcando opciones como diccionarios, listas y rangos numéricos. 

Adicionalmente, otra herramienta que se examina que es perfecta para la enumeración de recursos disponibles en una plataforma en línea, es **Burpsuite**. Burpsuite es una plataforma que integra características especializadas para realizar pruebas de penetración en aplicaciones web. Una de sus particularidades es la **función de análisis de páginas en línea**, empleada para identificar y enumerar los recursos accesibles en una página web.

**Burpsuite** cuenta con dos versiones: una **versión gratuita** (**Burpsuite Community Edition**) y una **versión de pago** (**Burpsuite Professional**).

## BurpSuite Community Edition

Es la **versión gratuita** de esta plataforma. Su función principal es desempeñar el panel de **proxy HTTP** para la aplicación, facilitando la realización de pruebas de penetración. 

Un **proxy HTTP** es un filtro de contenido de alto rendimiento, ampliamente utilizado en el hacking con el fin de interceptar el tráfico de red. Esto permite analizar, modificar, aceptar o rechazar todas las solicitudes y respuestas de la aplicación que se esté auditando.

Algunas de las ventajas que la versión gratuita ofrece son:

- **Gratuita:** La versión Community Edition es gratuita, lo que la convierte en una opción accesible para principiantes y profesionales con presupuestos limitados.
- **Herramientas básicas:** Incluye las herramientas esenciales para realizar pruebas de penetración en aplicaciones web, como el Proxy, el Repeater y el Sequencer.
- **Intercepción y modificación del tráfico:** Permite interceptar y modificar las solicitudes y respuestas HTTP/HTTPS, facilitando la identificación de vulnerabilidades y la exploración de posibles ataques.
- **Facilidad de uso:** La interfaz de usuario de la Community Edition es intuitiva y fácil de utilizar, lo que facilita su adopción por parte de usuarios con diversos niveles de experiencia.
- **Aprendizaje y familiarización:** La versión gratuita permite a los usuarios aprender y familiarizarse con las funcionalidades y técnicas de pruebas de penetración antes de dar el salto a la versión Professional.
- **Comunidad de usuarios:** La versión Community Edition cuenta con una amplia comunidad de usuarios que comparten sus conocimientos y experiencias en foros y blogs, lo que puede ser de gran ayuda para resolver problemas y aprender nuevas técnicas.

A pesar de que la Community Edition no ofrece todas las funcionalidades y ventajas de la version Professional, sigue siendo una opción valiosa para aquellos que buscan comenzar en el ámbito de las pruebas de penetración o que necesitan realizar análisis de seguridad básicos sin incurrir en costos adicionales.

## BurpSuite Professional

BurpSuite Professional es la **versión de pago** desarrollada por la empresa **PortSwigger**. Incluye, además del proxy HTTP, algunas herramientas de pentesting web como:

- **Escáner de seguridad automatizado:** Permite identificar vulnerabilidades en aplicaciones web de manera rápida y eficiente, lo que ahorra tiempo y esfuerzo.
- **Integración con otras herramientas:** Puede integrarse con otras soluciones de seguridad y entornos de desarrollo para mejorar la eficacia de las pruebas.
- **Extensibilidad:** A través de su API, BurpSuite Professional permite a los usuarios crear y añadir extensiones personalizadas para adaptarse a necesidades específicas.
- **Actualizaciones frecuentes:** La versión profesional recibe actualizaciones periódicas que incluyen nuevas funcionalidades y mejoras de rendimiento.
- **Soporte técnico:** Los usuarios de BurpSuite Professional tienen acceso a un soporte técnico de calidad para resolver dudas y problemas.
- **Informes personalizables:** La herramienta permite generar informes detallados y personalizados sobre las pruebas de penetración y los resultados obtenidos.
- **Interfaz de usuario intuitiva:** La interfaz de BurpSuite Professional es fácil de utilizar y permite a los profesionales de seguridad trabajar de manera eficiente.
- **Herramientas avanzadas:** Incluye funcionalidades avanzadas, como el módulo de intrusión, el rastreador de vulnerabilidades y el generador de payloads, que facilita la identificación y explotación de vulnerabilidades en aplicaciones web.

Tanto la Community Edition como la versión Professional de BurpSuite ofrecen un conjunto de herramientas útiles y eficientes para realizar pruebas de penetración en aplicaciones web. Sin embargo, la versión Professional brinda ventajas adicionales.

La elección entre ambas versiones dependerá del alcance y las necesidades específicas del proyecto o de la empresa. Si se requiere un conjunto básico de herramientas para pruebas de seguridad ocasionales, la Community Edition podría ser suficiente. No obstante, si se busca una solución más completa y personalizable, con soporte técnico y herramientas avanzadas para un enfoque profesional y exhaustivo, la versión Professional sería la opción más adecuada.
# Práctica

## Wfuzz

Cuando cargamos un diccionario en **wfuzz** mediante el parámetro **-w** es como si tuviésemos una especie de lista sobre la cual se itera para ir probando cada uno de los elementos. 

Esto mismo podremos hacerlo para enumerar probando una serie mayor de posibilidades, tal como es la extensión de archivos. 

Para ello también podríamos utilizar el parámetro **-z**, con este también podríamos llegar a cargar nuestro diccionario con la palabra clave **file** y acompañado de una coma, a un lado colocar nuestro diccionario:

```shell
wfuzz -c -t 100 -z file,/path-to-dictionary.txt https://www.amazon.com/FUZZ
```

Con ello en mente, también podríamos listar extensiones de archivos específicas como txt:

```shell
wfuzz -c -t 100 -z file,/path-to-dictionary.txt https://www.amazon.com/FUZZ.txt
```

Como podemos hacer esto, en lugar de probar con cada una de las extensiones en distintos ataques de fuerza bruta, podremos crear una lista con el parámetro **-z** y en lugar de colocar la palabra clave **file**, utilizaríamos la palabra clave **list**:

```shell
wfuzz -c -t 50 --hc=404 -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -z list,html-txt-php https://www.amazon.com/FUZZ.FUZ2Z
```

Cuando efectuamos una segunda lista de elementos a ir probando, utilizaríamos de igual manera la palabra clave **FUZZ**, pero al ser para una segunda lista tendríamos que colocar un número **2** entre ambas letras **z**. 

Con ello ya iría probando para cada elemento las tres extensiones diferentes, llegando a listarnos archivos:

![[Reconocimiento/Fuzzing/images/011.png]]

Para cargar un diccionario podremos hacerlo con cualquiera de los dos parámetros, pero desde luego es más cómodo hacerlo con el parámetro **-w**. 

En este caso vemos cómo se encuentra un archivo el cual es **security.txt**. Si intentamos abrirlo en el navegador apuntando a este recurso, veremos lo siguiente:

![[Reconocimiento/Fuzzing/images/012.png]]

Esto incluso nos muestra que Amazon está dentro del programa de Bounty en hackerone. 

Si nos enfocamos en los resultados del escaneo, en la parte superior tenemos las flags de lo que es el **ID**, **Response** (código de estado), **Lines** (número de líneas de la respuesta), **word** (número de palabras de la respuesta), **Chars** (número de caracteres de la respuesta) y también podremos filtrar por ellos.

Con **--hl** sería para esconder aquellas con un número específico de líneas y con **--sl** sería para mostrar aquellas con un número específico de líneas.

De la misma manera tenemos **--hw** y **--sw** para palabras. Finalmente, tenemos **--sh** para mostrar aquellas con un número de caracteres específicos o **--hh** para ocultar aquellas con un número de caracteres específicos, por lo que tenemos diversas formas de aplicar filtrados en cuanto a los resultados con **wfuzz**.

## Ffuf

**Ffuf** es otra herramienta del estilo, pero esta se encuentra escrita en **GO**. Teniendo en cuenta que Go es bastante bueno para el manejo de sockets y conexiones en redes, usualmente este tipo de programas van mucho más rápido cuando se escriben en lenguajes de programación como este. 

En este caso, yo clonaré la herramienta [Ffuf](https://github.com/ffuf/ffuf) de su repositorio en mi directorio **/opt** y me meteré en el mismo. Estando en el directorio, construiré la herramienta con **go build .** y con ello ya tendremos el ejecutable:

![[Reconocimiento/Fuzzing/images/013.png]]

Con ello ya tendremos el ejecutable, pero si checamos su peso con el comando **du** con el parámetro **-hc** veremos su peso:

![[Reconocimiento/Fuzzing/images/014.png]]

En este caso es de 14 MB, pero este es un valor que podremos llegar a reducir con la herramienta **upx** pasándole el ejecutable:

![[Reconocimiento/Fuzzing/images/015.png]]

Esto nos deja un tamaño mucho menor, pero incluso podríamos llegar a reducirlo si al momento de construir la aplicación con **go build** le agregamos el parámetro **-ldflags** y a este le pasamos como argumento **"-s -w"** y realizamos lo mismo que hicimos anteriormente con **upx**:

![[Reconocimiento/Fuzzing/images/016.png]]

Con ello vemos cómo llegamos a reducir el tamaño de una forma mucho mayor. 

**Ffuf** se utiliza casi de la misma manera y con los mismos parámetros:

```shell
./ffuf -c -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -u https://www.amazon.com/FUZZ
```

Al igual que wffuz el parámetro **-c** es para que nos reporte la información con colores. Además, si quisiéramos emplear hilos, se haría con el parámetro **-t**. En este caso se emplea la palabra clave **FUZZ** al igual que Wfuzz.

![[Reconocimiento/Fuzzing/images/017.png]]

En este caso vemos cómo nos muestra el código de estado **301** el cual se da cuando se aplican redirecciones. Si quisiéramos ver hacia dónde se dan estas redirecciones, podríamos utilizar el parámetro **-v** de verbose para mostrar información más a detalle:

```shell
./ffuf -c -t 50 -v -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -u https://www.amazon.com/FUZZ
```

![[Reconocimiento/Fuzzing/images/018.png]]

Si quisiéramos enfocarnos en un código de estado específico, sería utilizando el parámetro **--mc=200**. En el ejemplo anterior buscaría el match con aquellas que tengan el código de estado 200. 

Ffuz tiene bastantes opciones y ya sería checarlas nosotros mismos y ver de qué forma podremos trabajar con esta herramienta.

## Phonebook.cz

Como anteriormente hemos visto, phonebook para de forma pasiva mostrar subdominios, al igual que emails con la recopilación de información pública, también podremos utilizarla para de forma pacífica mostrar **URL's**. 

En este caso, si colocamos el dominio de **amazon.com** veremos resultados de URL's en este caso:

![[Reconocimiento/Fuzzing/images/019.png]]

## BurpSuite


# Siguientes apuntes

[[]]