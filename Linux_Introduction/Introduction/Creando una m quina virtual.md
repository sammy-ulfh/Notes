
## **Creación**

Para instalar otro sistema operativo tendríamos dos alternativas, una de ellas sería eliminar nuestro sistema actual e instalar nativamente Linux. Otra y la más recomendada sería instalar otro sistema dentro de nuestro sistema principal, lo cual es posible mediante virtualización.  

Para empezar con nuestra máquina virtual, en este caso se estará utilizando [VMWARE](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware+Workstation+Pro) (link de descarga directo), pero se puede utilizar cualquier aplicación que nos permita virtualizar un sistema.

![[6.PNG]]

Siendo lo anterior nuestra ventana principal al ejecutar VMware y tendremos que crear una nueva máquina virtual:

![[7.PNG]]

Seleccionaremos la recomendada y después solicitará un tipo de instalación, para ello le daremos a seleccionar nuestra imagen ISO y buscaremos entre las carpetas la que hemos descargado para instalar el sistema:

![[8.PNG]]

Como siguiente paso darle a continuar, seleccionaremos que estaremos instalando un Ubuntu de 64 bits, para que no tengamos ningún problema de configuración.

![[9.PNG]]

Como siguiente paso, veremos donde se almacenara la máquina virtual e incluso podremos modificar su PATH. Además de poder cambiar el nombre.

Es importante mencionar que si llegamos a borrar la máquina virtual de VMware, también tendremos que eliminarla, el directorio que se crea al crear la máquina, ya que este no se elimina directamente.

En este caso le nombraré a la VM **My parrot VM**:

![[11.PNG]]


Ahora tendremos que asignarle un espacio de disco virtual. Algo recomendado para que no de ningún problema es asignarle 80 GB, ya que es muy difícil de realmente acabarte el ese total de espacio.

Además, seleccionaremos que se guarde el disco virtual en un solo archivo:

![[12.PNG]]

## **Configuración**

Como pasos finales, podremos configurar la máquina virtual para asignarle ram y una configuración específica de red:

![[14.PNG]]

Para la memoria RAM lo mínimo recomendado serían 5 GB. Podríamos aumentarlo si lo consideramos bueno y siempre y cuando no afecte al rendimiento de nuestro ordenador en general.

Los procesadores también podremos configurarlos, podríamos asignar varios procesadores y el doble para core processors. En este caso, al mover la configuración, automáticamente nos mencionará si la que estamos colocando no sería buena considerando las capacidades de nuestro ordenador:

![[15.PNG]]

Finalmente, el apartado de network está seleccionado en NAT, eso quiere decir que tomaría por defecto la IP del propio ordenador.

![[16.PNG]]
  
La opción recomendada es configurarlo en el apartado BRIDGED y replicar la conexión del host. Esto hará que se tome nuestra VM como un dispositivo aislado dentro de nuestra red local, lo cual dará más seguridad al asignarle una IP propia y privada.

![[17.PNG]]

Ahora, por verificación:

- Nos iremos a **USB Controller** y nos aseguraremos de que se encuentre en USB 3.0 o mayor, agregando la posibilidad del reconocimiento de USB dentro de nuestra VM.

	![[18.PNG]]

- Nos iremos al apartado **Display** y nos aseguraremos de que este tenga la aceleración 3D activada.

	![[19.PNG]]
Finalmente, le damos a **close** y finalizamos la configuración.

## **Ejecución**

Finalmente, nos cargará nuestra máquina virtual y bastará con darle a encender la máquina virtual.

![[20.PNG]]

![[21.PNG]]

Nos saldrá un menú similar al anterior y tendremos que darle a **try/install**.

![[22.PNG]]

Con esto ya estaremos dentro del sistema, solo faltará seguir los pasos del instalador...

## **Siguientes apuntes**

[[System_installation]]