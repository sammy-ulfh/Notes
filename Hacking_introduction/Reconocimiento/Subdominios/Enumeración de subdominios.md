# Índice

# Introducción

La enumeracion de **subdominios** es una de las fases cruciales en la seguridad informatica para identificar los subdominios asociados a un dominio principal.

Los subdominios son parte de un dominio mas grande y a menudo estan configurados para apuntar a diferentes recursos de la red, como servidores web, servidores de correo electronico, sistema de bases de datos, sistemas de gestion de contenido, entre otros.

Al identificar los subdominios vinculados a un dominio principal, un atacante podria obtener informacion valiosa para cada uno de estos, lo que le podria llevar a encontrar **vectores de ataque potenciales**. Por ejemplo, si se identifica un subdominio que apunta a un servidor web vulnerable, el atacante podria utilizar esta informacion para intentar explotar esta vulnerabilidad y acceder al servidor en cuestion.

Existen diferentes herramientas y tecnicas para la enumeracion de subdominios, tanto pasivas como activas. Las **herramientas pasivas** permiten obtener informacion sobre los subdominios sin enviar ninguna solicitud a los servidores identificados, mientras que las **herramientas activas** envian solicitudes a los servidores identificados para encontrar subdominios bajo el dominio principal.

Algunas de las **herramientas pasivas** mas utilizadas para la enumeracion de subdominios incluyen la busqueda en motores de busqueda como Google, Bing o Yahoo, y la busqueda en registros DNS publicos como **Passive Total** o **Censys**. Estas herramientas permiten identificar subdominios asociados con un dominio, aunque no siempre son exhaustivas. Ademas, existen herramientas como **CTFR** que utilizan registros de certificados **SSL/TLS** para encontrar subdominios asociados a un dominio.

Tambien se pueden utilizar paginas online como **phonebook.cz** e **intelx.io**, o herramientas como **sublist3r**, para buscar informacion relacionada con los dominios, incluyendo subdominios.

Por otro lado, las **herramientas activas** para la enumeracion de subdominios incluyen herramientas de fuzzing como **wfuzz** o **gobuster**. Estas herramientas envian solicitudes a los servidores mediante ataques de fuerza bruta, con el objetivo de encontrar subdominios validos bajo el dominio principal.

Enlaces de las herramientas:

