# Indice

- [[#Introducción]]
- [[#Practica]]
- [[#HTTP]]
- [[#HTTPS]]
- [[#OpenSSL]]
- [[#SSLSCAN]]
- [[#SSLYZE]]
- [[#Heartbleed vulnerability]]
- [[#Siguientes apuntes]]

# Introducción

HTTP (Hypertext Transfer Protocol) es un protocolo de comunicación utilizado para la transferencia de datos en la World Wide Web; se utiliza para la transferencia de contenido de texto, imágenes, videos, hipervínculos, etc. El puerto predeterminado para HTTP es el puerto 80. 

HTTPS (Hypertext Transfer Protocol Secure) es una versión segura de HTTP que utiliza SSL / TLS para cifrar la comunicación entre el cliente y el servidor. Utiliza el puerto 443 por defecto. La principal diferencia entre HTTP y HTTPS es que HTTPS utiliza una capa de seguridad adicional para cifrar los datos, lo que los hace más seguros para la transferencia de los mismos.

Una de las herramientas que nos puede servir para inspeccionar el certificado SSL es OpenSSL. OpenSSL es una biblioteca libre y de código abierto que se utiliza para implementar protocolos de seguridad en línea, como TLS (Transport Layer Security), SSL (Secure Sockets Layer). La biblioteca OpenSSL proporciona una implementación de estos protocolos para permitir que las aplicaciones se comuniquen de manera segura y encriptada a través de la red. 

Uno de los comandos utilizados más adelante para verificarlo haciendo uso de esta herramienta es el siguiente:

```shell
openssl s_client -connect ejemplo.com:443
```

Este nos ayuda a inspeccionar el certificado SSL de un servidor web. Lo que hace es conectarse al servidor en el puerto 443 (el que corre el servidor HTTPS) y muestra información detallada sobre el certificado SSL, como la validez del mismo, la fecha de caducidad, el tipo de cifrado, etc. 

Otras de las herramientas que se mostrarán son __sslyze__ y __sslscan__. __Sslyze__ es una herramienta de análisis de seguridad SSL que se utiliza para evaluar la configuración SSL de un servidor. Proporcionando información detallada sobre el cifrado utilizado, los protocolos admitidos y los certificados SSL. __SSLScan__ es otra herramienta de análisis de seguridad SSL que se utiliza para evaluar la configuración SSL de un servidor. Proporciona información detallada sobre los protocolos SSL / TLS admitidos, el cifrado utilizado y los certificados SSL.

La principal diferencia entre __sslyze__ y __sslscan__ es que __sslyze__ se enfoca en la evaluación de la seguridad SSL/TLS de un servidor web mediante una exploración exhaustiva de los protocolos y configuraciones SSL/TLS, mientras que __sslscan__ se enfoca en la identificación de los protocolos SSL/TLS admitidos por el servidor y cifrados utilizados. 

La identificación de la información arrojada por las herramientas de análisis SSL/TLS es de suma importancia, ya que nos puede permitir detectar vulnerabilidades en la configuración de un servidor y tomar medidas para proteger nuestra información confidencial.

Por ejemplo, **Heartbleed** es una vulnerabilidad de seguridad que afecta a la biblioteca OpenSSL y permite a los atacantes acceder a la memoria de un servidor vulnerable. Si un servidor web es vulnerable a Heartbleed y lo detectamos a través de estas herramientas, esto significa que un atacante podría potencialmente acceder a información confidencial, como claves privadas, nombres de usuario, contraseñas, etc. 

Enlace al [repositorio](https://github.com/vulhub/vulhub/tree/master/openssl/CVE-2014-0160) tomado para mostrar la vulnerabilidad.

# Practica

### HTTP

Anteriormente ya hemos visto cómo podremos llegar a enumerar el servicio HTTP, el cual corre generalmente sobre el puerto 80. Donde, utilizando herramientas como WhatWeb o Wappalyzer, podremos llegar a averiguar qué versiones y tecnologías se están utilizando por detrás, hasta incluso si se está utilizando un CMS como WordPress, Joomla, entre otros. 

Además, con herramientas como wfuzz, fuff, gobuster, dirb, dirbuster (UI), dirsearch, podremos llegar a aplicar fuzzing para descubrir archivos y directorios que estén para la web. 

Todo lo anteriormente mencionado es para el puerto 80 (HTTP), pero también es posible aplicar enumeración al puerto 443 (HTTPS).
### HTTPS

Nos podemos ir a nuestro ejemplo que empezamos a ver con Hackerone, en este caso __tinder.com__, si nosotros lo abrimos en el navegador y vamos al candadito, veremos las siguientes opciones:

![[EnumServComunes/HTTP&HTTPS/images/001.png]]

Aquí si seleccionamos __Connection secure__, veremos lo siguiente:

![[EnumServComunes/HTTP&HTTPS/images/002.png]]

Finalmente, bastaría con irnos a más información, lo cual nos sería de ayuda para ver la información que tiene en cuanto a certificado respecta.

![[EnumServComunes/HTTP&HTTPS/images/003.png]]

Con ello, podremos irnos a __View certificate__ para ver la información del certificado SSL. Esto es importante debido a que en ocasiones, como common name, se pueden llegar a encontrar subdominios o, incluso observando detenidamente la información del certificado, podríamos llegar a encontrarnos con correos o nombres importantes, así como información de la autoridad que provee este certificado.

### OpenSSL

También podemos hacer uso de OpenSSL para, como cliente, intentar conectarnos a nuestro dominio por el puerto 443.

```shell
openssl s_client -connect tinder.com:443
```

Esto en ocasiones nos permitirá que, viendo la información que arroja, podamos llegar a observar en los atributos __common name__ (CN) cosas como correos, subdominios. 

En este caso no nos muestra información que se llegue a filtrar.
### SSLSCAN

Herramientas como sslscan nos permiten que, pasándole directamente el dominio, aplique cierto análisis, donde busca y reporta vulnerabilidades. 

Este escaneo llevará un ratito, ya que busca reportar a qué es y a qué no es vulnerable nuestra página o plataforma web a la que le estamos aplicando este escaneo con esta herramienta.

![[EnumServComunes/HTTP&HTTPS/images/004.png]]

![[EnumServComunes/HTTP&HTTPS/images/005.png]]

![[EnumServComunes/HTTP&HTTPS/images/006.png]]

En este caso no se ve que reporte alguna vulnerabilidad y es bueno porque quiere decir que todo está muy bien montado; por ello correremos un entorno vulnerable con Heartbleed.
### SSLYZE

__Sslyze__ nos sirve de la misma forma que sslscan; en este caso no se mostró su funcionalidad, ya que puede ser muy frecuente que tienda a quedarse un poco trabado o estático en un principio, siendo un proceso mucho más tardado. Pero se utiliza exactamente de la misma forma.
### Heartbleed vulnerability

Para este caso utilizaremos la carpeta mencionada del repositorio `https://github.com/vulhub/vulhub/tree/master/openssl/CVE-2014-0160`.

Lo clonaremos y entraremos en su carpeta. 

En este caso, para el contenedor que estaremos utilizando, tenemos dos opciones. 

La primera es utilizar el siguiente comando, que nos servirá para traer únicamente la carpeta que requerimos del repositorio de Vulnhub con la vulnerabilidad Heartbleed.

```shell
curl https://codeload.github.com/vulhub/vulhub/tar.gz/master | tar -xz --strip=2 vulhub-master/openssl/CVE-2014-0160
```

Otra opción es utilizar la página web [DownGit](https://downgit.github.io/#/home), donde basta con pegar el enlace de la subcarpeta de un repositorio y nos lo descarga en un archivo zip, el cual, al descomprimir, tenemos la subcarpeta que necesitamos en este caso. 

Una vez que tengamos la carpeta del proyecto, nos meteremos a la carpeta y lanzaremos el contenedor con el siguiente comando:

```shell
docker-compose up -d
```

En este caso, si observamos las instrucciones del README, en lugar de estar empleando el puerto 443, está empleando el 8443. Una vez que el contenedor esté corriendo, podremos verificar si todo está corriendo correctamente, abriendo la página de localhost en el puerto 8443 y, si todo está funcionando correctamente, nos abrirá la web. 

El único detalle en este caso es que, como se utiliza un certificado SSL autofirmado, nos pedirá aceptar los riesgos; una vez aceptados, veremos la web.

![[EnumServComunes/HTTP&HTTPS/images/007.png]]

Con nuestro entorno vulnerable corriendo, ahora podremos volver a utilizar SSLSCAN pasándole nuestro host y puerto donde está corriendo:

```shell
sslscan 127.0.0.1:8443
```

![[EnumServComunes/HTTP&HTTPS/images/008.png]]

De igual forma nos da bastante información, pero ahora lo que nos interesa es que, como este es un entorno vulnerable a Heartbleed, se nos estaría reportando esta vulnerabilidad:

![[EnumServComunes/HTTP&HTTPS/images/009.png]]

De esta manera vemos cómo, para las distintas versiones de TLS mostradas, se tiene esta vulnerabilidad. Además, Nmap también nos puede ayudar a detectar este tipo de vulnerabilidad. Si nosotros buscamos los scripts __.nse__ que utiliza nmap para encontrar vulnerabilidades y filtramos por Heartbleed, veremos cómo cuenta con un script para detectar esta vulnerabilidad:

![[EnumServComunes/HTTP&HTTPS/images/010.png]]

Por ende, considerando este script, podremos utilizarlo para realizar un escaneo sobre el puerto 8443, actuando como un checker para validar si es vulnerable o no a Heartbleed:

```shell
nmap --script ssl-heartbleed -p 8443 127.0.0.1
```

![[EnumServComunes/HTTP&HTTPS/images/011.png]]

Aquí se nos detecta y además se nos menciona que esta es una vulnerabilidad muy popular y su aspecto crítico viene en cuanto a que la librería criptográfica, al poseer esta vulnerabilidad, permite visualizar o extraer información que se encuentre en la memoria de la máquina. 

En este caso, el mismo repositorio comparte una Prueba de Concepto (POC) para verificar cómo funciona; este es un script en Python3, el cual está en la misma carpeta:

![[EnumServComunes/HTTP&HTTPS/images/012.png]]

A este script le tendremos que pasar en dónde está corriendo la página y con el parámetro __p__ indicar el puerto sobre el cual se encuentra corriendo, en este caso el 8443:

```shell
python3 ssltest.py 127.0.0.1 -p 8443
```

![[EnumServComunes/HTTP&HTTPS/images/013.png]]

Esto nos retorna bastante información que está intentando dumpear de la memoria, pero en este caso es información vacía; por ende, vamos a intentar quitar con __grep__ todos aquellos que contengan estos caracteres en 0.

```shell
python3 ssltest.py 127.0.0.1 -p 8443 | grep -v "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
```

![[EnumServComunes/HTTP&HTTPS/images/014.png]]

En este caso vemos bastante información que no es directamente visible, ya que está en un formato hexadecimal. Sin embargo, esta es una vulnerabilidad muy considerable, ya que, al extraer información almacenada en la memoria, puede llegar a permitir extraer cookies de sesiones activas o información muy sensible. 

Es por ello que, si se corre el script múltiples veces en un entorno real que se utiliza constantemente, se puede llegar a extraer distinta información cada vez que se ejecute.

En este caso muestra casi siempre el mismo contenido. Esto es algo que podremos ver más en casos en los que se tiene una máquina con múltiples procesos corriendo e intentar llegar a extraer cierta información sensible o privilegiada. 

Es por ello que también es importante que cualquier puerto que cuente con un certificado SSL, también es muy importante enumerarlo y buscar información al respecto.
# Siguientes apuntes

[[]]