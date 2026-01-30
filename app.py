import streamlit as st

# Page Configuration
st.set_page_config(page_title="Demo", page_icon="🎧") #!

# Page Protection
ALLOWED_LIST = st.secrets["authorized_users"]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "game_phase" not in st.session_state:
    st.session_state.game_phase = "Submission"

# Page Definition
login_page = st.Page("app.py", title="Log In", icon="🔐", default=True)
submission_page = st.Page("1_submission.py", title="Submission", icon="📤")
waiting_page = st.Page("waiting.py", title="Waiting")
voting_page = st.Page("2_voting.py", title = "Voting") #! Add Icon
results_page = st.Page("3_results.py", title = "Results") #! Add Icon


# Log In Page and Logic Loop Structure
if not st.session_state.authenticated:
    st.title("🔐 Demo Access")
    
    input_name = st.text_input("Enter your Player Name:")
    
    if st.button("Log In"):
        if input_name in ALLOWED_LIST:
            st.session_state.authenticated = True
            st.session_state.username = input_name
            st.rerun()
        else:
            st.error("Access Denied. That name is not on the guest list.")
    st.stop()

else: #Logic Loop Structure
    if st.session_state.game_phase == "Submission":
        pg = st.navigation([submission_page], position="hidden")
        pg.run()

    elif st.session_state.game_phase == "Voting":
        pg = st.navigation([voting_page], position="hidden")
        pg.run()

    elif st.session_state.game_phase == "Results":
        pg = st.navigation([results_page], position="hidden")
        pg.run()
    
    elif st.session_state.game_phase == "Waiting":
        pg = st.navigation([waiting_page], position="hidden")
        pg.run()