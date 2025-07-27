# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Phonebook.cz]]
- [[#CTFR]]
- [[#Gobuster]]
- [[#wfuzz]]
- [[#Sublist3r]]
- [[#Siguientes apuntes]]
# Introducción

La enumeración de **subdominios** es una de las fases cruciales en la seguridad informática para identificar los subdominios asociados a un dominio principal. 

Los subdominios son parte de un dominio más grande y a menudo están configurados para apuntar a diferentes recursos de la red, como servidores web, servidores de correo electrónico, sistema de bases de datos, sistemas de gestión de contenido, entre otros.

Al identificar los subdominios vinculados a un dominio principal, un atacante podría obtener información valiosa para cada uno de estos, lo que le podría llevar a encontrar **vectores de ataque potenciales**. Por ejemplo, si se identifica un subdominio que apunta a un servidor web vulnerable, el atacante podría utilizar esta información para intentar explotar esta vulnerabilidad y acceder al servidor en cuestión. 

Existen diferentes herramientas y técnicas para la enumeración de subdominios, tanto pasivas como activas. Las **herramientas pasivas** permiten obtener información sobre los subdominios sin enviar ninguna solicitud a los servidores identificados, mientras que las **herramientas activas** envían solicitudes a los servidores identificados para encontrar subdominios bajo el dominio principal.

Algunas de las **herramientas pasivas** más utilizadas para la enumeración de subdominios incluyen la búsqueda en motores de búsqueda como Google, Bing o Yahoo, y la búsqueda en registros DNS públicos como **Passive Total** o **Censys**. Estas herramientas permiten identificar subdominios asociados con un dominio, aunque no siempre son exhaustivas. Además, existen herramientas como **CTFR** que utilizan registros de certificados **SSL/TLS** para encontrar subdominios asociados a un dominio. 

También se pueden utilizar páginas online como **phonebook.cz** e **intelx.io**, o herramientas como **sublist3r**, para buscar información relacionada con los dominios, incluyendo subdominios.

Por otro lado, las **herramientas activas** para la enumeración de subdominios incluyen herramientas de fuzzing como **wfuzz** o **gobuster**. Estas herramientas envían solicitudes a los servidores mediante ataques de fuerza bruta, con el objetivo de encontrar subdominios válidos bajo el dominio principal. 

Enlaces de las herramientas:

- [Phonebook - Pasiva](https://phonebook.cz/)
- [Intelx - Pasiva](https://intelx.io/)
- [CTFR - Pasiva](https://github.com/UnaPibaGeek/ctfr)
- [GoBuster - Activa](https://github.com/OJ/gobuster)
- [Wfuzz - Activa](https://github.com/xmendez/wfuzz)
- [Sublist3r - Pasiva](https://github.com/huntergregal/Sublist3r)
# Práctica

## Phonebook.cz

La misma herramienta que vimos anteriormente, solo que ahora seleccionaremos **Domains** y buscaremos por **tinder.com**. Con ello, nos listará diversos subdominios bajo el dominio de Tinder:

![[Reconocimiento/Subdominios/imagenes/001.png]]

Si lo hiciéramos para **URL's** es algo similar, pero lo que sucede es que nos regresan enlaces, los cuales apuntan a una diversa cantidad de rutas que puedan existir en el propio dominio:

![[Reconocimiento/Subdominios/imagenes/002.png]]

En ocasiones puede llegar a suceder que con esta herramienta se muestren entornos de producción que no se llega a saber que están expuestos y se pueden llegar a realizar cositas, pero siempre que se sabe, ocultan y dejan de mostrar estos entornos expuestos.

## CTFR

En ocasiones nosotros podremos abusar de la transparencia del certificado SSL para encontrar información como subdominios u otras cosas. Para ello, utilizaremos la herramienta [CTFR](https://github.com/UnaPibaGeek/ctfr). 

Con el enlace de la página, lo que haremos será clonar el repositorio y entrar en el directorio del mismo:

![[Reconocimiento/Subdominios/imagenes/003.png]]

Con ello, ahora vamos a instalar las librerías necesarias de Python con el archivo **requirements.txt**:

```shell
pip3 install -r requirements.txt
```

![[Reconocimiento/Subdominios/imagenes/004.png]]

Al ejecutar el script **ctfr.py**, veremos cómo esta nos pedirá el argumento **-d** de dominio:

![[Reconocimiento/Subdominios/imagenes/005.png]]

Pasándole el dominio de Tinder con el parámetro **-d**:

![[Reconocimiento/Subdominios/imagenes/006.png]]

Esto funciona de forma pasiva, lo cual quiere decir es que en ningún momento se aplica fuerza bruta para llegar a listar subdominios. Esto lo podremos hacer con cualquier dominio y casi siempre nos reportará información, a excepción de que el propio dominio no tenga subdominios.

## Gobuster

Para instalar la versión más reciente tendremos que tener instalado **go** y con ello irnos al repositorio de [gobuster](https://github.com/OJ/gobuster). En el repositorio iremos al README y bajaremos hasta el apartado de **quickinstall**. Veremos este comando:

![[Reconocimiento/Subdominios/imagenes/007.png]]

Con ejecutarlo con **go**, ya tendremos instalada la versión las reciente de **gobuster**. 

Si lo ejecutamos, nos mostrará un panel de ayuda de comandos que se pueden utilizar con esta herramienta. En este caso, vamos a utilizar **vhost** que funcionará de forma activa para llegar a enumerarnos subdominios.

![[Reconocimiento/Subdominios/imagenes/008.png]]

Una vez agreguemos el comando **vhost**, podremos utilizar el parámetro **-h** y con ello nos listará todas las opciones posibles para este comando:

```shell
gobuster vhost -h
```

![[Reconocimiento/Subdominios/imagenes/009.png]]

Para colocar el dominio utilizaremos el parámetro **-u** y además tendremos que agregar una wordlist para tener una lista con todo lo que se va a tratar de encontrar mediante fuerza bruta. Esta la indicaremos con el parámetro **-w**. 

Podremos utilizar un repositorio para tener estas wordlists. Este repositorio es (https://github.com/danielmiessler/SecLists). Al clonar este repositorio, podremos almacenarlo nosotros en el directorio **/usr/share**. 

Este repositorio tiene un montón de listas que podremos utilizar en distintos casos, pero en este caso nos enfocaremos en los subdominios. Para ello podremos ver el archivo **Discovery/DNS/subdomains-top1million-5000.txt** que es una lista de subdominios a intentar. Esta es la siguiente:

![[Reconocimiento/Subdominios/imagenes/010.png]]

Esto lo que hará el propio programa es probarlo con el dominio que nosotros le pasemos, haciendo con cada uno algo como www\.tinder.com, mail.tinder.com, etc. 

Por ende ahora ejecutaríamos lo siguiente:

```shell
gobuster vhost -u https://tinder.com -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -t 20 --append-domain
```

El **append domain** lo que hace es aplicar este dominio con lo del diccionario para generar múltiples subdominios y validarlos de forma activa para tener el resultado. 

Con el comando anterior, además agregamos el parámetro **-t** que sería la forma de indicar la cantidad de hilos o tareas en paralelo que deseamos emplear para que nuestro ataque activo o de fuerza bruta vaya mucho más rápido.

![[Reconocimiento/Subdominios/imagenes/011.png]]

Los resultados nos mostrarán todos aquellos donde tenga un error **403** de que no se dio el acceso o no existe. Para evitarlo, utilizaremos grep con el parámetro **-v** para eliminar líneas con la coincidencia 403. De esta manera, ahora sí que nos reportaría los subdominios encontrados de una forma fácil de identificar:

![[Reconocimiento/Subdominios/imagenes/012.png]]

Con ello ya nos reportaría diversos subdominios, ya sea con un diccionario más pequeño o más grande, que estos están en el mismo directorio de donde tomamos el mismo diccionario. Solo cambiando la última parte del título.

## wfuzz

Esta herramienta es activa y emplea fuzzing al igual que **gobuster**. Se tendrá que instalar mediante la terminal también. 

Esta la podremos utilizar de forma muy similar. Si quisiéramos que nos reportara la información con colores, podríamos agregar el parámetro **-c**. Como hacemos con **gobuster**, el parámetro **-t** nos permitirá indicar los hilos y el parámetro **-w** el diccionario, que en este caso utilizaremos el mismo. 

Por el momento veríamos nuestro comando de la siguiente manera:

```shell
wfuzz -c -t 20 -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

El dominio al que vamos a aplicar el fuzzing el cual funciona de forma activa empleando solicitudes de forma directa al dominio para descubrir subdominios, tendría que ir al final. 

Con ello en mente primero explicaremos un concepto de **wfuzz**. En wfuzz se utiliza la palabra clave para indicar en que parte se sustituirá cada línea de nuestro diccionario, se suele utilizar al final como si de una ruta se tratase "**https:\//tinder.com/FUZZ**", con ello se indica que se reemplaza al final y esto se utiliza solamente cuando queremos mediante fuerza bruta reconocer rutas o archivos en un dominio.

En nuestro caso, al querer descubrir subdominios tendríamos que dejar el dominio normal y agregar antes un header con el parámetro **-H** y con comillas dobles agregaremos **"Host: subdominio.tinder.com"**. 

En este caso, en el inicio de nuestro dominio representado en el header se representa antes con un punto el subdominio, el cual de la misma forma tendrá que emplear la palabra clave para que la herramienta sepa que ahí tendrá que colocar cada uno de los subdominios a probar con nuestro diccionario. Quedando como **"Host: FUZZ.tinder.com"**:

```shell
wfuzz -c -t 20 -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.tinder.com" https://tinder.com
```

Con ello ya funcionaría, pero, como nos pasó con **gobuster** nos arrojara todos los errores **403**. Para evitar este output utilizaremos el parámetro **--hc** (hide code) y se lo daremos con un igual **"--hc=403"**, que sería lo mismo para mostrar solamente un código de estado como, por ejemplo, el 200 **--sc=200** (show code).

Quedándonos al final de la siguiente manera:

```shell
wfuzz -c -t 20 --hc=403 -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.tinder.com" https://tinder.com
```

Con ello ya nos mostraría resultados que encuentre, que recordemos que el 403 lo retorna cuando no logra encontrar nada con el subdominio que se ha intentado de la lista.

## Sublist3r

**Sublist3r** es una herramienta que igual funciona de forma pasiva mediante la recolección de información pública en internet para retornarnos subdominios que pueda encontrar; por lo tanto, este tipo de búsquedas mediante OSINT son legales. 

Primero clonaremos el repositorio de [sublist3r](https://github.com/aboul3la/Sublist3r). 

Una vez clonado, nos iremos a su directorio y ejecutaremos el **setup.py** junto con **install** para instalarlo:

```shell
python3 setup.py install
```

![[Reconocimiento/Subdominios/imagenes/013.png]]

Por último, instalaremos los requerimientos de la herramienta para evitar que de errores:

```shell
pip3 install -r requirements.txt
```

Con ello ya podremos ejecutar la herramienta desde la terminal:

![[Reconocimiento/Subdominios/imagenes/014.png]]

Finalmente, pasándole algún dominio con el parámetro **-d**, la herramienta empezará una búsqueda en internet para listarnos subdominios del dominio que le pasemos:

![[Reconocimiento/Subdominios/imagenes/015.png]]

En este caso solo encontró 3, pero si intentamos con otros como **lindedin.com**, nos encontraría más:

![[Reconocimiento/Subdominios/imagenes/016.png]]

Los resultados que esta herramienta nos de, dependerán completamente de la información pública al respecto en internet.

# Siguientes apuntes

[[Credenciales y brechas de seguridad]]