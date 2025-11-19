import streamlit as st
import time
import random
import os
from datetime import datetime

# --- CONFIGURATION ---
FRIEND_NAME = "SAYEDA SUBHA ASHRAFI SHIFA"

# Prediction messages
PREDICTION_MESSAGES = [
    "Your net worth will be measured in smiles, success, and a swimming pool full of rupees!",
    "A treasure chest of happiness and gold awaits your brilliant soul!",
    "Fortune favors your daring spirit—brace yourself for a rich adventure!",
    "Smiles, success, and sparkling gems are in your near future!",
    "Expect a cascade of prosperity, laughter, and golden opportunities!",
    "Your brilliance will turn every endeavor into gold and glory!"
]

# Celebration styles
CELEBRATION_STYLES = ["balloons", "toast_gold", "toast_diamond", "toast_crown"]

# Default image
DEFAULT_IMAGE_URL = "https://placehold.co/300x300/10b981/ffffff?text=Take+Selfie+to+Start"

# Folder to save selfie history (admin only)
HISTORY_DIR = "selfie_history"
os.makedirs(HISTORY_DIR, exist_ok=True)

# --- Helper Function to save selfie ---
def save_selfie(img):
    """Save selfie image with timestamp silently."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    saved_filename = f"{HISTORY_DIR}/{timestamp}_{FRIEND_NAME.replace(' ','_')}.png"
    with open(saved_filename, "wb") as f:
        f.write(img.getbuffer())
    return saved_filename

# --- Celebration function ---
def run_celebration(style):
    st.markdown("## 💸 SCANNING...", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(0, 101, 10):
        progress_bar.progress(i)
        status_text.markdown(f"Status: Analyzing **{i}%** of Future Success...")
        time.sleep(0.3)
    progress_bar.empty()
    status_text.empty()

    # Celebration
    if style == "balloons":
        st.balloons()
        st.markdown('<h2 style="text-align:center; color:#FF5733;">🎈 BALLOONS OF SUCCESS! 🎈</h2>', unsafe_allow_html=True)
    elif style == "toast_gold":
        st.markdown('<h2 style="text-align:center; color:#FFD700;">💰 TREASURE OF GOLD UNLOCKED! 💰</h2>', unsafe_allow_html=True)
    elif style == "toast_diamond":
        st.markdown('<h2 style="text-align:center; color:#00CED1;">💎 DIAMONDS OF SUCCESS SPARKLE! 💎</h2>', unsafe_allow_html=True)
    elif style == "toast_crown":
        st.markdown('<h2 style="text-align:center; color:#DAA520;">👑 YOU ARE THE KING/QUEEN OF SUCCESS! 👑</h2>', unsafe_allow_html=True)
    else:
        st.markdown('<h2 style="text-align:center; color:#4CAF50;">🎉 FORTUNE CALCULATED! 🎉</h2>', unsafe_allow_html=True)

    time.sleep(1)


# --- Streamlit Page Config ---
st.set_page_config(page_title="Future Riches Celebration", layout="centered", initial_sidebar_state="collapsed")

# --- Custom CSS for Full Centering ---
st.markdown("""
<style>
header, footer {visibility: hidden;}
.stApp { display: flex; flex-direction: column; align-items: center; justify-content: flex-start; }
.main-title { font-size: 2.5em; font-weight: 800; color: #FFD700; text-align: center; margin: 0.5em 0; }
.friend-name { font-size: 2.5em; font-weight: 900; color: #FFD700; text-align: center; animation: pulse 1.5s infinite; white-space: nowrap; }
@keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.03); } 100% { transform: scale(1); } }
.stImage img { display: block; margin-left: auto; margin-right: auto; }
</style>
""", unsafe_allow_html=True)

# --- Greeting ---
st.markdown(f'<h1 style="font-size: 3em; color: #FFD700; text-align: center; font-weight: 900;">👑 Hi Ma amr! 👑</h1>', unsafe_allow_html=True)
st.markdown('<div class="main-title">From Your Nalayek Friend which is me to you!!!</div>', unsafe_allow_html=True)

st.markdown('<div class="main-title">🥰But its true that I LOVE YOU. You are my best friend.❤️</div>', unsafe_allow_html=True)
st.markdown(f'<div class="friend-name">🎉 {FRIEND_NAME.upper()} 👑</div>', unsafe_allow_html=True)
st.markdown("---")

# --- Camera Input for Selfie ---
selfie = st.camera_input("Take a selfie to Start the Prediction!")

if selfie is not None:
    # Save selfie silently
    save_selfie(selfie)

    # Show the selfie
    st.image(selfie, caption="Your Selfie", width=200)

    # Random prediction & celebration
    prediction_message = random.choice(PREDICTION_MESSAGES)
    celebration_style = random.choice(CELEBRATION_STYLES)

    st.markdown(
        f'<p style="font-size: 1.5em; font-weight: bold; text-align: center; color: #4CAF50; margin-top: 2em;">Prediction: {prediction_message}</p>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<h3 style="text-align: center; margin-top: 1em; color: #FFD700;">💰💸💎 GO BE GREAT 💎💸💰</h3>',
        unsafe_allow_html=True
    )
    run_celebration(celebration_style)

else:
    st.image(DEFAULT_IMAGE_URL, caption="Future Richness Profile", width=200)
    st.markdown(
        f'<p style="font-size: 1.2em; text-align: center; color: #999999; margin-top: 3em;">Take a selfie to unlock your fortune!</p>',
        unsafe_allow_html=True
    )

