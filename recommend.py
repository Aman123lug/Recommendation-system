import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    reponse=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=6051011781320d7e592ad74d48b45957&language=en-US".format(movie_id))
    data=reponse.json()
    # st.text("https://api.themoviedb.org/3/movie/{}?api_key=f79c3fb07d0147d0484e0bb61934a0d4&language=en-US".format(movie_id))
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    dis=similarity[movie_index]
    movies_list=sorted(list(enumerate(dis)), reverse=True, key=lambda x: x[1])

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

st.header("Movie Recommender System" )

movies_dict=pickle.load(open("movies2.pkl","rb"))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open("similarity.pkl","rb"))

selected_movies=st.selectbox("See your favourite Movie in list",movies["title"].values)

if st.button("Recommend"):
    names, posters=recommend(selected_movies)
    # names=recommend(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0], width=130)
    with col2:
        st.text(names[1])
        st.image(posters[1], width=130)
    with col3:
        st.text(names[2])
        st.image(posters[2], width=130)
    with col4:
        st.text(names[3])
        st.image(posters[3], width=130)
    with col5:
        st.text(names[4])
        st.image(posters[4], width=130)