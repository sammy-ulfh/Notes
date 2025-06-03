
# Apuntes anteriores

- [[Subnetting - Introduccion]]

# Indice

- [[#Máscaras de red]]
- [[#Máscaras de red personalizadas]]
- [[#Ejemplos prácticos]]
- [[#Siguientes apuntes]]

## Máscaras de red

En cuanto a las IP, existen tres tipos de máscara de red: **CLASE A, CLASE B y CLASE C**

- Las redes de **clase A** utilizan una máscara de subred predeterminada de 255.0.0.0 y su primer octeto esta entre 0-127. La dirección **10.52.36.11**, por ejemplo, es una dirección **Clase A**, su primer octeto está entre 1 y 126.
- Las redes **Clase B**, utilizan una máscara de subred predeterminada de 255.255.0.0 y sus primer octeto esta entre 128-191. La dirección **172.16.52.63**, por ejemplo, es una dirección **Clase B**. Su primer octeto es 172, que está entre 128-191.
- Las redes de **Clase C** usan una máscara de subred predeterminada de 255.255.255.0 y tienen de 192-223 como su primer octeto. La dirección **192.168.123.132**, por ejemplo, es una dirección de **Clase C**. Su primer octeto es 192, que está entre 192-223.

## Máscaras de red personalizadas

Es importante tener en cuenta que, además de estos tres tipos de máscaras de red también existen **máscaras de red personalizadas** que se pueden utilizar para crear subredes de diferentes tamaños dentro de una red.

Como ya lo consideramos, **CIDRs (ClassLess Inter-Domain Routing)**, se trata de un método de asignación de direcciones IP que permite dividir una dirección IP en una parte que identifica la red y otra parte que identifica el host. Esto se logra mediante el uso de una máscara de red, que se presenta en notación **CIDR** como una dirección IP base seguida de un número que indica la cantidad de bits que corresponden a la red.

Con **CIDR**, se pueden asignar direcciónes IP de forma más precisa, lo que reduce la cantidad de direcciones IP desperdiciadas y facilita la administración de la red.

El número que sigue a la dirección IP base en notación CIDR se llama *prefijo* o *lonjitud de prefijo*, y representa el número de bits en la máscara de red que esta en "1".

Por ejemplo, una dirección IP con prefijo de **/24** indica que los primeros 24 bits de la dirección IP corresponden a la red, mientras que los 8 bits restantes se utilizan para identificar los hosts.

Para calcular la cantidad de hosts disponibles en una red CIDR, se deben de contar el numero de bits "0" en la máscara de red y elevar **2 a la potencia** de ese número. Esto se debe a que cada bit "0" en la máscara de red representa un bit que se puede utilizar para identificar un host.

Por ejemplo, una máscara de red **255.255.255.0 (/24)**, tiene 8 bits en "0", lo que significa que hay 2^8 = 256 direcciones IP disponibles para los hosts en esa red.

## Ejemplos prácticos

- Una dirección IP con un prefijo de **/28** (255.255.255.240), esto nos deja 4 bits en "0", por lo que permite hasta **16 direcciónes IP** para los hosts (2^4), ya que los primeros 28 bits corresponden a la red.
- Una dirección IP con un prefijo de **/26** (255.255.255.192) permite hasta 64 direcciones IP para los hosts (**2^6**), ya que los primeros 26 bits corresponden a la red.
- Una dirección IP con prefijo de **/22** (255.255.252.0) permite hasta 1024 direcciones IP para los hosts (2^10), ya que los primeros 22 bits corresponden a la red.

## Siguientes apuntes

[[Subnetting – Máscaras de subred, tipos de clase e interpretación de prefijos de red]]