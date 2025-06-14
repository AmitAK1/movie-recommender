🎥 Movie Recommender System

A simple, beginner-friendly movie recommender system built with Streamlit, using cosine similarity on precomputed movie embeddings.

We generate numerical vectors for each movie using tags (genre, cast, etc.), then compute their pairwise similarity using cosine similarity.

This similarity matrix is saved and reused for fast recommendations.

This app suggests 5 movies similar to the one selected by the user, along with their posters fetched from the TMDb API.

📁 Project Structure

├── app.py               # Main Streamlit app
├── movies.pkl           # Movie metadata
├── similarity.pkl       # Precomputed cosine similarity matrix
├── requirements.txt     # Python dependencies

📄 Features

Choose a movie from a dropdown

Get 5 similar movie recommendations

View poster images using the TMDb API

Fully responsive and modern UI (dark theme)

Works offline with preloaded data

🚀 Run Locally

1. Clone the repository

git clone <your_repo_url>
cd <your_repo_folder>

2. Install dependencies

pip install -r requirements.txt

3. Run the app

streamlit run app.py

🌐 Deployment (Streamlit Cloud)

No need to upload .pkl files manually — they will be downloaded from Google Drive automatically on first run.

Required setup:

Push your repo to GitHub

Go to Streamlit Cloud and deploy from the GitHub repo

If your app uses any API keys like TMDb, you should store them securely in Streamlit:

Go to Settings > Secrets

Add your key like this:

[general]
TMDB_API_KEY = "your_key_here"

Then, access it in code with:

st.secrets["TMDB_API_KEY"]

Note: For simplicity, this app uses the API key directly in code. It's fine for beginners or demos, but avoid this in production.

🎨 UI Preview



🔧 Tech Stack

Python

Streamlit

Pandas / NumPy

TMDb API

Pickle (for saved model files)

✅ Future Improvements

Add movie search bar with autocomplete

Include genre or director-based filters

Add hover effects or animation for posters

Use a model-based recommender (e.g., NLP or embeddings)

🙌 Author

Amit Kamble

Indian Institute of Information Technology, Design and Manufacturing, Kancheepuram

Computer Science-with Major in AI.
