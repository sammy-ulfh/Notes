# Indice

- [[#Etiquetas para textos]]
	- [[#Encabezados]]
	- [[#Parrafos]]
	- [[#Salto de linea]]
	- [[#Salto de linea con division]]
	- [[#Resaltado en negritas]]
	- [[#Texto en cursiva]]
	- [[#Contenedor de texto]]
	- [[#Contenedor en formato de cita o con un tabulado especial]]
- [[#Siguientes apuntes]]

## Etiquetas para textos

Mucho del contenido que mostramos en una pagina web es practicamente texto. Es por ello que una de las cosas mas importantes son las etiquetas de utilicemos para textos en html. 

Lo que sucede es que con HTML construimos una maqueta basica de la información que queremos mostrar, mientras con otras tecnologias o lenguajes lo hacemos mas atractivo visualmente o incluso interactivo, que es donde entra el lenguaje de programacion javascript.

### Encabezados

Si bien lo vimos ya, los encabezados son una parte muy importante de nuestro etiquetado en HTML. Tenemos distintos niveles de ancabezado del 1 a el 6, donde el 1 es el mas importante y deberiamos tener solamente uno como el titulo de nuestra pagina, mientras que de los niveles del 2 al 6 si podriamos tener mas de uno.

```HTML
<h1></h1>
<h2></h2>
<h3></h3>
<h4></h4>
<h5></h5>
<h6></h6>
```

### Parrafos

En HTML podemos definir bloques de texto los cuales seran considerados parrafos con la etiqueta <\p>, lo cual veriamos de la siguiente manera:

```HTML
<p>
	Mi primer parrafo
</p>
```

Si esto lo colocamos dentro de nuestro body de la pagina que hemos estado construyendo, después de nuestros encabezados, en la pagina lo veriamos de la siguiente manera:

![[IMG_007.png]]

Y si copeamos la misma etiqueta con este contenido y la pegamos debajo de la misma, nos quedaria en un parrafo distinto:

![[IMG_008.png]]

Nuestro body hasta ahora lo tendremos de esta forma:

```HTML
<body>
	<h1>Titulo de mi web</h1>
	<h2>Bienvenidos a mi web</h2>

	<p>
		Mi primer parrafo
	</p>

	<p>
		Mi primer parrafo
	</p>
</body>
```

Existe una página, la cual es [Lorem Ipsum]([Lorem Ipsum - All the facts - Lipsum generator](https://www.lipsum.com/)), de ella podremos generar parrafos de ejemplo y colocarlo en cada una de las etiquetas de parrafo para ver como se verian:

![[IMG_009.png]]

### Salto de linea

Con html podremos agregar dentro de los párrafos, entre texto o incluso entre elementos, saltos de linea. Esto nos ayuda a mapear de forma distinta, con un salto de linea la información o texto a mostrar. 

La etiqueta que nos ayuda a realizar esto es <\br/>, esta etiqueta, al no tener contenido, no necesita tener una de apertura y una de cierre, por lo que con colocarla tal cual como esta representada nos funcionaria. En este caso dentro de nuestro parrado, podriamos colocarla justo después de un punto, para que asi aplique un salto de linea y lo veamos en nuestra pagina.

```HTML
<p>
	Esta es mi primera web. <br/>De verdad estoy muy feliz.
</p>
```

Con el ejemplo donde anteriormente ya tenemos un párrafo, al colocarlo lo veríamos de esta forma:

![[IMG_010.png]]

![[IMG_011.png]]

Esta etiqueta podremos utilizarla las veces que nosotros consideremos y si la utolozamos mas de una vez, se mostraran mas de un salto de linea.

### Salto de linea con division

Podremos realizar un salto de linea, dibujando una linea horizontal como si de una division se tratase. Para lograr esto se utilizaria la etiqueta <\hr/> y se utiliza de la misma forma que <\br> al no llevar contenido.

![[IMG_012.png]]

De la misma forma que con el salto de línea tradicional, podremos utilizar mas de uno, con la diferencia de que en cada salto de linea dibujara una linea. 

Con esto en mente, en nuestro código ahora podriamos quitar este tipo de salto de linea y colocarlo después de nuestros parrafos a forma de separados, para después agregar un nuevo encabezado de valor 3:

![[IMG_013.png]]

![[IMG_014.png]]

### Resaltado en negritas

Como ya vimos anteriormente, la etiqueta <\strong> nos permite que el texto que tenga como contenido se vea de forma resaltada; es por ello, que esto podremos probarlo en el parrafo después de nuestro tercer encabezado:

```HTML
<strong>Nullam ut tristique lectus. Nulla mollis in sapien non efficitur.</strong>
```

![[IMG_015.png]]

### Texto en cursiva

Similar a strong, se puede utilizar <\em> o <\i>, la diferencia es que esta etiqueta en lugar de mostrar su contenido en negritas, lo que hace es mostrar su contenido en cursivas:

```HTML
<em>Nulla porttitor libero vel fringilla commodo</em>
<i>Nulla porttitor libero vel fringilla commodo</i>
```

![[IMG_016.png]]

Recordemos que todas aquellas etiquetas que tengan contenido dentro, ocuparan de apertura y cierre. De no ser asi, podrian tener unicamente su apertura, colocando al final un '/' como su propio cierre dentro de la apertura.

### Contenedor de texto

Como ya mencionamos, CSS nos ayuda a estilar nuestra pagina para mejorarla visualmente. Es por ello que existe una forma de realizar pequenos contenedores de texto lo cuales no tienen ninguna accion sobre el texto, pero permiten colocar un identificador o mediante el atributo "class" colocar nombre de clases definidas mediante CSS para una mejora visual.

Para ello se utiliza la etiqueta <\span>.

```HTML
<span id="texto" class="rojo negritas">Mi texto online</span>
```

El id es un identificador unico de este elemento que encierra a su contenido "Mi texto online" para poder hacer referencia hacia el, ademas de que __class__ permite agregar nombres colocados a una serie de instrucciones de estilos. Por ejemplo, yo creo mi clase a la cual nombro "rojo", dentro de esta defino que mi texto se muestre color rojo.

Cuando asigne este nombre de clase mediante el atributo __class__, hare que el texto que contiene esta etiqueta <\span>, se muestre de color rojo, ya que fue el comportamiento indicado y se lo estoy otrogando a este bloque.

### Contenedor en formato de cita o con un tabulado especial

La etiqueta <\blockquote> nos ayuda a que el texto que esté dentro de la misma se muestre en un formato tipo cita, donde se muestra con una tabulacion especial y el formato se da a notar automaticamente.

```HTML
<blockquote>
Este es mi texto en un <strong>formato muy lindo</strong>.<em>Recomendado!</em>
</blockquote>
```

Si agregamos lo anterior a nuestro codigo actual o modificamos lo que tenemos, veremos como se notara este formato facilmente:

![[IMG_017.png]]

## Siguientes apuntes

[[]]