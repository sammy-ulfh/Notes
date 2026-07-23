## Práctica

Burp Suite cuenta con distintas extensiones y podremos buscar e instalar las que nos interesen en la parte de **BApp Store;** algunas requerirán de Burp Suite en su versión Pro.

En este caso buscaremos una que es **Copy as Python Request**; bastará con darle al botón de instalar. Luego podremos verla en Instaladas.

![[044.png]]

Si ahora nos fuésemos a interceptar una petición con el proxy, por ejemplo la de intentar un login, podremos dar clic derecho y en **extensions** utilizar la extensión que acabamos de instalar.

![[045.png]]

Si lo copiamos como request, veremos como ahora en código Python tendremos la forma de tramitar esta petición:

```python
import requests

burp0_url = "http://localhost:8000/login1.php?msg=1"
burp0_cookies = {"PHPSESSID": "dc08ab8d0029da93f7bf222fa58ec622"}

burp0_headers = {"Cache-Control": "max-age=0", "sec-ch-ua": "\"Not-A.Brand\";v=\"24\", \"Chromium\";v=\"146\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Linux\"", "Accept-Language": "en-US,en;q=0.9", "Origin": "http://localhost:8000", "Content-Type": "application/x-www-form-urlencoded", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "http://localhost:8000/login1.php?msg=1", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"}

burp0_data = {"uid": "bob", "password": "password"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
```

Esto lo hace incluso arrastrando las sesiones; esto es más como una capa de personalización en base a lo que mejor nos convenga utilizar de forma personal.
### Pruebas sobre las peticiones con SQLMAP

Algo que podremos hacer con alguna petición es que, al tenerla seleccionada, la podemos almacenar como un archivo; haremos esto en este caso y la almacenaremos como **request.req**.

Será la opción **copy to file** o, en caso de no estar, será **save selected text to file;** en dicho caso tendremos que seleccionar todo lo que contiene la petición y almacenarlo.

![[046.png]]

Con esto veremos la misma petición, ahora almacenada en nuestro ordenador, y con ella podríamos utilizar SQL MAP para que pruebe inyecciones SQL, para en este caso hacerlo en el campo del usuario.

```shell
sqlmap -r request.req -p uid --batch --dbs --dbms mysql --proxy http://localhost:8080
```

De esta forma le damos a sqlmap la petición con el archivo; con **-p** le indicamos que dentro del valor para que intente las inyecciones será el __uid__, que es el valor o campo del nombre de usuario.

Con **batch** se le indica que, independientemente de lo que pregunte, se ponga la opción por defecto; con **dbs** se le indica que lo que se busca es obtener las bases de datos y, finalmente, con **dbms** podemos indicarle directamente que lo haga para **mysql,** que es lo que se utiliza por detrás, ahorrando inyecciones de otros tipos.

Lo interesante de herramientas como **Sqlmap** es que nos permite pasar todo este tráfico por el proxy; interceptando el tráfico o no, podremos ver las peticiones. Interceptándolas, las veremos una a una y necesitaremos permitir que el flujo continúe y, si no las interceptamos, aparecerán en nuestro HTTP history si quitamos lo del target scope y las configuraciones que agregamos en un inicio.

![[047.png]]

Mientras sqlmap está probando las inyecciones, veremos las peticiones que nos van apareciendo en Burp Suite debido a que redireccionamos el tráfico hacia el proxy. Si vemos el campo **uid**, veremos cómo se esta incertando información, que en este caso está URL encodeada.

Como vimos anteriormente, seleccionando y presionando CTRL + SHIFT + U, la veremos en texto plano.

![[048.png]]

Y vemos cómo, por detrás, lo que está intentando sqlmap es inyecciones SQL para mostrarnos información al respecto, que sí es posible nos llegaría a mostrar las bases de datos que maneja la página por detrás.

Que si vemos la terminal, ya cuando finaliza, consigue la información:

![[049.png]]

Múltiples herramientas nos permiten redirigir el tráfico de cosas que se realicen mediante un proxy, como en este caso. Un ejemplo de otra herramienta sería Gobuster, que también tiene este parámetro.

## Siguientes notas

- [[Introduccion a SQLI]]