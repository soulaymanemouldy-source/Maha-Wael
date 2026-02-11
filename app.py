import streamlit as st
import time

st.set_page_config(page_title="For You ❤️")

st.title("For You ❤️")

if "clicked" not in st.session_state:
    st.session_state.clicked = False

if st.button("💝 Click with love 💝"):
    st.session_state.clicked = True

if st.session_state.clicked:
    messages = [
        "💖 Happy Valentine's Day 💖",
        "",
        "Maha 🌸",
        "",
        "I made this program for you, I hope you like it 🤗💌",
        "",
        "After 6 years knowing you, I love you more than words can say ❤️🌹",
        "",
        "I love you every day, every minute, every second ❤️✨",
        "",
        "You make my life more beautiful 💕",
        "",
        "From Wael 💖"
    ]

    for msg in messages:
        st.write(msg)
        time.sleep(0.4)
