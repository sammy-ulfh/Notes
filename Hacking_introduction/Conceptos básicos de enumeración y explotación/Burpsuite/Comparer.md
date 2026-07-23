## Práctica

Para el comparer, podríamos irnos a nuestro target y del site map buscar dos peticiones distintas.

Un ejemplo sería el del **index.php** y el del **login.php**. Seleccionamos primero una, le damos clic derecho y la enviamos al comprarer; hacemos lo mismo con la segunda.

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/041.png]]

En el comparer lo veremos de la siguiente manera:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/042.png]]

Esto nos permite, en la parte inferior, hacer una comparativa, ya sea por **bytes** o por **words**. En este caso haremos la comparación por palabras (words) y veremos lo siguiente.

![[043.png]]

En este caso, las diferencias entre peticiones se marcan en colores:

- Azul: Para valores que hayan sido modificados entre una petición u otra.
- Rojo: Valores que hayan sido eliminados de una petición a otra.
- Verde: Valores nuevos que hayan sido agregados entre una petición u otra.
### Extensions

- [[Extensions]]