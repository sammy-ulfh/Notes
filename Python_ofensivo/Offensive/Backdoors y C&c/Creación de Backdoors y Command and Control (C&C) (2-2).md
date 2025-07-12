
# Práctica

Es momento de mejorar nuestro script del lado de atacante. Primeramente, lo mejoraremos adaptando todo lo que tenemos para que sea una clase a la cual le pasaremos tanto la IP como el puerto en donde lo correremos:

![[Offensive/Backdoors y C&c/images/010.PNG]]

En este caso nuestro constructor se encarga de la creación del socket y de colocarlo en escucha en el puerto indicado, finalmente hace que la conexión que se reciba sea un atributo de la clase, para que así nuestro **run** que sea arrancar el que esté en bucle constante enviando el comando y en escucha por la respuesta del mismo pueda acceder al socket del cliente para manejar los envíos de esta información. 

Por último, podremos agregar lo de gestionar la salida del programa al presionar **CTRL + C** con las librerías signal y sys al inicio del programa.

Con esto ya tendremos totalmente funcional una ejecución remota de comandos gracias a nuestro script que es un backdoor en el sistema de la máquina víctima. Aunado a esto, agregaremos métodos que realicen una serie de pasos, lo cual ya sería un Command and Control.

Esto podría ser generando nuestro propios **comandos** y si hace match el ingresado con **get users** por ejemplo. Este no es un comando del sistema, pero podremos tomarlo nosotros para mandar a llamar un método, el cual se encargue de ejecutar un comando que le de los usuarios del sistema y después enviarlos por correo con la función que utilizamos anteriormente.

De esta manera, ya estaríamos incorporando una funcionalidad de un Command and Control, centralizando una serie de instrucciones con un comando propio del script que nos estamos montando. 

Lo que haremos ahora será que si nosotros ingresamos, **get users** nos ejecute un método el cual será **get_users**, extraiga los usuarios de la máquina víctima y nos lo envíe por correo:

![[Offensive/Backdoors y C&c/images/011.PNG]]

De esta manera, al agregar "get user", a pesar de no ser un comando, nosotros ya tenemos centralizado que recopilara esta información y luego nos la enviará por correo.

![[Offensive/Backdoors y C&c/images/012.PNG]]

De esta manera es como se construye o se considera con Command and Control. Centralizando en un mismo programa una serie de operaciones, las cuales podremos mandar a llamar con un solo "comando" que nuestro programa reconozca.
## Siguientes apuntes

[[Creación de Forward Shell (1-4)]]