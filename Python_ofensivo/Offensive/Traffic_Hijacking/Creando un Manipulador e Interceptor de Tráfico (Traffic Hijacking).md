
# Introducción

Crearemos paso a paso un Manipulador e interceptor de tráfico conocido como **Traffic Hijacking**, una técnica avanzada de ciberseguridad ofensiva. El objetivo es aprender a controlar y alterar el tráfico de una red para manipular lo que un usuario ve en respuesta a sus acciones en la web.

Para lograr esto utilizaremos nuevamente la herramienta **netfilterqueue** en combinación con **iptables**. **NetfilterQueue** nos permite interceptar paquetes que pasan por la red y manipularlos antes de que continúen su camino. Mediante iptables redirigiremos el tráfico relevante (como las solicitudes HTTP/HTTPS) a una cola NFQUEUE, donde podremos inspeccionar y modificar estos paquetes utilizando un script personalizado. 

Una aplicación práctica de esta técnica es alterar las respuestas de las solicitudes web. Por ejemplo, cuando un usuario solicita una página web, podemos interceptar la respuesta del servidor y modificarla antes de que llegue al usuario. Esto puede incluir cambiar textos, insertar scripts maliciosos, redirigir a sitios de phishing, entre otros. Es una forma poderosa de controlar la experiencia del usuario en la web y puede ser utilizada para una variedad de propósitos malintencionados.

# Práctica

## IPTABLES

Para este script que nos permitirá modificar el contenido de una página al realizar una petición HTTP utilizaremos **NetfilterQueue** en conjunto con **iptables** que nos permitan redirigir el tráfico a una cola de NFQUEUE. Para interceptar el tráfico de una máquina víctima será necesario aplicarle un ataque **ARP Spoof** para interceptar su tráfico mediante la NFQUEUE. 

Una vez aplicadas las reglas con **iptables** no tendremos internet, ya que los paquetes no viajarán a su destino a menos que sean aceptados en el script que construiremos. Por ello, es importante ya tener listas las librerías **netfilterqueue** y **scapy**. 

Las reglas que tendremos que aplicar en nuestro ordenador de atacante son las siguientes:

```shell
iptables -I INPUT -j NFQUEUE --queue-num 0
iptables -I OUTPUT -j NFQUEUE --queue-num 0
iptables -I FORWARD -j NFQUEUE --queue-num 0
iptables --policy FORWARD ACCEPT
```

Además, tendremos que habilitar el IP forwarding seteando el archivo ip_forward a 1:

```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```

## Script

Para nuestro script comenzaremos creando un objeto con una instancia de la clase **NetfilterQueue()** de la librería **netfilterqueue**, nos asociaremos a la cola con el número 0 que fue el que definimos con las iptables y como segundo argumento le pasaremos la función con la que trataremos cada paquete, que en este caso será **process_packet** y finalmente utilizaremos el método **run()** para indicar que se inicie el tratado de cada paquete que se encuentre en la NFQUEUE.

![[Offensive/Traffic_Hijacking/images/001.PNG]]

En este caso aceptamos el paquete y con ello, al ejecutar el script, ahora sí que los paquetes podrán viajar y tendremos internet. 

Primeramente, vamos a crear un paquete IP con scapy mediante el payload de nuestro paquet eobtenido con **nfqueue**, recordemos que este paquete al utilizar el método **get_payload()** son datos en bruto y no podemos tratarlo directamente, por ello lo transformamos con scapy para poder modificarlo y tratar con él:

![[Offensive/Traffic_Hijacking/images/002.PNG]]

En este caso buscamos modificar el contenido de la capa **Raw** que es la que como tal nos traerá el contenido de la página o ciertas cabeceras que son enviadas como información para el servidor. 

En esta capa se encuentra el atributo **load** el cual es el que tiene esta información. Cuando el cliente la envía es información que es visible en texto claro, pero si entre las indicaciones que pueda tener esta información se encuentra **Accept-Encoding: gzip** u otro tipo de encoding, el servidor enviará la información o datos de la página como datos comprimidos para que viaje con mayor rapidez, por lo tanto, nosotros no lo veríamos legible. 

