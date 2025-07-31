# Índice

# Introducción

El tiempo de vida (**TLL**) hace referencia a la cantidad de tiempo o **saltos** que se ha establecido que un paquete debe de existir dentro de una red antes de ser descartado por un enrutador. El TLL también se utiliza en otros contextos, como el almacenamiento en caché de CDN y el almacenamiento en caché de DNS. 

Cuando se crea un paquete de información y se envía a través de internet, está el riesgo de que siga pasando de enrutador a enrutador indefinidamente. Para mitigar esta posibilidad, los paquetes se diseñan con una caducidad denominada **tiempo de vida** o **límite de saltos**. El TLL de los paquetes también puede ser útil para determinar cuánto tiempo ha estado en circulación un paquete determinado, y permite que el remitente pueda recibir información sobre la trayectoria de un paquete a través de internet.

Cada paquete tiene un lugar en el que se almacena un valor numérico que determina cuánto tiempo debe seguir moviéndose en la red. Cada vez que un enrutador recibe un paquete, resta uno al recuento del TLL y lo pasa al siguiente lugar de la red. Si en algún momento el recuento del TLL llega a cero después de la resta, el enrutador descartará el paquete y enviará un mensaje ICMP al host de origen. 

¿Qué tiene que ver esto con la identificación del sistema operativo? En diferentes sistemas operativos tienen diferentes valores predeterminados de TTL. Por ejemplo, en sistemas operativos Windows, el valor predeterminado de TTL es 128, mientras que en sistemas operativos Linux es 64.

Por ende, si enviamos un paquete a una máquina y recibimos una respuesta con un valor de TLL de **128**, es probable que la máquina esté ejecutando **Windows**. Si recibimos una respuesta con un valor de TTL de **64**, es más probable que la máquina esté ejecutando Linux. 

Este método **no es infalible** y puede ser engañado por los administradores de red, pero puede ser útil en ciertas situaciones para identificar el sistema operativo de una máquina.

Enlaces a utilizar:

- [Subinsb - Web con valores de TTL](https://subinsb.com/default-device-ttl-values/)
# Práctica

Cuando nosotros lanzamos un ping a una máquina le estamos enviando un paquete y en la respuesta nosotros recibiremos el TTL de la misma. 

Si le enviamos un ping a nuestra propia máquina Linux, veremos lo siguiente:

![[Reconocimiento/OS/images/001.png]]

Aquí veremos el valor del TTL y entonces podemos asumir que es una máquina Linux. En este caso, si es así. 

Si nosotros revisamos la web, veremos que existen diversos valores de TTL para distintos sistemas operativos, pero desde luego lo más común sería llegar a visualizar entre Linux y Windows.

Estos valores no son siempre exactos, por lo que podrán llegar a verse ligeramente distintos o incluso se pueden llegar a modificar, por lo cual no es un indicador 100% claro del sistema, pero sin que haya sido modificado, podremos intuir ante qué máquina nos enfrentamos.
# Siguientes apuntes

[[]]