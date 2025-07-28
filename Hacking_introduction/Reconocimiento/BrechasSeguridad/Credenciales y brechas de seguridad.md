# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#DeHashed]]
- [[#Linkedin]]
- [[#Siguientes apuntes]]
# Introducción

La seguridad de la información es un tema crítico en el mundo digital actual, especialmente cuando se trata de datos sensibles como **contraseñas**, **información financiera** o de **identidad**. Los ataques informáticos son una amenaza constante para cualquier empresa u organización, y una de las principales técnicas utilizadas por los atacantes es la **explotación de las credenciales** y **brechas de seguridad**. 

Una de las formas más comunes en las que los atacantes aprovechan las brechas de seguridad es mediante el uso de leaks de bases de datos. Estos leaks pueden ser resultado de errores de configuración, vulnerabilidades en el software o ataques malintencionados. Cuando una base de datos se ve comprometida, los atacantes pueden acceder a una gran cantidad de información sensible, como nombres de usuario, contraseñas y otra información personal.

Una vez que los atacantes tienen acceso a esta información, pueden utilizarla para realizar ataques de fuerza bruta, phishing y otros ataques de ingeniería social para acceder a sistemas y cuentas protegidas. En algunos casos, los atacantes pueden incluso vender esta información en el **mercado negro** para que los atacantes la utilicen. 

Es importante entender que muchas de estas bases de datos filtradas y vendidas en línea **son accesibles públicamente** y, en algunos casos, incluso se venden por una pequeña cantidad de dinero. Eso significa que cualquier persona puede acceder a esta información y utilizarla para llevar a cabo ataques malintencionados.

Enlace de la página que estaremos utilizando: [DeHased](https://www.dehashed.com/).
# Práctica

## DeHashed

En este caso, en **DeHashed**, nosotros podremos buscar por un dominio o incluso un correo y, en el mejor de los casos, nos podrá incluso dar la contraseña del mismo de las brechas de seguridad que se hayan dado. 

En este caso buscaremos por **tinder.com** y veremos que obtenemos resultados; sin embargo, estos no podremos verlos:

![[Reconocimiento/BrechasSeguridad/images/001.png]]

Usualmente, en esta plataforma será necesario tener un plan de paga para poder visualizar estos resultados de brechas de seguridad que recopilan y tienen en su plataforma. 

Si nosotros pagáramos la suscripción, podríamos visualizarlo de la siguiente manera:

![[Reconocimiento/BrechasSeguridad/images/002.png]]

En este caos veremos cómo estos resultados pertenecen a la plataforma **Dumsmash data** e incluso podremos ver la contraseña, pero hasheada debido a las buenas prácticas de esta plataforma en su base de datos:

![[Reconocimiento/BrechasSeguridad/images/003.png]]

Pero si que podremos llegar a encontrar resultados en los cuales tengamos las credenciales en texto claro:

![[Reconocimiento/BrechasSeguridad/images/004.png]]

Esto puede venir bien porque, de cara al reconocimiento y análisis para emplear distintas técnicas de ataques como phishing, nos puede servir este tipo de páginas para, por ejemplo, si ya tenemos el email del CEO de una empresa y llegamos a encontrar información como credenciales. 

Basándonos en esto, ya podríamos incluso ver similitudes entre credenciales para llegar a montar con alguna herramienta un diccionario para poder emplear en algún punto un ataque de fuerza bruta. 

Con ello ya podríamos tener aproximaciones de contraseñas o incluso sería posible que a día de hoy siga reutilizando esa contraseña en algun otro sitio o que el mismo sitio en el que estaba registrado tenga la misma.
## Linkedin

Otra de las formas que tenemos de recolectar información sobre empleados de una empresa para incluso enfocarnos en aquellos perfiles que tengan más peso o privilegios dentro de la misma, puede ser LinkedIn. 

Es muy usual que las personas que trabajen en una empresa lo adjunten a su perfil y por ende si nosotros vamos al perfil de la empresa podríamos buscar el apartado de sus empleados y con base en ello realizar un análisis y buscar posibles targets de los que podríamos aprovecharnos para llegar a tener una entrada posible a vulnerar mediante técnicas como phishing.

![[Reconocimiento/BrechasSeguridad/images/005.png]]

En casos de tener ya un posible perfil, podríamos intentar diversas cosas. Una de ellas sería realizar distintas combinaciones como **dan.amodio\@tinder.com** o **d.amodio\@tinder.com** y con base en ello realizar cosas como la verificación de que sea un correo válido y luego buscar información con ese correo si es que es válido. 

O incluso llegar a utilizar herramientas como PimEyes para tratar de obtener muchísima más información al respecto de esta persona para realizar un análisis a fondo y ver que podríamos llegar a recopilar que pueda ser de utilidad.
# Siguientes apuntes

[[Identificación de las tecnologías en una página web]]