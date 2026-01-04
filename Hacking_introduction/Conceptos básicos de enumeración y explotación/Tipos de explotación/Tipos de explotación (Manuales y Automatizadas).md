# Índice

# Introducción

A continuación se verán dos tipos de explotación utilizados en ataques informáticos: Manuales y Automatizados.

- __Explotación Manual__: Es un tipo de explotación que se realiza de __manera manual__ y requiere que el atacante tenga conocimiento profundo del sistema y sus vulnerabilidades. En este enfoque, el atacante utiliza herramientas y técnicas específicas para identificar y explotar vulnerabilidades en un sistema operativo. Este enfoque es más lento y requiere más esfuerzo y habilidad por parte del atacante, pero también es más preciso y permite un mayor control sobre el proceso de explotación.
- __Explotación Automatizada__: Es un tipo de explotación que se realiza __automáticamente__ mediante el uso de __herramientas automatizadas__, como scripts o programas diseñados específicamente para identificar y explotar vulnerabilidades de un sistema objetivo. Este enfoque es más rápido y menos laborioso que el enfoque manual, pero también puede ser menos preciso y puede generar más ruido en la red objetivo, lo que aumenta el riesgo de detección.

Es importante tener en cuenta que el tipo de explotación utilizado en un ataque dependerá de los objetivos del atacante, sus habilidades y del nivel de seguridad implementado en el sistema objetivo. En general, los ataques de explotación manual son más precisos y discretos, pero también requieren más tiempo y habilidades. Por otro lado, los ataques de explotación automatizada son más rápidos y menos laboriosos, pero también pueden ser más ruidosos y menos precisos.

[Proyecto utilizado para mostrar ambos enfoques](https://github.com/appsecco/sqlinjection-training-app).

# Practica

El proyecto utilizado para mostrar ambos tipos de explotacion lo clonaremos en nuestro dispositivo y lo inicializaremos con __docker-compose__:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/001.PNG]]

Esperaremos un momento a que todo se despliegue y este eproyecto basicamente lo que nos permite es practicar inyecciones SQL en distintos laboratorios. Como lo dicen las indicaciones del proyecto, se desplegara una web en el puerto 8000 y esto podremos verlo en la web:

![[Conceptos básicos de enumeración y explotación/Tipos de explotación/images/002.PNG]]

Primeramente iremos al enlace __reset database__ para que en cuanto a la practica que tendremos para la explicacion de ambos enfoques, tengamos todo correctamente.

Una vez hecho volvemos a la pagina principal.

De los enlaces que se muestran como laboratorios, entraremos al que es el __login 1__.

