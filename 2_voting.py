import streamlit as st
import pandas as pd
import os

df = pd.read_csv('submissions.csv')

# Preventing Non-Logged in Players From Accessing This Page
if "username" not in st.session_state or st.session_state.username == "":
    st.warning("Please go to the Home page and enter your name first!")
    st.stop() 

## Check if the current user has already voted
user_has_voted = ((df['Player'] == st.session_state.username) & (df['Has Voted'] == 1)).any()
if user_has_voted:
    # If they already voted, don't let them go back to "Voting"
    if st.session_state.game_phase == "Voting":
        # Redirect them to Waiting
        st.session_state.game_phase = "Waiting"
        st.rerun()
else:

    # Voting Logic
    if os.path.exists('submissions.csv'):  
        st.write("### Review the submissions:")
        
        # Voting Logic
        with st.form("vote_form"):
            # Create a list of other players' submissions
            other_submissions = df[df['Player'] != st.session_state.username]['Song'].tolist()
            
            selection = st.selectbox("What song best fits the theme?", other_submissions)
            if st.form_submit_button("Cast Vote"):
                df.loc[df['Song'] == selection, 'Votes'] += 1
                df.loc[df['Player'] == st.session_state.username, 'Has Voted'] = 1
                df.to_csv('submissions.csv', index=False)
                st.success(f"Voted for: {selection}")

                st.session_state.game_phase = "Waiting"
                st.rerun()
                st.stop()
