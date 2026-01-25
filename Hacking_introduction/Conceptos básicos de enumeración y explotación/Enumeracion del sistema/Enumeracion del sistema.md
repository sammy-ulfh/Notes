
# Índice

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

Cuando nosotros nos enfrentamos a un CTF, tendemos a enfrentarnos a vulnerar servicios, los cuales finalmente nos dan acceso a una máquina. Una vez que nosotros estemos dentro del sistema, el objetivo es poder alcanzar los permisos máximos __root__ (para Linux) o