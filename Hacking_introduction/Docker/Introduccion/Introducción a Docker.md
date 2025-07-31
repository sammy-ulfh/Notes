# Apuntes anteriores

[[Identificación y verificación externa de la versión del sistema operativo]]
# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Siguientes apuntes]]
# Introducción

**Docker** es una plataforma de **contenedores** de software que permite crear, distribuir y ejecutar aplicaciones en entornos aislados. Esto significa que se pueden empaquetar las aplicaciones con todas sus dependencias y configuraciones en un contenedor que se puede mover fácilmente de una máquina a otra, independientemente de la configuración del sistema operativo o del hardware. 

Algunas de las ventajas que se presentan a la hora de practicar hacking usando Docker son:

- **Aislamiento:** los contenedores de Docker están aislados entre si, lo que significa que si una aplicación dentro de un contenedor es comprometida, el resto del sistema no se verá afectado.
- **Portabilidad:** los contenedores de Docker se pueden mover fácilmente de un sistema a otro, lo que los hace ideales para desplegar entornos vulnerables para prácticas de hacking.
- **Reproducibilidad:** los contenedores de Docker se pueden configurar de forma precisa y reproducible, lo que es importante en el hacking para poder recrear escenarios de ataque.
# Práctica

Los contenedores en Docker nos permiten encapsular servicios o aplicaciones en una imagen que funciona como si de una cajita se tratase y esta pudiésemos moverla a otros ordenadores. 

Podríamos verlo como un ejemplo típico de que tenemos un código en nuestro ordenador y todo funciona, pero cuando lo movemos hacia otro ordenador, podría no funcionar por falta de dependencias u otros aspectos. En estos casos, los contenedores nos ayudan a evitar estos problemas debido a que una persona podrá colocar todas las dependencias en el mismo contenedor y al moverlo a otro ordenador no tendremos ningún problema y todo continuará funcionando.

Viéndolo de otra forma comparándolo con máquinas virtuales, un contenedor funciona con el mismo kernel de nuestro ordenador y se encapsula en el mismo, lo que genera una funcionalidad similar a la de una máquina virtual, funcionando en un entorno aislado pero con las mismas características del sistema nativo. 

Esto se usa usualmente en entornos donde se llega a colocar alguna aplicación en línea, si esta llega a ser vulnerada al menos el atacante podría destruir el contenedor en general, pero al final al sistema nativo no le sucedería nada, aunque existen formas de llegar a escapar del entorno de este contenedor y llegar al sistema nativo.

Para comprender más cómo es que funcionan los contenedores, podríamos revisar los siguientes videos:

- [Docker resumido](https://www.youtube.com/watch?v=vh1Ri-PMy5I)
- [Docker: explicacion y ejemplo de uso](https://www.youtube.com/watch?v=9eTVZwMZJsA)

# Siguientes apuntes

[[Instalación de Docker en Linux]]
