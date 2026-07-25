## Introducción

**SQL INJECTION (SQLI)** es una técnica de ataque utilizada para explotar vulnerabilidades en aplicaciones web que **no validan adecuadamente** la entrada del usuario en la consulta SQL que se envía a la base de datos. Los atacantes pueden utilizar esta técnica para ejecutar consultas SQL maliciosas y obtener información confidencial, como nombres de usuario, contraseñas y otra información almacenada en la base de datos.

Las inyecciones SQL se producen cuando los atacantes insertan código SQL malicioso en los campos de entrada de una aplicación web. Si la aplicación no valida adecuadamente la entrada del usuario, la consulta SQL maliciosa se ejecutará en la base de datos, lo que permitirá al atacante obtener información confidencial o incluso controlar la base de datos.

Hay varios tipos de inyecciones SQL, incluyendo:

- **Inyección SQL basada en errores**: Este tipo de inyecciones SQL aprovecha **errores en el código SQL** para obtener información. Por ejemplo, si una consulta devuelve un mensaje con un error específico, se puede utilizar este mensaje para obtener información adicional del sistema.
- **Inyección SQL basada en tiempo**: Este tipo de inyección SQL utiliza una consulta que **tarda mucho tiempo en ejecutarse** para obtener información. Por ejemplo, si se utiliza una consulta que realiza una búsqueda en una tabla y se añade un retardo en la consulta, se puede utilizar este retardo para obtener información adicional.
- **Inyección SQL basada en booleanos**: Este tipo de inyección SQL utiliza consultas con **expresiones booleanas** para obtener información adicional. Por ejemplo, se puede utilizar una consulta con una expresión booleana para determinar si un usuario existe en una base de datos.
- **Inyección SQL basada en uniones**: Este tipo de inyecciones utiliza la cláusula **UNION** para combinar con dos o más consultas en una sola. Por ejemplo, si se utiliza una consulta que devuelve información sobre los usuarios y se agrega una cláusula **UNION** con otra consulta que devuelve información sobre los permisos, se puede obtener información adicional sobre los permisos de los usuarios.
- **Inyección SQL basada en stacked queries**: Este tipo de inyección SQL aprovecha la posibilidad de **ejecutar múltiples consultas** en una sola sentencia para obtener información adicional. Por ejemplo, se puede utilizar una consulta que inserta un registro en una tabla y luego agregar una consulta adicional que devuelve información sobre la tabla.

Además de estas, existen diversos tipos de inyecciones SQL. Sin embargo, estas son algunas de las más populares y comúnmente utilizadas por los atacantes en páginas web vulnerables.

Asimismo, es necesario hacer una breve distinción de los distintos tipos de base de datos existentes:

- **Bases de datos relacionales**: Las inyecciones SQL son más comunes en bases de datos relacionales como MySQL, SQL Server, Oracle, PostgreSQL, entre otros. En estas bases de datos se utilizan consultas SQL para acceder a los datos y realizar operaciones en la base de datos.
- **Bases de datos NoSQL**: Aunque las inyecciones SQL son menos comunes en bases de datos NoSQL, todavía es posible realizar este tipo de ataque. Las bases de datos NoSQL, como MongoDB o Cassandra, no utilizan el lenguaje SQL, sino un modelo de datos diferente. Sin embargo, es posible realizar inyecciones de comandos en las consultas que se realizan en estas bases de datos.
- **Bases de datos de grafos**: Las bases de datos de grafos como Neo4j, también pueden ser vulnerables a inyecciones SQL. En estas bases de datos, se utilizan consultas para acceder a los nodos y relaciones que se han almacenado en la base de datos.
- **Base de datos de objetos**: Las bases de datos de objetos, como db40, también pueden ser vulnerables a inyecciones SQL. En estas bases de datos, se utilizan consultas para acceder a los objetos que se han almacenado en la base de datos.

Es importante entender los diferentes tipos de inyecciones SQL y cómo pueden utilizarse para obtener información confidencial y controlar una base de datos. Los desarrolladores deben asegurarse de validar adecuadamente la entrada del usuario y de utilizar técnicas de defensa, como la sanitización de entrada y la preparación de consultas SQL, para prevenir inyecciones SQL en sus aplicaciones web.

