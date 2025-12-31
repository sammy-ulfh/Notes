# Índice

# Introducción

Un [__payload__](https://keepcoding.io/blog/que-es-un-payload/) es un bloque de código malicioso, el cual busca explotar alguna vulnerabilidad en la máquina víctima.

Tipos de payloads:

- __Staged__: Es un tipo de payload que se __divide en dos o más etapas__. La primera etapa es una pequeña parte del código que se envía al objetivo, cuyo propósito es establecer una conexión segura entre el atacante y la máquina objetivo. Una vez que se establece la conexión, el atacante envía la segunda etapa del payload, que es la carga útil real del ataque. Este enfoque permite a los atacantes sortear medidas de seguridad adicionales, ya que la carga útil real no se envía hasta que se establece una conexión segura.
- __Non-staged__: Es un tipo de payload que se envía como __una sola entidad__ y __no se divide en múltiples etapas__. La carga útil completa se envía al objetivo en un solo paquete y se ejecuta inmediatamente después de ser recibida. Este enfoque es más simple que el Payload Staged, pero también es más fácil de detectar por los sistemas de seguridad, ya que se envía todo el código malicioso de una sola vez.

Es importante tener en cuenta que el tipo de payload utilizado en un ataque dependerá del objetivo y de las medidas de seguridad implementadas. En general, los payloads staged son más difíciles de detectar y son preferidos por los atacantes, mientras que los payloads non-staged son más fáciles de implementar, pero también son más fáciles de detectar.

# Practica
