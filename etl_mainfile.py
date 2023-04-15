import pandas as pd

#ETL PROCESS
#Transformation of "datasets"
def transformation(df, word, platform):
    df['show_id']= word + df['show_id'] #Addtion of the extra word
    df['rating'].fillna('G', inplace= True) #replace NaN with "G"
    df['date_added']= pd.to_datetime(df['date_added']) #Type change of "date_added" column from Object to DateTime
    df= df.applymap(lambda s: s.lower() if type(s)== str else s) #Lower case all the Dataframe elements
    df[['duration_int', 'duration_type']]= df['duration'].str.split(' ', expand= True) #Split of "duration" columns into "duration_int" and "duration_type"
    df.insert(loc= df.columns.get_loc('duration') + 1, column='duration_int',value=df.pop('duration_int')) #Relocation of "duration_int" column
    df.insert(loc= df.columns.get_loc('duration') + 2, column='duration_type',value=df.pop('duration_type')) #Relocation of "duration_type" column
    df['duration_type']=df['duration_type'].str.replace('seasons','season') #Standarize "seasons" and "season" into "season"
    df= df.drop(columns=['duration']) #Drop of duration column
    df['platform']= platform #Column added to filter
    return df

#Import of Dataframes
df_amazon= pd.read_csv(r'datasets/amazon_prime_titles.csv')
df_disney= pd.read_csv(r'datasets/disney_plus_titles.csv')
df_hulu= pd.read_csv(r'datasets/hulu_titles.csv')
df_netflix= pd.read_csv(r'datasets/netflix_titles.csv')
df_ratings= pd.read_csv(r'dataset_ratings.csv',index_col='movieId')

#Transformation of the Dataframes
df_amazon= transformation(df_amazon,'a','amazon')
df_disney= transformation(df_disney,'d','disney')
df_hulu= transformation(df_hulu,'h','hulu')
df_netflix= transformation(df_netflix,'n','netflix')

#Concatenate all the datasets
df_platform= pd.concat([df_amazon,df_disney,df_hulu,df_netflix], axis=0)