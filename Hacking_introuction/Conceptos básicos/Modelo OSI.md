
# Apuntes anteriores
[[Protocolos comunes (UDP, TCP) y el famoso Three-Way Handshake]]

# Indice

[[#¿En qué consiste y cómo se estructura la actividad de red en capas?]]
## **¿En qué consiste y cómo se estructura la actividad de red en capas?**

En redes de ordenadores, el modelo OSI (Open Systems Interconnection) es una estructura de 7 capas que se utiliza para describir el proceso de comunicación entre dispositivos. Cada capa proporciona servicios y funciones específicas que permiten a los dispositivos comunicarse a través de una red.

**Las 7 capas del modelo OSI:**

![[013.png]]

1. **Capa Fisica:**
	Es la capa más baja del modelo OSI, que se encarga de la transmisión de datos a través del medio físico de la red como cables de cobre o fíbra optica.
2. **Capa de Enlace de datos:**
	Esta capa se encarga de la transferencia confiable de datos entre dispositivos de la misma red. También proporciona funciones para la detección y corrección de los errores de datos transmitidos. 
3. **Capa de Red:**
	La capa de red se encarga del enrutamiento de paquetes de datos a través de múltiples redes. Esta capa direcciones lógicas, como direcciones IP, para identificar dispositivos y rutas de red.
4. **Capa de Transporte:**
	La capa de transporte se encarga de la entrega confiable de datos entre dispositivos finales, proporcionando servicios como el control de flujo y la corrección de errores.
5. **Capa de Sesión:**
	Esta capa se encarga de establecer y mantener las sesiones de comunicación entre dispositivos. También proporcionan servicios de gestión de sesiones como la autenticación y la autorización.
6. **Capa de Presentación:**
	La capa de presentación se encarga de la representación de datos, proporcionando funciones como la codificación y decodificación de datos, la compresión y el cifrado.
7. **Capa de Aplicación:**
	La capa de aplicación proporciona servicios para aplicaciones de usuario finales, como correo electrónico, navegadores web y transferencia de archivos.

Comprender la estructura del modelo OSI es esencial para cualquier analista de seguridad, ya que permite tener una visión completa del funcionamiento de la red y las posibles vulnerabilidades que puedan existir en cada una de las capas.

Esto nos permite identificar de manera efectiva los puntos débiles de una red y aplicar medidas de seguridad adecuadas para protegerla de posibles ataques.

## **Siguientes apuntes**

[[Subnetting]]
