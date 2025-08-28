import streamlit as st

# --- Title ---
st.set_page_config(page_title="AI Movie Recommender", page_icon="🎬")
st.title("🎬 AI Movie Recommendation Assistant")
st.write("Answer a few questions and I'll recommend some movies for you!")

# --- Expanded Movie Dataset with Posters ---
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "actor": "Leonardo DiCaprio", "mood": "Adventurous",
     "poster": "https://m.media-amazon.com/images/I/51nbVEuw1HL._AC_.jpg"},
    {"title": "La La Land", "genre": "Romance", "actor": "Emma Stone", "mood": "Happy",
     "poster": "https://m.media-amazon.com/images/I/81Jg4bgluvL._AC_SY679_.jpg"},
    {"title": "The Avengers", "genre": "Action", "actor": "Robert Downey Jr.", "mood": "Adventurous",
     "poster": "https://m.media-amazon.com/images/I/81ExhpBEbHL._AC_SY679_.jpg"},
    {"title": "Interstellar", "genre": "Sci-Fi", "actor": "Matthew McConaughey", "mood": "Thoughtful",
     "poster": "https://m.media-amazon.com/images/I/71n58UdFKbL._AC_SY679_.jpg"},
    {"title": "The Dark Knight", "genre": "Action", "actor": "Christian Bale", "mood": "Intense",
     "poster": "https://m.media-amazon.com/images/I/51k0qaOiYYL._AC_.jpg"},
    {"title": "Moana", "genre": "Animation", "actor": "Auli'i Cravalho", "mood": "Relaxed",
     "poster": "https://m.media-amazon.com/images/I/81K74r7rYRL._AC_SY679_.jpg"},
    {"title": "Finding Nemo", "genre": "Animation", "actor": "Ellen DeGeneres", "mood": "Relaxed",
     "poster": "https://m.media-amazon.com/images/I/81pE9L2W3WL._AC_SY679_.jpg"},
    {"title": "Titanic", "genre": "Romance", "actor": "Kate Winslet", "mood": "Sad",
     "poster": "https://m.media-amazon.com/images/I/81VrD4YVrFL._AC_SY679_.jpg"},
    {"title": "The Lion King", "genre": "Animation", "actor": "Matthew Broderick", "mood": "Happy",
     "poster": "https://m.media-amazon.com/images/I/81Z0bBQnCNL._AC_SY679_.jpg"},
    {"title": "Frozen", "genre": "Animation", "actor": "Kristen Bell", "mood": "Fun",
     "poster": "https://m.media-amazon.com/images/I/81cFG84BswL._AC_SY679_.jpg"},
    {"title": "Joker", "genre": "Drama", "actor": "Joaquin Phoenix", "mood": "Dark",
     "poster": "https://m.media-amazon.com/images/I/81bJ0z0W1-L._AC_SY679_.jpg"},
    {"title": "Black Panther", "genre": "Action", "actor": "Chadwick Boseman", "mood": "Exciting",
     "poster": "https://m.media-amazon.com/images/I/91b0C2YNS8L._AC_SY679_.jpg"},
    {"title": "Guardians of the Galaxy", "genre": "Action", "actor": "Chris Pratt", "mood": "Fun",
     "poster": "https://m.media-amazon.com/images/I/81M3gCu1dGL._AC_SY679_.jpg"},
    {"title": "Spider-Man: No Way Home", "genre": "Action", "actor": "Tom Holland", "mood": "Exciting",
     "poster": "https://m.media-amazon.com/images/I/81QF7g5Q5LL._AC_SY679_.jpg"},
    {"title": "Forrest Gump", "genre": "Drama", "actor": "Tom Hanks", "mood": "Thoughtful",
     "poster": "https://m.media-amazon.com/images/I/71xBLR4O4XL._AC_SY679_.jpg"},
    {"title": "The Matrix", "genre": "Sci-Fi", "actor": "Keanu Reeves", "mood": "Adventurous",
     "poster": "https://m.media-amazon.com/images/I/51EG732BV3L._AC_.jpg"},
    {"title": "Bridgerton", "genre": "Romance", "actor": "Phoebe Dynevor", "mood": "Romantic",
     "poster": "https://m.media-amazon.com/images/I/91C1p6tfi5L._AC_SY679_.jpg"},
    {"title": "The Wolf of Wall Street", "genre": "Drama", "actor": "Leonardo DiCaprio", "mood": "Energetic",
     "poster": "https://m.media-amazon.com/images/I/81AwKHVBD+L._AC_SY679_.jpg"},
    {"title": "Avengers: Endgame", "genre": "Action", "actor": "Chris Evans", "mood": "Exciting",
     "poster": "https://m.media-amazon.com/images/I/81ExhpBEbHL._AC_SY679_.jpg"},
    {"title": "Crazy Rich Asians", "genre": "Romance", "actor": "Constance Wu", "mood": "Happy",
     "poster": "https://m.media-amazon.com/images/I/91bl0jQpPfL._AC_SY679_.jpg"},
]

# --- Options ---
genres = sorted(list(set([m["genre"] for m in movies])))
actors = sorted(list(set([m["actor"] for m in movies])))
moods = sorted(list(set([m["mood"] for m in movies])))

# --- User Input ---
st.subheader("Step 1: Select your preferred genre")
genre_choice = st.selectbox("Genre", ["Any"] + genres)

st.subheader("Step 2: Select a favorite actor")
actor_choice = st.selectbox("Actor", ["Any"] + actors)

st.subheader("Step 3: Choose your mood (horizontal buttons)")
mood_choice = st.radio("Mood", ["Any"] + moods, horizontal=True)

# --- Recommendation Logic ---
def recommend_movies(genre, actor, mood):
    recommendations = []
    for movie in movies:
        score = 0
        if genre != "Any" and genre.lower() in movie["genre"].lower():
            score += 1
        if actor != "Any" and actor.lower() in movie["actor"].lower():
            score += 1
        if mood != "Any" and mood.lower() in movie["mood"].lower():
            score += 1
        if score > 0:
            recommendations.append((score, movie))
    recommendations.sort(reverse=True, key=lambda x: x[0])
    return [movie for score, movie in recommendations][:5]

# --- Display Recommendations in Columns ---
if st.button("Get Recommendations"):
    recs = recommend_movies(genre_choice, actor_choice, mood_choice)
    if recs:
        st.success("✅ Based on your choices, we recommend:")
        cols = st.columns(len(recs))
        for col, movie in zip(cols, recs):
            col.write(f"**{movie['title']}**")
            col.image(movie['poster'], use_container_width=True)
    else:
        st.warning("😕 Sorry, no matches found. Try different choices!")