- [Phonebook - Pasiva](https://phonebook.cz/)
- [Intelx - Pasiva](https://intelx.io/)
- [CTFR - Pasiva](https://github.com/UnaPibaGeek/ctfr)
- [GoBuster - Activa](https://github.com/OJ/gobuster)
- [Wfuzz - Activa](https://github.com/xmendez/wfuzz)
- [Sublist3r - Pasiva](https://github.com/huntergregal/Sublist3r)
# Práctica

## Phonebook.cz

La misma herramienta que vimos anteriormente, solo que ahora seleccionaremos **Domains** y buscaremos por **tinder.com**, con ello nos listara diversos subdominios bajo el dominio de tinder:

![[Reconocimiento/Subdominios/imagenes/001.png]]

Si lo hicieramos para **URL's** es algo similar, pero lo que sucede es que nos regresa enlaces los cuales apuntan a una diversa cantidad de rutas que puedan existir en el propio dominio:

![[Reconocimiento/Subdominios/imagenes/002.png]]

En ocasiones puede llegar a sucedes que con esta herramienta se muestren entornos de produccion que no se llega a saber que estan expuestos y se pueden llegar a realizar cositas, pero siempre que se sabe ocultan y dejan de mostrar estos entornos expuestos.

## CTFR

En ocasiones nosotros podremos abusar de la transparencia del certificado SSL para encontrar informacion como subdominios u otras cosas. Para ello, utilizaremos la herramienta [CTFR](https://github.com/UnaPibaGeek/ctfr).

Con el enlace de la pagina, lo que haremos sera clonar el repositorio y entrar en el directorio del mismo:

![[Reconocimiento/Subdominios/imagenes/003.png]]

Con ello, ahora vamos a instalar las librerias necesarias de python con el archivo **requirements.txt**:

```shell
pip3 install -r requirements.txt
```

![[Reconocimiento/Subdominios/imagenes/004.png]]

Al ejecutar el script **ctfr.py**, veremos como esta nos pedira el ardumento **-d** de dominio:

![[Reconocimiento/Subdominios/imagenes/005.png]]

Pasandole el dominio de tinder com el parametro **-d**:

![[Reconocimiento/Subdominios/imagenes/006.png]]

Esto funciona de forma pasiva, lo cual quiere decir es que en ningun momento se aplica fuerza bruta para llegar a listar subdominios. Esto lo podremos hacer con cualquier dominio y casi siempre nos reportara informacion a excepcion de que el propio dominio no tenga subdominios.

## Gobuster

Para instalar la version mas reciente tendremos que tener instalado **go** y con ello irnos al repositorio de [gobuster](https://github.com/OJ/gobuster). En el repositorio iremos al README y bajaremos hasta el apartado de **quickinstall**, veremos este comando:

![[Reconocimiento/Subdominios/imagenes/007.png]]

Con ejecutarlo con **go**, ya tendremos instalada la version las reciente de **gobuster**.

Si lo ejecutamos, nos mostrara un panel de ayuda de comandos que se pueden utilizar con esta herramienta. En este caso vamos a utilizar **vhost** que funcionara de forma activa para llegar a enumerarnos subdominios.

![[Reconocimiento/Subdominios/imagenes/008.png]]

Una vez agreguemos el comando **vhost**, podremos utilizar el parametro **-h** y con ello nos listara todas las opciones posibles para este comando:

```shell
gobuster vhost -h
```

![[Reconocimiento/Subdominios/imagenes/009.png]]

Para colocar el dominio utilizaremos el parametro **-u** y ademas tendremos que agregar una wordlist para tener una lista con todo lo que se va a tratar de encontrar mediante fuerza bruta, esta la indicaremos con el parametro **-w**.

Podremos utilizar un repositorio para tener esta wordlists, este repositorio es (https://github.com/danielmiessler/SecLists). Al clonar este repositorio podremos almacenarlo nostros en el directorio **/usr/share**.

Este repositorio tiene un monton de listas que podremos utilizar en distintos casos, pero en este caso nos enfocaremos en los subdominios, para ello podrremos ver el archivo **Discovery/DNS/subdomains-top1million-5000.txt** que es una lista de subdominios a intentar, esta es la siguiente:

![[Reconocimiento/Subdominios/imagenes/010.png]]

Esto lo que hara el propio programa es probarlo con el dominio que nosotros le pasemos, haciendo con cada uno algo como www\.tinder.com, mail.tinder.com, etc.

Por ende ahora ejecutariamos lo siguiente:

```shell
gobuster vhost -u https://tinder.com -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -t 20 --append-domain
```

El **append domain** lo que hace es aplicar este dominio con lo del diccionario para generar multiples subdominios y validarlos de forma activa para tener el resultado.

Con el comando anterior ademas agregamos el parametro **-t** que seria la forma de indicar la cantidad de hilos o tareas en paralelo que deseamos emplear para que nuestro ataque activo o de fuerza bruta vaya mucho mas rapido.

![[Reconocimiento/Subdominios/imagenes/011.png]]

Los resultados nos mostrara todos aquellos donde tenga un error **403** de que no se dio el acceso o no existe, para evitarlo utilizaremos grep con el parametro **-v** para eliminar lineas con la coincidencia 403. De esta manera ahora si que nos reportaria los subdominios encontrados de una forma facil de identificar:

![[Reconocimiento/Subdominios/imagenes/012.png]]

Con ello ya nos reportaria diversos subdominios, ya sea con un diccionario mas pequeno o mas grande, que estos estan en el mismo directorio de donde tomamos el mismo diccionario. Solo cambiando enla ultima parte del titulo.
# Siguientes apuntes