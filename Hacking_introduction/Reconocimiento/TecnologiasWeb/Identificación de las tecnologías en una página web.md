# Índice

# Introducción

Desde el punto de vista de seguridad, es fundamental conocer las **tecnologías** y **herramientas** que se utilizan en una página web. La identificación de estas tecnologías permite a los expertos en seguridad evaluar los riesgos potenciales de un sitio web, identificar vulnerabilidades y diseñar estrategias efectivas para proteger información sensible y los datos críticos. 

Existen diversas utilidades y herramientas en línea que permiten identificar las tecnologías utilizadas en una página web. Algunas de las herramientas más populares incluyen **Whatweb**, **Wappalyzer** y **builtwith.com**. Estas herramientas escanean la página web y proporcionan información detallada sobre las tecnologías utilizadas, como el lenguaje de programación, el servidor web, los sistemas de gestión de contenido, entre otros.

La herramienta **Whatweb** es una utilidad de análisis de vulnerabilidades que escanea la página web y proporciona información detallada sobre las tecnologías utilizadas. Esta herramienta también puede utilizarse para identificar posibles vulnerabilidades y puntos débiles de la página web. 

**Wappalyzer**, por otro lado, es una extensión del navegador que detecta y muestra las tecnologías utilizadas en la página web. Esta herramienta es especialmente útil para los expertos en seguridad que desean identificar rápidamente las tecnologías utilizadas en una página web sin tener que realizar un escaneo completo.

**Builtwith.com** es una herramienta en línea que también permite identificar las tecnologías utilizadas en una página web. Esta herramienta proporciona información detallada sobre las tecnologías utilizadas, así como también estadísticas útiles como el tráfico y la popularidad de la página web. 

Enlaces de las herramientas utilizadas:

- [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
- [Wappalyzer/](https://addons.mozilla.org/es/firefox/addon/wappalyzer/)
- [https://builtwith.com/](https://builtwith.com/)
# Práctica

Cuando nosotros hablamos de las tecnologías que una página web emplea, nos referimos a los lenguajes de programación y herramientas que se utilizan para el desarrollo de toda la web y el mantenerla activa. 

Esto no es de mucha ayuda para saber cómo proceder basándonos en un sitio web. Por ejemplo, en casos como **wordpress** tenemos herramientas como **wpscan** que pueden ser de mayor ayuda para enumerar información. En casos como **Joomla** que también es un CMS como **wordpress**, para este tenemos herramientas como [Joomscan](https://github.com/OWASP/joomscan) que ayudan a aplicar un análisis de vulnerabilidades y reconocimiento en la web.

En función del gestor de contenidos, nosotros tendríamos que saber o investigar por dónde efectuar un análisis más en profundidad o incluso cómo inicializar un ataque. 

La idea es enumerar las tecnologías que tenga la página para con ello saber cómo proceder con el reconocimiento de la misma. En hackerone cambiaremos de target y ahora nos enfocaremos en **xiaomi**. 

En este caso nos enfocaremos específicamente en la página **miwifi.com**.

## Whatweb

Esta es una herramienta que funciona en la terminal y podremos instalarla con nuestro mismo instalador de paquetes. 

Como la utilizaremos, será pasándole el dominio como argumento sin ningún parámetro:

```shell
whatweb http://miwifi.com
```

Esto nos podrá listar información de tecnologías que están corriendo e incluso información que se llegue a ver, como información que luego se queda en cabeceras o incluso emails que se alcanzan a recopilar, **whatweb** nos los llega a listar.

![[Reconocimiento/TecnologiasWeb/images/001.png]]

Esto nos reporta cierta información como que se está corriendo un servidor con **Tengine**, si nosotros investigamos que es esto:

![[Reconocimiento/TecnologiasWeb/images/002.png]]

Con ello en mente, otro concepto que tendríamos que ver es que es **nginx**, que al final es prácticamente lo mismo que un **apache**, que nos ayuda a levantar un servidor. 

En este caso no nos ha reportado ninguna versión de nada, pero en ocasiones si que lo hace y en dados casos podríamos investigar al respecto de dicha tecnología e incluso si es una versión antigua investigar sobre vulnerabilidades o exploits y todo esto tendría que ir en un reporte profesional en caso de estar realmente auditando a la empresa.

Esto que hacemos no es ilegal porque al final es recolección de información pública. Además, para conceptos o cosas nuevas de las cuales no tengamos idea, lo recomendable siempre será investigar y curiosear que al final eso nos ayuda y potencia a llegar a más en esta área tan inmensa de ciberseguridad ofensiva.
## Wappalyzer

**Wappalizer** es un addon o extensión que está disponible tanto para Chrome como para Firefox. Al agregar este a nuestro navegador, realizará un escaneo muy por encima para recopilar las tecnologías de la web que estamos visitando y nosotros podemos verlo.

![[Reconocimiento/TecnologiasWeb/images/003.png]]

En este caso, aparte de la información que hemos recopilado anteriormente, vemos que también emplea una herramienta de análisis para recopilar cosas como la visita a la página y, además, se utiliza **jQuery** el cual es una librería de JavaScript y se está utilizando en su versión 1.5.1. 

Cuando vemos versiones en un dato muy importante para nosotros como atacantes, porque con base en ello podremos investigar por versiones más recientes y en caso de que la que tenga el servicio sea una más antigua, eso quiere decir que tenemos una versión que muy posiblemente sea vulnerable a ciertas técnicas.

En este casi nosotros investigamos para jQuery en esta versión, encontraremos algunas vulnerabilidades tipo **XSS**. 

En este caso visitando la página **security.snik.io** de los propios resultados:

![[Reconocimiento/TecnologiasWeb/images/004.png]]

Como mencionamos anteriormente, todo esto es algo que si o si tendría que estar en un reporte en caso de encontrarnos auditando a una empresa, ya que tenemos que ser detallados en nuestros reportes profesionales cuando vamos a reportar una vulnerabilidad.
## builtwith.com

Aquí lo haremos con la página **www\.miwifi.com**.

En esta herramienta bastará con colocar el enlace de la misma página y con ello nos listará de una forma mucho más detallada información sobre la página:

![[Reconocimiento/TecnologiasWeb/images/005.png]]

En este caso ya sería cuestión de checar más en profundidad todo lo que nos reporta, ya que es mucho más extenso y podríamos llegar a obtener bastante información para saber cómo proceder.
# Siguientes apuntes

[[Fuzzing y enumeración de archivos en un servidor web (1-2)]]