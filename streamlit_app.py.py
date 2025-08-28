import streamlit as st

# -------------------------
# Dataset of movies
# -------------------------
movies = [
    {"title": "Inception", "genre": "sci-fi", "actor": "Leonardo DiCaprio", "mood": "adventurous"},
    {"title": "The Wolf of Wall Street", "genre": "drama", "actor": "Leonardo DiCaprio", "mood": "energetic"},
    {"title": "Interstellar", "genre": "sci-fi", "actor": "Matthew McConaughey", "mood": "thoughtful"},
    {"title": "The Dark Knight", "genre": "action", "actor": "Christian Bale", "mood": "intense"},
    {"title": "La La Land", "genre": "romance", "actor": "Emma Stone", "mood": "happy"},
    {"title": "Crazy Rich Asians", "genre": "romance", "actor": "Constance Wu", "mood": "happy"},
    {"title": "The Avengers", "genre": "action", "actor": "Robert Downey Jr.", "mood": "adventurous"},
    {"title": "Joker", "genre": "drama", "actor": "Joaquin Phoenix", "mood": "dark"},
    {"title": "Moana", "genre": "animation", "actor": "Auli'i Cravalho", "mood": "relaxed"},
    {"title": "Finding Nemo", "genre": "animation", "actor": "Ellen DeGeneres", "mood": "relaxed"}
]

# -------------------------
# Streamlit chatbot setup
# -------------------------
st.set_page_config(page_title="AI Movie Recommender", page_icon="🎬")
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎬 AI Movie Recommendation Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4b7bec;'>Hi! I will recommend 2–3 movies based on your preferences. Let's chat!</p>", unsafe_allow_html=True)

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "genre" not in st.session_state:
    st.session_state.genre = ""
if "actor" not in st.session_state:
    st.session_state.actor = ""
if "mood" not in st.session_state:
    st.session_state.mood = ""

# -------------------------
# Step-by-step conversation
# -------------------------
def next_step():
    st.session_state.step += 1

# Step 1: Genre
if st.session_state.step == 1:
    st.markdown("<h3 style='color:#ff793f;'>1️⃣ What genre do you prefer?</h3>", unsafe_allow_html=True)
    st.session_state.genre = st.text_input("", placeholder="e.g., action, romance, drama, sci-fi, animation")
    if st.button("➡️ Enter Genre"):
        if st.session_state.genre.strip() != "":
            next_step()

# Step 2: Actor
elif st.session_state.step == 2:
    st.markdown("<h3 style='color:#ff793f;'>2️⃣ Who is one of your favourite actors?</h3>", unsafe_allow_html=True)
    st.session_state.actor = st.text_input("", placeholder="e.g., Leonardo DiCaprio, Emma Stone")
    if st.button("➡️ Enter Actor"):
        if st.session_state.actor.strip() != "":
            next_step()

# Step 3: Mood
elif st.session_state.step == 3:
    st.markdown("<h3 style='color:#ff793f;'>3️⃣ What mood are you in?</h3>", unsafe_allow_html=True)
    st.session_state.mood = st.text_input("", placeholder="e.g., happy, adventurous, relaxed, dark, intense, thoughtful")
    if st.button("➡️ Enter Mood"):
        if st.session_state.mood.strip() != "":
            next_step()

# Step 4: Recommendations
elif st.session_state.step == 4:
    st.markdown("<h2 style='color:#2ed573;'>🎯 Based on your answers, here are some movie recommendations:</h2>", unsafe_allow_html=True)
    recommendations = []

    for movie in movies:
        if (
            st.session_state.genre.lower() in movie["genre"].lower() or
            st.session_state.actor.lower() in movie["actor"].lower() or
            st.session_state.mood.lower() in movie["mood"].lower()
        ):
            recommendations.append(movie["title"])

    if recommendations:
        for rec in recommendations[:3]:
            st.markdown(f"<p style='color:#ffa502; font-size:18px;'>🎬 {rec}</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#ff6b81;'>😕 Sorry, I couldn’t find a perfect match. Try different answers!</p>", unsafe_allow_html=True)

    # Restart option
    if st.button("🔄 Restart Chat"):
        st.session_state.step = 1
        st.session_state.genre = ""
        st.session_state.actor = ""
        st.session_state.mood = ""
