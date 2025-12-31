
# Índice

- [[#Introducción]]
  - [[#Practica]]
  - [[#MKFIFO]]
  - [[#Forward shell]]
- [[#Continuar apuntes]]

# Introducción

La __Forward Shell__ se utiliza en los casos donde no se pueden establecer conexiones Reverse o Bind debido a las reglas del Firewall implementadas en la red. Por lo tanto, se logra mediante el uso de __mkfifo__, que crea un archivo __FIFO (named pipe)__, que se utiliza como una especie de "__consola simulada__" interactiva a través de la cual el atacante puede operar en la máquina remota.

En lugar de establecer una conexión directa, el atacante redirige el tráfico a través del archivo __FIFO__, lo que permite la comunicación bidireccional con la máquina remota.

Entonces, el caso que considera el emplear una __Forward Shell__ es donde no podamos entablar una conexión, pero aprovechemos un archivo FIFO para simular una terminal interactiva en una posible ejecución de comandos que tengamos.

![[Conceptos básicos de enumeración y explotación/Shells/images/013.png]]

# Practica

Para la práctica utilizaremos el mismo laboratorio que hemos construido desde la __Reverse Shell__ y que de igual forma nos sirvió para la __Bind Shell__. 

La ejecución de comandos mediante la web es solo una ejecución de comandos momentánea, lo cual podríamos ver como siempre estar en el mismo punto cada que se ejecuta un comando, por lo que no podremos hacer cosas como movernos entre directorios o cosas interactivas como ejecutar aplicaciones tipo nano.

Esto sucede debido a que la ejecución de cada comando es totalmente separada, como ejecutar un comando a la vez, sin que cada vez que se ejecute alguno se tenga noción de lo ejecutado anteriormente. 

A esto comúnmente se le llama terminal interactiva y es la que podemos tener generalmente en nuestro sistema. Esto podremos comprobarlo incluso escribiendo en nuestro sistema __tty__ como comando.

Si hacemos lo mismo en la web o intentamos ejecutar nano, simplemente no es posible:

![[Conceptos básicos de enumeración y explotación/Shells/images/014.png]]

![[Conceptos básicos de enumeración y explotación/Shells/images/015.png]]

Con nano, evidentemente, no obtenemos el editor de texto porque el navegador no es una terminal interactiva. 

Este caso se está considerando porque se está teniendo en cuenta el caso en el que, mediante la ejecución de comandos, no podemos establecer ni una __Reverse Shell__ o __Bind Shell__. Esto generalmente es debido a las reglas de firewall, donde para un dispositivo dado se pueden bloquear conexiones salientes y entrantes, por lo que únicamente tenemos la posibilidad de la ejecución de comandos, pero sigue sin ser una terminal interactiva.

## MKFIFO

Aquí es donde nos aprovechamos de la misma ejecución de comandos y la carpeta para archivos temporales __/tmp__, donde las tuberías sin nombre nos ayudan a simular una terminal interactiva y eso incluso nos permitiría movernos entre directorios.

__mkfifo__

Lo que nosotros hacemos es con __mkfifo__ crear un archivo de entrada y uno de salida. Lo que nos ayuda a esto es el siguiente comando:

```shell
mkfifo input; tail -f input | /bin/sh 2>&1 > output
```

Esto nos dejará la terminal ocupada, pero podremos aprovecharnos de otra instancia para ver cómo funcionan estos archivos.

![[Conceptos básicos de enumeración y explotación/Shells/images/016.png]]

Técnicamente, lo que sucede es que cualquier comando que enviemos al archivo input será interpretado por una terminal __sh__ la cual almacenará el output, ya sea error o no, dentro de nuestro archivo __output__. 

Lo cual nos ayuda a simular una terminal interactiva.

## Forward shell

Realizar una Forward Shell es aprovechar totalmente este principio. Esto se puede hacer con un lenguaje de programación como Python. 

En este caso utilizaremos un script existente para demostrarlo; el siguiente [proyecto de github](https://github.com/sammy-ulfh/forward_shell) se aprovecha de la misma ejecución de comandos que estamos utilizando en este caso.

![[Conceptos básicos de enumeración y explotación/Shells/images/017.png]]

Puedes ver cómo hacer este tipo de script para una forward shell paso a paso [aquí](https://github.com/sammy-ulfh/Notes/tree/main/Python_ofensivo/Offensive/forward_shell).

Se puede aprovechar el mismo laboratorio ya construido.

> Las notas son construidas en Obsidian, por lo que, para una mejor experiencia, ver todas las imágenes y que los enlaces funcionen, lo recomendable es instalar Obsidian, clonar el repositorio y abrir el vault de apuntes de __Python ofensivo__.

# Continuar apuntes
[[Introducción a Shells]]