<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/f/fc/UPC_logo_transparente.png" alt="Logo UPC">


# Universidad Peruana de Ciencias Aplicadas

Ingeniería de Software

Ciclo 2023-02

<hr>

# <center>Complejidad Algoritmica</center>

## TP REPORT

**Sección:** WX73

**Profesor**: Luis Martin Canaval Sanchez

**Producto**: AutoGo

### Team Members:

| Member                            |    Code    |
| :-------------------------------- | :--------: |
| Rojas Ccama, Carlos Andres        | U202114657 |
| Pozo Campos, Rodrigo Jair         | U20181E187 |
| Gamio Upiachihua, Brenda Lucía    | U202120344 |


<br>
<br>


Agosto del 2023

</div>

# Contenido

## Tabla de Contenidos

### [Contenido](#contenido)

### [Student Outcome](#student-outcome-1)

### [Hito I: Descripción del problema ](#1-descripción-del-problema)

### [Hito II: Descripción y vizualición del conjunto de datos ](#2-descripción-y-vizualición-del-conjunto-de-datos)

### [Hito III: Propuesta ](#3-propuesta)

### [Hito IV: Diseño del Aplicativo](#4-diseño-del-aplicativo)


## Student Outcome

**ABET - EAC - Student Outcome 4**

**Criterio:** La capacidad de reconocer responsabilidades éticas y profesionales en situaciones de ingeniería y hacer juicios informados, que deben considerar el impacto de las soluciones de ingeniería en contextos globales, económicos, ambientales y sociales.

En el siguiente cuadro se describen las acciones realizadas y enunciados de conclusiones por parte del grupo, que permiten sustentar el haber alcanzado el logro del ABET - EAC - Student Outcome 4.

|                              Criterio específico                            |             Acciones realizadas             |                             Conclusiones                                     |   
| :-------------------------------------------------------------------------- | ------------------------------------------- |-----------------------------------------------------------------------------:|
| Demuestra ética profesional en el ejercicio de la ingeniería de software. | Carlos Rojas Ccama, Propuesta<br><br>Rodrigo Pozo Campos, Descripción del problema<br><br>Brenda Gamio Upiachihua, Descripción y visualización del conjunto de datos. | La colaboración en equipo, guiada por prácticas de desarrollo Agile, fue fundamental para fortalecer nuestra cohesión como grupo. La metodología Agile, junto con nuestra colaboración, desempeñó un papel crucial en nuestro logro. Descubrimos la relevancia de trabajar juntos de manera ágil en el ámbito de la ingeniería de software. |
| Demuestra Responsabilidad profesional para el logro de los objetivos. | Carlos Rojas Ccama, Propuesta<br><br>Rodrigo Pozo Campos, Descripción del problema<br><br>Brenda Gamio Upiachihua, Descripción y visualización del conjunto de datos. | El compromiso en la elaboración de la propuesta es evidencia de la dedicación para alcanzar metas en mi campo de trabajo. El desarrollo continuo en equipo demostró responsabilidad. |
| Emite juicios considerando el impacto de las soluciones de ingeniería de software en el contexto global, impacto social, ambiental y económico. | Carlos Rojas Ccama, Propuesta<br><br>Rodrigo Pozo Campos, Descripción del problema<br><br>Brenda Gamio Upiachihua, Descripción y visualización del conjunto de datos. | El equipo exhibe una sólida ética profesional y adopta un enfoque integral hacia la ingeniería de software, considerando no solo los aspectos técnicos, sino también su impacto en un contexto más amplio. |


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
  - **Bordes.txt:**
  Este archivo de texto contiene las aristas que conformarán el grafo. Estas aristas poseen únicamente una columna, la cual hace referencia al “Quadcode” en los registros.
  - **Calles.txt:**
  Este último archivo de texto contiene los nombres de cada una de las calles que contiene la zona elegida.

| STREETSEGID |  QUADCODE  |     ST_NAME    |
| :----------:| :--------: | :-------------:| 
|      1      |      3     |    Bangor St   |
|      5      |      2     |   Florida Ave  |
|      11     |      1     |      O St      |
|      12     |      1     |      T St      |
|      13     |      1     |   Whittier St  |
|      15     |      1     |    19th St     |
|      16     |      4     |  Maryland Ave  |
|      17     |      1     |     8th St     |
|      19     |      3     |      K St      |
|      22     |      2     | Kenilworth Ave |
|      24     |      1     |  Chesapeake St |
|      26     |      2     |      H St      |
|      27     |      2     |      C St      |
|      29     |      2     |     4th St     |

