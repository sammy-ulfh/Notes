#### Adicional: Instalacion Python2

Para instalarlo tendremos que agregar a **\/etc\/apt\/sources.list** el repositirio de debian:

```
deb http://deb.debian.org/debian buster main
```

Actualizamos e instalamos python2.

Ahora, para el problema de las librerías, al no tener pip2, tendremos que instalar primeramente pip2. Para ello ejecutamos lo siguiente para cada usuario:

```
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
python2 get-pip.py
```

Esto nos almacenara pip en una ruta similar a **'\/home\/user\/.local\/bin'** y tendremos que agregarla al PATH, con lo cual ya tendriamos pip2.

Con esto solo instalamos las librerias requeridas para el script.