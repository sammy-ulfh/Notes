# Práctica

El proxy funciona como intermediario en las peticiones que realizamos en el navegador; las peticiones cliente-servidor las observa el proxy como intermediario y nos permite ver más a detalle lo que está pasando por detrás, así como modificar las peticiones y ver cómo se comporta la comunicación entre la aplicación web y el servidor.

Esto es muy importante en pentesting, ya que nos permite observar el comportamiento de una aplicación y, en ocasiones, encontrar bugs o comportamientos raros que nos pudiesen permitir accesos no autorizados en una aplicación.

Como primer caso, en el login que nos encontremos de la aplicación desplegada con Docker Compose, si comenzamos a interceptar las peticiones con burpsuite y enviamos el login, observaremos la petición y cómo se envían los parámetros de usuario y contraseña hacia el servidor.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/012.png]]

Si observamos la petición, nos muestra el host, que en este caso es "localhost", en una página web con certificado y dominio, lo que se mostraría sería el dominio.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/013.png]]

El resto es información sobre la petición y, si observamos hasta el final, veremos cómo se envían el usuario y la contraseña en las variables **uid** y **password**.

Si esta petición la editáramos y para uid colocáramos "bob" y para password "password", estas son credenciales por default válidas. Al darle forward a la petición, permitiríamos que continúe, tal como la hemos modificado, y esto nos loguearía, a pesar de que los valores enviados desde el navegador fueron distintos, debido a que interceptamos y modificamos esa petición con valores reales y válidos.

Cada petición que se genere se quedará congelada mientras estemos interceptando las peticiones. Si tenemos el interceptar las peticiones apagado, el flujo será normal; de lo contrario, el flujo dependerá de permitir que siga con "forward" o eliminar peticiones con "Drop", lo cual elimina directamente la petición y nunca se recibe la respuesta de la misma hacia el navegador.

Esto es por el lado del proxy. Con estas peticiones podemos trabajar de otras maneras con las herramientas que Burpsuite nos proporciona; una de ellas es el Repeater, presionando CTRL + R.

Otro concepto interesante del lado de la configuracion del Proxy, es que en Burpsuite tenemos un apartado de __target__ > __site map__; nos representa una variedad de dominios en funcion del trafico que vayamos teniendo:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/014.png]]

Esto es debido a que no tenemos definido un alcance. Definiendo un alcance, lo que podemos hacer es que, de cara a todas las peticiones que recibimos, solo se nos vayan al sitemap aquellos dominios que estén considerados dentro de nuestro alcance.

Esto es de ayuda porque cuando nosotros estamos realizando un ataque, podremos tener un dominio objetivo y, por ende, no nos interesa ningún dominio externo o totalmente distinto al objetivo.

En lo que nos sale actualmente de dominios, seleccionaremos todos y daremos clic derecho para eliminar todos los ítems seleccionados.

Una vez eliminados, nos regresaremos al proxy e iremos a Options; finalmente, nos vamos hasta el final y marcaremos la casilla que dice "Don't send items to Proxy history or live tasks, if out of scope":

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/015.png]]

De esta manera, nos aseguramos de que solo se envíe al sitemap el scope que tengamos definido. Para definir un scope, iremos nuevamente a **target** > **scope**:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/016.png]]

Con esto, aquí en el primer apartado para incluir, podremos agregar el dominio o los dominios con los que estaremos trabajando. En este caso, como la página está corriendo en localhost, sería "http://localhost:8000".

Si tenemos el intercept apagado para evitar que se detengan las peticiones, y empezamos a navegar ahora, veremos como en el site map ahora solo nos aparece el dominio que hemos agregado y las peticiones que se han realizado:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/017.png]]

De esta forma se trabajaría de una forma mucho más organizada, representando únicamente aquello que nos interesa. Al seleccionar cada peticion aquí, veremos cómo se nos muestra la petición como la respuesta.

Si nos vamos a **Proxy** > **HTTP history**, también veremos un historial de todas las peticiones que han pasado por el proxy. Podríamos volver a borrar todo el historial debido a las modificaciones realizadas y ahora se reflejarian en el historial unicamente las que esten en el scope.

Si ahora nos ponemos a interceptar tráfico con el proxy, supongamos que intentamos loguearnos; esta petición queda y, si solo damos a "forward" para permitir que esta continúe, nunca veremos la respuesta del servidor. Si queremos verla en Burp Suite, tendremos que dar clic derecho > **Do intercept** y darle a que intercepte las respuestas por parte del servidor.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/018.png]]

Al hacer esto y darle forward para que continúe la petición, recibiremos la respuesta del servidor aquí mismo y podremos verla.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/019.png]]

Esto también es importante, porque puede haber casos donde una respuesta sí tenga contenido, pero por alguna razón esté dando alguna redirección con un código de estado 302, que en este caso lo que lo muestra es la primera línea. Lo que podría evitarnos la redirección en un caso así sería cambiar este 302 por un 200 y así nos mostraría el contenido.

La forma de continuar a recibirla es nuevamente darle a forward. Evidentemente, forzar que no aplique la redirección y que nos muestre el contenido funciona únicamente en webs que no estén correctamente montadas y se aseguren de evitar estos casos.

### Replacements

En las respuestas podemos aplicar reemplazos, que se aplique un match para reemplazar alguna cosa por otra. Tomando como ejemplo el código de estado de la petición, podremos aplicar un match que nos cambie todo **200 OK** por **201 PRUEBA,** que claramente no existe.

Para ello tendríamos que irnos al menú **Match and Replace** dentro de Proxy. Aquí podremos agregar este match para que haga un reemplazo en caso de existir:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/020.png]]

En este caso, inicialmente seleccionamos que este match se encontrara en el header de la respuesta (es el que se tiene que seleccionar; por default está para la solicitud o request) y será reemplazar el 200 OK por el 201 PRUEBA. Una vez agregado, estará hasta abajo la nueva regla, seleccionada; los que no estén seleccionados no se aplican.

Ahora, para verificar que se aplique, dejaríamos de interceptar y volveríamos a interceptar para interceptar nuevamente una petición de login en nuestra web. Podríamos darle nuevamente clic derecho > Do intercept y hacer lo mismo para interceptar la respuesta o irnos a las configuraciones de proxy y seleccionar la casilla de response intercept para que lo haga de forma automática. Esto nos permitirá interceptar las peticiones y su respuesta de forma automática, sin tener que hacerlo manualmente.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/021.png]]

Es la casilla que dice sobre interceptarlo en base a las siguientes reglas.

Si ahora interceptamos nuevamente y dejamos que la petición fluya, al recibir la respuesta del servidor, se aplicará de forma automática el reemplazo sobre el match que hemos agregado.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/022.png]]

Lo mismo aplica para cualquier parte de la petición; siguiendo el mismo ejemplo del reemplazo, podríamos agregar algo que incluso con regex busque un match e incluso se podría cambiar parte de la web a mostrar como respuesta y mostrar una cosa totalmente distinta cuando llegue al navegador.

Ahora podrías aplicar para el body (la página que se muestra o HTML puro) alguna sustitución que se refleje al dejar que fluya la respuesta hacia el navegador. Un ejemplo sería cambiar el título o algún texto que se muestra en la web. Cabe recalcar que, estemos interceptando o no las peticiones, todas pasan por Burp Suite porque es lo que tenemos como proxy habilitado; por ende, si tenemos reglas como la del matching que hace un replacement, se aplicará igualmente.

## Siguientes notas

- [[Intruder]]