* Puntos de direcciones con 144 108 registros. De estos registros se podría sacar:
  
    - **Nodos.txt:**
  El presente archivo de texto contiene datos de referencia sobre los nodos que conformarán nuestro grafo en el futuro. Estos nodos representarán las intersecciones entre dos calles. El formato del archivo consta de cuatro columnas, donde las cuatro corresponden a las coordenadas geográficas precisas (Coordenada X, Coordenada Y, Latitud y Longitud).
  - **Bordes.txt:**
  Este archivo de texto contiene las aristas que conformarán el grafo. Estas aristas poseen únicamente una columna, la cual hace referencia al número de dirección. 
  - **Calles.txt:**
  Este último archivo de texto contiene los nombres de cada una de las calles que contiene la zona elegida.

| ADDRESS_NUMBER |   STREET_NAME   | Y_COORDINATE | X_COORDINATE |  LATITUDE   |   LONGITUD   | 
| :-------------:|:---------------:|:------------:|:------------:|:-----------:|:------------:|
|      7428      |     GEORGIA     |   145855.59  |   397663.49  | 38.98062369 | -77.02696622 |
|        2       | REV LLOYD YOUNG |   136378.23  |   401734.22  | 38.89525024 | -76.98000891 |
|        4       | REV LLOYD YOUNG |   136385.15  |   401734.75  | 38.89531258 | -76.98000278 |
|        6       | REV LLOYD YOUNG |   136391.27  |   401734.22  | 38.89536771 | -76.98000888 |
|        8       | REV LLOYD YOUNG |   136397.39  |   401733.95  | 38.89542284 | -76.98001197 |
|       10       | REV LLOYD YOUNG |   136403.24  |   401733.95  | 38.89547554 | -76.98001196 |
|       12       | REV LLOYD YOUNG |   136408.83  |   401733.95  | 38.8955259  | -76.98001194 |
|       14       | REV LLOYD YOUNG |   136415.21  |   401733.68  | 38.89558337 | -76.98001504 |
|       16       | REV LLOYD YOUNG |   136421.87  |   401733.42  | 38.89564337 | -76.98001802 |
|      2007      |     TRENTON     |   130814.77  |   402173.11  | 38.8451317  | -76.97496722 |
|      1302      |     TRINIDAD    |   137308.68  |   401194.41  | 38.9036333  | -76.98622991 |
|      1327      |    UNDERWOOD    |   144587.65  |   397316.83  | 38.96920114 | -77.03096214 |
|       511      |     BRUMMEL     |   145786.18  |   398130.87  | 38.97999988 | -77.02157188 |
|      4712      |      ALTON      |   142116.05  |   391904.38  | 38.94690312 | -77.09338929 |

**¿Cómo se va a utilizar en el aplicativo?**

 Los datos recopilados serán empleados en la elaboración de nuestro programa, para la elaboración del mapa utilizaremos los algoritmos necesarios, en el cual se realizarán las búsquedas de caminos.
 
Con la información del archivo nodes, bordes y calles, iremos creando nuestro grafo el cual representará y se mostrará en la aplicación como el mapa el cual abarca la zona elegida. También en la App mostraremos una lista de las calles que tenemos en nuestra data, siendo las calles que componen el alcance de nuestro mapa.


## 3. Propuesta
El objetivo principal de esta propuesta es desarrollar un sistema de navegación eficiente que permita a los usuarios encontrar la ruta más corta entre dos puntos dentro de una ciudad. Este sistema debe ser fácil de usar, preciso y rápido, y deberá tener en cuenta varios factores como el tráfico en tiempo real, las preferencias del usuario y otros elementos relevantes.

El objetivo del programa que vayamos a realizar es dirigir al usuario desde un cierto punto de la ciudad a otro evitando coincidir con el tráfico y de esa manera ahorrar tiempo de llegada.
Las técnicas que utilizaremos para el desarrollo de esta App serán las mismas que hemos estado estudiando durante el ciclo actual, el uso de Backtracking, Dijkstra y otros algoritmos que sean necesarios, además se investigará a los distintos algoritmos de tipo topológico que nos ayude a realizar las acciones que hará nuestra aplicación.  

Los algoritmos de búsqueda de la ruta más eficiente desempeñarán un papel fundamental en nuestra aplicación. Uno de los algoritmos clave que utilizaremos es el algoritmo de Dijkstra, el cual se encarga de identificar la ruta más óptima en nodos que tienen asignados valores específicos, que en nuestro caso representan la longitud de las calles en una ciudad. Esto nos permitirá determinar la ruta más corta entre dos ubicaciones especificadas por el usuario. Además de la implementación de varios algoritmos para el funcionamiento de la aplicación, es esencial mantenerla actualizada de forma constante y proporcionar alternativas en caso de que surjan obstáculos en el cálculo de la ruta más eficiente en la vida real, como cierres de calles, accidentes u otros problemas que puedan afectar las condiciones de la vía.


   - **Recopilación de datos:**
     Obtener datos cartográficos detallados de la ciudad, que incluyan información sobre calles, carreteras,   
     intersecciones, señales de tráfico
   - **Algoritmo de enrutamiento**
     Implementar un algoritmo de enrutamiento eficiente, como el algoritmo Dijkstra, que calcule la ruta más corta entre 
     dos puntos.
   - **Interfaz de usuario**
     Desarrollar una interfaz de usuario intuitiva para la aplicación, que permita a los usuarios ingresar sus puntos de 
     inicio y destino.
     Mostrar la ruta recomendada en el mapa, junto con información relevante, estimado de llegada, el tráfico y las 
     instrucciones paso a paso.


