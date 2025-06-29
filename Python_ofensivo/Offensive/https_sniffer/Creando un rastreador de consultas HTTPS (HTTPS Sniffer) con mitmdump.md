# Introduccion

Nos sumergiremos en el mundo del espionaje de tráfico HTTPS creando un rastreador de consultar HTTPS (HTTPS Sniffer) con **mitmdump**. **Mitmdump** es una herramienta potente que actúa como proxy, permitiéndonos interceptar, modificar y analizar el tráfico entre un cliente y un servidor, tanto para HTTP como para HTTPS. 

El desafío con el tráfico HTTPS, que está cifrado para proteger la privacidad y seguridad de los datos, es que no se puede leer directamente. Aquí es donde entra en juego la instalación de un certificado en la máquina víctima. Al hacer esto, engañamos al dispositivo para que confíe en nuestro proxy, lo que nos permite descifrar y acceder al contenido del tráfico HTTPS.

 # Practica

En este caso ya no sera necesario utilizar en envenamiento ARP (ARP Spoofer). Emplearemos un MITM Attack pero en su lugar emplearemos un proxy.

Un **proxy** es una herramienta que nos ayuda como intermediario a nuestras conexiones cliente-servidor, filtrando todos los paquetes entre ambos. De tal forma que el proxy se encarga en realizar la peticiones por nootros, para que asi el servidor no se entere de que nosotros por detras somos los que realizamos estas peticiones.

Para ello utilizaremos **mitmdump**, la cual es una herramienta open source que no permitira levantar un servidor proxy tipo MITM. Lo realizaremos de esta manera ya que el principal problema al interceptar trafico HTTPS e que ete viaja cifrado y por ende no tenemo la posibilidad de verlo.

Por ello, nos aprovecharemos de un certificado el cual no permite hacer que la maquina victima confie en nosotros como proxy y a nivel de navegacion no note ningun cambio, pero estaremos interceptando el trafico en general y en este caso al confiar en nosotro como proxy, si que podremos ver el trafico HTTPS.

En este caso asumiremos que nosotros ya hemos vulnerado la maquina victima y nos encontramos con permisos de administrador dentro de ella, primeramente se mostrara la forma manual de habilitar el proxy y instalar el certificado, pero despues lo realizaremos desde la terminal, simulando mas un entorno donde hemos vulnerado dicha maquina y nos encontremos en una sesion de powershell (en este caso la victima sera una maquina windows).

Primeramente, en nuestra maquina atacante nos descargaremos los binarios de **mitmproxy** para linux, desde [aqui](https://mitmproxy.org/).

Esto nos decargara un binario comprimido y tendremos que extraerlo:

![[Offensive/https_sniffer/images/001.png]]


