import streamlit as st
import datetime
import time
import pytz

# --- TIMEZONE SETUP ---
# Adjust to 'US/Central', 'US/Mountain', or 'US/Pacific' if needed
US_TZ = pytz.timezone('US/Eastern') 
TARGET_DATE = US_TZ.localize(datetime.datetime(2026, 5, 10, 0, 0, 0))

st.set_page_config(page_title="For My Dearest Mom", page_icon="💖", layout="wide")

# --- ADVANCED STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #fff5f7 0%, #fef9e7 100%);
    }
    .main-title {
        font-family: 'Playfair Display', serif;
        color: #7209b7;
        text-align: center;
        font-size: 3.5rem;
        padding-top: 20px;
    }
    .countdown-box {
        font-family: 'monospace';
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        color: #f72585;
        background: white;
        border-radius: 30px;
        padding: 50px;
        width: 70%;
        margin: 50px auto;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: 2px solid #f72585;
    }
    .photo-card {
        border-radius: 15px;
        transition: transform 0.3s ease;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .photo-card:hover {
        transform: scale(1.03);
    }
    </style>
    """, unsafe_allow_html=True)

def get_countdown():
    now = datetime.datetime.now(US_TZ)
    remaining = TARGET_DATE - now
    if remaining.total_seconds() <= 0:
        return None
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}d : {hours}h : {minutes}m : {seconds}s"

# Current US Time
now_us = datetime.datetime.now(US_TZ)

if now_us < TARGET_DATE:
    # --- LOCKED SCREEN ---
    st.markdown("<h1 class='main-title'>A Surprise for the World's Best Mom</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.2rem;'>Your special gift unlocks at midnight on May 10th (US Time)</p>", unsafe_allow_html=True)
    
    placeholder = st.empty()
    while datetime.datetime.now(US_TZ) < TARGET_DATE:
        timer = get_countdown()
        if timer:
            placeholder.markdown(f"<div class='countdown-box'>{timer}</div>", unsafe_allow_html=True)
        time.sleep(1)
    st.session_state['unlocked'] = True
    st.rerun()

else:
    # --- UNLOCKED CELEBRATION ---
    if st.session_state.get('unlocked', True):
        st.toast("🎉 Happy Birthday & Mother's Day, Mom!", icon="💖")
        st.balloons()
        st.session_state['unlocked'] = False

    st.markdown("<h1 class='main-title'>Happy Birthday & Mother's Day!</h1>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🌸 The Celebration", "📸 Beautiful Memories"])

    with tab1:
        st.write("## To my mother,")
        col_msg_left, col_msg_right = st.columns([1, 1.5])
        with col_msg_left:
            st.image("mom1.png", use_container_width=True) # First photo here
        with col_msg_right:
            st.markdown(f"""
            ### Happy Mother's Day!
            I think of you every single day, and since your birthday falls on the **10th of May**, 
            I wanted to combine both celebrations into this one digital gift.
            
            You are the heart of our family, and I hope this year brings you as much 
            joy as you have given me. 
            
            **I love you!**
            """)

    with tab2:
        st.write("## Our Journey")
        # Creating a masonry-style grid for the rest of the photos
        col1, col2 = st.columns(2)
        
        with col1:
            st.image("mom2.png", caption="Mom & Daughter", use_container_width=True)
            st.image("mom4.png", caption="Celebrations", use_container_width=True)
        
        with col2:
            st.image("mom3.png", caption="Special Moments", use_container_width=True)
            st.image("mom5.png", caption="Always Smiling", use_container_width=True)

    st.markdown("---")
    st.write("✨ *Built with love by your favorite coder* ✨")
