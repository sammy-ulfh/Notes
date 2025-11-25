
## Distinción entre archivos y directorios

Cuando nosotros utilizamos el comando **ls \-l** observaremos que nos retorna una mayor información sobre los directorios y archivos.

Aprenderemos a como interpretar estos permisos y modificarlos.

Primeramente, tendremos que visualizar el primer carácter de cualquier archivo o directorio. Estos son los que nos dirán si estamos ante un archivo o ante un directorio:

![[54.PNG]]

En este caso, observamos como estando en el directorio principal absolutamente todos son directorios y por ello todos tienen una letra **d** al inicio.

Si creáramos un archivo dentro del mismo directorio, existen dos formas en las que podría estar representada el primer carácter, ya sea un punto o un guion, esto querrá decirnos que estamos ante un archivo:

![[55.PNG]]

## Interpretación de permisos

Los permisos de archivos y directorios en Linux se dividen en 3 apartados iguales.

Tenemos tres apartados que tienen:

rwx | rwx | rwx

r => Read
w => Write
x => Execute

Estos tres apartados se deben a que estos permisos se dividen en distintas posibilidades.

El primer apartado representa al usuario que es el propietario de dicho archivo o directorio, el segundo apartado representa al grupo que tiene asignado dicho archivo o directorio y finalmente el tercer apartado hacer referencia a otros, lo cual ya es una consideración más general donde se colocan permisos para cualquier usuario del sistema.

| propietario | grupo | otros |
| ----------- | ----- | ----- |
| rwx         | rwx   | rwx   |
¿Cómo podremos saber quién es el propietario y cuál es el grupo asignado?

Seguido de los permisos tenemos dos apartados más, el primero será el nombre del usuario que es el propietario de dicho archivo o directorio, mientras que el segundo indicara que grupo asignado tiene dicho archivo o directorio.

![[56.PNG]]
En este caso para todos estos directorios el propietario es el usuario **sammy** y el grupo asignado es **sammy**.

Los permisos en archivos:

- **read**

	El permiso de lectura en archivos hace referencia a que tendremos la posibilidad de ver el contenido de dicho archivo si ha sido asignado para nuestro apartado (ya sea estando en el grupo asignado, otros o como propietario).

- **write**

	El permiso de escritura en un archivo hace referencia a que podremos modificar y guardar cambios en dicho archivo, si este permiso ha sido asignado para nosotros.

- **execute**

	El permiso de ejecución, quiere decir que nosotros podremos ejecutar dicho archivo, si nos encontráramos ante un binario como Firefox, pero no tuviésemos los permisos de ejecución, simplemente no se abriría para nosotros.

Los permisos de directorios:

- **read**

	El permiso de lectura en un directorio hace referencia a que podremos listar y observar el contenido que tiene este directorio.

- **write**

	El permiso de escritura hace referencia a que podremos crear y eliminar contenido en dicho directorio.

- **execute**

	El permiso de ejecución en directorios hace referencia a que podremos atravesar o entrar en estos directorios con **cd**.

## Modificar permisos

Para la asignación de permisos tendremos que utilizar el comando **chmod**, con este podremos utilizar distintos parámetros para indicar a qué apartado asignaremos los permisos:

- **u+**: asignar al propietario
- **g+**: asignar al grupo
- **o+**: asignar a otros
- **a+**: asignar a todos (por defecto si se omite)

De esta manera, el **+** indica que agregaremos permisos, después de esto indicaremos que permisos deseamos agregar, si quisiéramos agregar el permiso de ejecución únicamente para el usuario propietario, sería de la siguiente manera:

![[57.PNG]]

En este caso, el archivo ya tiene el permiso de ejecución para el propietario, así como el de lectura que ya tenía anteriormente, lo que se debe a que la asignación es como en formato append y no eliminara los permisos que ya estaban anteriormente.

**Eliminación de permisos**

El remover permisos sigue la misma idea, con la diferencia de que cambiamos el signo por un **\-**, con posibilidad de ahora eliminar el permiso que agregamos:

![[58.PNG]]

## Permisos en formato octal

Los permisos podremos modificarlos a nuestro gusto de esta manera, pero existe una forma mucho más eficiente de realizarlo que es de forma numérica.

Tendremos que ver a los permisos con números, los cuales sumados dan 7:

- r => 4
- w => 2
- x => 1

De esta manera, si quisiéramos agregar un permiso individual, agregamos únicamente el número individual al asignar el permiso, pero si queremos asignar permisos en conjunto, bastará con sumar su número base, si le asignáramos a un archivo el permiso 5, estaríamos agregando el de lectura y ejecución.

De esta manera tendremos que colocar un número para cada uno de los tres apartados al momento de asignar los permisos:

![[59.PNG]]

Como vemos, en este caso al colocar directamente los permisos para cada apartado, bastara con solo colocar los permisos de forma numérica, donde 7 abarca los 3 permisos para el usuario administrador (primer apartado), 1 abarca únicamente el permiso de ejecución para el grupo asignado (para el segundo apartado) y el último 1 abarca el mismo permiso para otros (tercer apartado).

## Modificar propietario y grupo de un archivo o directorio

Para realizar esta modificación tendremos que utilizar el comando **chown** donde separado por dos puntos indicaremos primeramente el usuario que será el nuevo propietario y seguido de los puntos el nuevo grupo que le asignaremos, finalmente indicamos el archivo o directorio al que le aplicaremos dichos cambios:

![[60.PNG]]

De esta manera se ha realizado correctamente los cambios (lo anterior fue realizado como root).

Podremos cambiar cada uno de forma individual, sin agregar nada del lado del propietario o del grupo, pero siempre colocando los puntos para saber si lo que se cambiara será el propietario, grupo o ambos:

![[61.PNG]]

De esta manera, ahora como el usuario sammy se encuentra dentro del grupo sammy que le hemos asignado, tendrá los permisos del apartado del grupo.

Cambiar al propietario:

![[62.PNG]]

## Siguientes apuntes

[[Permisos especiales]]
## Material de apoyo

[Permisos y derechos en Linux](https://blog.desdelinux.net/permisos-y-derechos-en-linux/)
[Permisos en Linux](https://www.profesionalreview.com/2017/01/28/permisos-basicos-linux-ubuntu-chmod/)
[Como modificar permisos](https://www.softzone.es/linux/tutoriales/permisos-archivos-directorios-linux/)
[Modificación de permisos y propietarios](https://www.hostinger.es/tutoriales/cambiar-permisos-y-propietarios-linux-linea-de-comandos/)