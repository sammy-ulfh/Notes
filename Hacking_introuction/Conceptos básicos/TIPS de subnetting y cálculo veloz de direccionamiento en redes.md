# Apuntes anteriores

[[Subnetting – Interpretación de los rangos de red que el cliente nos ofrece para auditar]]

# Indice

- [[#Cálculo aritmetico]]
- [[#Apoyo]]
- [[#Ejercicios]]

## Cálculo aritmetico

Como todo lo anterior, ahora realizaremos estos cálculos de forma aritmética para encontrar el Network ID, Broadcast Address y la Network Mask.

Para ello, tenemos la IP:

**172.14.15.16/17**

Primero convertiremos la IP a binario, para ello podremos utilizar **obase** en linux:

```shell
echo "obase=2;numero" | bc
```

![[016.png]]

De esta forma transformamos cada uno de los octetos:

**1 0 1 0 1 1 0 0 . 0 0 0 0 1 1 1 0 . 0 0 0 0 1 1 1 1 . 0 0 0 1 0 0 0 0** (172.14.15.16)

Para la Network Mask, sabemos que al tener el CIDR de **/17**, los primeros 17 bits pertenecen a la red y el resto para hosts, por lo tanto llenaremos de **1** de izquierda a derecha hasta cubrir estos 17 bits:

**1 1 1 1 1 1 1 1 .  1 1 1 1 1 1 1 1 . 1 0 0 0 0 0 0 0 . 0 0 0 0 0 0 0 0**

Esto ya seria nueestra Network Mask, para saber que numero contiene cada octeto ahora podriamos utilizar **obase** para pasarle como input nuestro numero binario y nos retorne el decimal:

```shell
echo "ibase=2;11111111" | bc
```

![[017.png]]

Por lo tanto, nuestra mascara de red es **255.255.128.0**

Lo siguiente es aplicar el AND, colocando **1** cuando ambos esten en 1:

**1 0 1 0 1 1 0 0 . 0 0 0 0 1 1 1 0 . 0 0 0 0 1 1 1 1 . 0 0 0 1 0 0 0 0** (172.14.15.16)
**1 1 1 1 1 1 1 1 .  1 1 1 1 1 1 1 1 . 1 0 0 0 0 0 0 0 . 0 0 0 0 0 0 0 0** (255.255.128.0)

**1 0 1 0 1 1 0 0 . 0 0 0 0 1 1 1 0 . 0 0 0 0 0 0 0 0 . 0 0 0 0 0 0 0 0** (172.14.0.0 - Network ID)

Ahora, para calcular nuestra Broadcast Address, cambiarmos todos los bits correspondientes a hosts a 1, que en este caso seria restarle los bits de red a 32 (32 - 17 = 15)

Por lo tanto, los ultimos 15 bits de la network ID los cambiariamos a 1:

**1 0 1 0 1 1 0 0 . 0 0 0 0 1 1 1 0 . 0 1 1 1 1 1 1 1 . 1 1 1 1 1 1 1 1** (172.14.127.255 - Broadcast Address)

## Apoyo

La siguiente pagina te ayudara a comprobar los calculos: [IPCALCULATOR](https://blog.jodies.de/ipcalc)

## Ejercicios


| IP                | Net-Mask | Net-ID | Broadcast |
| ----------------- | -------- | ------ | --------- |
| 192.112.114.29/13 |          |        |           |
| 13.51.47.131/4    |          |        |           |
| 13.51.47.131/15   |          |        |           |
| 10.18.51.23/23    |          |        |           |

NOTA:

La dirección IP **13.51.47.131/4** es un caso especial, se puede considerar un error tipográfico o una confusión en la notación. Esto se debe a que una máscara de subred **/4** es inusual en la práctica y no se ajusta a las asignaciones rales de direcciones IP.

La máscara de subred generalmente tiene un valor entre **/8** y **/32**. El caso puntual que hemos representado no se ajusta a las asignaciones de direcciones IP en la vida real, por lo tanto obtenemos estos resultados.