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
st.markdown("<p style='text-align: center; color: #4b7bec;'>“😌 Looks like you’re in the mood to unwind and escape for a bit… Let’s find some movies that will make you smile, relax, and just enjoy the moment!”</p>", unsafe_allow_html=True)

# -------------------------
# Initialize session state
# -------------------------
if "step" not in st.session_state:
    st.session_state.step = 1
if "genre" not in st.session_state:
    st.session_state.genre = ""
if "actor" not in st.session_state:
    st.session_state.actor = ""
if "mood" not in st.session_state:
    st.session_state.mood = ""

def next_step():
    st.session_state.step += 1

def restart_chat():
    st.session_state.step = 1
    st.session_state.genre = ""
    st.session_state.actor = ""
    st.session_state.mood = ""

# -------------------------
# Step-by-step conversation
# -------------------------
if st.session_state.step == 1:
    st.markdown("<h3 style='color:#ff793f;'>1️⃣ What genre do you prefer?</h3>", unsafe_allow_html=True)
    st.session_state.genre = st.text_area("", placeholder="e.g., action, romance, drama, sci-fi, animation", height=50)
    if st.button("➡️ Enter Genre"):
        if st.session_state.genre.strip():
            next_step()

elif st.session_state.step == 2:
    st.markdown("<h3 style='color:#ff793f;'>2️⃣ Who is one of your favourite actors?</h3>", unsafe_allow_html=True)
    st.session_state.actor = st.text_area("", placeholder="e.g., Leonardo DiCaprio, Emma Stone", height=50)
    if st.button("➡️ Enter Actor"):
        if st.session_state.actor.strip():
            next_step()

elif st.session_state.step == 3:
    st.markdown("<h3 style='color:#ff793f;'>3️⃣ What mood are you in?</h3>", unsafe_allow_html=True)
    st.session_state.mood = st.text_area("", placeholder="e.g., happy, adventurous, relaxed, dark, intense, thoughtful", height=50)
    if st.button("➡️ Get Recommendations"):
        if st.session_state.mood.strip():
            next_step()

elif st.session_state.step == 4:
    st.markdown("<h2 style='color:#2ed573;'>🎯 Based on your answers, we recommend:</h2>", unsafe_allow_html=True)
    recommendations = []
    for movie in movies:
        if (
            st.session_state.genre.lower() in movie["genre"].lower() or
            st.session_state.actor.lower() in movie["actor"].lower() or
            st.session_state.mood.lower() in movie["mood"].lower()
        ):
            recommendations.append(movie)

    if recommendations:
        cols = st.columns(len(recommendations[:3]))
        for col, movie in zip(cols, recommendations[:3]):
            col.markdown(f"**{movie['title']}**")
            col.image(movie["poster"], use_container_width=True)
    else:
        st.warning("😕 Sorry, no matches found. Try different answers!")

    if st.button("🔄 Restart Chat"):
        restart_chat()
