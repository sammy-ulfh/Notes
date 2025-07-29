# Índice

- [[#Introducción]]
- [[#BurpSuite Community Edition]]
- [[#BurpSuite Professional]]
- [[#Práctica]]
- [[#Wfuzz]]
- [[#Ffuf]]
- [[#Phonebook.cz]]
- [[#BurpSuite]]
- [[#Configuración del navegador]]
- [[#Tráfico en BurpSuite]]
- [[#Fuzzing con información de peticiones que realiza la plataforma por detras]]
- [[#Enumeración]]
- [[#Siguientes apuntes]]

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

**Burpsuite** es una herramienta que funciona como proxy capturando el tráfico y, si queremos interceptarlo para realizar distintas cosas o ver más a fondo lo que está sucediendo, nos lo permite. 

Esta herramienta la podremos instalar con nuestro instalador de confianza del sistema, de no ser así, quiere decir que no se encuentra en los repositorios y tendremos que buscar otra alternativa. 

Cuando nosotros ejecutemos **BurpSuite** tendremos que aceptar los términos y condiciones. Al pasar a la siguiente ventana solo le daremos a siguiente y finalmente iniciar burp.

Con ello ya tendríamos BurpSuite Community Edition para empezar a utilizarlo:

![[Reconocimiento/Fuzzing/images/020.png]]

Nos enfocaremos en la funcionalidad de proxy. Si vamos al apartado de Proxy y a las configuraciones del mismo, veremos lo siguiente:

![[Reconocimiento/Fuzzing/images/021.png]]

Veremos que se encuentra un proxy en escucha corriendo en local en el puerto 8080. 

Con BurpSuite tenemos dos opciones: en el apartado de **target** y después en **site map** nos dejará abrir un navegador basado en Chromium el cual ya trae el propio BurpSuite con todo correctamente configurado y ya podremos empezar a navegar e ir viendo el tráfico en burpsuite.

Por otro lado, podemos configurar nosotros mismos un proxy y un certificado en un navegador aparte.

## Configuración del navegador

Con ello en mente, ahora en nuestro navegador Firefox agregaríamos el addon (extensión) de **FoxyProxy**, con ello podremos permitir que nuestro tráfico en el navegador pase por bursuite una vez configuremos el proxy para **BurpSuite**. 

Cuando agreguemos el addon, vamos a abrirlo y veremos lo siguiente:

![[Reconocimiento/Fuzzing/images/022.png]]

Nos iremos a las opciones y en proxies agregaremos un nuevo proxy:

![[Reconocimiento/Fuzzing/images/023.png]]

![[Reconocimiento/Fuzzing/images/024.png]]

Una vez lo guardemos, nos aparecerá en nuestra ventana de la extensión cuando la presionemos:

![[Reconocimiento/Fuzzing/images/025.png]]

Al seleccionarlo, ya estaría pasando el tráfico por BurpSuite, pero de primeras tendremos el siguiente error:

![[Reconocimiento/Fuzzing/images/026.png]]

Esto se debe a que es tráfico HTTP y tendremos que agregar un certificado al navegador para confiar en bursuite. Este podremos descargarlo accediendo a la página **http:\//burpsuite**. Confiaremos en la página HTTP y en la parte superior derecha donde dice **CA CERTIFICATE** presionaremos y nos dejará descargarlo, podría ser en la carpeta de descargas. 

Ahora en la configuración de nuestro navegador filtraremos por **certificates** y en **view certificates** le daremos a importar y agregaremos este certificado que acabamos de descargar en nuestro ordenador:

![[Reconocimiento/Fuzzing/images/027.png]]

Al momento de agregarlo, seleccionaremos la primera opción y le daremos a **ok**:

![[Reconocimiento/Fuzzing/images/028.png]]

## Tráfico en BurpSuite

Con ello ya estaría listo y ahora podríamos navegar tranquilamente, pero mientras tanto veremos cómo en **BurpSuite** en el apartado de **target** y después en **site map** se está capturando:

![[Reconocimiento/Fuzzing/images/029.png]]

También tenemos la posibilidad de irnos al apartado de **Proxy** y veremos cómo intercept está en **off**. Si lo encendemos, ahora el tráfico que pase por nosotros se quedará en espera antes de continuar su tráfico, ya que nosotros tendremos que aceptarlo o rechazarlo:

![[Reconocimiento/Fuzzing/images/030.png]]

Esto nos sirve bastante en enfoques ya más preciosos como lo es el hacking web, además de que nos permite visualizar a qué rutas de la página se están realizando las peticiones. Recordemos apagar el interceptor si no queremos estar aceptando cada solicitud.

## Fuzzing con información de peticiones que realiza la plataforma por detras

En este caso para enumeración **BurpSuite** puede ser de ayuda para ir viendo toda la información como peticiones que se hacen por detrás, como a la API que en ocasiones puede llegar a estar como subdominio del mismo dominio y basándose en los lugares en donde pueda realizar otras peticiones aplicar **FUZING**. Un ejemplo claro sería cuando Amazon o alguna tienda hace peticiones para mostrar un producto. 

En estos casos en ocasiones la petición se hace mediante una URL a la cual mediante parámetros se le puede pasar el ID del producto.

Desde luego abra productos que no existan, pero sí tenemos como ejemplo la ruta: **amazon.com\/productId=1567**, podríamos hacer fuzzing con una herramienta como **wfuzz** y crear una lista de rango de números con el parámetro **-z range,1-20000**, esto nos generaría una lista de números del 1 al 20,000 y con la palabra clave FUZZ podríamos probarla con cada productId. 

Si vemos que muchas peticiones repiten el mismo número de líneas, por ejemplo, podríamos esconder esas peticiones con el parámetro **--hl** que esconde peticiones referentes a ciertos números de líneas en su respuesta.

Finalmente, ya nos podría mostrar de forma más segura los productos que realmente existen y esto es posible aplicando **FUZZING**. 

En el caso de Amazon no es así, ya que se le pasa bastante contexto de un producto seleccionado y por ende es un tanto distinto.

## Enumeración

En cuanto al tráfico que estemos generando, **BurpSuite** nos irá almacenando los subdominios o dominios por los que por detrás se llegan a realizar peticiones en la navegación y podremos llegar a visualizarlos en el apartado de **target** y **site map** dentro de target, incluso si desplegamos los dominios que nos aparecen podríamos llegar a listar recursos como archivos y directorios:

![[Reconocimiento/Fuzzing/images/031.png]]

Toda esta información la vemos porque las plataformas por detrás hacen búsquedas que nosotros no visualizamos para mostrarnos el resultado esperado en la navegación de la misma. 

Con estas herramientas ya tenemos un alcance muy potente para el reconocimiento de información importante y aplicación de **Fuzzing** para búsqueda de recursos o directorios.
# Siguientes apuntes

[[Google Dorks - Google Hacking (Los 18 Dorks más usados)]]