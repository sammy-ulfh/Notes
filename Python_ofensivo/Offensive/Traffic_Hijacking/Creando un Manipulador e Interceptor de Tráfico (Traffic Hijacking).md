
# Introducción

Crearemos paso a paso un Manipulador e interceptor de tráfico conocido como **Traffic Hijacking**, una técnica avanzada de ciberseguridad ofensiva. El objetivo es aprender a controlar y alterar el tráfico de una red para manipular lo que un usuario ve en respuesta a sus acciones en la web.

Para lograr esto utilizaremos nuevamente la herramienta **netfilterqueue** en combinación con **iptables**. **NetfilterQueue** nos permite interceptar paquetes que pasan por la red y manipularlos antes de que continúen su camino. Mediante iptables redirigiremos el tráfico relevante (como las solicitudes HTTP/HTTPS) a una cola NFQUEUE, donde podremos inspeccionar y modificar estos paquetes utilizando un script personalizado. 

Una aplicación práctica de esta técnica es alterar las respuestas de las solicitudes web. Por ejemplo, cuando un usuario solicita una página web, podemos interceptar la respuesta del servidor y modificarla antes de que llegue al usuario. Esto puede incluir cambiar textos, insertar scripts maliciosos, redirigir a sitios de phishing, entre otros. Es una forma poderosa de controlar la experiencia del usuario en la web y puede ser utilizada para una variedad de propósitos malintencionados.

# Práctica