Enlace a la herramienta [Extendclass](https://extendsclass.com/mysql-online.html) que se utilizará a continuación.

## Instalación y explicación

Para ello, primero tendremos que tener SQL en nuestro sistema. Una forma de tenerlo totalmente en terminal y en una versión ligera es utilizando **MariaDB**, la cual es una herramienta de línea de comandos que nos ayuda a desplegar el servicio de MySQL y acceder al mismo.

Para este caso, instalaremos mariadb-server, apache2 y php-mysql (para poder montarnos un script en PHP y esto pueda ser interpretado). A lo largo de las explicaciones con las inyecciones SQL, se utilizará tanto php como python scripting.

```shell
apt install mariadb-server apache2 php-mysql -y
```

## ¿Cómo funciona MySQL o una base de datos?

Cuando nosotros tenemos una aplicación e iniciamos sesión en ella, por detrás, al enviar las credenciales, lo que sucede es que viaja una sentencia definida con el lenguaje SQL, lo que hace es comunicarse con una base de datos disponible para validar si estos datos son existentes y, por lo tanto, si este usuario con dicha contraseña es correcto o no para loguearse a la aplicación.

## Habilitando servicios

Estos funcionarán como demonios o servicios en nuestro ordenador, por lo tanto tendremos que habilitarlos para que se encuentren funcionando.

```shell
service mysql start # Servicio de base de datos
service apache2 start # Servicio HTTP (levanta un servidor)
```

Para acceder a la línea de comandos de MySQL, tendremos que iniciar sesión para acceder a lo que tenemos disponible para un usuario; en este caso será con el usuario **root**:

```shell
mysql -u root -p
```

Al iniciar, veremos que tendremos una terminal interactiva, aquí podremos tener existentes diversas bases de datos, que en este caso podremos ver con el comando **show databases;**. Aquí toda la información que veamos o agreguemos, como crear una base de datos, una tabla, agregar columnas a una tabla, insertar, consultar o eliminar información; sera completamente con consultas SQL.

Para iniciar, nos pedirá una contraseña, pero inicialmente no tenemos ninguna contraseña, por lo que tendremos que darle al **Enter**. Si no funciona o se rechaza la conexión, es porque tendremos que estar como usuario **root** en la propia terminal del sistema para tener todos los permisos.

![[OWASP TOP 10 y Vulnerabilidades Web/SQLI/images/001.png]]

Para ingresar a una base de datos, veremos con con **use** y el nombre, podremos entrar en ella. Además, las sentencias SQL siempre finalizan con un punto y coma (**;**).

## Explicación inicial y de concepto

Todo lo que se utiliza en este lenguaje son sentencias para manejar las bases de datos y su información. Por lo tanto, en un escenario de inyección, lo que se buscará es que, con la mala validación de las propias sentencias, si algunas llevan tal cual el texto insertado en campos de formulario, se pueden utilizar caracteres para romper el propio flujo de la sentencia y crear sentencias alternativas.

Un ejemplo sería para la consulta de credenciales de un usuario. Si tienes a un usuario que tiene una contraseña específica, una validación sencilla y directa es que te retorne un usuario si existe ese usuario con esa contraseña; de lo contrario, no retorna nada.

```SQL
SELECT username FROM user WHERE user = 'user' AND password = 'passwd';
```

En este caso, los valores insertados por el usuario irían en los campos donde se coloca el texto. Lo que sucede es que esto se interpreta directamente por el lenguaje, por lo que puede ser manipulado por sus propios caracteres.

Un ejemplo sería romper la propia cadena de texto con otra comilla y ahí daría error, pero SQL, al ser un lenguaje, tiene comentarios, por lo que si seguido de romper el string agregas un comentario, estarías ignorando la segunda parte de la sentencia, que sería la contraseña, y por ende te lo tomaría como válido ignorando la contraseña, permitiéndote loguearte como dicho usuario.

```SQL
SELECT username FROM user WHERE user = 'username'or 1=1-- -' AND password = 'passwd';
```

De esta manera, si observamos, al romper el string, ahora estamos dentro de la propia sentencia y podríamos agregar cosas; en este caso se agrega una validación que siempre dará TRUE (1=1) y se comenta el resto de la sentencia con **-- -**.

De tal manera que se valida de forma automática, permitiendo un acceso no autorizado. Por lo tanto, una inyección SQL es aprovechar el mal manejo de las sentencias para inyectar sentencias alternativas que nos permitan acceder a información o incluso nos permitan modificar la base de datos de forma no autorizada.

## Navegando sobre SQL

Como hemos visto, si queremos ver las tablas que tengamos al entrar en una base de datos, podremos utilizar el comando __show tables;__.

Una vez veamos las tablas existentes, podremos tener curiosidad sobre qué columnas de información se encuentran en esta tabla, por lo que esto lo podremos ver con la sentencia **describe** y el nombre de la propia tabla:

![[OWASP TOP 10 y Vulnerabilidades Web/SQLI/images/002.png]]

De esta forma vemos todas las columnas de los datos que almacena, el tipo de dato que es, si puede estar como **NULL** o no, entre otros datos. Aquí ya podríamos intentar aplicar una consulta donde veamos la información almacenada, por ejemplo, en las columnas **User** y **Password**.

```SQL
SELECT user,password FROM user;
```

![[OWASP TOP 10 y Vulnerabilidades Web/SQLI/images/003.png]]


