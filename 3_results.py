import streamlit as st
import pandas as pd
import os

# Preventing Non-Logged in Players From Accessing This Page
if "username" not in st.session_state or st.session_state.username == "":
    st.warning("Please go to the Home page and enter your name first!")
    st.stop() # This prevents the rest of the page from loading 

# Showing Results
st.title("🏆 The Results Are In!")

df = pd.read_csv('submissions.csv')
results_df = df.sort_values(by="Votes", ascending=False)

winner_song = results_df.iloc[0]['Song']
winner_player = results_df.iloc[0]['Player']
winning_votes = results_df.iloc[0]['Votes']

st.markdown(f"### 👑 The winner is **{winner_player}**!")
st.write(f"with the song: *{winner_song}* ({winning_votes} votes)")
st.balloons()

#leaderboard
st.markdown("### Full Leaderboard")
st.table(results_df[['Player', 'Song', 'Votes']])
st.balloons()
