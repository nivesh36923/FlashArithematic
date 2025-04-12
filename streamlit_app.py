import streamlit as st
import random
import time

st.set_page_config(page_title="Flash Arithmetic", layout="centered")
st.title("🧠 Flash Arithmetic Game")

# Define levels
levels = {
    "Easy": {"count": 3, "min": 10, "max": 50, "speed": 1.0},
    "Medium": {"count": 5, "min": 10, "max": 50, "speed": 1.0},
    "Hard": {"count": 7, "min": 10, "max": 50, "speed": 1.0}
}

# Select difficulty level
level = st.selectbox("Choose Difficulty Level", list(levels.keys()))
config = levels[level]

# Session state variables
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "numbers" not in st.session_state:
    st.session_state.numbers = []

# Start Game
if st.button("🎮 Start Game"):
    st.session_state.numbers = [random.randint(config["min"], config["max"]) for _ in range(config["count"])]
    st.session_state.game_started = True

    # Countdown timer
    countdown = st.empty()
    for i in range(3, 0, -1):
        countdown.markdown(f"<h2 style='text-align:center;'>Starting in {i}...</h2>", unsafe_allow_html=True)
        time.sleep(1)
    countdown.empty()

    # Show numbers one by one
    placeholder = st.empty()
    for number in st.session_state.numbers:
        placeholder.markdown(f"<h1 style='text-align:center;'>{number}</h1>", unsafe_allow_html=True)
        time.sleep(config["speed"])
        placeholder.markdown("<h1 style='text-align:center;'> </h1>", unsafe_allow_html=True)

    st.success("Now enter the total sum!")

# Answer section
if st.session_state.game_started:
    user_answer = st.number_input("Your answer:", step=1, format="%d")
    if st.button("✅ Submit"):
        correct_sum = sum(st.session_state.numbers)
        if user_answer == correct_sum:
            st.success(f"✅ Correct! The sum was {correct_sum}")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect. The correct sum was {correct_sum}")
        st.session_state.game_started = False

# Display Score
st.markdown(f"### 🏆 Score: {st.session_state.score}")
