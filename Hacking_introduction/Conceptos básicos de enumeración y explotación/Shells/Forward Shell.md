
# Índice

# Introducción

La __Forward Shell__ se utiliza en los casos donde no se pueden establecer conexiones Reverse o Bind debido a las reglas del Firewall implementadas en la red. Por lo tanto, se logra mediante el uso de __mkfifo__, que crea un archivo __FIFO (named pipe)__, que se utiliza como una especie de "__consola simulada__" interactiva a través de la cual el atacante puede operar en la máquina remota.

En lugar de establecer una conexión directa, el atacante redirige el tráfico a través del archivo __FIFO__, lo que permite la comunicación bidireccional con la máquina remota.

Entonces, el caso que considera el emplear una __Forward Shell__ es donde no podamos entablar una conexión, pero aprovechemos un archivo FIFO para simular una terminal interactiva en una posible ejecución de comandos que tengamos.

![[Conceptos básicos de enumeración y explotación/Shells/images/013.png]]

# Practica

