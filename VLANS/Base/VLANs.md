
## Segmentacion logica de una VLAN en diferentes dominios de broadcast

Tipos: 

- Default: Si no hay configs de VLAN's, todos son VLAN 1
- Data: Trafico de datos de usuario, solo data
- Voice: Trafico de voz, mayor prioridad
- Management: Administra el switch, VLAN 1
- Native: Trafico no etiquetado en puerto troncal

## Tipos de coniguracion de puerto para la transmision de VLAN

- **Puerto de acceso**: Permite 1 sola VLAN
- **Puerto troncal**: Permite multiples VLAN's (Recomendado de aprox 50 vlans), permite el trafico de varias VLANS.


## Protocolo 802.1Q

- Agrega una etiqueta o tag a tramas de etehernet para identificacion
- Permite a multiples VLAN's compartir un enlace fisico

- **ETIQUETAR UNA TRAMA**:
	- Se etiqueta un switch al recibir un frame desde un punto de acceso antes de enviarlo por enlace troncal
	- La etiqueta contiene un VID que dice la VLAN  a la que pertenece