## 4. Diseño del Aplicativo

En el proceso de diseño de nuestro proyecto de aplicación, nos enfocaremos en analizar los algoritmos que implementaremos en la aplicación. Esta elección se debe a la importancia de garantizar el correcto funcionamiento de los algoritmos en nuestra aplicación, ya que es crucial monitorearlos constantemente en busca de posibles fallas o errores en el código. Asimismo, se realizarán las correcciones necesarias a lo largo de todo el desarrollo de la aplicación.

Dado que nuestra aplicación se centra en las calles de las ciudades, podemos interpretarlas como grafos ponderados, donde cada calle se convierte en una arista y los cruces en vértices. Esta representación facilita la aplicación de algoritmos y cálculos basados en grafos, especialmente al calcular la ruta más corta entre diferentes puntos. Por lo tanto, utilizar y entender las calles como grafos conectados con pesos específicos resulta óptimo para la ejecución de nuestra aplicación.

Para la elaboración del programa, hemos decidido emplear diversos algoritmos como solución.

**En primer lugar, consideramos la implementación del algoritmo de Dijkstra.**

 Este método, ideado por Edsger Dijkstra, un destacado científico de la computación neerlandés, se utiliza para determinar la ruta más corta entre un vértice de origen y otros vértices conectados por aristas con pesos específicos. En nuestro proyecto, que se centra en calcular la ruta más eficiente entre las calles de diferentes ubicaciones en el país, encontramos que este algoritmo es idóneo. Cada calle se considera como una arista con un peso correspondiente a su longitud, y los puntos entre los cuales se desea calcular la ruta se interpretan como los vértices de un grafo.

**Otro algoritmo que contemplamos es el de Bellman-Ford.**

 Este enfoque busca la ruta más corta en un grafo ponderado, permitiendo incluso aristas con valores negativos. A diferencia del algoritmo de Dijkstra, el de Bellman-Ford puede utilizarse en grafos con aristas de peso negativo. En nuestro proyecto, planeamos implementar este algoritmo para explorar diferentes métodos de generación de rutas eficientes, evitando sobrecargar un único algoritmo con todas las rutas que la aplicación pueda trazar.

**Finalmente, evaluamos la posibilidad de incorporar el algoritmo de Johnson.**

 Este método busca las rutas más cortas entre pares de vértices en un grafo dirigido disperso, permitiendo pesos negativos en las aristas. Utiliza el algoritmo de Bellman-Ford para eliminar aristas con peso negativo, y posteriormente aplica el algoritmo de Dijkstra en el grafo resultante.

 Algunas capturas de la aplicacion funcionando y en donde se podran realizar las solicitudes:

<br>
 <img src="https://cdn.discordapp.com/attachments/1172398225219657818/1172620739451555880/Imagen_de_WhatsApp_2023-11-10_a_las_10.07.40_16a96d30.jpg?ex=6560fb2a&is=654e862a&hm=2f89e718a8b8ada23b6fafe3f78feb12f3c3c5e4089664f4ab97ef73c3b8a005&" alt="Login Aplicacion">

<br>
 <img src="https://cdn.discordapp.com/attachments/1172398225219657818/1172620767578562762/Imagen_de_WhatsApp_2023-11-10_a_las_10.07.40_1b9d8b2e.jpg?ex=6560fb31&is=654e8631&hm=9cb06ebb5de0bbeaca9088e394cf393600e87cbe30b82b61b3c2357a576e12fa&" alt="Home Aplicacion">



## 5. Bibliografía
Washington DC: una ciudad moldeada por y para el poder, una concentración de poder. (s. f.). https://geoimage.cnes.fr/fr/geoimage/washington-dc-una-ciudad-moldeada-por-y-para-el-poder-una-concentracion-de-poder

Parábola Estudio. (2018, 15 mayo). Vistas desde el cielo de 10 sorprendentes ciudades planificadas. Medium. https://medium.com/@parabola.redes/vistas-desde-el-cielo-de-10-sorprendentes-ciudades-planificadas-2c0a3def7368

Address points. (s. f.). https://opendata.dc.gov/datasets/DCGIS::address-points/explore?showTable=true

Street Centerlines 2013. (s. f.). https://opendata.dc.gov/datasets/8655869366064bdca04bb6793cc02a54_3/explore?location=38.894894%2C-77.025952%2C13.00&showTable=true

