import etl_mainfile as etl
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Dataset load
df_platform= etl.df_platform
#Reset index
df_platform= df_platform.reset_index()
#Fill N/A records with 0
df_platform= df_platform.fillna(0)
#Transform 0 (int) to "0"(string)
df_platform= df_platform.astype(str)
#Creation of the column that will be evaluated
df_platform['title_description']= df_platform['title']+df_platform['description']
#Data processing
vectorized= TfidfVectorizer(analyzer='word', ngram_range=(1, 2), stop_words=['english','0'])
X= vectorized.fit_transform(df_platform['title_description'])
#Create similarity matrix
similarity_matrix= cosine_similarity(X)