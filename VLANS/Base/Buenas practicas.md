
- Asignacion de puerto de VLAN:
	-  Asignar ID's unicos a cada VLAN, evitando la 0 y 1 que se utilizan para administracion.
	
- VLAN 1 predeterminada para administracion y apagar los puertos no utilizados:
	-  Todos los puertos deben estar asignados a una o mas VLAN's
	- Separar el trafico de usuarios y administradores al usar la VLAN 1 para administrar (asignar IP a administrador)
	- Comunicacion con switch (debe tener ip configurada desde la VLAN de admin - VLAN1)
- Seguridad de VLAN's
	- Implementar ACL para restringir trafico entre VLAN's (de la 10 a la 20)
	- Seguridad de puertos, restringiendo el acceso a MAC address relevantes
- Mantener al minimo las VLAN's
	- Evitar redes redundantes
	- Optimizar las redes lo mejor posible
- Crear VLAN sin salida para los puertos no utilizados:
	- Aisla los puertos que no se utilicen del resto de VLAN's
- Telefonos IP's en una VLAN:
	- Utilizar una VLAN independiente para el trafico de voz y datos de telefonia (por ancho de banda)
- Routing entre VLAN's
	En caso de utilizar routing entre VLAN's resringir el trafico  mediante listas de control de acceso (ACL)