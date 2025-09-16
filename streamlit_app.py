import streamlit as st
from datetime import datetime
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

with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("user input", placeholder="e.g. Plan a trip to Dubai for 5 days")
    submit_button = st.form_submit_button("send")

if submit_button and user_input.strip():
    try:
        with st.spinner("loading..."):
            payload = {"query": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)
            print("response submitted")

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned")
            print("answer received from main.py")
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
        raise RuntimeError(f"The response failed due to {e}")