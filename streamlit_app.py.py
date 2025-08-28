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
st.title("🎬 AI Movie Recommendation Chatbot")
st.write("Hi! I will recommend 2–3 movies based on your preferences. Let's chat!")

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

if st.session_state.step == 1:
    st.session_state.genre = st.text_input("1️⃣ What genre do you prefer? (e.g., action, romance, drama, sci-fi, animation)")
    if st.session_state.genre:
        next_step()

elif st.session_state.step == 2:
    st.session_state.actor = st.text_input("2️⃣ Who is one of your favourite actors? (e.g., Leonardo DiCaprio, Emma Stone)")
    if st.session_state.actor:
        next_step()

elif st.session_state.step == 3:
    st.session_state.mood = st.text_input("3️⃣ What mood are you in? (e.g., happy, adventurous, relaxed, dark, intense, thoughtful)")
    if st.session_state.mood:
        next_step()

# -------------------------
# Show recommendations
# -------------------------
elif st.session_state.step == 4:
    st.write("🎯 Based on your answers, here are some movie recommendations:")
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
            st.write(f" - {rec}")
    else:
        st.write("😕 Sorry, I couldn’t find a perfect match. Try different answers!")

    # Option to restart
    if st.button("🔄 Restart Chat"):
        st.session_state.step = 1
        st.session_state.genre = ""
        st.session_state.actor = ""
        st.session_state.mood = ""
