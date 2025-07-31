# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Enfoque en un dominio]]
- [[#Encontrar subdominios]]
- [[#Encontrar archivos por extensión]]
- [[#Herramientas de Google Hacking]]
- [[#Exploit-db]]
- [[#Siguientes apuntes]]
# Introducción

El **Google Dork** es una técnica de búsqueda avanzada que utiliza operadores y palabras clave específicas en el buscador de Google para encontrar información que normalmente no aparece en los resultados de búsqueda regulares. 

La técnica de **Google Dorking** se utiliza a menudo en el hacking para encontrar información sensible y crítica en línea. Es una forma eficaz de recopilar información valiosa de una organización o individuo que puede ser utilizada para realizar pruebas de penetración y otros fines de seguridad.

Al utilizar Google Dorks, un atacante puede buscar información como nombres de usuarios y contraseñas, archivos confidenciales, información en bases de datos, números de tarjetas de crédito y otra información crítica. También se puede utilizar esta técnica para identificar vulnerabilidades en aplicaciones web, sitios web y otros sistemas en línea. 

Es importante tener en cuenta que esta técnica de Google Dorking **no es ilegal en si misma**, pero puede ser utilizada con fines maliciosos. Por lo tanto, es crucial utilizar esta técnica con responsabilidad y ética en el contexto de la seguridad informática y el hacking ético.
# Práctica

Google hacking es una forma de aprovechar la posibilidad de búsquedas avanzadas en Google. Dichas búsquedas podemos realizarlas con palabras clave como **site**.

## Enfoque en un dominio

Si nosotros buscamos en Google **amazon.com** nos arrojará resultados que incluso no estén bajo el dominio de Amazon, pero si le agregamos **site:** antes del dominio, ahora si que nos listaría únicamente resultados para este dominio:

![[Reconocimiento/GoogleDorks/images/001.png]]

![[Reconocimiento/GoogleDorks/images/002.png]]

## Encontrar subdominios

También podremos aprovechar este tipo de búsquedas para llegar a enumerar subdominios de un mismo dominio como si de una expresión regular se tratase, utilizando **site:\*.amazon.com**:

![[Reconocimiento/GoogleDorks/images/003.png]]

Esto podría llegar a ser una técnica extra para enumerar subdominios de forma pasiva, por lo que es legal todo esto al ser recolección de información pública. 

La desventaja con esto, a diferencia de las herramientas que vimos para la enumeración de subdominios, es que en ocasiones un solo subdominio arroja muchísimos resultados y es muy repetitivo, por lo que nos puede complicar la tarea de reconocer diversos subdominios distintos.

## Encontrar archivos por extensión

En un dominio nosotros podremos llegar a buscar archivos por su extensión, en este caso utilizando el mismo dominio, podremos agregar también la palabra clave **filetype:** y agregar el prefijo de terminación de los tipos de archivos como **txt** o **pdf**:

![[Reconocimiento/GoogleDorks/images/004.png]]

En este caso vemos cómo llegamos a listar archivos como **security.txt** el cual también llegamos a enumerar con las herramientas de enumeración activa. 

También podremos utilizar el prefijo **ext:** para, mediante OR -> **|**, indicar múltiples extensiones para realizar la búsqueda, como **pdf** y **txt**:

![[Reconocimiento/GoogleDorks/images/005.png]]

Cuando nosotros hacemos este tipo de búsquedas si llegamos a encontrar algún recurso interesante, como por ejemplo en este caso uno de los PDF, podríamos abrirlo y copeando el enlace traerlo hacia nuestra máquina con **wget** y existe una herramienta en terminal la cual es **exiftool** que pasándole un archivo nos permite ver sus metadatos:

![[Reconocimiento/GoogleDorks/images/006.png]]

Esto es importante porque en ocasiones podríamos encontrar archivos que nos den información valiosa en sus metadatos al momento de empezar nuestra etapa de reconocimiento teniendo un target.

## Herramientas de Google Hacking

Podríamos buscar en Google **pentest-tools** y, en específico, la página `https://pentest-tools.com/` es la que nos interesaría. En ella nos iremos al apartado de **tools** y entre las múltiples herramientas que tiene buscaremos la de Google hacking:

![[Reconocimiento/GoogleDorks/images/007.png]]

Esta herramienta recolecta una serie de aproximadamente 20 Dorks los cuales nos permiten realizar distintas búsquedas para llegar a encontrar cosas vulnerables. 

Nosotros tendríamos que colocar el target y seleccionar, por ejemplo, para buscar documentos que estén públicamente expuestos:

![[Reconocimiento/GoogleDorks/images/008.png]]

Esto nos crea un Dork que nos contempla la búsqueda de múltiples archivos que ciertamente podrían ser potencialmente delicados. Incluso nosotros podríamos agregarle al final con otro OR la extensión txt y nos listaría los archivos txt que se encuentren de forma pública expuestos. 

En este caso no se da nada, pero aislado a archivos de texto, luego se puede llegar a encontrar reportes, archivos ofimáticos, presentaciones, etc.

**Directory listing vulnerabilities** es otro que podríamos seleccionar en la herramienta que puede llegar a buscar algo expuesto que contenga una lista de dominios y subdominios de la misma plataforma que en ocasiones suelen almacenarlo en algún archivo. 

También tenemos cosas a las que usualmente se llega a apuntar como el caso de **wordpress** que se suele tener el directorio **wp-content** expuesto en ocasiones y esto ya es algo muy vulnerable porque ya con esto podremos llegar a listar plug-ins y mucha información delicada que nos puede incluso ahorrar la etapa de enumeración.

También podremos intentar el Dork por archivos de configuración expuestos. Si lo hiciéramos con el dominio de Tinder, veremos cómo se encuentra un archivo **sitemap.xml** el cual, si lo abrimos, tendrá una estructura de los recursos existentes en la web:

![[Reconocimiento/GoogleDorks/images/009.png]]

![[Reconocimiento/GoogleDorks/images/010.png]]

Con esta información podríamos llegar a abrir el primer enlace, por ejemplo, que nos llevaría a un archivo, el cual, si lo vemos bien, tiene rutas que seguramente pertenezcan al propio dominio principal:

![[Reconocimiento/GoogleDorks/images/011.png]]

Este archivo expuesto puede llegar a ser interesante, ya que directamente nos permitiría ver y conocer distintas rutas del propio Tinder. En este caso, lo que sucede es que no tiene una estructura sólida para llegar a identificar bien cada ruta, pero usualmente no se representan de esta manera. 

En si esta herramienta nos permite realizar varios tipos de filtro para búsquedas como **paginas de login**, **errores SQL**, entre otras. Incluso podríamos aprovecharnos de paste bin o **GitHub** en caso de que Tinder tenga un proyecto por ahí expuesto, el cual nos permita llegar a tener muchísima información y en casos privilegiados.

Esto es muy importante, ya que nos podría llegar a permitir listar información interesante en casos de que llegue a estar algo expuesto que nos de información delicada.

## Exploit-db

[exploit-db](https://www.exploit-db.com/) es otra página que nos puede servir en este caso, además esta plataforma es una muy interesante que podremos llegar a utilizar en algunos casos, ya que tiene una lista muy grande de vulnerabilidades y además te llega a reportar códigos que te permiten explotar estas vulnerabilidades, por lo cual, es una plataforma muy potente y que puede llegar a servirnos de cara a vulnerabilidades que lleguemos a encontrar.

Aquí también podremos encontrar Google Dorks y, en este caso, en la pestaña izquierda es la segunda opción la que nos lleva a este apartado, la primera sería el propio logo de la plataforma:

![[Reconocimiento/GoogleDorks/images/012.png]]

Este sería como otro almacén de Google Dorks pero ahora en esta plataforma. Imaginando que tenemos una página la cual utiliza WordPress por detrás, aquí podríamos filtrar por Dorks para WordPress y llegar a ver algunos que nos serían de ayuda para casos en donde una plataforma esté empleando WordPress por detrás:

![[Reconocimiento/GoogleDorks/images/013.png]]

Como **ejemplo general** de lo que se podría llegar a encontrar en WordPress, nosotros en Google buscaremos con el prefijo **inurl:** por **wp-config.php.txt**. Esto es porque WordPress cuenta con un archivo de configuración, el cual es **wp-config.php** el cual no podemos llegar a visualizar porque la propia plataforma lo va a interpretar. 

A pesar de ello, luego los desarrolladores llegan a crear backups de estos archivos como con terminación **txt** y lo terminan dejando expuesto, lo cual es riesgoso, ya que estos archivos usualmente tienen información de credenciales como de conexión a las bases de datos:

![[Reconocimiento/GoogleDorks/images/014.png]]

Abriendo alguno de los resultados veríamos lo anterior que ya directamente es algo que nos da la información de la base de datos, el usuario y la contraseña. Esto por si solo no es ilegal, ya que al final es recolección de información pública. Lo que ya puede llegar a complicarlo es lo que nosotros realicemos con esta información expuesta de forma pública. 

Esto luego se llega a dejar de lado porque son cosas tan simples que por nociones básicas de seguridad no se suele dejar nada expuesto, pero luego por cosas tan sencillas como esta se llegan a acontecer ciertos hackeos dejando de lado cierta parte de la explotación al dejar tan sencillamente información importante y crítica expuesta. Por ende, es importante de que, aunque sea algo tan básico, tenerlo siempre en consideración porque nunca sabremos si algún recurso crítico puede estar expuesto y nunca está de más considerarlo.
# Siguientes apuntes

[[Identificación y verificación externa de la versión del sistema operativo]]