# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Hackerone]]
- [[#Gobuster]]
- [[#Wfuzz]]
- [[#Siguientes apuntes]]
# Introducción

Haremos uso de **wfuzz** y **gobuster** para aplicar **Fuzzing**. Esta técnica se utiliza para descubrir rutas y recursos ocultos en un servidor web mediante ataques de fuerza bruta. El objetivo es encontrar recursos ocultos que podrían ser utilizados por atacantes malintencionados para obtener acceso no autorizado al servidor. 

**Wfuzz** es una herramienta de descubrimiento de contenido y una herramienta de inyección de datos. Básicamente, se utiliza para automatizar los procesos de prueba de vulnerabilidades en aplicaciones web.

Permite realizar ataques de fuerza bruta en parámetros y directorios de una aplicación web para identificar recursos existentes. Una de las ventajas de **Wfuzz** es que es altamente personalizable y se puede ajustar a diferentes necesidades de pruebas. Algunas de las **desventajas** de Wfuzz incluyen la necesidad de comprender la sintaxis de sus comandos y que puede ser más lenta en comparación con otras herramientas de descubrimiento de contenido. 

Por otro lado, **Gobuster** es una herramienta de descubrimiento de contenido que se utiliza para buscar archivos y directorios ocultos en una aplicación web. Al igual que Wfuzz, Gobuster se basa en ataques de fuerza bruta para encontrar archivos y directorios ocultos. Una de las principales ventajas de **Gobuster** es su velocidad, ya que es conocida por ser una de las herramientas de descubrimiento de contenido más rápidas. También es fácil de usar y su sintaxis es simple. Sin embargo, una **desventaja** de Gobuster es que puede no ser tan personalizable como Wfuzz.

Tanto Wfuzz como Gobuster son herramientas útiles para pruebas de vulnerabilidades en aplicaciones web, pero tienen diferencias en su enfoque y características. La elección entre una u otra dependerá de las necesidades y preferencias de cada uno.

Enlaces a las herramientas:

- [Wfuzz](https://github.com/xmendez/wfuzz)
- [Gobuster](https://github.com/OJ/gobuster)

# Práctica

## Hackerone

Primero tendremos que fijar un target en **hackerone** el cual, leyendo lo permitido y los scopes, no de un target posible, el cual sea legal enumerar mediante un ataque de fuerza bruta. 

En este caso no enfocaremos en Amazon que tiene el dominio de **amazon.com** de Estados Unidos dentro del programa:

![[Reconocimiento/Fuzzing/images/001.png]]

Iniciando con la enumeración, primeramente utilizaremos **Gobuster**.

## Gobuster

En gobuster tenemos distintos comandos que nos sirven para enumerar con respecto a nuestras necesidades. En este caso, como buscamos enumerar directorios y recursos ocultos dentro de un dominio, vamos a utilizar el comando **dir**. Si nosotros ejecutamos gobuster con **--help** veríamos los distintos comandos y una descripción de para cómo podríamos utilizar cada uno. 

Con el parámetro **-u** indicaremos el dominio, y con el parámetro **-w** indicaremos nuestra lista de directorios a efectuar para el ataque de fuerza bruta. En este caso utilizaremos el diccionario **/usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt**. Recordemos que **SecList** lo hemos sacado de un repositorio que contiene una gran cantidad de diccionarios a emplear en diversas situaciones.

Además, utilizaremos para el primer ejemplo una cantidad de **200** hilos, lo cual indicamos con el parámetro **-t**:

```shell
gobuster dir -u https://www.amazon.com -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -t 200
```

![[Reconocimiento/Fuzzing/images/002.png]]

En este caso podremos observar como se repite el código de estado **429** o incluso el **503**, estos suelen ser errores, el 429 hace referencia a que se han hecho una gran cantidad de solicitudes y el servidor no responde correctamente a la misma, el **503** hace referencia a que ese servicio no lo puede responder el servidor, ya que está temporalmente dado de baja. 

Cada código de estado, nosotros mismos podremos investigarlo y ver el significado. En este caso, ocultaremos estos códigos de estado y esto lo haremos con el parámetro **-b**, esto lo podremos checar con **--help** al final al ejecutar nuestro comando:

![[Reconocimiento/Fuzzing/images/003.png]]

El parámetro **-s** es para enfocar en que solo nos muestre códigos de estado específicos y **-b** es para ignorar aquellas que respondan con ciertos códigos de estado. 

Si nos queremos enfocar en ciertos códigos de estado con el parámetro **-s**, también tendremos que colocar el parámetro **-b** con una cadena vacía "**-b ''**", de lo contrario nos daría error.

Nuestro comando ignorando los códigos de estado **429** y **503** ahora quedaría así:

```shell
gobuster dir -u https://www.amazon.com -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -t 200 -b 429,503
```

Con gobuster en ocasiones tendremos errores como el siguiente:

![[Reconocimiento/Fuzzing/images/004.png]]

En este caso, nos menciona que para poder efectuar el ataque de fuerza bruta para enumerar directorios tendríamos que ignorar el error **404** que puede retornar el servidor para recursos no existentes. Como no nos interesa, también lo ignoraremos y ahora sí que funcionaría:

![[Reconocimiento/Fuzzing/images/005.png]]

El **301** como podemos ver hace referencia a redirecciones y algunas de estas se pueden llegar a dar porque nuestro target es **https:\//www.amazon.com/dirname** y en ocasiones el servidor hace una redirección hacia **https:\//www.amazon.com/dirname/**, si quisiéramos reducir la cantidad de output podría ser de ayuda el **--add-slash**, ya que hace que ahora se intente cada uno de los directorios con un slash al final. 

Podremos utilizar el parámetro **-x** para indicar extensiones como **html**, **txt**, **php** para que además de directorios, nos reporte archivos con estas extensiones.

Si queremos listar tanto directorios como archivos, entonces tendremos que quitar el parámetro **--add-slash**, esto se debe a que cuando sean archivos, de igual manera agregará un slash al final y esto no es correcto para los archivos, ya que cuando son archivos se accede a estos sin un slash al final. 

Nuestro comando entonces quedaría de la siguiente manera:

```shell
gobuster dir -u https://www.amazon.com -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -t 200 -b 429,503,404 -x php,html,txt
```

Con ello ya veremos cómo nos reporta tanto archivos como directorios encontrados. Todos los parámetros utilizados podremos verlos más a detalle utilizando el parámetro **--help**.

![[Reconocimiento/Fuzzing/images/006.png]]

## Wfuzz

**Wfuzz** es un programa que no funciona para las versiones recientes de Python, funciona con Python 3.7, por ende para que nos funcione tendríamos que ejecutarlo con esta versión e instalar las librerías necesarias. 

En **wfuzz** tenemos el parámetro **-c** para que nos represente el output con colores. Los hilos se colocan de la forma que en gobuster y nuestro diccionario lo indicamos con el mismo parámetro que con gobuster.

La diferencia es que aquí colocaremos nuestro target al final y, como buscamos listar directorios, en este caso jugaremos con la palabra clave **FUZZ** al final de nuestro target:

```shell
wfuzz -c -t 200 -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt https://www.amazon.com/FUZZ
```

Con ello ya nos empezaría a reportar resultados:

![[Reconocimiento/Fuzzing/images/007.png]]

En **wfuzz** para ocultar códigos de estados utilizamos el parámetro **--hc** que viene de "hide code" y para enfocarnos en mostrar ciertos códigos de estados es con **--sc** que viene de "show code". 

En este caso, como se repite mucho el **404**, lo ocultaremos y si quisiéramos ocultar más de 1, sería separados por comas:

```shell
wfuzz -c -t 200 --hc=404 -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt https://www.amazon.com/FUZZ
```

![[Reconocimiento/Fuzzing/images/008.png]]

Vemos cómo tenemos los códigos de estado **301**, los cuales hacen referencia a que se da una redirección; sin embargo, no nos está mostrando hacia dónde es redirigido. En **wfuzz** para que haga un seguimiento, cuando se realice una redirección tendremos que utilizar el parámetro **-L**:

```shell
wfuzz -c -t 200 -L --hc=404 -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt https://www.amazon.com/FUZZ
```

![[Reconocimiento/Fuzzing/images/009.png]]

En este caos habrá resultados que no nos reporte y esto se debe a la razón que mencionamos con gobuster cuando nos enfocamos únicamente en directorios y es el slash del final, por ende en este caso después de la palabra **FUZZ** le agregaremos el slash y nos podría llegar a reportar mayores resultados en casos de directorios que requieran el slash al final:

![[Reconocimiento/Fuzzing/images/010.png]]

Algo que también podremos notar es que, de diversas ocasiones que lo ejecutemos, nos podrá llegar a arrojar diferentes resultados. Esto se debe a la cantidad de hilos que estamos empleando. Si empleamos una cantidad menor como **50** tendremos una certeza mayor de los resultados reportados. 

Si hacemos lo de agregar la barra al final, incluso podríamos quitar el follow del redirect que es el parámetro **-L**, esto nos viene bien, pero en casos en los que todos o casi todos los directorios siempre se muestran con una barra al final.

En el caso de Amazon no es así, ya que se realizan redirecciones a directorios con nombres distintos. 

Ya con alguno de los descubiertos, podríamos incluso abrir el navegador e intentar entrar a uno y nos llevaría a algún lado de los que Amazon tenga disponibles, tal como **amazon.com\/full**, que termina haciendo una redirección a un producto.

# Siguientes apuntes

[[Fuzzing y enumeración de archivos en un servidor web (2-2)]]