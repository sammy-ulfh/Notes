# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Hunter.io]]
- [[#Intelligence X]]
- [[#Phonebook.cz]]
- [[#Verificación de correo]]
- [[#Verify Email Address]]
- [[#Email Checker.NET]]
- [[#TheHarvester]]
- [[#Siguientes apuntes]]
# Introducción

La importancia de la recolección de información en la fase de **OSINT** es crucial durante una auditoría. En particular, la recolección de correos electrónicos. Los correos electrónicos pueden ser una valiosa fuente de información para la vulneración de posibles paneles de autenticación y la realización de campanas de **Phishing**. 

Serán presentadas diversas herramientas online que pueden ser de ayuda en este proceso. Por ejemplo, se explica cómo usar **hunter.io** para buscar correos electrónicos asociados a un dominio en particular. También se muestra cómo utilizar **intelx.io** para buscar información relacionada con direcciones de correo electrónico, nombres de usuarios y otros detalles.

Otra herramienta interesante es **phoneboock.cz**, que permite buscar correos electrónicos y otros datos de contacto relacionados con empresas de todo el mundo. 

Se proporcionarán los enlaces a las herramientas online que se verán:

- [Hunter](https://hunter.io)
- [intelligence X](https://intelx.io)
- [Phonebook.cz](https://phonebook.cz)

La recolección de correos electrónicos es una tarea importante en la fase inicial de OSINT y puede proporcionar información valiosa. Sin embargo, es importante tener en consideración que la recolección de correos por sí sola no permite identificar directamente posibles vulnerabilidades en una red o sistema.
# Práctica

![[Reconocimiento/Correos/images/001.png]]

Para hacer un poco más realista este apartado de reconocimiento, fijaremos un target el cual será **tinder**. Al entrar a este programa que se nos muestra dentro de la página de **hackerone**, veremos toda la información, pero sobre todo lo siguiente:

![[Reconocimiento/Correos/images/002.png]]

Estos son los dominios a los cuales tendremos permitido auditar. Cuando vemos algo como **\*.tinder.com**, esto quiere decir que dentro del programa se encuentran todos los subdominios del dominio **tinder.com**. 

Lo que buscaremos ahora será, basándonos en una compañía dada, realizar un descubrimiento de correos electrónicos y para ello tendremos una serie de herramientas.
## Hunter.io

Una vez logueados en hunter.io, en la barra de búsqueda tendremos que buscar por el dominio **tinder.com** y con ello veremos que nos arrojará resultados:

![[Reconocimiento/Correos/images/003.png]]

Si vemos los resultados, podremos observar cómo con ello tenemos una lista de 17 correos electrónicos que corresponden a **Tinder**:

![[Reconocimiento/Correos/images/004.png]]

La mayoría estarán de esta forma, debido a que con el tiempo, todas las plataformas que nos permiten realizar este tipo de búsquedas se han vuelto de paga. 

Si vemos el primer resultado que nos ha dado, podremos observar cómo en el centro tiene una descripción y su enlace al perfil de LinkedIn, al cual de la misma manera solo podremos acceder fuera del plan gratuito.

En este caso, con respecto al primer resultado, es algo que ya se había conocido con las versiones anteriores de la misma plataforma y es **lina.alcala@tinder.com** y de ella misma es el perfil de LinkedIn. 

Esto lo podremos verificar si realizamos una búsqueda para un email específico, brindando nombre y compañía:

![[Reconocimiento/Correos/images/005.png]]

Y de aquí podríamos ir al perfil de LinkedIn. 

Estaremos utilizando más adelante el perfil de LinkedIn para el reconocimiento de imágenes.

## Intelligence X

Esta es otra de las herramientas la cual es muy potente y en ella podríamos llegar a realizar una búsqueda sencilla sin siquiera loguearnos. Lo que pasa es que en este usualmente solo podremos ver la información si tenemos un plan PRO:

![[Reconocimiento/Correos/images/006.png]]

Aquí podríamos llegar a encontrar correos e incluso credenciales de brechas de seguridad que se hayan dado en algún punto.

## Phonebook.cz

Esta plataforma sí es totalmente gratuita y nos permite ver los correos que tenga registrados. El único inconveniente es que actualmente ya realizan una pequeña verificación para el correo, no sea de los típicos como "gmail.com" o "proton.me".

El correo registrado tendrá que pertenecer a cualquier institución y, una vez en phonebook.cz, tendrás que loguearte en intelligence con el enlace que proporciona la página, para lograr tener acceso gratuito a esta información. Después de esto podremos buscar por tinder y lo tendremos:

![[Reconocimiento/Correos/images/007.png]]

Esto nos arroja bastante información, si nosotros fuésemos muy buenos en ingeniería social, esto sería algo que podríamos aprovechar, ya que de cara a phishing que quisiéramos aplicar, mientras mayor sea la cantidad de targets, mayor será la cantidad de usuarios que caigan y puedan llegar a darnos acceso privilegiado a alguna cosa. 

Podríamos verlo como si del 100% que tenemos, al menos cayera entre el 5-10 %. 

**Clearbit** era una extensión muy potente solo para Chrome que funcionaba para encontrar muchísima información, además de los correos, que usualmente reportaba correos con **\@gotinder.com**. Sin embargo, fue descontinuada de chrome.

## Verificación de correo

En ocasiones estas páginas nos podrán llegar a dar falsos positivos, como correos que actualmente ya no se encuentran activos. 

Para ello, tenemos otras dos utilidades que, con solo colocar el correo, nos permitirán verificar si el mismo es válido o no. 

En esta ocasión lo haremos para el correo mencionado en un inicio **lina.alcala\@tinder.com**.
### Verify Email Address

[VerifyEmailAddres.org](https://www.verifyemailaddress.org/)

![[Reconocimiento/Correos/images/008.png]]

Veremos que parece que esta es una dirección válida.

### Email Checker.NET

[Email-Checker](https://email-checker.net)

![[Reconocimiento/Correos/images/009.png]]

De igual forma, nos retorna que esta es una dirección de correo electrónico válida.

## TheHarvester

Esta es una herramienta que funcionará en nuestra terminal, por lo tanto, tendremos que instalarla y esta es **theHarvester**. Corriéndola como root, podremos listar su panel de ayuda con **--help**:

![[Reconocimiento/Correos/images/010.png]]

Con esta herramienta se ha vuelto más complicado el poder obtener correos electrónicos, sin embargo, si nosotros con el parámetro **-d** le damos nuestro dominio como target y con **-b** le indicamos algún source, en este caso Bing. 

Podremos llegar a listar subdominios de la propia empresa que tenemos como víctima:

![[Reconocimiento/Correos/images/011.png]]

![[Reconocimiento/Correos/images/012.png]]
# Siguientes apuntes

[[Reconocimiento de imágenes]]