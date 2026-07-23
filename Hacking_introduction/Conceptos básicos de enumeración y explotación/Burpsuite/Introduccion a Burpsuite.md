# Índice

# Introducción

**Burpsuite** es una herramienta de prueba de penetración utilizada para encontrar vulnerabilidades de seguridad en aplicaciones web. Es una de las herramientas de penetración más populares y utilizadas en la industria de la seguridad informática. Burpsuite se compone de varias herramientas diferentes que se pueden utilizar juntas para identificar vulnerabilidades en una aplicación web.

Las principales herramientas que componen a Burpsuite son las siguientes:

- __Proxy__: Es la herramienta principal de Burpsuite y actúa como un intermediario entre el navegador web y el servidor web. Esto permite a los usuarios interceptar las solicitudes y respuestas HTTP y HTTPS enviadas entre el navegador y el servidor. El proxy también es útil para la identificación de vulnerabilidades, ya que permite a los usuarios examinar el tráfico y analizar las solicitudes y respuestas.
- __Scanner__: Es una herramienta de prueba de vulnerabilidades automatizada que se utiliza para identificar vulnerabilidades en aplicaciones web. El scanner utiliza técnicas de exploración avanzadas para detectar vulnerabilidades en la aplicación web, como inyecciones SQL, cross-site scripting (XSS), vulnerabilidades de seguridad de la capa de aplicación (OWASP TOP 10) y más.
- __Repeater__: Es una herramienta que permite a los usuarios reenviar y repetir solicitudes HTTP y HTTPS. Esto es útil para probar diferentes entradas y verificar la respuesta del servidor. También es útil para la identificación de vulnerabilidades, ya que permite a los usuarios probar diferentes valores y detectar respuestas inesperadas.
- __Intruder__: Es una herramienta que se utiliza para automatizar ataques de fuerza bruta. Los usuarios pueden definir diferentes payloads para diferentes partes de la solicitud, como la URL, el cuerpo de la solicitud y las cabeceras. Posteriormente, el intruder automatiza la ejecución de las solicitudes utilizando diferentes payloads y los usuarios pueden examinar las respuestas para identificar vulnerabilidades.
- __Comparer__: Es una herramienta que se utiliza para comparar dos solicitudes HTTP o HTTPS. Esto es útil para detectar diferencias entre las solicitudes y respuestas y analizar la seguridad de la aplicación.

Se trata de una herramienta extremadamente potente, la cual se utiliza para identificar una gran variedad de vulnerabilidades de seguridad en una aplicación web. Al utilizar las diferentes herramientas que son parte de Burpsuite, los usuarios pueden identificar vulnerabilidades de forma automatizada o manual, según sus necesidades. Esto permite a los usuarios encontrar vulnerabilidades y corregirlas antes de que sean explotadas por un atacante.

En resumen, Burpsuite es una herramienta imprescindible para cualquier profesional de la seguridad informática que busque asegurar la seguridad de aplicaciones web.

# Práctica

## Despliegue y configuración

Para la parte práctica se utilizará el siguiente proyecto que se tendrá que desplegar con Docker Compose: [SQL Training App](https://github.com/appsecco/sqlinjection-training-app)

Una vez desplegado, recordemos reiniciar la base de datos con el botón al inicio de la web. Esta web será la que utilizaremos para ver las funcionalidades dentro de Burpsuite. Dentro de nuestro navegador, nos iremos a la parte de **multiple exercises** en la web.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/001.png]]

Esto nos llevará a un panel de login. Aquí es donde ya podremos abrir burpsuite para empezar a visualizar lo que podemos realizar con el mismo. Al abrirlo, nos saltan opciones que tenemos que responder; bastará con darle a siguiente o aceptar lo que nos aparezca.

Una vez realizado, veremos el panel general de Burpsuite:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/002.png]]

Si nos vamos a Proxy y opciones, veremos cómo el proxy está automáticamente seteado para funcionar en localhost en el puerto 8080. De esta manera se permite que las peticiones pasen por burpsuite como intermediario.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/003.png]]

Para que las peticiones de nuestro navegador pasen por el proxy de Burpsuite, tendremos que utilizar una extensión en nuestro navegador que nos permita redirigir el tráfico. En este caso, la extensión que nos sirve perfectamente es FoxyProxy.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/004.png]]

Para configurar un proxy, seleccionaremos la extensión que hemos agregado, nos iremos a opciones y después a proxies, dándole a "ADD" para agregar uno nuevo.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/005.png]]

Agregamos el localhost "127.0.0.1" y el puerto donde estará en escucha el proxy de burpsuite, que en este caso es el puerto 8080.

Al guardarlo, podremos utilizarlo seleccionando nuestra extensión y seleccionando el proxy que hemos agregado para que redirija el tráfico hacia este.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/006.png]]

Una vez habilitado, es posible que tengamos problemas con el certificado de confianza del proxy, es por ello que nos iremos a [Burp Web CA](http://burp/) y le daremos al botón de CA CERTIFICATE para descargar el certificado.

Una vez descargado, tendremos que irnos a la configuración del navegador > certificados. Aquí tendremos que agregar este que hemos descargado: "view certificates".

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/009.png]]

Aquí iremos al apartado Authorities, le daremos a **import** y seleccionaremos el certificado descargado.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/010.png]]

Finalmente, le damos a OK en ambas ventanas para almacenarlo. Aquí, al encender el proxy, empezaremos a recibir las peticiones del navegador y estas estarán en espera hasta que las redireccionemos o las desechemos.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/011.png]]

Es posible que, aunque la configuración esté correctamente realizada en el navegador, tengamos problemas y el tráfico de la página que tenemos desplegada con Docker no pase por BurpSuite. En dado caso, lo mejor será utilizar otro navegador o, para mayor seguridad, el navegador que tiene el propio burpsuite, que además ya viene configurado.
## Apartados de Burpsuite

- [[Proxy]]
- [[Intruder]]
- [[Repeater]]
- [[Decoder]]
- [[Comparer]]
- [[Extensions]]

## Siguientes apuntes

[[Introduccion a SQLI]]