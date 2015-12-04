import pandas as pd
import numpy as np


def extract_donnees():
    """ simple extraction des donne de movielens dans une matrice"""
    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings = pd.read_table('ml-100k/u.data', sep='\t', names=r_cols)
    
    m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
    movies = pd.read_table('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5))
    
    u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols)

    
    return ratings,movies,users

def most_highly_rated_film(movies, users,ratings):

    movie_ratings = pd.merge(movies, ratings)
    lens = pd.merge(movie_ratings, users)
    
    movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
    movie_stats.head()
    atleast_100 = movie_stats['rating']['size'] >= 100
    top=movie_stats[atleast_100].sort([('rating', 'mean')], ascending=False)[:5]
    return top
    
def most_rated_film(movies, users,ratings):
    movie_ratings = pd.merge(movies, ratings)
    lens = pd.merge(movie_ratings, users)


    most_rated = lens.groupby('title').size().order(ascending=False)[:25]
    most_rated
    return lens.title.value_counts()[:5]
    
if __name__=='__main__':

    ratings,movies,users = extract_donnees()
    top = most_highly_rated_film(movies,users,ratings)
    print "les film les mieux note sont :",top,'\n'
    most_rated=most_rated_film(movies, users,ratings)
    print "les films les plus note sont :",most_rated,'\n'
    
