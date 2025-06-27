# Introduccion

Nos sumergiremos en el mundo del espionaje de tráfico HTTPS creando un rastreador de consultar HTTPS (HTTPS Sniffer) con **mitmdump**. **Mitmdump** es una herramienta potente que actúa como proxy, permitiéndonos interceptar, modificar y analizar el tráfico entre un cliente y un servidor, tanto para HTTP como para HTTPS. 

El desafío con el tráfico HTTPS, que está cifrado para proteger la privacidad y seguridad de los datos, es que no se puede leer directamente. Aquí es donde entra en juego la instalación de un certificado en la máquina víctima. Al hacer esto, engañamos al dispositivo para que confíe en nuestro proxy, lo que nos permite descifrar y acceder al contenido del tráfico HTTPS.

 # Practica
