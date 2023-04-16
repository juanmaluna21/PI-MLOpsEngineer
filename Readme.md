<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **1ST INDIVIDUAL PROJECT** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

Welcome to this first individual project! On this occasion, I take on the role of a ***MLOps Engineer***.  

<hr>  

## **Main files used:**

<p align="left">
<img src="https://github.com/juanmaluna21/PI-MLOpsEngineer/blob/main/src/Screen%20Shot%202023-04-16%20at%2001.29.11.png"  height=300>
</p>


## **Context**

The client requested and delivered several datasets to us, with the objective that we process them and create a recommendation system.

Original rating datasets are saved in a drive in a drive on this [link](https://drive.google.com/drive/folders/1MPv6HkTOC9_nOIazZ-gVTQhJgWUni97a?usp=share_link)

Original platform datasets are saved in a drive in a drive on this [link](https://drive.google.com/drive/folders/1GcvjWP-P--1D_ihVA6oR8VNI4DX_lGNd?usp=share_link)

<br/>

## **Data treatment:**
[etl_mainfile.py](https://github.com/juanmaluna21/PI-MLOpsEngineer/blob/main/etl_mainfile.py)

[etl_support.ipynb](https://github.com/juanmaluna21/PI-MLOpsEngineer/blob/main/transformation%20-%20support%20notebook.ipynb)

In order to better structure the information in the data, we proceeded to:

For files of each platform (found in the 'datasets' folder): Amazon, Disney, Hulu, and Netflix.

+ A new id field was generated: Each new **`id`** is composed of the first letter of the platform name, followed by the show_id already present in the datasets (example for Amazon titles = **`as123`**).

+ Null values in the rating field were replaced with the string “**`G`**” ('general for all audiences').

+ The format of the 'date_added' column was changed to **`YYYY-mm-dd`**.

+ "All fields were converted to **lowercase**, no exceptions.

+ "Duration" field was divided into two: **`duration_int`** and **`duration_type`**. The first field is an **`int`** and the second is a **`string`** indicating the duration unit of measurement: min (minutes) or season (seasons), which were all changed to singular form in order to facilitate search.

+ A 'platform' column was added in order to facilitate the construction of the API and queries.

For rating files (from 1 to 8):
+ A new column was added to indicate which platform each ID in the 'movieId' column belongs to.

+ The 8 datasets were concatenated into a single one and exported, so that it could later be uploaded to GitHub after being loaded, since, due to the size of the datasets, it was not possible to deploy on Render.

<br/>

## **API Development:**
[main.py](https://github.com/juanmaluna21/PI-MLOpsEngineer/blob/main/main.py)

With the transformed datasets, they were made available to the client through an API built with ***FastAPI*** library, featuring various queries for the user:

+ Movie (not TV series, etc.) with the longest duration by year, platform, and duration type. Function name: `get_max_duration(year, platform, duration_type)`. Returns the name of the movie

+ Number of movies (not TV series, etc.) by platform, with a score higher than XX in a given year. Function name: `get_score_count(platform, scored, year)`. Returns an 'int', with the total number of movies that meet the requested criteria.

+ Number of movies (not TV series, etc.) by platform. Function name: `get_count_platform(platform)`. Returns an int, with the total number of movies for that platform. The platforms are named: Amazon, Netflix, Hulu, and Disney.

+ Actor who appears most frequently by platform and year. Function name: `get_actor(platform, year)`. Returns the name of the actor who appears most frequently according to the given platform and year.

+ The number of contents/products (all available streaming content) released by country and year. Function name: `prod_per_country(content_type, country, year)`. It returns the number of the specified content type (movie, series) per country and year in a dictionary with the variables 'country' (country name), 'year' (year), 'movie' (number of movies).

+ Number of content/products (everything available for streaming, series, movies, etc) according to the given audience rating (for which audience the content was classified). Function name: `get_contents(rating)`. It returns the total number of contents with that audience rating.

<br/>

## **Deployment:**
The deployment was carried out through Render at the following link, with the project name: [PI-MLOpsEngineer](https://pi-mlopsengineer.onrender.com/docs#/).

<br/>

## **Exploratory Data Analysis:**
[eda_mainfile.ipynb](https://github.com/juanmaluna21/PI-MLOpsEngineer/blob/main/eda_mainfile.ipynb)

To obtain a first global overview of the datasets' structure, functions such as `.shape, .dtype, .describe, .info, and .head` were used. In order to observe a little more in detail, a `box plot` diagram was graphed, where several outliers were found in the "duration_int" column. Finally, to complement this analysis, the `ProfileReport` tool from `pandas_profiling` library was used, where it was possible to observe that there are no duplicate values. The platform "Hulu" contains the most null values, some columns such as "cast" do not contain any values. Additionally, it was observed that the movie with the lowest score was "filth" with a score of 0.5.

<br/>

## **Recommendation system:**
[Recommendation_system.ipynb](https://github.com/juanmaluna21/PI-MLOpsEngineer/blob/main/Recommendation_system.ipynb)

"Cosine Similarity" model was used for the recommendation system. The name of the function can be found on the same API interface as a seventh query, called `get_recomendation(title)`, where you enter the title of a movie and it returns a list of 5 recommended movies based on that input title.
(After processing the information and running the model, a .pickle file was printed as [similarity_matrix.pickle](https://drive.google.com/file/d/1gIPsPKwgEdCEO-iqo_XdATjEKX6f9-QS/view?usp=share_link), which is stored on a drive, as it was not possible to load it on GitHub due to its size.)

<br/>

## **Video explanation:**
[link]