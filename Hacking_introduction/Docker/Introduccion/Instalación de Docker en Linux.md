# Índice

- [[#Introducción]]
- [[#Práctica]]
- [[#Siguientes apuntes]]
# Introducción

Instalar docker en linux:

- **Arch Linux:** `sudo pacman -S docker`
- **Debian Based:** `sudo apt install docker.io`

Esto nos instalará el paquete de Docker desde el repositorio de paquetes del sistema operativo. Es importante mencionar que, dependiendo de la distribución que se esté utilizando este comando para instalarlo, va a cambiar. 

Una vez que Docker haya sido instalado, tendremos que inicializar el servicio, ya que Docker corre como demonio en el sistema.
# Práctica

Cuando tengamos Docker instalado en el sistema, no podremos utilizarlo directamente. Esto se debe a que Docker corre como servicio en segundo plano en el sistema, por ende tendríamos que inicializarlo. Esto podremos hacerlo con **systemctl**:

```shell
sudo systemctl start docker
```

Esto nos iniciará el demonio de Docker y finalmente nos permitirá empezar a utilizarlo:

![[Docker/Introduccion/images/001.png]]

- **docker ps** nos permite verificar si se encuentra algún contenedor que hayamos desplegado corriendo.
- **docker images** nos permite verificar si tenemos alguna imagen construida de algún contenedor que se encuentre lista para correrla.

Como funciona con Docker es que todas las instrucciones a considerar dentro del contenedor van en un **Dockerfile** y después este archivo se construye como imagen para finalmente ejecutarse como servicio de Docker.

# Siguientes apuntes

[[Definiendo la estructura básica de Dockerfile]]