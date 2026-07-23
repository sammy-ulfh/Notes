## Práctica

El decoder nos sirve para decodificar textos que estén codificados; por ejemplo, si utilizamos el texto URL encodeado, Burp Suite nos permitirá seleccionar este tipo de codificación para decodificarlo en esta herramienta y ver cómo realmente es el texto:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/028.png]]

Lo mismo aplica para mensajes codificados, por ejemplo, en base 64:

```shell
echo "Hola mundo, soy hacker" | base64
> SG9sYSBtdW5kbywgc295IGhhY2tlcgo=
```

Si esto lo ponemos en nuestro decoder y seleccionamos base64, veremos cómo nos da el mensaje que codificamos:

![[Conceptos básicos de enumeración y explotación/Burpsuite/images/029.png]]

- [[Intruder]]
