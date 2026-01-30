import streamlit as st
import pandas as pd
import os

file_path = 'submissions.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(columns=['Player', 'Song', 'Votes', 'Has Voted'])
    df.to_csv(file_path, index=False)

# Save Submission Function
def save_submission(name, text):
    new_data = pd.DataFrame([[name, text, 0, 0]], columns=['Player', 'Song', 'Votes', 'Has Voted'])
    
    if not os.path.isfile(file_path):
        new_data.to_csv(file_path, index=False)
    else:
        new_data.to_csv(file_path, mode='a', header=False, index=False)

# Preventing Non-Logged in Players From Accessing This Page
if os.path.exists('submissions.csv'):
    if "username" not in st.session_state or st.session_state.username == "":
        st.warning("Please go to the Home page and enter your name first!")
        st.stop() 

## Check if the current user has already submitted a song
df = pd.read_csv('submissions.csv')
user_has_submitted = st.session_state.username in df['Player'].values

if user_has_submitted:
    st.session_state.game_phase = "Waiting"
    st.rerun()
    st.stop()
else:
    # Run Submission
    st.title(f"Welcome, {st.session_state.username}!")
    st.subheader("Pick a song that...")

    with st.form("my_submission"):
        user_input = st.text_input("You would play on the aux on the way to the function!")
        
        if st.form_submit_button("Submit"):
            save_submission(st.session_state.username, user_input)
            st.session_state.game_phase = "Waiting"
            st.rerun()
        