import streamlit as st
import datetime
import requests
import sys

BASE_URL ="http://localhost:8000"  ##Backend endpoint

st.set_page_config(
    page_title="llmops streamlit frontend",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Travel planner")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("let me help you plan a trip. where do you want to visit?")

with st.form():
    user_input=""
    submit_button=""

if submit_button and user_input.strip():
    try:
        with st.spinner("loading..."):
            payload - {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned")
            markdown_content = f"""AI travel planner

            # Generated: {datetime.now().strftime('%Y-&m-%d at %H:%M')}
            # Created by: Bee travel agent

            ---

            {answer}

            ---
            """
            st.markdown(markdown_content)
        else:
            st.error("bot failed to respond: " + response.text)
    except Exception as e:
        raise f"The response failed due to {e}"