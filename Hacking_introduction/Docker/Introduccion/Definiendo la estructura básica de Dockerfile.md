# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Siguientes apuntes]]
# Introducción

Un archivo **Dockerfile** se compone de varias secciones, cada una de las cuales comienzan con una **palabra clave** en **mayúsculas**, seguida de uno o más argumentos. 

Algunas de las secciones más comunes de un archivo **Dockerfile** son:

- **FROM:** Se utiliza para especificar la imagen base desde la cual se construirá la nueva imagen.
- **RUN:** Se utiliza para ejecutar comando en el interior del contenedor, como la instalación de paquetes o la configuración del entorno.
- **COPY:** Se utiliza para copiar archivos desde el sistema host al interior del contenedor.
- **CMD:** Se utiliza para especificar el comando que se ejecutará cuando se arranque el contenedor.

Además de estas secciones, también se pueden incluir otras instrucciones para configurar el entorno, instalar paquetes adicionales, exponer puertos de red y más.
# Práctica

Considerando lo anterior, en una estructura básica de un **Dockerfile**, tendremos que utilizar **FROM**, ya que este nos permite indicar qué servicio o incluso sistema y versión deseamos en nuestro contenedor. 

Para ver esto, crearemos un archivo con nombre **Dockerfile** y en el interior colocaremos lo siguiente:

![[Docker/Introduccion/images/003.png]]

![[Docker/Introduccion/images/002.png]]

Con FROM le estamos indicando que queremos que nuestro contenedor sea un Ubuntu y, después de los dos puntos, podremos indicar qué versión deseamos que sea. En este caso, como queremos que sea la última versión, colocamos **latest**. 

Finalmente, **MAINTAINER** nos permite colocar una especia de mensaje en la cual usualmente colocaremos el creador o autor de dicho contenedor.

Por ahora esto sería una estructura muy básica, pero la iremos puliendo mientras vamos viendo esta estructura y su construcción.
# Siguientes apuntes

[[Creación y construcción de imágenes]]