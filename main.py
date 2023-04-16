import pandas as pd
import etl_mainfile as etl
import pickle
from fastapi import FastAPI

#Tittle and description of the API
app = FastAPI(title= 'Movies and Series database',
              description= 'Through this API you can find the movies/series of the following platforms: Amazon, Disney Plus, Hulu and Netflix')

# welcome
@app.get('/')
async def index():
    return {"Welcome!!!"}

@app.get('/about')
async def about():
    return 'Soy Henry first Individual Project'

#datasets load
df_platform= etl.df_platform
df_ratings= etl.df_ratings

with open('similarity_matrix.pickle', 'rb') as f:
    similarity_matrix = pickle.load(f)


#QUERIES
#1) max duration movie
@app.get('/get_max_duration/{year}/{platform}/{duration_type}')
async def get_max_duration(year:int, platform:str, duration_type:str):
    max_duration = df_platform[(df_platform['platform']== platform) & (df_platform['release_year']== year) & (df_platform['duration_type']== duration_type) & (df_platform['type']=='movie')].sort_values(by= ['duration_int']).iloc[-1]
    return {'movie':max_duration['title']}

#2) Number of movies per platform with a rating > XX
@app.get('/get_score_count/{platform}/{scored}/{year}')
async def get_score_count(platform: str, scored: float, year:int):
    return {'platform':platform,
            'number':len(df_ratings[(df_ratings['year']== year) & (df_ratings['platform']== platform) & (df_ratings['rating']> scored)]),
            'year':year,
            'score':scored}

#3) Number of movies per platform
@app.get('/get_count_platform/{platform}')
async def get_count_platform(platform:str):
    return {'platform':platform, 'movies':len(df_platform[df_platform['platform']== platform])}

#4) Actor who appears the most frequently by platform and year
@app.get('/get_actor/{platform}/{year}')
async def get_actor(platform:str, year:int):
    by_actor = df_platform.loc[(df_platform['platform'] == platform) & (df_platform['release_year'] == year), 'cast']
    all_actors = [actor.strip() for cast_list in by_actor.str.split(',') if isinstance(cast_list, list) for actor in cast_list]
    if not all_actors: #If the column is empty
        return {'platform':platform, "year":year,'actor':'no information','times':0}
    else:
        #Most common actor and frequence
        most_common_actor = max(set(all_actors), key = all_actors.count)
        frequency = all_actors.count(most_common_actor)
        return {'platform':platform, "year":year,'actor':most_common_actor,'times':frequency}

#5) Number of content/products (everything available on streaming) that was published per country and year
@app.get('/prod_per_country/{type}/{country}/{year}')
async def prod_per_country(type:str,country:str,year:int):
    return {'country':country, 'year':year, 'movies':len(df_platform[(df_platform['type']==type) & (df_platform['country']==country) & (df_platform['release_year']== year)])}

#6) Total number of content/products (everything available on streaming, series, documentaries, movies, etc.)
#according to the given audience rating (for which audience the movie was classified).
@app.get('/get_contents/{rating}')
async def get_contents(rating:str):
    return {'rating':rating,'content':len(df_platform[(df_platform['rating']==rating)])}

#7) Sistema de recomendación:
@app.get('/get_recomendation/{title}')
async def get_recomendation(title:str):
    #Obtain movie index
    idx = df_platform[df_platform['title'] == title].index[0]
    #Obtain similar movies related to "title"
    similar_movies = list(enumerate(similarity_matrix[idx]))
    #Order movies by cosine similarity
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    #5 similiar movies
    top_movies = [df_platform.iloc[i[0]].title for i in similar_movies[1:6]]
    return {'recomeendation':top_movies}