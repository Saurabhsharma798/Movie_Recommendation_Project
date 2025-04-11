import streamlit as st
import pickle
import requests
from streamlit_option_menu import option_menu
import gdown
import os

if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1yoIOYqY9qjFeufnEyhxCmcNXkAsTfkWX"
    gdown.download(url, "similarity.pkl", quiet=False)

if not os.path.exists("similarity.pkl"):
    st.info("Downloading similarity data... Please wait ⏳")




st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")


#navigation menu

menu=option_menu(
    menu_title=None,
    options=["Home","About","contact"],
    icons=["house","info-circle","telephone"],
    orientation='horizontal'
)


new_df=pickle.load(open('movies.pkl','rb'))
movies=new_df['title'].values
# recommend=pickle.load(open('recommend.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    api_key='257bd0e75682fbbd0e68bc8943f1d0f0'
    url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response=requests.get(url)
    data=response.json()
    poster_path=data['poster_path']
    poster_url='https://image.tmdb.org/t/p/w500'+poster_path

    return poster_url

def recommend(movie):
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id=new_df.iloc[i[0]].movie_id
        recommended_movies.append(new_df.iloc[i[0]].title)
        #fetch poster from api 
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters

st.title('🎬 Movie Recommendation System')
if menu=="Home":
    selected_movie= st.selectbox(
        "Please select the movie"
        ,movies
    )
    if st.button('Recommend'):
        with st.spinner('Loading recommendations...'):

        
            names,posters=recommend(selected_movie)
            col1,col2,col3,col4,col5=st.columns(5)

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


    st.markdown("""
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.0);
            color: gray;
            font-size: 14px;
        }
        </style>

        <div class="footer">
            Made by Saurabh 👨‍💻
        </div>
    """, unsafe_allow_html=True)


elif menu=="About":
    st.title("ℹ️ About the App")

    st.markdown("""
    Welcome to the Movie Recommendation System!  
    This app helps you discover new movies based on your favorites using a content-based recommendation algorithm.

    ### Features
    - 🔍 Search for a movie
    - 🎞️ Get similar movie recommendations
    
    
    """)
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.0);
            color: gray;
            font-size: 14px;
        }
        </style>

        <div class="footer">
            Made by Saurabh 👨‍💻
        </div>
    """, unsafe_allow_html=True)

elif menu=="contact":
    
    st.title("☎️ Contact me")

    st.markdown("""
    <style>
        a.contact {
        text-decoration: none;
        color: inherit;
        font-size: 18px;
    }
    </style>
    <a class="contact" href="https://github.com/Saurabhsharma798" target="_blank">🛠️ GitHub</a>

                
    """,unsafe_allow_html=True)
    st.markdown("""
    <style>
        a.contact {
        text-decoration: none;
        color: inherit;
        font-size: 18px;
    }
    </style>
    <a class="contact" href="mailto:k.saurabhsharma798@gmail.com" target="_blank">📧 Gmail</a>

                
    """,unsafe_allow_html=True)
    st.markdown("""
    <style>
        a.contact {
        text-decoration: none;
        color: inherit;
        font-size: 18px;
    }
    </style>
    <a class="contact" href="https://www.linkedin.com/in/saurabh-kumar-92337a247" target="_blank">🔗 Linkedin</a>

                
    """,unsafe_allow_html=True)