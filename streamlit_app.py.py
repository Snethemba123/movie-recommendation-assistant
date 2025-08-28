import streamlit as st

# -------------------------
# Dataset of movies with posters
# -------------------------
movies = [
    {"title": "Inception", "genre": "sci-fi", "actor": "Leonardo DiCaprio", "mood": "adventurous",
     "poster": "https://m.media-amazon.com/images/I/51nbVEuw1HL._AC_.jpg"},
    {"title": "The Wolf of Wall Street", "genre": "drama", "actor": "Leonardo DiCaprio", "mood": "energetic",
     "poster": "https://m.media-amazon.com/images/I/81AwKHVBD+L._AC_SY679_.jpg"},
    {"title": "Interstellar", "genre": "sci-fi", "actor": "Matthew McConaughey", "mood": "thoughtful",
     "poster": "https://m.media-amazon.com/images/I/71n58UdFKbL._AC_SY679_.jpg"},
    {"title": "The Dark Knight", "genre": "action", "actor": "Christian Bale", "mood": "intense",
     "poster": "https://m.media-amazon.com/images/I/51k0qaOiYYL._AC_.jpg"},
    {"title": "La La Land", "genre": "romance", "actor": "Emma Stone", "mood": "happy",
     "poster": "https://m.media-amazon.com/images/I/81Jg4bgluvL._AC_SY679_.jpg"},
    {"title": "Crazy Rich Asians", "genre": "romance", "actor": "Constance Wu", "mood": "happy",
     "poster": "https://m.media-amazon.com/images/I/91bl0jQpPfL._AC_SY679_.jpg"},
    {"title": "The Avengers", "genre": "action", "actor": "Robert Downey Jr.", "mood": "adventurous",
     "poster": "https://m.media-amazon.com/images/I/81ExhpBEbHL._AC_SY679_.jpg"},
    {"title": "Joker", "genre": "drama", "actor": "Joaquin Phoenix", "mood": "dark",
     "poster": "https://m.media-amazon.com/images/I/81bJ0z0W1-L._AC_SY679_.jpg"},
    {"title": "Moana", "genre": "animation", "actor": "Auli'i Cravalho", "mood": "relaxed",
     "poster": "https://m.media-amazon.com/images/I/81K74r7rYRL._AC_SY679_.jpg"},
    {"title": "Finding Nemo", "genre": "animation", "actor": "Ellen DeGeneres", "mood": "relaxed",
     "poster": "https://m.media-amazon.com/images/I/81pE9L2W3WL._AC_SY679_.jpg"}
]

# -------------------------
# Streamlit setup
# -------------------------
st.set_page_config(page_title="AI Movie Recommender", page_icon="🎬")
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎬 AI Movie Recommendation Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4b7bec;'>Answer a few questions and I'll recommend 2–3 movies for you!</p>", unsafe_allow_html=True)

# -------------------------
# User inputs
# -------------------------
genre = st.text_input("1️⃣ What genre do you prefer? (e.g., action, romance, drama, sci-fi, animation)")
actor = st.text_input("2️⃣ Who is one of your favourite actors? (e.g., Leonardo DiCaprio, Emma Stone)")
mood = st.text_input("3️⃣ What mood are you in? (e.g., happy, adventurous, relaxed, dark, intense, thoughtful)")

# -------------------------
# Recommendation logic
# -------------------------
if st.button("🎯 Get Recommendations"):
    recommendations = []

    for movie in movies:
        if (
            (genre.strip().lower() in movie["genre"].lower() if genre else False) or
            (actor.strip().lower() in movie["actor"].lower() if actor else False) or
            (mood.strip().lower() in movie["mood"].lower() if mood else False)
        ):
            recommendations.append(movie)

    if recommendations:
        st.success("✅ Based on your answers, we recommend:")
        cols = st.columns(len(recommendations[:3]))
        for col, movie in zip(cols, recommendations[:3]):
            col.markdown(f"**{movie['title']}**")
            col.image(movie['poster'], use_container_width=True)
    else:
        st.warning("😕 Sorry, no matches found. Try different answers!")