Trabajaremos con la página de [Accunetix](http://testphp.vulnweb.com/login.php).

Para evitar esto, buscamos sustituir esta parte de tal forma que la eliminemos del **load** para así recibir los datos del servidor (en este caso el HTML) en texto claro. Para ello utilizaremos la librería **re** y con ayuda del método **sub** podremos agregar una expresión regular que, si encuentra un match, realizará una sustitucion con nuestro segundo argumento.

![[Offensive/Traffic_Hijacking/images/003.PNG]]

En este caso primero verificamos que el paquete tenga la capa **Raw**, de ser así tendrá el atributo **load** que es el que nos interesa. Además, nos interesa la capa **TCP**, ya que, en este caso, en lugar de utilizar UDP como en casos anteriores, se hace mediante TCP.

Esta capa TCP tiene dos atributos principales que nos interesan, los cuales son **dport** (destination port) y **sport** (source port), cuando el **destination port** sea **80** quiere decir que nosotros estamos enviando el contenido hacia un servidor http, pero cuando el **source port** sea **80** quiere decir que el servidor http nos está respondiendo. 

De esta forma podremos identificar entre la solicitud y la respuesta.

Cuando **dport** sea **80** (nuestra solicitud) aplicaremos las sustituciones si nuestra regex encuentra un match. La regex **Accept-Encoding:.\*?\\\\r\\\\n*** buscar un match donde el texto sea el que colocamos y **.\*** representa que ahí podemos tener cualquier tipo de contenido como lo es **gzip**, pero podría ser cualquier otra cosa y finalmente **\\\\r\\\\n** que para que la regex no pueda detectarlo como un carácter para la expresión regular ignoramos la barra.

El signo de interrogación nos sirve para indicar que se quede desde donde comienza el **Accept** hasta solamente el primer match, ya que pueden existir diversos matches y si no indicamos esto se quedaría hasta el último elemento de caracteres que sean **\\r\\n**.

De esta manera, cuando encuentre match, lo cambiará por nada, ya que no colocamos contenido en nuestro segundo argumento y nuestro tercer argumento será el load de nuestra capa **Raw** en nuestro paquete scapy que podemos interpretar. Nuestros primeros dos argumentos tienen una **b** al inicio, ya que es la forma de indicar que ambos se trabajaran en formato bytes.

Una vez aplicado el cambio y almacenar esto en nuestra variable **modified_load** utilizaremos una función **set_load** la cual recibirá como argumentos nuestro paquete scapy y el nuevo load para realizar el cambio en el paquete, además de eliminar de nuestra capa **IP** los atributos **len** y **chksum**. 

Para nuestra capa **TCP** no contamos con el atributo **len**, pero sí con **chksum**, por ende para esta capa será el que eliminaremos. Recordemos que estos atributos sirven para verificar la integridad del paquete y que no hayan sido modificados, por ende al modificarlos evitamos esta validación y así nuestro paquete no será descartado:

![[Offensive/Traffic_Hijacking/images/004.PNG]]

Finalmente, después de recibir el paquete lo construiremos con **build** para tenerlo en el mismo formato que cuando lo sacamos del paquete original y con **set_payload** ya lo estaremos modificando en el nuevo paquete. 

De esta forma, al enviar la solicitud al servidor ya estaremos eliminando el apartado **Accept-Encoding** que indica que la página es capaz de interpretar los datos con una compresión aplicada. 

Ahora para filtrar por la respuesta será con el atributo **sport**, si este equivale a 80 quiere decir que el servidor nos ha respondido y en este el **load** de la capa **Raw** ya puede contener el HTML de la propia página.

![[Offensive/Traffic_Hijacking/images/005.PNG]]

Aquí, de la misma manera, al ya tener directamente el HTML de la página, primeramente con una **regex** buscamos el match con la etiqueta title que tendrá algún contenido. De hacer match, cambiará esta parte por el título **Hacked ;D** que estamos agregando nosotros. Además, tome exactamente la primera etiqueta **a** del código de la página que tome de la propia página. Recordemos que estamos trabajando con la página [Login Test de Accunetix](http://testphp.vulnweb.com/login.php). 

Esto aplica la sustitución y aprovechándonos de la función que ya habíamos colocado que nos almacena el load y modifica todo retornándonos un nuevo paquete para después setearlo en el paquete original con **set_payload()**. Con esto ya estaríamos modificando directamente el código de la página y lo veríamos reflejado en nuestra máquina víctima:

![[Offensive/Traffic_Hijacking/images/006.PNG]]

Con esto ya sabremos que dependiendo de la página que sea nuestro target podremos insertar cosas, incluso llegar a buscar un match o en lugar de utilizar **regex** utilizar la función replace y con ello buscar el cierre de la etiqueta body y llegar a insertar JavaScript y llegar a tener un mayor alcance. 

Esta página en concreto no acepta JavaScript, pero podremos llegar a probarlo nosotros con una página que nos montemos con un servidor http de Python e intentar insertar una etiqueta **script** detectando la etiqueta body de cierre.
## Siguientes apuntes

[[Creando un Keylogger (1-2)]]
