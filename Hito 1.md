# Informe del trabajo final

| Nombre y Apellido      | Código | Carrera |
| ---------------------- | ------ | ------- |
| Nombre    | UXXXXXXXX | Ingeniería de xxxxx|
| Pozo Campos, Rodrigo Jair | U20181E187 | Ingeniería de Software|
| Gamio Upiachihua, Brenda Lucía | U202120344 | Ingeniería de Software |

## 1. Descripción del problema

En el contexto del curso de complejidad algorítmica, se exploran temas que ofrecen soluciones a desafíos actuales. Estos desafíos incluyen cuestiones como la gestión vehicular y el estresante tráfico que ocurre alrededor del mundo. Los algoritmos aplicados resultan sorprendentemente prácticos y se encuentran presentes en nuestras actividades cotidianas a través de diversas aplicaciones. Es relevante destacar que uno de los más destacados es el algoritmo Dijkstra, cuyo propósito principal es "definir criterios para alcanzar metas específicas y construir un modelo con una jerarquía que tome en cuenta diversos factores o atributos para guiar la toma de decisiones" (Pavas, A. 2016). Este algoritmo desempeñará un papel central en nuestro proyecto. 

Un ejemplo representativo es la aplicación Waze, líder a nivel global, que se dedica a optimizar el tiempo y los recursos en los desplazamientos. Esta aplicación recomienda rutas alternativas basándose en la información recopilada de sus usuarios. En este contexto, es importante señalar lo que la Universidad de Georgetown afirma: "En la era digital actual, los algoritmos adquieren un rol cada vez más preponderante en los procesos tecnológicos y, por consiguiente, en nuestra vida cotidiana". En parte lo que nos comenta la Universidad de Georgetown es cierto ya que cada vez vivimos en un mundo que está estrechamente ligado con tecnologías de cualquier índole. 
 
Decidimos que será en esta ciudad ya que según Gizmodo, blog acerca de ciencia, tecnología y cultura digital menciona que: La ciudad de Washington DC es la segunda ciudad mejor planificada del mundo. Por lo que, esta ciudad conocida por su relevancia en la política y la cultura de los Estados Unidos, se convierte en el foco de nuestra investigación. 
  
Nuestro objetivo en el curso es desarrollar una aplicación similar a Waze, que se especialice en encontrar la ruta más eficiente entre dos puntos de una ciudad seleccionada. Esta se representa mediante un grafo el cual representa los detalles de la ciudad.
  
Para abordar esta problemática, utilizaremos conjuntos de datos (datasets) que incluyen "edges" (tramos de carretera), "nodes" (nodos de intersección y coordenadas) y "streets" (nombres de calles), en ese mismo orden. También elegimos esta ciudad ya que presenta distintas avenidas diagonales  con grandes intersecciones, tal como podemos ver en la **imagen** 1.
   
   <img src="https://cdn.discordapp.com/attachments/1155624463161896970/1155624467066790068/foto_aerea.jpg" alt="Imagen Aerea Washington DC">

**Imagen 1. Washington DC.** Recuperado de [https://aerialarchives.photoshelter.com/image/I0000xtaFsXx.VLU](https://aerialarchives.photoshelter.com/image/I0000xtaFsXx.VLU)





## 2. Descripción y vizualición del conjunto de datos
Para llevar a cabo este proyecto, adquirimos dos conjuntos de datos con el propósito de abordar la cuestión planteada en la introducción. Estos conjuntos de datos contienen un total de 178 167 registros, de las que usarán 1500 de estos de acuerdo con las indicaciones de la guía. Nuestra intención es utilizar esta información para construir una solución efectiva y eficiente mediante el uso de gráficos y varios algoritmos.
* Líneas centrales de la calle 2013 con 34 059 registros. De estos registros se podría sacar:
  
  - **Nodos.txt:**
  El presente archivo de texto contiene contiene los nodos que conformarán el grafo. Estos nodos poseen únicamente una columna, la cual hace referencia al “StreetSegid” en los registros.
  - **Bordes.txt:***
  Este archivo de texto contiene las aristas que conformarán el grafo. Estas aristas poseen únicamente una columna, la cual hace referencia al “Quadcode” en los registros.
  - **Calles.txt:**
  Este último archivo de texto contiene los nombres de cada una de las calles que contiene la zona elegida.

* Puntos de direcciones con 144 108 registros. De estos registros se podría sacar:
  
    - **Nodos.txt:**
  El presente archivo de texto contiene datos de referencia sobre los nodos que conformarán nuestro grafo en el futuro. Estos nodos representarán las intersecciones entre dos calles. El formato del archivo consta de cuatro columnas, donde las cuatro corresponden a las coordenadas geográficas precisas (Coordenada X, Coordenada Y, Latitud y Longitud).
  - **Bordes.txt:***
  Este archivo de texto contiene las aristas que conformarán el grafo. Estas aristas poseen únicamente una columna, la cual hace referencia al número de dirección. 
  - **Calles.txt:**
  Este último archivo de texto contiene los nombres de cada una de las calles que contiene la zona elegida.


## 3. Propuesta
Aquí iría la descripción

## 4. Bibliografía
<https://opendata.dc.gov/datasets/DCGIS::address-points/explore?location=38.890346%2C-77.017197%2C12.76&showTable=true>
<https://opendata.dc.gov/datasets/8655869366064bdca04bb6793cc02a54_3/explore?showTable=true>
