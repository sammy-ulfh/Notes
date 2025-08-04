# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Desplegando el entorno]]
- [[#Descubrimiento de tipos de archivo aceptables]]
# Introducción

El proyecto que estaremos viendo ahora tambien pertenece al mismo repositorio de vulnhub y este es correspondiente a la vulnerabilidad **ImageMagick (ImageTracking)**:

- [Proyecto](https://github.com/vulhub/vulhub/tree/master/imagemagick/CVE-2016-3714)
# Práctica

## Desplegando el entorno

Para traernos esto a nuestra máquina podríamos utilizar nuevamente la herramienta en línea **Downgit**. Una vez en nuestro ordenador, desplegaríamos todo de la misma forma con el comando **docker-compose up -d**.

![[Docker/MaquinasVulnerbales/images/015.png]]

Si vemos en qué puerto está corriendo el servicio con el comando **docker port**, veremos que está en el puerto 8080 de nuestra máquina y el 8080 del contenedor:

![[Docker/MaquinasVulnerbales/images/016.png]]


En este caso, vamos a trabajar con este entorno vulnerable, el cual tiene un servicio corriendo que nos permite la carga de archivos. Realmente sabemos que procesa imágenes y por detrás utiliza **ImageMagick** para procesarlas. 

La idea con esto, por probar y experimentar, es que podríamos crear un archivo el cual sea **test.txt** y colocar cualquier cosa dentro y abriendo el servicio en nuestro navegador, ver qué sucede si subimos el archivo txt que hemos creado:

![[Docker/MaquinasVulnerbales/images/017.png]]

Veremos cómo al subir un archivo txt nos dice que es un tipo de archivo no soportado y cómo por detrás maneja ImageMagick, pues sabemos que por detrás este servicio procesa las imágenes. En caso en el que no sepamos que pueda hacer cualquier herramienta o cosa que lleguemos a encontrar, lo suyo para aprender a desenvolvernos en entornos nuevos sería investigarlo. 

## Descubrimiento de tipos de archivo aceptables

En este caso, podríamos aplicar fuzzing con herramientas como **wfuzz** para probar múltiples extensiones de archivos y averiguar con qué tipos de archivos realmente funciona este servicio. En este caso, en lugar de emplear estas herramientas, utilizaremos **BurpSuite**.

Como ya vimos anteriormente, BurpSuite es una herramienta que nos permite habilitar un proxy que usualmente está para ser activado en la máquina local en el puerto 8080. En este caso, este puerto ya está ocupado, por lo que tendríamos que modificar esto. 

Nos iríamos para ello al apartado de configuración y en proxy buscaríamos seleccionar el que está y modificar el puerto para que sea el 8081:

![[Docker/MaquinasVulnerbales/images/018.png]]

![[Docker/MaquinasVulnerbales/images/019.png]]

Cuando almacenemos todo, tendríamos que tener la opción del proxy configurado seleccionada:

![[Docker/MaquinasVulnerbales/images/020.png]]

Con ello ya tendríamos listo el proxy, para evitar problemas con el tráfico que capture burpsuite del navegador. Lo mejor será utilizar el propio navegador que nos ofrece burpsuite que ya está previamente configurado. 

Para ello, nos iríamos al apartado de **proxy** y le daríamos a **open browser**:

![[Docker/MaquinasVulnerbales/images/021.png]]

En este caso, además de solo llegar a ver el tráfico, podríamos primero abrir la página que se encuentra corriendo en nuestro host y empezar a interceptar el tráfico. Por ahora está en **intercept off** pero tendríamos que encenderlo.


# Siguientes apuntes