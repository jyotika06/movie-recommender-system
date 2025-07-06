# 🎬 Movie Recommender System

This is a content-based movie recommender system built with **Python**, **Pandas**, **scikit-learn**, and **Streamlit**. It uses movie metadata from TMDB (The Movie Database) to suggest similar movies based on your selection.

## 🔍 Features

- Suggests top 5 similar movies based on selected movie
- Fetches posters using the TMDB API
- Interactive web interface using Streamlit
- Clean layout with poster previews

## 🧠 Technologies Used

- Python
- Pandas, NumPy
- scikit-learn
- Streamlit
- TMDB API

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/jyotika06/movie-recommender-system.git
cd movie-recommender-system

# Create a virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
