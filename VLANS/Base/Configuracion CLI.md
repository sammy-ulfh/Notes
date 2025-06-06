
## VLAN's y Switch conf

- vlan ${ID}
- name ${nombre}
- int ${interface}
- switchport mode access || switchport mode trunk
- switchport access vlan ${ID}

## Protocolo 802.1Q router

- int ${interface}.\${IDVLAN}
- encapsulation dot1Q ${IDVLAN}
- ip address ${ip} ${mask}
- int ${interface}
- no shutdown

## Direccionamiento router

- **Estatico**
	- ip route ${ip destino} ${mark destino} ${ip del router al que va a saltar o por donde se tiene que ir}
- **Dinamico**
	- router rip
	- version 2
	- no auto-summary
	- network ${primera ip red}

## nombre

- host ${nombre}
## message of the day

- banner motd #${message}#

## Passwords

- Consola
	- line con 0
	- password ${password}
	- login
	- exit
- Enable
	- enable secret ${password}
	- exit
- Telnet
	- line vty 0 15
	- password ${password}
	- login
	- exit

## Entrar a una interfaz

- interface ${interfaz id}
- ip address ${ip} ${mask}
- no shutdown
