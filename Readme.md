<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **1ST INDIVIDUAL PROJECT** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

¡Bienvenidos a este primer proyecto individual! En esta ocasión me sitúo en el rol de un ***MLOps Engineer***.  

<hr>  

## **Main files used:**

1) main.py
2) transformation.py
3) support notebook

## **Context**

EL cliente pidió nos entregó varios datasets, con el obejtivo que los tratáramos y finalmente hagamos un sitema de recomendación.

## **Tratamiento de los datos:**

Con el fin de estructurar mejor la información de los datos se procedió a:

Para los archivos de cada plataforma(se encuentran en la carpeta "datasets": Amazon, Disney, Hulu y Netflix):

+ Se generó un campo **`id`**: Cada nuevo id se compone de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**).

+ Los valores nulos del campo rating se reemplazaron por el string “**`G`**” ( “general for all audiences”).

+ Se cambió el formato de la columna "date_added" a **`AAAA-mm-dd`**.

+ Todos los campos fueron pasados **minúsculas**, sin excepciones.

+ Se dividió el campo ***duration*** en dos: **`duration_int`** y **`duration_type`**. El primero campo a un **`int`** y el segundo a un **`string`** indicando la unidad de medición de duración: min (minutos) o season (temporadas), los cuales pasaron a ser todos los registros de este ultimo campo en singular con el fin de facilitar la búsqueda.

+ Se agregó una columna "platform" con el fin de facilitar el armado de la API y las queries.

Para los archivos de los ratings (desde el 1 al 8):
+ Se les agrego una nueva columna que indican a que plataforma pertenece cada id de la columna "movieId".

+ Se concatenaron los 8 datasets en uno solo y exportó, para despues poder cargarlo y subirlo GitHub, dado que, debido al tamaño de los datasets, no se me permitía hacer el deployment desde Render.

<br/>

## **Desarrollo API:**

Ya con los datasets transformados, se los disponibilizó para el cliente a través de una API, construida con la librería ***FastAPI***, con diferentes queries para el usuario:

+ Película (sólo película, no serie, etc) con mayor duración según año, plataforma y tipo de duración.
Nombre de la función: `get_max_duration(year, platform, duration_type)`. Devuelve el nombre de la película.

+ Cantidad de películas (sólo películas, no series, etc) según plataforma, con un puntaje mayor a XX en determinado año.
Nombre de la función: `get_score_count(platform, scored, year)`. Devuelve un int, con el total de películas que cumplen lo solicitado.

+ Cantidad de películas (sólo películas, no series, etc) según plataforma.
Nombre de la función: `get_count_platform(platform)`. Devuelve un int, con el número total de películas de esa plataforma. Las plataformas se llaman: amazon, netflix, hulu, disney.

+ Actor que más se repite según plataforma y año.
Nombre de la función: `get_actor(platform, year)`. Devuelve el nombre del actor que más se repite según la plataforma y el año dado.

+ La cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año.
Nombre de la función: `prod_per_country(tipo,pais,anio)`. Devuelve el tipo de contenido (pelicula,serie) por pais y año en un diccionario con las variables llamadas 'pais' (nombre del pais), 'anio' (año), 'pelicula' (cantidad de películas).

+ La cantidad total de contenidos/productos (todo lo disponible en streaming, series, peliculas, etc) según el rating de audiencia dado (para que publico fue clasificada la pelicula).
Nombre de la función: `get_contents(rating)`. Devuelve el numero total de contenido con ese rating de audiencias.


