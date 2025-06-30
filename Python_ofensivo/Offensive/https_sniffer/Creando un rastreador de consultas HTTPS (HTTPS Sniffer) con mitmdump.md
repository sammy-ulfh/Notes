
# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Configuración para la máquina víctima]]
- [[#Configuración del proxy]]
- [[#Certificado de confianza en nuestro proxy]]
- [[#Script]]
# Introducción

Nos sumergiremos en el mundo del espionaje de tráfico HTTPS creando un rastreador de consultar HTTPS (HTTPS Sniffer) con **mitmdump**. **Mitmdump** es una herramienta potente que actúa como proxy, permitiéndonos interceptar, modificar y analizar el tráfico entre un cliente y un servidor, tanto para HTTP como para HTTPS. 

El desafío con el tráfico HTTPS, que está cifrado para proteger la privacidad y seguridad de los datos, es que no se puede leer directamente. Aquí es donde entra en juego la instalación de un certificado en la máquina víctima. Al hacer esto, engañamos al dispositivo para que confíe en nuestro proxy, lo que nos permite descifrar y acceder al contenido del tráfico HTTPS.

# Práctica

En este caso ya no será necesario utilizar en envenenamiento ARP (ARP Spoofer). Emplearemos un MITM Attack, pero en su lugar emplearemos un proxy. 

Un **proxy** es una herramienta que nos ayuda como intermediario a nuestras conexiones cliente-servidor, filtrando todos los paquetes entre ambos. De tal forma que el proxy se encarga en realizar las peticiones por nosotros, para que así el servidor no se entere de que nosotros, por detrás, somos los que realizamos estas peticiones. 

Para ello utilizaremos **mitmdump**, la cual es una herramienta open source que no permitirá levantar un servidor proxy tipo MITM. Lo realizaremos de esta manera, ya que el principal problema al interceptar tráfico HTTPS es que este viaja cifrado y, por ende, no tenemos la posibilidad de verlo. 

Por ello, nos aprovecharemos de un certificado el cual no permite hacer que la máquina víctima confíe en nosotros como proxy y a nivel de navegación no note ningún cambio, pero estaremos interceptando el tráfico en general y en este caso al confiar en nosotros como proxy, sí que podremos ver el tráfico HTTPS. 

En este caso asumiremos que nosotros ya hemos vulnerado la máquina víctima y nos encontramos con permisos de administrador dentro de ella, primeramente se mostrara la forma manual de habilitar el proxy e instalar el certificado, pero después lo realizaremos desde la terminal, simulando más un entorno donde hemos vulnerado dicha máquina y nos encontremos en una sesión de PowerShell (en este caso la víctima será una máquina Windows).

Primeramente, en nuestra máquina atacante nos descargaremos los binarios de **mitmproxy** para Linux, desde [aquí](https://mitmproxy.org/). 

Esto nos decargara un binario comprimido y tendremos que extraer el contenido:

![[Offensive/https_sniffer/images/001.png]]

## Configuración para la máquina víctima

En este caso, desde nuestra máquina víctima vamos a abrir el navegador y abriremos la página **mitm.it**. De primeras solo veremos un mensaje:

![[Offensive/https_sniffer/images/002.PNG]]

Lo vemos así por el momento, ya que no estamos corriendo nada desde nuestra máquina atacante, pero en esta página, al momento en el que nuestro tráfico está siendo redirigido mediante mitmproxy. 

Para ello, en nuestra máquina víctima tendremos que ejecutar el binario **mitmweb** que lo que hace es crear un servidor en el equipo local de atacante mediante el puerto 8080:

![[Offensive/https_sniffer/images/003.PNG]]

En el puerto 8081 corre un servicio HTTP que es como una página de configuración en el propio servicio que estamos corriendo. 

Al tener el proxy corriendo en el puerto 8080, veremos cuál es nuestra IP como atacantes, en este caso, es la IP **192.168.100.81**. Con ello nos iremos a nuestra máquina víctima y primeramente configuraremos el proxy.

## Configuración del proxy

### Manual

Abriremos la configuración del proxy en nuestra máquina víctima:

![[Offensive/https_sniffer/images/004.PNG]]

Nos iremos a la configuración manual y habilitaremos el proxy:

![[Offensive/https_sniffer/images/005.PNG]]

En address colocaremos la IP del atacante y el puerto en el que se encuentra corriendo nuestro proxy y lo guardaremos dándole a save.

### Terminal

También podremos configurar el proxy utilizando la terminal, para ello primeramente vamos a eliminar la configuración que colocamos del proxy y además vamos a deshabilitarlo. 

Después, en la barra de búsqueda buscaremos el editor de registros:

![[Offensive/https_sniffer/images/008.PNG]]

Lo ejecutaremos y veremos lo siguiente:

![[Offensive/https_sniffer/images/009.PNG]]

Realmente lo que se hace es que se aplica un cambio a nivel de registro donde se habilita el proxy y se setea la IP y el puerto. 

En el editor de registros desplegaríamos primeramente la carpeta **HKEY_CURRENT_USER**, después la carpeta **SOFTWARE**, despues la carpeta **MICROSOFT**, despues la carpeta **Windows**, despues la carpeta **CurrenVersion**, despues buscaremos la carpeta **Internet Settings** y presionaremos sobre ella, viendo lo siguiente del lado derecho:

![[Offensive/https_sniffer/images/010.PNG]]

En este caso vemos como se ha quedado cacheado lo de la configuración del proxy en **ProxyServer** a pesar de que ya lo hemos deshabilitado y borrado la configuración, esto realmente podremos darle clic derecho y eliminarlo, para visualizar el cambio solo seleccionamos otra carpeta del lado izquierdo y despues volvemos a seleccionar la de **Internet Settings**.

Si observamos el valor de **ProxyEnable** veremos como entre paréntesis nos muestra un valor, en este caso sale uno porque en la configuración sigue activo, pero si lo deshabilitamos en la configuración y cambiamos de selección de carpeta para verlo actualizado, veremos como el valor cambia a cero, por ende este valor almacena cuando el proxy esté deshabilitado (0) o habilitado (1). 

Por ende, si queremos habilitar o deshabilitar el proxy bastará con cambiar el valor de este archivo que almacena esta configuración con los valores 0 o 1. Para nosotros modificar esto utilizaríamos el comando **reg add** y tendremos que correr la terminal (CMD) en modo administrador. 

Seguido del comando agregaríamos la ruta de donde se encuentra el archivo **ProxyEnable** para nosotros poder habilitar el proxy. La ruta comenzaría desde **HKEY_CURRENT_USER**, despues de colocar la ruta, utilizaríamos **/v** para indicar el nombre del archivo, en este caso **ProxyEnable**.

También tendremos que indicarle el tipo de dato que vamos a agregar. Para ello se utilizará **/t** y le decimos que **REG_DWORD** y, a nivel de dato, con **/d** le asignaremos el 1, que en este caso sería indicar que se habilite el proxy. 

Esto nos dejaría nuestro comando completo para realizar el cambio, pero si el archivo ya se encuentra, que es el caso, solicitará una confirmación diciéndote que ya existe y que sí deseas sobreescribirlo. Para evitar esto, agregamos al final un **/f** para forzar la acción que queremos realizar, sin que nos solicite confirmación. 

Nuestro comando final sería:

```POWERSHELL
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f
```

Con esto, cambiando el valor entre 1 y 0, veremos cómo, si vamos viendo nuevamente en la interfaz gráfica la configuración del proxy, se estará habilitando y deshabilitando:

![[Offensive/https_sniffer/images/011.PNG]]

Utilizaríamos el mismo principio para agregar la IP y el puerto de nuestra máquina atacante corriendo el servidor del proxy, como lo vimos anteriormente en este caso sería **ProxyServer** y en este caso como no agregaremos un número, sino, una cadena la cual tenga la estructura "{IP}:{PORT}", utilizaremos **REG_SZ** con **/t** para indicar que le asignaremos una cadena y finalmente con **/d** que en sí es para indicar a nivel de dato que le vamos a setear, en este caso será "**192.168.100.81:8080**", recordemos que con **/v** indicamos el nombre y con **/f** lo forzamos en caso de que el archivo ya exista. 

El comando nos quedaría como:

```POWERSHELL
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d "192.168.100.81:8080" /f
```

![[Offensive/https_sniffer/images/012.PNG]]

Con ello ya habremos configurado el proxy desde terminal. 

Al configurar el proxy, como aún no tenemos ningún certificado que confie en nuestro proxy, si intentamos acceder a cualquier página web desde nuestra maquina víctima observaremos lo siguiente:

![[Offensive/https_sniffer/images/006.PNG]]

Esto ya tendrá que ser con nuestro **mitmweb** corriendo en nuestra maquina de atacante, de lo contrario la víctima simplemente no tendrá conexión a internet, ya que no estamos redirigiendo su tráfico ni interceptándolo, solo no va a ninguna parte debido a que no lo estamos interceptando.
## Certificado de confianza en nuestro proxy

Por ello, en la página **mitm.it** tenemos los certificados para poder descargarlos. Sí, ahora que nuestro tráfico pasa por el proxy intentamos acceder nuevamente, ya veremos las opciones para descargarlos:

![[Offensive/https_sniffer/images/007.PNG]]

### Instalación manual

Para la instalación manual, solo tendremos que descargarlo y, como al instalar cualquier aplicación, le daremos a siguiente hasta llegar al apartado de la contraseña.

![[Offensive/https_sniffer/images/013.PNG]]

Cuando lleguemos al apartado de la contraseña, solo le damos lo siguiente, de esta manera lo tendremos sin contraseña y no nos preocuparemos por nada más. Finalmente, cuando lleguemos al partado del almacenamiento del certificado:

![[Offensive/https_sniffer/images/014.PNG]]

Seleccionaremos la segunda opción para seleccionar nosotros dónde almacenarlo y lo almacenaremos en las entidades de certificacion de confianza:

![[Offensive/https_sniffer/images/015.PNG]]

En este caso, la segunda opción, le damos a ok y siguiente. Finalmente, nos pedirá una confirmación y le daremos a "si":

![[Offensive/https_sniffer/images/016.PNG]]

Con ello, ya tendríamos el certificado en el ordenador que es nuestra víctima. Finalmente, si deseáramos, podríamos eliminar de la carpeta de descargar el certificado, así como de la carpeta que almacena los archivos eliminados para no dejar rastro alguno. 

Esto no nos salta el antivirus debido a que es un certificado, no malware. Es un certificado que nosotros mismos, como el propio "usuario" de la máquina, estamos importando y confiándolo en él.
### Instalación desde terminal (CMD as Admin)

-- Falta investigar...........

Con el certificado instalado y nuestro **mitmweb** corriendo desde nuestra maquina atacante, si ahora como prueba cerramos el navegador y lo abrimos nuevamente, al buscar cualquier cosa en internet ya no saldrá ninguna alerta y podremos navegar sin problemas:

![[Offensive/https_sniffer/images/017.PNG]]

La víctima podría navegar siempre y cuando no cerremos nuestro programa **mitmweb**, de lo contrario tendríamos que deshabilitarle el proxy para que no notara nada. Teniendo todo esto, nosotros como atacantes ya tenemos la posibilidad de descifrar este tráfico HTTPS y ver qué es lo que nuestra maquina víctima está enviando a nivel de datos en las solicitudes que realiza.

## Capturar el tráfico

Para ver el tráfico, estaremos utilizando en nuestra maquina de atacante el binario **mitmproxy** en lugar de **mitmweb**. Esto nos abre un panel en el cual podremos ver el tráfico de una mejor manera:

![[Offensive/https_sniffer/images/018.PNG]]

Si en el navegador ahora realizamos una búsqueda como "hack4u", capturaremos todo este tráfico:

![[Offensive/https_sniffer/images/019.PNG]]

Podremos movernos hacia arriba o abajo con las flechas entre cada solicitud o directamente utilizar el cursor y presionar en alguna, en este caso seleccioné una de las que tenía **www\.bing.com**, ya que estoy en el navegador Edge y al presionar en la solicitud vemos de forma más extendida la información sobre esta, viendo como en el apartado **referer** vemos la URL de la solicitud y si nos fijamos en la búsqueda que realizamos en el navegador, es la misma URL.

![[Offensive/https_sniffer/images/020.PNG]]

Por lo tanto, ya estamos capturando todo el tráfico HTTPS sin ningún problema gracias a mitmproxy. Si ahora nos vamos a Facebook y enviamos una solicitud para loguearnos, evidentemente Facebook nos responderá que las credenciales son incorrectas:

![[Offensive/https_sniffer/images/021.PNG]]

Pero si nos vamos a nuestra maquina de atacante y vemos la solicitud POST, veremos cómo esta envía los datos y podemos verlos:

![[022.PNG]]

En este caso vemos que la contraseña que viaja está cifrada. Esto seguramente es porque el front-end también se encarga de realizar algo como medida de seguridad. Es posible que utilice base64 de alguna forma para no enviarlo al servidor en texto claro. 

Cuando vemos los paquetes con el **mitmproxy** podemos observar cómo vemos dos flechitas **>>** apuntando a la petición en la que nos encontramos posicionados. Esta herramienta también tiene la posibilidad de repetir alguna petición que envió la víctima si presionamos la letra **r** y esto le repetiría a la víctima esta petición.

Ahora saldremos de **mitmproxy** con ESC y despues **y**. Utilizaremos en su lugar **mitmdump** que, si observamos con el manual (**--help**) veremos cómo tenemos la opción **--scripts**:

![[023.PNG]]

Esto lo que nos permite es adjuntarle un script a esta herramienta para nosotros manejar de la forma que consideremos el tráfico que nos llegue de la víctima.

## Script

Por ello, ahora nos crearemos nuestro **https_sniffer.py**.

