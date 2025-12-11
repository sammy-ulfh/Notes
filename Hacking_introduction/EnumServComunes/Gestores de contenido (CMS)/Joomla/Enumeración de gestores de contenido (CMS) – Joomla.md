
# Indice

- [[#Introducción]]
- [[#Practica]]
- [[#Despliegue]]
- [[#Enumeración]]
- [[#Joomscan]]
- [[#Siguientes apuntes]]

# Introducción

Ahora veremos cómo enumerar el gestor de contenido __Joomla__. Joomla es un sistema de gestión de contenidos (CMS) de código abierto que se utiliza para crear sitios web y aplicaciones en línea. Joomla es muy popular debido a su facilidad de uso y flexibilidad, lo que lo hace una opción popular para sitios web empresariales, gubernamentales y de organizaciones sin fines de lucro. 

Joomla es altamente personalizable y cuenta con una gran cantidad de extensiones disponibles, lo que permite a los usuarios añadir funcionalidades adicionales a sus sitios web sin necesidad de conocimientos avanzados de programación. Joomla también cuenta con una comunidad activa de desarrolladores y usuarios que comparten sus conocimientos y recursos para mejorar el CMS.

El proyecto utilizado en esta ocasión es`https://github.com/vulhub/vulhub/tree/master/joomla/CVE-2015-8562`.

Una de las herramientas que se utilizarán es __Joomscan__. Joomscan es una herramienta de línea de comandos diseñada específicamente para escanear sitios web que utilizan Joomla y buscar posibles vulnerabilidades y debilidades de seguridad. 

Joomscan utiliza una variedad de técnicas de enumeración para identificar información sobre el sitio web de Joomla, como la versión de Joomla utilizada, los plugins y módulos instalados y los usuarios registrados en el sitio. También utiliza una base de datos de vulnerabilidades conocidas, para buscar posibles vulnerabilidades en la instalación de Joomla.

Para utilizar Joomscan, tendremos que clonar su repositorio y dentro de él ejecutar el script de Perl.

Proyecto: `https://github.com/OWASP/joomscan`

```shell
perl joomscan.pl -u <URL>
```

Donde __<\URL>__ es la URL del sitio web que deseamos escanear. Joomscan escaneará el sitio web y nos proporcionará una lista detallada de posibles vulnerabilidades y debilidades de seguridad. 

Es importante considerar que Joomscan no es una herramienta infalible y puede generar __falsos positivos__ o __falsos negativos__. Por lo tanto, es importante utilizar Joomscan junto con otras herramientas y técnicas de seguridad para tener una imagen completa de la seguridad del sitio web de Joomla que estemos auditando.

# Practica

## Despliegue

Primeramente, tenemos que tener la carpeta del proyecto mencionada anteriormente. Una vez la tengamos, tendríamos que meternos a ella y desplegar el entorno.

```shell
docker-compose up -d
```

Esto nos desplegará todo el proyecto, el cual nos deja habilitada una base de datos y una página web:

![[EnumServComunes/Gestores de contenido (CMS)/Joomla/images/001.png]]

Si vamos al navegador, veremos la página de la siguiente manera:

![[EnumServComunes/Gestores de contenido (CMS)/Joomla/images/002.png]]

## Enumeración

### Joomscan

Tendremos que clonar el repositorio y entrar en él:

```shell
git clone https://github.com/OWASP/joomscan.git \
cd joomscan
```

Una vez con ello listo, bastaría con ejecutar con Perl el script:

```shell
perl joomscan.pl
```

Para empezar a enumerar un Joomla, tendríamos que utilizar esta herramienta y, con el parámetro -u, pasarle el enlace o URL del servicio:

```shell
perl joomscan.pl -u http://127.0.0.1:8080
```

Estos nos arrojan varios resultados. 

Vulnerabilidades:

![[EnumServComunes/Gestores de contenido (CMS)/Joomla/images/003.png]]

Aquí podremos ver cómo, para la versión 3.4.5, son todas las vulnerabilidades que ha encontrado. 

Rutas o recursos encontrados:

![[EnumServComunes/Gestores de contenido (CMS)/Joomla/images/004.png]]

En este caso vemos cómo está expuesto el panel de administrador y, por ende, podríamos entrar al mismo desde el navegador:

![[EnumServComunes/Gestores de contenido (CMS)/Joomla/images/005.png]]

Lo padre o interesante de esta herramienta es que además nos genera un reporte de todo lo encontrado. Nos genera una carpeta __reports/__ a la cual, al acceder, veremos lo siguiente:

![[EnumServComunes/Gestores de contenido (CMS)/Joomla/images/006.png]]

Se genera una carpeta que tiene como nombre la URL a la cual le hemos realizado el escaneo y dentro de esta nuestro reporte, tanto en HTML como en TXT. 

Cambiamos el nombre de nuestro archivo HTML a index.html, para poder habilitar un servidor con PHP o Python y acceder al mismo desde el navegador y que nos muestre esta página, que sería nuestro reporte.

```python3
python3 -m http.server 80
```

```php
php -S 127.0.0.1:80
```

![[EnumServComunes/Gestores de contenido (CMS)/Joomla/images/007.png]]

![[EnumServComunes/Gestores de contenido (CMS)/Joomla/images/008.png]]

Nos da distintas cosas y veremos cómo lo que está en verde son pestañas que podemos desplegar para ver con detalle lo encontrado. 

Para Joomla, en cuanto a enumeración, esto será todo; más adelante se verá cómo explotar dichas vulnerabilidades; por lo pronto, avanzaremos con la enumeración de otro gestor de contenido (CMS).

# Siguientes apuntes

[[Enumeración de gestores de contenido (CMS) – Drupal]]