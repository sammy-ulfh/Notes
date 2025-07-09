# Introducción

Ahora nos aseguraremos de hacer eficiente nuestro keylogger, enfocándonos en la optimización en el proceso de capturar las teclas, así como en el envío automático de las capturas mediante correo electrónico. 

Nos aseguraremos de que el sistema de envío mediante el correo electrónico sea eficaz y eficiente, así como seguro y confiable, para que el registro de pulsaciones llegue con frecuencia a nuestro correo. 

Será recomendable realizarlo con una cuenta de Gmail nueva que además tenga activado el segundo factor de autenticación para que todo nos funcione de forma correcta.
# Práctica

## Mejorando el keylogger

Con lo anterior que ya teníamos nos aseguraremos de reacomodarlo para trabajar con la clase **Keylogger** y ahora las funciones las trataremos como métodos, además de que podremos utilizar el constructor para definir **log** como un atributo de la propia clase. 

Lo que tenemos fuera de funciones, lo dejaremos dentro de un método inicial **start**:

![[Offensive/Keylogger/images/015.PNG]]

Ahora crearemos un archivo **main.py** al cual importaremos nuestro archivo y utilizaremos esta clase que trabaja como nuestro keylogger, inicializándolo con el método start.

![[Offensive/Keylogger/images/016.PNG]]

Con esto, al ejecutarlo, ya tendremos todo funcional, pero podremos llegar a notar como, cuando queremos aplicar el cierre del programa con **CTRL + C**, esto no se aplica correctamente debido a que se queda el hilo del timer que hemos inicializado corriendo. 

Para ello podremos llamar en nuestro def_handler un método el cual sea **shutdown()** para aplicar un cambio en un atributo el cual al ser **True** nuestro método **clear_log** ya no vuelva a llamar a la misma función. Además, haremos que nuestro **timer** también sea atributo para finalizarlo con **time.cancel()** y finalice el programa al instante sin quedarse esperando a que finalice la última instancia del hilo.

![[Offensive/Keylogger/images/017.PNG]]

![[Offensive/Keylogger/images/018.PNG]]

Con esto veremos como al ejecutar **main.py** y aplicar un **CTRL + C** se cerrará automáticamente de forma rápida y segura.
## Envío de correos

Para ello ocuparemos las librerías **smtplib** y **email.mime.text** de la cual traeremos **MIMEText**. Con ello crearemos un método el cual sea **send_email()**, este tendrá como argumentos necesarios: **subject, sender, body, recipients, password**. 

En este caso **body** es el cuerpo del correo, como tal el mensaje que enviaremos, **recipients** es a quien lo enviamos y esto tendremos que colocarlo en una lista por si son más de un correo quien lo recibirá "\[''email1\@gmail.com ,'email2\@gmail.com']" y **password** será de una aplicación que crearemos en nuestro correo y nos dará una contraseña.

![[Offensive/Keylogger/images/019.PNG]]

Con ello podremos mandar a llamar este método antes de vaciar nuestro log y pasarle los datos necesarios:

![[Offensive/Keylogger/images/020.PNG]]

En este caso, la contraseña no es real. Pero la sacaremos de nuestro propio Gmail de Google. 

Primeramente, nos aseguraremos de tener la doble autenticación activada, ya que, de lo contrario, no podremos. Buscaremos en la configuración el apartado de seguridad y luego en [**Contrasenas de aplicaciones**](https://security.google.com/settings/security/apppasswords). 

Crearemos una aplicación aquí, en este caso yo le pondré **keylogger** de nombre:

![[Offensive/Keylogger/images/021.PNG]]

Al crearla automáticamente, tendremos nuestra contraseña:

![[Offensive/Keylogger/images/022.PNG]]

Esta la tendremos que colocar en el apartado de password de nuestro método **send_email**.

![[Offensive/Keylogger/images/023.PNG]]

Con esto vemos como se nos envía por correo de forma automática antes de volver a setear nuestro log como un string vacío. Si tal, como cosa final nosotros mismos podríamos llegar a colocar un log que nos indique que se ha enviado el mensaje y finalmente, como al correr el keylogger de primeras tenemos un string vacío, podremos hacer que en la primera ejecución de nuestro **clear_log**, en lugar de recibir una cadena vacía sea un string que nos diga que se ha inicializado el keylogger. 

En este caso es un keylogger que puede estar enfocado totalmente a Linux por las librerías, por lo que podremos sencillamente ejecutarlo en segundo plano en nuestra máquina víctima y dejarlo corriendo para ir recibiendo en nuestro correo sus pulsaciones por teclado, lo cual podría ser con el comando:

```shell
python3 keylogger.py &> /dev/null & disown
```

Con esto tendríamos listo nuestro keylogger con el cual recibiríamos toda la entrada por teclado, la máquina en la que lo instalemos y pongamos a correr en segundo plano.

## Siguientes apuntes

[[Creación de Malware (1-2)]]