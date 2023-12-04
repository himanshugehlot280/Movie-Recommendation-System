import streamlit as st
import pandas as pd
import codecs
import streamlit.components.v1 as stc
import pickle
import pandas
import requests
from streamlit_option_menu import option_menu
from pathlib import Path
from PIL import Image



def main():
    menu = ["Home", "About Us"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=f85fe66718be85aca0596a5b6403170b&language=en-US'.format(
                    movie_id))
            data = response.json()
            print(data)
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]
            recommended_movies = []
            recommended_movies_poster = []
            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                # fetch poster from api
                recommended_movies_poster.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_poster

        movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        similarity = pickle.load(open('similarity.pkl', 'rb'))

        st.title('Movie Recommender System')
        selected_movie_name = st.selectbox(
            'How would you like to be contacted?',
            (movies['title'].values))

        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)

            col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

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

            with col6:
                st.text(names[5])
                st.image(posters[5])

            with col7:
                st.text(names[6])
                st.image(posters[6])

            with col8:
                st.text(names[7])
                st.image(posters[7])

            with col9:
                st.text(names[8])
                st.image(posters[8])

        def add_bg_from_url():
            st.markdown(
                f"""
                 <style>
                 .stApp {{
                     background-image: url("data:image/jpeg;base64,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");
                     background-attachment: fixed;
                     background-size: cover
                 }}
                 </style>
                 """,
                unsafe_allow_html=True
            )

        add_bg_from_url()

    elif choice == "About Us":
        st.header("About Us")

        hasClicked = card(
            title="Himanshu Gehlot",
            text="CSS|Streamlit|ML himanshugehlot280@gmail.com",
            image="data:image/jpeg;base64,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",
        url = "https://www.linkedin.com/in/himanshu-gehlot-465186207"
        )





if __name__ == '__main__':
    main()
