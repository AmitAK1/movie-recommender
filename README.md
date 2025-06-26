# 🎥 Movie Recommender System

A simple, beginner-friendly **movie recommender system** built with **Streamlit**, using **cosine similarity** on precomputed movie embeddings.

We generate numerical vectors for each movie using metadata (e.g., genres, cast, director, keywords), then compute their pairwise similarity using **cosine similarity**. This similarity matrix is stored and reused for fast recommendations.

This app suggests **5 similar movies** to the one selected by the user, along with their **poster images** fetched from the **TMDb API**.

---

🌐 Live Demo
You can try the app live here:
👉 https://movierecommender010.streamlit.app/

## 📄 Features

- Choose a movie from a dropdown  
- Get 5 similar movie recommendations  
- View poster images using the **TMDb API**  
- Fully responsive and modern UI (dark theme)  
- Works offline with preloaded data  

---

## 📁 Project Structure

├── app.py # Main Streamlit app
├── movies.pkl # Movie metadata with titles and IDs
├── similarity.pkl # Precomputed cosine similarity matrix
├── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## 🔧 Tech Stack

- **Python**  
- **Streamlit** – for web UI  
- **Pandas / NumPy** – for data processing  
- **scikit-learn** – for:
  - `CountVectorizer` – converts text metadata to vector form  
  - `cosine_similarity` – measures similarity between movies  
- **Pickle** – for saving/loading the processed data  
- **TMDb API** – to fetch real movie poster images  

---

## 🚀 Run Locally

1. **Clone the repository**
git clone https://github.com/your-username/movie-recommender-app.git
  cd movie-recommender-app
Install dependencies
  pip install -r requirements.txt
Run the app
  streamlit run app.py

🌐 Deployment (Streamlit Cloud)
You can deploy this app easily with Streamlit Cloud.

Required Setup:
Push your repo to GitHub

Go to Streamlit Cloud and deploy the repo

If your app uses any API keys (e.g., TMDb), store them securely:

Store TMDb API Key:
Go to Settings > Secrets

Add your API key like this:

[general]
TMDB_API_KEY = "your_key_here"
Access it in your app:
  st.secrets["TMDB_API_KEY"]
💡 Note: This app uses the API key directly in code for simplicity. It's fine for learning or demos, but avoid this in production.

🧠 How It Works
Movie metadata (title, cast, director, genres, keywords) is combined into a single string

CountVectorizer converts this string into a numerical vector

cosine_similarity compares these vectors to find similar movies

Top 5 recommendations are returned with poster URLs from TMDb

🎨 UI Preview


✅ Future Improvements
Add movie search bar with autocomplete

Include genre or director-based filters

Add hover effects or animations for posters

Replace with deep learning-based embeddings (e.g., Word2Vec or BERT)

🙌 Author
Amit Kamble
Indian Institute of Information Technology, Design and Manufacturing, Kancheepuram
B.Tech Computer Science – Major in Artificial Intelligence
