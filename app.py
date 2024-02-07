import streamlit as st
import pandas as pd
import pickle

def recommend(selected_movie_name):
        movie_index = movies[movies['title'] == selected_movie_name]['id'].index[0]
        distance = similarity[movie_index]
        movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

        recommended_movies = []
        posters = []

        for i in movies_list:
            l = path.iloc[i[0]]['poster_path']
            recommended_movies.append(movies.iloc[i[0]].title)
            posters.append("https://image.tmdb.org/t/p/w500" + l) 
        return recommended_movies,posters

# path = pickle.load(open('path.pkl','rb'))
# movies = pickle.load(open('movies.pkl','rb'))
# movies_list = movies['title'].values
# similarity = pickle.load(open('similarity.pkl','rb'))
path = pd.compat.pickle_compat.load(open('path.pkl','rb'))
movies = pd.compat.pickle_compat.load(open('movies.pkl','rb'))
movies_list = movies['title'].values
similarity = pd.compat.pickle_compat.load(open('similarity.pkl','rb'))

st.title('Movies Recommender System')

selected_movie_name = st.selectbox(
    'Select Movies',
    movies_list)


if st.button('Recommend'):
    
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

        
    st.write()