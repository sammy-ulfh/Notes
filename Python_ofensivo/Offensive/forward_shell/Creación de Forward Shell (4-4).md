# Práctica

Si buscamos imprimir ahora el comando, es importante considerar que nuestro comando llegará hasta un elemento antes del último y comenzará a partir del tercer elemento. Esto se debe a que el primero será una cadena vacía **''**, mientras que el segundo será el propio comando que ejecutamos, por lo tanto, el tercero será donde inicie nuestro comando. 

Con ello en mente, tomaremos a partir del tercer elemento hasta el penúltimo, lo cual lo haríamos con **\[2:-1]**:

![[058.PNG]]

Con ello, ahora ya lo tendríamos totalmente funcional:

![[059.PNG]]

Bastaríamos con eliminar el print que nos muestra la lista para observar que concuerde correctamente y que sí estemos tomando todos los elementos del output del comando ejecutado. Como aquí no estamos colocando la traza de la pseudo terminal, podríamos colocarlo antes de cada comando, copiando el primero de cuando se inicia la pseudo terminal o colocándolo en la misma lista para el **join**:

![[060.PNG]]

Ya por último, para nuestra Shell, podríamos agregar que cuando nos encontremos en una pseudo terminal y escribamos el comando **exit**, nos cambie a **False** el contenido del atributo **is_pseudo_terminal** y además de evitar que se imprima el output del comando y en su lugar mostrar un mensaje como que se ha salido de la pseudo terminal. 

De esta manera, realmente ya lo tendremos e incluso podríamos agregar cosas, como una enumeración de archivos buscando aquellos que tengan permisos especiales como el SUID, lo cual podremos hacer enviando un comando ```find / -perm -4000 2>/dev/null | xargs ls -l``` 

Esto ya lo podremos gestionar en nuestra Shell para que el usuario pueda efectuar esto únicamente utilizando un comando dado por nosotros, tal como **enum suid**, con lo cual ya tendríamos la posibilidad de incluso crear un C&C dentro de nuestra misma Forward Shell.

# Fin de las notas ;D