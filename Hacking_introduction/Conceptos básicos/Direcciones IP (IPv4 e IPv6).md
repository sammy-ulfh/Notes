# Índice

- [[#Introducción]]
- [[#¿Qué es una IP?]]
- [[#Siguientes apuntes]]

## Introducción

Las direcciones IP son identificadores numéricos únicos que se utilizan para identificar dispositivos en una red, como ordenadores, routers, servidores y otros dispositivos conectados a internet.

Existen dos versiones de direcciones IP: *IPv4* e *IPv6*. La dirección *IPv4* utiliza un formato de dirección de 32 bits y se utiliza actualmente en la mayoría de las redes. La dirección *IPv6* utiliza un formato de dirección de 128 bits y se está implementando gradualmente en todo el mundo para hacer frente a la escasez de direcciones *IPv4*.

Las direcciones *IPv4* se representan como cuatro números separados por puntos, como **192.168.0.1**, mientras que las direcciones *IPv6* se representan en notación hexadecimal y se separan por dos puntos como **2001:0db8:85a3:0000:0000:8a2e:0370:7334**

## ¿Qué es una IP?

Una dirección IP se considera una etiqueta numérica que identifica de manera lógica y jerárquica a una interfaz en la red de un dispositivo que utilice el protocolo de Internet.

La representación de una IP no son más que bits y su representación son 4 octetos (pares de 8 bits). También es importante tener en cuenta que 1 byte es equivalente a 8 bits, por lo tanto, al representar la IP completa en binario estaríamos representando 4 bytes o 32 bits.

Esto lo podremos ver de una forma más práctica, convirtiendo cada par de 8 bits en binario. De tal manera que veríamos más fácilmente esto, comenzaremos convirtiendo el propio 192 de una dirección IP de decimal a binario:

![[Conceptos básicos/images/001.png]]

De esta manera observamos cómo la conversión del 192 nos da como resultado en binario la representación del propio número con un total de 8 bits.

De tal manera que podríamos generar la representación completa de una IP en binario:

![[Conceptos básicos/images/002.png]]

## ¿Existe un límite total de IP's?

Es evidente y claro que si existe un límite, aunque es demasiado grande, este está sujeto a 32 bits en total en una dirección IP, por lo que entonces tendríamos un total de 2^32 combinaciones posibles:

![[Conceptos básicos/images/003.png]]

Como podremos observar el total de combinaciones existentes es de 4 mil millones y actualmente somos más de 8 mil millones de personas es en el mundo, por lo que es evidente que también nos estamos quedando eventualmente sin direcciones IPv4.

Para ello existe la implementación adicional de las *IPv6* las cuales ya contienen 128 bits y podremos ver que el total de posibles combinatorias es bastante superior:

![[Conceptos básicos/images/004.png]]

# Inicio

[[#Índice]]
# **Siguientes apuntes**

[[Direcciones MAC (OUI y NIC)]]

