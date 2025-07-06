import streamlit as st
import pickle
import pandas as pd
import requests
import os

# ⬇️ Auto-download similarity.pkl if not found
def download_similarity_file():
    url = "https://limewire.com/d/Co5Eo#mBhuTYhIWd"
    filename = "similarity.pkl"
    if not os.path.exists(filename):
        st.write("Downloading similarity.pkl...")
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
        st.write("Download complete.")
    else:
        st.write("similarity.pkl already exists.")

download_similarity_file()

# ⬇️ Function to get poster from TMDB
def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=e8a73c9d002b5dd0c3a47aeef0c783c0&language=en-US'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# ⬇️ Recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_movies_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# ⬇️ Load data
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# ⬇️ Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