## **Deployment:**
El deployment fue realizado a través de Render en el siguiente link, con el nombre del proyecto: [PI-MLOpsEngineer](https://pi-mlopsengineer.onrender.com/docs#/).


<br/>

## **Exploratory Data Analysis:**

<br/>



## **Recommendation system:**

Par el sistema de recomendación se utilizó el modelo "Cosine Similarity"

<br/>







<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/raw/main/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=500>
</p>

<sub> Nota que aqui se reflejan procesos no herramientas tecnologicas. Has el ejercicio de entender cual herramienta del stack corresponde a cual parte del proceso<sub/>

## **Propuesta de trabajo (requerimientos de aprobación)**

**`Transformaciones`**:  Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Vas a hacer estas, ***y solo estas***, transformaciones a los datos:


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

**`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***, generando diferentes endpoints que se consumiran en la API.

Creas 6 funciones (recuerda que deben tener un decorador por cada una (@app.get(‘/’)):

+ Película (sólo película, no serie, etc) con mayor duración según año, plataforma y tipo de duración. La función debe llamarse get_max_duration(year, platform, duration_type) y debe devolver sólo el string del nombre de la película.
+ Cantidad de películas (sólo películas, no series, etc) según plataforma, con un puntaje mayor a XX en determinado año. La función debe llamarse get_score_count(platform, scored, year) y debe devolver un int, con el total de películas que cumplen lo solicitado.

+ Cantidad de películas (sólo películas, no series, etc) según plataforma. La función debe llamarse get_count_platform(platform) y debe devolver un int, con el número total de películas de esa plataforma. Las plataformas deben llamarse amazon, netflix, hulu, disney.

+ Actor que más se repite según plataforma y año. La función debe llamarse get_actor(platform, year) y debe devolver sólo el string con el nombre del actor que más se repite según la plataforma y el año dado.

+ La cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año. La función debe llamarse prod_per_county(tipo,pais,anio) deberia devolver el tipo de contenido (pelicula,serie) por pais y año en un diccionario con las variables llamadas 'pais' (nombre del pais), 'anio' (año), 'pelicula' (tipo de contenido).

+ La cantidad total de contenidos/productos (todo lo disponible en streaming, series, peliculas, etc) según el rating de audiencia dado (para que publico fue clasificada la pelicula). La función debe llamarse get_contents(rating) y debe devolver el numero total de contenido con ese rating de audiencias.



<br/>


**`Deployment`**: Conoces sobre [Render](https://render.com/docs/free#free-web-services) y tienes un [tutorial de Render](https://github.com/HX-FNegrete/render-fastapi-tutorial) que te hace la vida mas facil :smile: . Tambien podrias usar [Railway](https://railway.app/), pero ten en cuenta que con este si necesitas dockerizacion.

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente :eyes: ), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior.  Sabes que puedes apoyarte en librerías como _pandas profiling, sweetviz, autoviz_, entre otros y sacar de allí tus conclusiones 😉

**`Sistema de recomendación`**: 

Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas. Éste consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Debe ser deployado como una función adicional de la API anterior y debe llamarse get_recommendation(titulo: str).

<br/>

**`Video`**: Necesitas que al equipo le quede claro que tus herramientas funcionan realmente! Haces un video mostrando el resultado de las consultas propuestas y de tu modelo de ML entrenado!

<sub> **Spoiler**: El video NO DEBE durar mas de ***7 minutos*** y DEBE mostrar las consultas requeridas en funcionamiento desde la API** y una breve explicacion del modelo entrenado para el sistema de recomendacion. <sub/>

<br/>

## **Criterios de evaluación**

**`Código`**: Prolijidad de código, uso de clases y/o funciones, en caso de ser necesario, código comentado. 

**`Repositorio`**: Nombres de archivo adecuados, uso de carpetas para ordenar los archivos, README.md presentando el proyecto y el trabajo realizado

**`Cumplimiento`** de los requerimientos de aprobación indicados en el apartado `Propuesta de trabajo`

NOTA: Recuerde entregar el link de acceso al video. Puede alojarse en YouTube, Drive o cualquier plataforma de almacenamiento. **Verificar que sea de acceso público**.

<br/>
Aqui te sintetizamos que es lo que consideramos un MVP aprobatorio, y la diferencia con un producto completo.



<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/raw/main/src/MVP_MLops.PNG"  height=250>
</p>


## **Fuente de datos**

+ [Dataset](https://drive.google.com/drive/folders/1b49OVFJpjPPA1noRBBi1hSmMThXmNzxn): La carpeta 'ratings' tiene varios archivos con las reseñas de los usuarios, la carpeta raíz tiene un dataset por proveedor de servicios de streaming.
<br/>

## **Material de apoyo**

En este mismo repositorio podras encontrar algunos [links de ayuda](hhttps://github.com/HX-PRomero/PI_ML_OPS/raw/main/Material%20de%20apoyo.md). Recuerda que no son los unicos recursos que puedes utilizar!



  
<br/>

## **Deadlines importantes**

+ Apertura de formularios de entrega de proyectos: **Lunes 17, 10:00 hs gmt -3**

+ Cierre de formularios de entrega de proyectos: **Martes 18, 16:00hs gmt-3**
  
+ Demo: **Martes 18, 16:00hs gmt-3** 
