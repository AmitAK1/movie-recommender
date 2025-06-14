import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
import os
import gdown


def download_file_from_google_drive(file_id, output_path):
    if not os.path.exists(output_path):
        url = f"https://drive.google.com/uc?id={file_id}&confirm=t"
        gdown.download(url, output_path, quiet=False, fuzzy=True)

# Download the files if not present
download_file_from_google_drive('1nlHYXIyVHFyFdUm8aZeS9DcdfQGYMNmM', 'movies.pkl')
download_file_from_google_drive('18Z3uoE6P7KM1iVDmtJFewy6O3UMV35iE', 'similarity.pkl')

movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].tolist()

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bd86f3f971333d90b427565297c95d99&language=en-US"
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        # fallback image if poster is missing
        return "https://via.placeholder.com/300x450?text=No+Poster+Available"

def Recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    print('movie_index', movie_index,movie)
    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        index=i[0]
        movie_id=movies_df.iloc[index]['id']
        recommended_movies.append(movies_df.iloc[i[0]].title)
        #fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters



selected_movie=st.selectbox(
    'Which movie would you like to watch?',
    movies_list
)
if st.button('Recommend'):
    st.markdown("### 🎬 Movie Recommendations")
    names, posters = Recommend(selected_movie)
    cols = st.columns(5)

    for idx, col in enumerate(cols):
        with col:
            # Make title smaller and centered
            st.markdown(
                f"<p style='text-align: center; font-size: 16px; font-weight: 600;'>{names[idx]}</p>",
                unsafe_allow_html=True
            )
            st.image(posters[idx], use_container_width=True)
