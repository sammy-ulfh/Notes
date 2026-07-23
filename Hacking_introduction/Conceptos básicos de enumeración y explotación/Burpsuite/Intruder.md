## Práctica

Cuando tenemos una petición interceptada, podremos enviarla al Intruder con clic derecho y enviar a Intruder o de una forma más fácil: CTRL + I

Una vez enviado al intruder, si nos vamos a este apartado, lo veremos de la siguiente manera:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/023.png]]

Lo interesante del Intruder es que, si vemos el primer menú, nos muestra tipos de ataques. Con ello en mente podríamos llegar a aplicar un ataque de fuerza bruta utilizando esta petición.
### Sniper Attack

Para esto dejaremos el snipper attack; supongamos que sabemos que existe el usuario "admin" pero no sabemos su contraseña. Para ello editaremos la petición colocando este usuario en el campo uid y con el cursor seleccionaremos lo que tenemos en el campo de contraseña y le daremos a "Add" para colocar este campo como payload a intercambiar y, con ayuda de un diccionario, podremos hacer que en cada petición se intercambie por cada una de las contraseñas almacenadas en un diccionario.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/024.png]]

El tipo de ataque **sniper** utiliza únicamente un payload, que en este caso será el campo de contraseña.

Si nos fijamos en el apartado de payloads, veremos cómo en payload configuration podremos darle a **load** para cargar un diccionario. Podría ser, por ejemplo, uno de contraseñas del repositorio de [**SecLists**](https://github.com/danielmiessler/SecLists). Clonándolo y tomando el diccionario de /passwords/common-credentials y las 10000 contraseñas más comunes. Cargar un diccionario como el rockyou no es muy recomendable porque puede petar al ser un diccionario tan grande.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/025.png]]

Si con ello le damos a iniciar ataque, se nos abrirá una segunda ventana donde se verá el ataque y, si observamos cada petición, veremos como el campo del payload es el que se cambia por cada una de las contraseñas del diccionario.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/026.png]]

El Burp Suite Community Edition va intentando las peticiones una a una; sin embargo, el Burp Suite Professional tiene hilos y nos permite ir mucho más rápido, haciendo múltiples peticiones al mismo tiempo.

En casos como estos, si no se cuenta con Burp Suite Professional, lo mejor será tirar de scripting con Python o Bash para realizar este ataque.

En el apartado de configuración del payload, si nos vamos al final, veremos el apartado de encoding; en este caso, lo mejor sería deshabilitarlo para evitar que nos encodee caracteres especiales al ser una contraseña con lo que estamos trabajando, ya que aplica URL encoding. Este es el típico encoding que aplican las URL de los navegadores con caracteres especiales.

## Encodign

Si nosotros escribimos caracteres especiales, los seleccionamos y presionamos CTRL + U, esto aplicará el encoding y veremos cómo se mostrará encodeado:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/027.png]]

Si ahora presionáramos CTRL + SHIFT + U, volveríamos a ver el texto sin el encoding; por ello, al ser contraseñas, no queremos que nos aplique este tipo de encoding en el ataque de fuerza bruta.

- [[Decoder]]

## Validaciones automáticas

Ahora, en la petición que tenemos en el Intruder, he cambiado el usuario por **bob**, sabemos que la contraseña de este usuario es **password** y se encuentra en el diccionario, casi al inicio.

Con ello en mente, si nos vamos a la configuración del Intruder y buscamos **Grep-Extract**, al darle a **Add** tomará la petición, le daremos a **Fetch Response** y veremos la respuesta del servidor; en este caso, el mensaje que arroja para contraseñas no válidas es **invalid password!**, este será el que seleccionaremos:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/030.png]]

Al seleccionarlo, se nos crea una regex para la validación; con darle a OK y verificar que está habilitada la opción, si ahora volvemos a intentar el ataque, veremos cómo cada petición con un login incorrecto nos mostrará el mensaje si se encuentra en la respuesta:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/031.png]]

Como podemos observar, justamente el de **password,** que es la contraseña válida, no muestra este mensaje debido a que no viene en la respuesta del servidor; por ende, sabemos que es una respuesta que se comporta de forma distinta a cuando las credenciales son incorrectas.

El sniper attack, como ya se mencionó, es únicamente de un payload; por ende, si agregáramos un segundo payload, como el usuario, cuando se realice el ataque, el propio Burp Suite considerará como prioritario el primer payload que se encuentre y, por ende, en cada petición cambiaría lo que sería únicamente el valor del usuario, dejando el valor de la contraseña el que estaba inicialmente en la petición.

### Cluster bomb

Si queremos que se intenten x número de contraseñas para 2 o más usuarios, tendríamos que utilizar el tipo de ataque **cluster bomb**, que permitirá agregar un diccionario por cada payload.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/032.png]]

Existen varios tipos de payloads, pero únicamente estaremos trabajando con listas por ahora, que perfectamente pueden ser diccionarios que tengamos.

En este caso, del mismo proyecto **seclists** de GitHub, en la carpeta usernames seleccioné la lista corta para el primer payload y para el segundo seleccioné el diccionario de 10 mil contraseñas.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/033.png]]

En este caso, podremos ver que el comportamiento es intentar la misma contraseña para todos los usuarios y después pasar a la siguiente contraseña y volverla a intentar para todos los usuarios.

### Battering ram

El battering ram trabaja nuevamente con un único payload; lo que hace es que, si tenemos más de un campo seleccionado para intercambiar con el payload, en todos colocará el mismo payload.

Por ejemplo, si nuestro payload es **root** se pondrá tanto en el campo de usuario como en el de contraseña seleccionados como parte del payload. Lo que quiere decir que recibe únicamente un diccionario.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/024.png]]

En este caso, seleccionando el diccionario de usuarios, sabemos que para **admin** la contraseña es **admin**. Podremos irnos a esta petición mostrada en el ataque y tratar de ver la respuesta del servidor. Una de las cosas que nos permite Burp Suite es renderizar la respuesta, tal como lo hace un navegador.

Aquí veremos cómo lo que nos muestra sigue siendo el login a pesar de ser las credenciales incorrectas, cuando deberíamos estar logueados.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/035.png]]

Aquí nos puede quedar duda de qué es lo que está pasando; por ende, podríamos enviar la petición al **Repeater** para trabajar con esta petición, presionando CTRL + R, mientras esté seleccionada.

- [[Repeater]]

### Pitchfork

Este tipo de ataque funciona de la siguiente manera.

| username | password    |
| -------- | ----------- |
| admin    | password123 |
| root     | admin       |
| pepito   | popeye      |
| armando  | hernandez   |
| hat      | red         |

Considerando que tenemos estos dos diccionarios, cada uno para cada payload, nos permite hacer que el ataque se haga combinando ambos diccionarios a la vez.

Para la primera petición, intentará la primera línea de ambos diccionarios, luego la segunda, luego la tercera y así hasta terminar el diccionario.

Por ende, intentará **admin** con **password123**, **root** con **admin**, etc.

## Siguientes notas

- [[Comparer]]