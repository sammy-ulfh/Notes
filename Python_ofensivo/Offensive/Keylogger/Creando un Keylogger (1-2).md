# Introducción

Un **keylogger** es una herramienta fundamental en el mundo de la ciberseguridad ofensiva. Para esto, utilizaremos la biblioteca **pynput** de Python, que es una herramienta efectiva para monitorear y registrar las pulsaciones del teclado. 

**pynput** es una biblioteca que nos permite controlar y monitorear la entrada del usuario desde teclado y el ratón. En el contexto de un **keylogger**, nos centraremos en la capacidad de pynput para registrar cada tecla presionada en el teclado. Esto es específicamente útil en escenarios de ciberseguridad ofensiva, donde la recopilación de pulsaciones de teclas puede revelar información sensible como contraseñas, mensajes privados o cualquier otro tipo de datos ingresados a través del teclado. 

El aspecto clave será no solo registrar estas pulsaciones, sino también aprender a enviar esta información de manera automática y discreta por correo electrónico. Esto implica configurar un sistema que agrupe las pulsaciones de teclas capturadas y las envíe periódicamente a una dirección de correo electrónico especificada. Esta funcionalidad aumenta la eficacia del keylogger, permitiéndonos acceder a la información capturada de forma remota y continua, lo cual es crucial para operaciones prolongadas de vigilancia o recopilación de datos.
# Práctica

En esta ocasión importaremos **pynput.keyboard**, con esto crearíamos un objeto utilizando el método **Listener** donde, como parámetro **on_press** le pasaremos una función que recibirá el paquete y con ella lo trataremos nosotros.

![[Offensive/Keylogger/images/001.PNG]]

En este caso imprimimos directamente la tecla presionada. Además al final de nuestro script jugaremos con **with** para utilizar el método **join()** en el objeto que hemos creado de la tecla para que se encargue de esperar y cerrar correctamente cada proceso con cada tecla presionada, evitando así errores.

![[Offensive/Keylogger/images/002.PNG]]

Cuando estemos corriendo el script y empecemos a presionar teclas, veremos algo como esto:

![[Offensive/Keylogger/images/003.PNG]]

Nos lo va representando uno a uno y en un formato específico, aquí nosotros podremos colocar todo dentro de una variable la cual definamos de forma pública y sea nuestro **log** el cual irá almacenando la tecla poco a poco y así irlo mostrando:

![[Offensive/Keylogger/images/004.PNG]]

Además, al almacenarlo aplicamos un typecast para asegurarnos de tener un string. Esto nos es de ayuda para los casos de las teclas especiales como los **Enter**, **Espacios**, entre otras teclas. Si con ello imprimiéramos log tendríamos lo siguiente:

![[Offensive/Keylogger/images/005.PNG]]

Seguimos teniendo un formato un poco raro en la representación, para evitar que en las letras nos muestre, utilizaremos el atributo **char** de nuestra **key**:

![[Offensive/Keylogger/images/006.PNG]]

![[Offensive/Keylogger/images/007.PNG]]

![[Offensive/Keylogger/images/008.PNG]]

Con ello podremos ver cómo ya tenemos lo que son las letras en mejor formato, pero cuando presionamos una tecla especial como el espacio o el entre, veremos que recibimos el error de que para estas teclas no existe este atributo, viendo que es el error **AttributeError**.

Como sabemos que al ser estas teclas no tenemos este atributo, podremos aprovecharnos de esta excepción y cuando sea el caso de que no cuente con el atributo, colocar únicamente la **key** con un typecast de string y agregarle un espacio a los lados para evitar que nos lo represente muy pegado a las teclas normales como letras o símbolos:

![[Offensive/Keylogger/images/009.PNG]]

![[Offensive/Keylogger/images/010.PNG]]

De esta manera, sea cualquiera de ambos casos, nos aseguramos de mostrarlo de forma correcta y ahora sí que lo tendríamos con un mejor formato. Adicionalmente, buscaremos representar de mejor forma aquellas teclas especiales. El espacio que lo tenemos como **Key.space** buscaremos representarlo como un espacio y el resto de teclas nos enfocaremos en recuperar su parte después del punto y con **upper()** mostrarlo en mayúsculas. 

Para ello, mediante un condicional, primeramente verificamos si es el espacio. De ser así solo dejamos un espacio y, de lo contrario, recuperamos la parte después del punto y lo hacemos mayúsculas:

![[Offensive/Keylogger/images/011.PNG]]

De esta manera, si es exactamente el espacio, solo colocaremos una cadena con un espacio y, de lo contrario, recuperaremos el segundo elemento al convertirlo en lista con el punto como delimitador y lo convertiremos en mayúsculas, quedándonos lo siguiente:

![[Offensive/Keylogger/images/012.PNG]]

Con esto ya lo tenemos en un mejor formato. Buscaremos cada cierto tiempo limpiar nuestro log y antes de limpiarlo enviarnos esta información a nosotros mediante internet, en este caso será por correo. Primeramente, nos aseguraremos de limpiar correctamente el log cada cierto tiempo, para ello crearemos un **timer** con la librería **threading**.

![[Offensive/Keylogger/images/013.PNG]]

Aquí creamos nuestra función **clear_log** y asegurándonos de, mediante la función global **log** para trabajar en un ámbito global con los mismos datos que está modificando la otra función. 

Lo vamos a deja en un string vacío y con **threading.Timer()** construimos un objeto el cual como primer argumento tendrá un número el cual serán los segundo en los cuales llamara a una función nuevamente, en este caso nos aprovechamos de la recursividad para que se llame a sí misma cada 5 segundos y nos deje vacío nuestro string. 

Finalmente, para asegurarnos de que se realice, inicializamos nuestro hilo. Para asegurarnos de que este se esté ejecutando por detrás, tendremos que inicializar primeramente la función, es por ello que donde indicamos el **join()** nos aseguramos de colocar la función para que se ejecute en un inicio y ya se quede por detrás ejecutándose así misma cada 5 segundo, vaciando por completo el log:

![[Offensive/Keylogger/images/014.PNG]]

Con ello ya tendremos listo la primera parte de capturar las teclas y limpiar nuestra captura cada cierto tiempo.
## Siguientes apuntes

[[Creando un Keylogger (2-2)]]