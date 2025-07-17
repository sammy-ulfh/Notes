
# Apuntes anteriores

- [[Modelo OSI]]

# Indice

- [[#¿Qué es y cómo se interpreta una máscara de red?]]

## ¿Qué es y cómo se interpreta una máscara de red?

**Subnetting** es una técnica utilizada para dividir una red IP en subredes más pequeñas y manejables. Esto se logra mediante el uso de *máscaras de red* que permiten definir qué bits de la dirección IP corresponden a la *red* y cúales a los hosts.

Para interpretar una máscara de red, se deben identificar los bits que están en "1". Estos bits representan la porción de la dirección IP que corresponde a la red. Por ejemplo, una máscara de red de **255.255.255.0** indica que los primeros tres octetos de la dirección IP corresponden a la red, mientras que el último octeto de utiliza para identificar los hosts.

Ahora bien, cuando hablamos de **CIDR** (acrónimo de **Classless Inter-Domain Routing**), a lo que nos referimos es a un método de asignación de direcciones IP más eficiente y flexible que el uso de clases de redes IP fijas. Con **CIDR** una dirección IP se representa mediante una dirección IP base y una máscara de red, que se escriben juntas, separadas por una barra **/**.

Por ejemplo, la dirección IP **192.168.1.1** con una máscara de red **255.255.255.0** se escribiría como **192.168.1.1/24**.

La máscara de red se representa en notación de prefijo, que indica el número de bits que estan en "1" en la máscara. En este caso, la máscara de red **255.255.255.0** tiene **24** bits en "1" (los primeros tres octetos), por lo que su notación en prefijo es **/24**.

Para calcular la máscara de red a partir de una notación de prefijo, se deben escribir los bits "1" en los primeros bits de una dirección IP de 32 bits y los bits "0", en los bits restantes. Por ejemplo, la máscara de red **/24** se calcularía como **11111111.11111111.11111111.00000000** en binario, lo que equivale a **255.255.255.0** en decimal.

## Cómo se considera la máscara?

Para la máscara podremos verlo se la siguiente manera:


| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |

Podremos considerar lo anterior cómo todos los bits de un octeto en una IP, por lo tanto al tener todo esto, realmente seria como tener el **255** en uno de los octetos.

Esto lo podremos ver si lo calculamos de forma que multipliquemos el valor superior por el inferior y sumemos todos los resultados, considerando que nuestro valor inferior (bit) puede ser 0 o 1.

De esta manera, la suma de:
**(128x1) + (64x1) + (32x1) + (16x1) + (8x1) + (4x1) + (2x1) + (1x1) = 255**

Con esto en mente, sabemos que en una IP tenemos un total de 4 octetos y podremos visualizar la IP que hemos considerado hasta ahora en un excel con este principio:

![[Conceptos básicos/images/014.png]]

Ahora podremos contemplar el **CIDR** el cual es un estandar de red para interpretar direcciones IP, asi como consideraremos un total de host, para en funcion de la mascara de red asignada saber cuantos host se pueden configurar o estar existentes.

Esto basicamente seria contar todos aquellos espacios en los cuales el bit representado sea 1, por lo que en este caso tendriamos:

**255.255.255.0/24**

## Siguientes apuntes

[[Subnetting - CIDRs y cálculo total de hosts]]
