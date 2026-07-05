
# Índice

- [[#Enumeración del sistema]]
- [[#Introducción]]
- [[#Practica]]
- [[#Manual]]
- [[#Automatizado]]
- [[#Herrameientas pre-creadas]]
- [[#PSPY]]
- [[#Nuestra propia Herramienta]]
- [[#procmon.sh]]
- [[#Siguientes apuntes]]

# Enumeración del sistema

## Introducción

La enumeración es un proceso crítico para identificar, por ejemplo, vías potenciales de poder elevar nuestros privilegios de usuario, así como para comprender la estructura del sistema objetivo y encontrar información util para futuros ataques. 

Algunas de las herramientas que utilizaremos son:

- __LSE (Linux Smart Enumeration)__: Es una herramienta de enumeración para sistemas Linux que permite a los atacantes obtener información detallada sobre la configuración del sistema, los servicios en ejecución y los permisos de archivos. LSE utiliza una variedad de comandos de Linux para recopilar información y presentarla en un formato fácil de entender. Al utilizar LSE, los atacantes pueden detectar posibles vulnerabilidades y encontrar información valiosa para futuros ataques.
- __Pspy__: Es una herramienta de enumeración de procesos que permite a los atacantes observar los procesos y comandos que se ejecutan en el sistema objetivo a intervalos regulares de tiempo. Pspy es una herramienta útil para la detección de malware y backdoors, así como para la identificación de procesos maliciosos que se ejecutan en segundo plano sin la interacción del usuario.

Además, se desarrollará un script en bash ideal para la detección de tareas y comandos que se ejecutan en el sistema a intervalos regulares de tiempo, abusando para ello del comando __ps -eo user,command__ que nos mostrará todo lo necesario.

Herramientas:

- [LSE](https://github.com/diego-treitos/linux-smart-enumeration)
- [PSPY](https://github.com/DominicBreuker/pspy)

## Practica

Cuando nosotros nos enfrentamos a un CTF, tendemos a enfrentarnos a vulnerar servicios, los cuales finalmente nos dan acceso a una máquina. Una vez que nosotros estemos dentro del sistema, el objetivo es poder alcanzar los permisos máximos __root__ (para Linux).

En estos sistemas operativos dependiendo de malas configuraciones del sistema, es posible llegar a tener formas de movernos hacia el usuario con maximos privilegios.

Para ello podemos realizar dos tipos de enumeracion: manual o automatizada.

### Manual

Para una enumeración manual, tendríamos que empezar a ver sobre qué nos estamos moviendo en nuestra sesión de terminal. Comandos como `whoami`, `groups`, `id`, `find / -perm -4000 2>/dev/null`, `cat /etc/passwd`.

Todos estos comandos nos pueden ayudar a listar información importante del sistema, para saber por dónde estamos parados y descubrir ciertas configuraciones que, dependiendo de cómo estén realizadas, pueden ser vías potenciales de escalar nuestros privilegios en el sistema.

### Automatizado

#### Herrameientas pre-creadas

Gracias a la comunidad existen diversas herramientas que nos hacen un reconocimiento total del sistema y de las cosas importantes que generalmente es bueno saber. En este caso veremos herramientas como __LSE (Linux Smart Enumeration)__ o __PSPY__.

__LSE__:

La forma en que podemos traer este script a nuestro sistema es con el siguiente enlace:

```shell
wget "https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh" -O lse.sh;chmod 700 lse.sh
```

Si por alguna razón en algún momento deja de funcionar, lo recomendable es ir al repositorio compartido en la parte superior y descargar el script de forma directa donde sea que se encuentre dentro del repositorio. Podemos utilizar el mismo comando grep, con el enlace que nos da el navegador si abrimos el script en formato raw.

Al ser un script de bash, bastará con darle permisos de ejecución y, al ejecutarlo, nos pedirá una contraseña para que pueda validar con ella cosas potenciales que podría hacer el usuario. Cómo convertirse en root al hacer sudo y poner la propia contraseña del usuario; en este caso no colocaremos nada, solo daremos Enter y continuaremos.

![[Conceptos básicos de enumeración y explotación/Enumeracion del sistema/images/001.png]]

Linux Smart Enumeration tiene 3 modos para mostrar la información (del 0-2); la que siempre estará por default es la 0, que es la que menos información da de forma directa; solo muestra el reporte de forma general, con lo que sí se podría realizar y con lo que no.

La opción 1 se enfoca en información más interesante o que podría ser más potencial para realizar ciertas cosas para escalar privilegios y, finalmente, la opción 2, que muestra de forma detallada el reporte del análisis total.

![[Conceptos básicos de enumeración y explotación/Enumeracion del sistema/images/002.png]]

Si lo ejecutáramos con el parámetro -l 2, veríamos cómo nos lista todo de forma más detallada.

#### PSPY

Para pspy, bastaría con irnos al repositorio y en la parte de releases descargarnos la versión de 64 bits (pspy64).

Este bastará con darle permisos de ejecución y ejecutarlo como si de un script se tratase. Esta herramienta está enfocada en listar los comandos o procesos que están siendo ejecutados de forma recurrente en el sistema.

Es interesante porque también lo reporta con colores, por lo que si se encuentra algún proceso interesante o considerable para que sea una vía potencial de escalar privilegios, se nos mostrará con un color más agresivo como el rojo.

![[Conceptos básicos de enumeración y explotación/Enumeracion del sistema/images/003.png]]

#### Nuestra propia Herramienta

#### procmon.sh

Siguiendo el approach de la herramienta anterior, podemos montarnos un script propio, el cual haga lo mismo, se enfoque en analizar los comandos que están siendo ejecutados en el sistema y los muestre de forma constante.

Para ello podemos utilizar el comando `ps -eo user,command`, este nos dará de forma automática todo lo que se esté ejecutando con la información de usuario que es dueño del proceso, gracias a que así decidimos mostrarlo, primero el usuario y después el comando.

Como no es que el comando esté en constante escaneo, sino que retorna en esa instancia lo que se está ejecutando, nosotros montaremos un script que lo haga de forma automatizada hasta que decidamos detenerlo.

```shell
#!/bin/bash

# Funcion que gestiona el cierre del programa
function ctrl_c(){
  echo "\n\n[!] Saliendo...\n"
  tput cnorm; exit 1
}

# Definicion de la captura del CTRL + C para ejecutar la funcion ctrl_c para cerrar el flujo del programa
trap ctrl_c SIGINT


# Funcion principal
function main(){
  tput civis # Ocultar cursor

  registry=$(ps -eo user,command) # Hacer un registro inicial de lo que se ejecuta

  while true; do
    current_registry=$(ps -eo user,command) # Registro actual
    diff <(echo "$registry") <(echo "$current_registry") | grep -E ">|<" | grep -vE "worker" # Se hace un diff entre los dos para mostrar unicamente lo mas reciente y se filtra por (> y <) para mostrar los comandos ejecutados y los cierres de los mismos. Finalmente se filtra para eliminar por la palabra clave worker, ya que aparece mucho como procesos del sistema corriendo por root.
    registry=$(ps -eo user,command) # Se actualiza el registro inicial.
  done
}

main # Se ejecuta la funcion principal
```

## Siguientes apuntes

[[Introduccion a Burpsuite]]