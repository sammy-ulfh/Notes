# Apuntes anteriores

[[Subnetting - CIDRs y cálculo total de hosts]]

# Indice

- [[#Cálculo de máscara de red, hosts, identificador de red y Broadcast]]
- [[#Cálculo de la máscara de red]]
- [[#Cálculo del total de hosts a repartir]]
- [[#Cálculo del Network ID]]
- [[#Cálculo de Broadcast address]]
- [[#Siguientes apuntes]]


## Cálculo de máscara de red, hosts, identificador de red y Broadcast

Para la dirección IP **192.168.1.0/26** cálcula su máscara de red, el número total de hosts a repartir, el identificador de red y la dirección Broadcast.
### Cálculo de la máscara de red

Para la IP **192.168.1.0/26**, tenemos un total de 26 bits ocupador por la red y los ultimos 6 pertenecen a los hosts.

Para calcular la máscara de red tenemos que colocar los primeros 26 bits en 1 y los 6 restantes en cero:

11111111.11111111.11111111.11000000

Cada octeto de la máscara se compone de 8 bits. El valor de cada octeto se determina convirtiendo los 8 bits a decimal. En este caso el valor completo de los primeros 3 octetos esta en 1, lo que quiere decir que en estos 3 el valor sera **255**, mientras que el ultimo octeto tiene los primeros dos bits en uno y el resto en cero.

#### Convertir el binario a decimal


| 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
Al tener la tabla anterior, tendríamos en consideracion el valor de cada bit, por lo tanto lo que haremos sera sumar de izquierda a derecha este valor, siempre y cuando el bit se encuentre en **1**.

| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 1   | 0   | 0   | 0   | 0   | 0   | 0   |

En este caso, con nuestro número binario tendríamos los primeros dos bits en **1**, por lo que tenemos **128 + 64** y esto nos da **192**.

Teniendo finalmente como nuestra máscara de red **255.255.255.192**

### Cálculo del total de hosts a repartir

En este caso, se utilizan los **6 bits** que quedan disponibles para representar la parte del **host**. En una máscara de red de 26 bits, los 6 bits restantes representan **2^6**, lo que nos da el total de direcciones IP posibles **2^6 = 64** pero todas no se ocupan para asignar hosts.

El calculo de los hosts que se pueden asignar se hace con **2^n - 2**, que en este caso es **2^6 - 2 = 62**. Esto se debe a que de los otros 2 restantes, uno sera utilizado para la dirección de la red (la primera dirección IP de la red -> **Network ID**) y el otro para el broadcast (la última dirección IP de la red).

### Cálculo del Network ID

Para calcular el **Network ID**, lo que debemos hacer es aplicar la máscara de red a la direccion IP. En este caso la máscara de red es **255.255.255.192**, lo que significa que los primeros **26** digitos de la IP pertenecen a la parte de la red.

Se tiene que convertir tanto la dirección IP como la máscara de red en binario y luego se hace una operacion **AND** lógica entre ambos. La operación AND compara el bit que se encuentre en la misma posicion y solo sera **1** cuando ambas posiciones esten en **1**.

En este caso, la dirección IP es **192.168.1.0** en decimal y en binario es **11000000.10101000.00000001.00000000**. La máscara de red es **255.255.255.192** en deciamal y se convierte a binario como **11111111.11111111.11111111.11000000**.

La forma de convertir decimal a binario es utilizando la tabla de los 8 bits con su potencia, donde se recorre la tabla de izquierda a derecha, si el numero que tenemos es mayor, le restamos esa posicion y la colocamos en 1, pasando a la siguiente.

Finalmente, aplicamos la operación AND entre los dos valores binarios bit a bit. Los bits correspondientes en ambos valores se comparan de la siguiente manera:

1 1 1 1 1 1 1 1 . 1 1 1 1 1 1 1 1 . 1 1 1 1 1 1 1 1 . 1 1 0 0 0 0 0 0    -   Máscara de red
1 1 0 0 0 0 0 0 . 1 0 1 0 1 0 0 0 . 0 0 0 0 0 0 0 1 . 0 0 0 0 0 0 0 0    -   Dirección IP

AND

1 1 0 0 0 0 0 0 . 1 0 1 0 1 0 0 0 . 0 0 0 0 0 0 0 1 . 0 0 0 0 0 0 0 0     - **Network ID (Primera dirección de red)**

En decimal: **192.168.1.0**
Este es el identificar único de la subred a la que pertenecen los hosts.

### Cálculo de Broadcast address

La **Broadcast address** es la dirección de red que se utiliza para enviar paquetes a **todos los hosts de la subred**.

Para calcularla, necesitamos saber el **Network ID** y la cantidad de hosts disponibles en la subred.

En el ejemplo que se esta trabajando ya se ha calculado el Network ID como **192.168.1.0**. La cantidad de hosts disponibles se calcula como **2^n - 2**, donde **n** es la cantidad de bits utilizados para representar la parte de host en la máscara de red. En este caso, **n** es 6, ya que hay 6 bits disponibles asignar hosts.

Para calcular la **Broadcast Address**, debemos asignar todos los bits de la parte del host de la dirección IP a **1**, en este caso la dirección IP es **192.168.1.0** y se convierte a binario como **11000000.10101000.00000001.00000000**.

Para encontrar la dirección Broadcast, llenamos con **1** la parte correspondiente a los bits de host, es decir, los últimos 6 bits.

**11000000.10101000.00000001.00111111**

Finalmente, convertimos cada octeto a decimal para tener nuestra IP en decimal y con esto tendremos la direccion de broadcast **192.168.1.63**.

Está es la dirección a la que se enviarán los paquetes para llegar a todos los hosts de subred.

De esta manera, al ralizar estos calculos con el IP que puedamos obtener para alguna auditoria, ya sabremos sobre que rango tendremos que movernos en una red para realizar nuestro escaneo.

## Siguientes apuntes

[[Subnetting – Interpretación de los rangos de red que el cliente nos ofrece para auditar]]

