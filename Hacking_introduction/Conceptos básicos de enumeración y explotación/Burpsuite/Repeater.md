## Práctica

Con la petición en el repeater, si la enviamos y vemos la respuesta, veremos que regresa un código de estado 302, el cual es una redirección.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/036.png]]

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/037.png]]

Aquí lo interesante es que además tenemos el botón de **follow redirection,** el cual nos permitirá seguir la redirección que se aplica en la petición.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/038.png]]

Esto ya nos traería la respuesta al estar logueados y, si renderizamos, lo veríamos correctamente.

Si vemos tal cual las peticiones, veremos cómo nos redirecciona de /login a /products:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/039.png]]

Cuando ya realizamos diversas peticiones para ver cómo nos está respondiendo el servidor, en el Intruder tenemos las flechitas que nos permiten movernos entre estas peticiones, y la flechita hacia abajo nos permite ver un histórico de las que se han realizado desde esta petición enviada al Repeater:
![[Conceptos básicos de enumeración y explotación/Burpsuite/images/040.png]]

Ahora podremos regresar a ver el [[Intruder]] en el __pitchfork__ attack.