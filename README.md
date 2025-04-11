# 🎬 Movie Recommendation System

A content-based movie recommendation system built using **NLP vectorization** and **Streamlit**. Get smart suggestions based on the movies you love!

---

## 📌 Features

- 🔍 Recommend similar movies based on title input  
- 🧠 Uses NLP techniques (CountVectorizer + Cosine Similarity)  
- 🎞️ Fetches posters using TMDB API  
- ⚡ Fast and lightweight  
- 💻 Clean and responsive UI with Streamlit  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- Scikit-learn  
- Streamlit  
- TMDB API  

---

## 🚀 How it Works

1. The app vectorizes movie overviews using NLP techniques.
2. Computes cosine similarity to find similar movies.
3. Uses TMDB API to fetch movie posters.
4. Displays results in an interactive Streamlit app.

---

## 🧪 Installation


Follow these steps to run the app locally:

1. **Clone the repository**

```bash
git clone https://github.com/Saurabhsharma798/Movie_Recommendation_App.git
cd movie_Recommendation_App
```

2. **Create and activate a virtual environment**

```bash
python -m venv env
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate
```

3. **Install the required dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**

```bash
streamlit run app.py
```