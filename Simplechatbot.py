import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

st.set_page_config(
    page_title="Hashim",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_dotenv()
secret_key=os.getenv("OPENAI_API_KEY")
openai_client=OpenAI(api_key=secret_key)

greeting_message={
    "role":"assistant",
    "content":"Hello! I am your Travel Agent. How Can I Help You Today?"
}

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {
            "role":"system",
            "content":"""
            Assume you are a travel agent. You conduct travel programs across the world.
            Respond to queries within 2-3 sentences.
            """
        },
        greeting_message
    ]

prompt=st.chat_input(greeting_message["content"])

if prompt:
    st.session_state["messages"].append({ "role":"user","content":prompt})
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=st.session_state["messages"],
            # max_tokens=300  # Limit the response length (optional, commented out)
        )

    ai_message=response.choices[0].message.content

    st.session_state["messages"].append({"role":"assistant","content":ai_message})

for message in st.session_state["messages"][1:]:  
    with st.chat_message(message["role"]): 
        st.markdown(message["content"])  