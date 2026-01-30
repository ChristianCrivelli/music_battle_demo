import streamlit as st
import pandas as pd
import os

ALLOWED_LIST = st.secrets["authorized_users"]
df = pd.read_csv('submissions.csv')
player_number = len(ALLOWED_LIST)

# Preventing Non-Logged in Players From Accessing This Page
if "username" not in st.session_state or st.session_state.username == "":
    st.warning("Please go to the Home page and enter your name first!")
    st.stop() 

# Game Phase Logic
user_has_voted = ((df['Player'] == st.session_state.username) & (df['Has Voted'] == 1)).any()

## Directing Players to Voting if Necessary (but not to vcoting if they already have)
if (not user_has_voted):
    if (player_number == len(df.index)):
        st.session_state.game_phase = "Voting"
        st.rerun()

## Directing Players to Results if Necessary
if (df['Has Voted'].sum() == player_number): 
    st.session_state.game_phase = "Results"
    st.rerun()

# The Waiting Page
st.title("Sit Tight! Waiting for other players.")

# Refreshing Every 5 secs
from time import sleep
sleep(5)
st.rerun()