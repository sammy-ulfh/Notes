
## **Agregar nuevos usuarios**

En Linux es posible agregar nuevos usuarios al sistema, para ello se utiliza el comando **useradd**, este tiene que ser ejecutado como administrador y para generar un nuevo usuario tenemos que tener en consideración una serie de parámetros:

- **\-m**: se utiliza para generar el directorio personal del usuario
- **\-G**: se utiliza para asignarle grupos al usuario
- **\-s**: se utiliza para asignarle una Shell específica al usuario
- **\-c**: se utiliza para agregar un comentario para ese usuario

![[63.PNG]]

Como ya vimos, podremos combinar parámetros, en este caso no afecta porque el único que requiere argumento es **G** y con **m** le indicamos que nos genere el usuario home del usuario. Lo que le pasamos seguido del parámetro **G** son los grupos que le asignamos, seguido del nombre del usuario y finalmente con el parámetro **\-s** se le asigna una terminal Bash, con la ruta absoluta de la misma (todo se ejecuta como usuario root).

Finalmente, tendremos que asignarle una contraseña al usuario, para ello utilizaremos el comando **passwd** al cual tendremos que pasarle el nombre del usuario al que le asignaremos la contraseña:

![[64.PNG]]

**¿Cómo verifico que se haya creado correctamente el usuario?**

Para ello podremos verificar el archivo de configuración **group** el cual se encuentra en la ruta **\/etc\/** y filtrar por el nombre de usuario, ya que recordemos que automáticamente se crea un grupo con el mismo nombre del usuario:

![[65.PNG]]

Lo que se ve primero, antes de los dos puntos son los grupos y vemos como existe el grupo **pepe**.
## **Sticky bit**

Para ver como funciona este permiso especial haremos uso del usuario **pepe**, como usuario root dentro dl directorio **\/home\/Downloads** de **sammy** crearemos una carpeta y le asignaremos como propietario y grupo a **pepe**, pero le asignaremos todos los permisos a todos los apartados:

![[66.PNG]]
Ahora con los permisos necesarios en el usuario pepe, migraremos a este usuario con el comando **su** pasándole el usuario al que deseamos cambiar y con ello entraremos en el directorio recién creado y generaremos un archivo pasándole contenido, viendo los permisos de este:

![[67.PNG]]

Si vemos bien, los permisos de escritura en el archivo solamente están para el propietario que es el usuario **pepe**, por ende él podrá incluso borrar el archivo. Considerando que la carpeta principal tiene todos los permisos, incluyendo el de escritura para todos los usuarios.

¿El usuario sammy podría eliminar el archivo?

Aunque los permisos del archivo den a entender que no es posible, realmente sí se podría debido a que de alguna manera se respetan los permisos de la carpeta principal, ya que puede crear o eliminar cualquier cosa dentro del directorio.

![[68.PNG]]

Es por ello que aquí entra en juego el permiso especial sticky bit, que tendrá que colocarlo sobre la carpeta, el usuario pepe.

Para asignar este permiso, en la forma normal tendríamos que agregar como permiso una letra **t**, o en su forma octal un **1**:

- **con letras**
	![[69.PNG]]

- **octal**
	![[70.PNG]]

De esta manera, ahora podríamos crear nuevamente el archivo y veremos como ya no puede eliminarlo el usuario sammy, a pesar de los permisos de la carpeta:

![[71.PNG]]

Además, es importante mencionar que este permiso siempre se colocara en la parte de **otros** en donde se coloca el permiso de ejecución, si este permiso se encuentra habilitado para dicho directorio o archivo, veremos como la letra **t** que representa al permiso es minúscula. Pero si el archivo o directorio no cuenta con permiso de ejecución, la letra aparece en mayúscula, lo mismo aplica para los permisos SUID y SGID.

## Permisos SUID y SGID

Estos permisos pueden ser potencialmente más peligrosos en nuestro ordenador. Ya que al agregarlo a ciertos archivos puede permitirnos la ejecución de dicho archivo como si del propietario (SUID) se tratase o como si del grupo (SGID) se tratase.

Python es un lenguaje de programación que además nos permite ejecutar comandos en el sistema gracias a la librería **os**. Si llega a tener alguno de los permisos especiales recientemente mencionados, sería como si la ejecución de cualquier usuario fuese como root, o si fuese el SGID, como si la ejecución del grupo que la está ejecutando sea **root**, esto es debido a que en este binario, tanto el propietario como el grupo son root:

![[72.PNG]]
## SUID

Este permiso, si en dicho caso lo tuviese el binario de Python, nos permitiría realizar su ejecución como usuario root, ya que al ser otros tenemos el permiso de ejecución, pero al tener el permiso SUID automáticamente se ejecuta como si root lo ejecutase.

- **normal**

	Para asignar el permiso SUID, tendríamos que especificar que queremos asignar el permiso al usuario propietario **u** y agregarle el permiso **s**, que en este caso sería considerado el SUID:

	![[73.PNG]]

	De esta forma ya tendríamos el SUID en el binario de Python y como está el permiso de ejecución para cualquier usuario, si ejecutamos Python como usuario sammy e intentamos solicitar una terminal con la librería **os**, nos lo permitirá gracias a este permiso.

	Para lograrlo directamente tendríamos que cambiar el uid que tenemos, que en este caso es el del usuario que está ejecutando Python, como sabemos que el uid de root siempre es 0, entonces buscamos cambiarlo a este mismo:

	![[74.PNG]]
	

