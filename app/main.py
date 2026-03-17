import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st # type: ignore
from research_agent import search_topic
from script_writer import generate_script
from utils import format_script

st.set_page_config(page_title="YouTube Content Agent", page_icon="🎬")

st.title("🎬 AI YouTube Content Creation Agent")

st.write("Generate YouTube Shorts scripts using AI")

topic = st.text_input("Enter your YouTube topic")

if st.button("Generate Script"):

    with st.spinner("Researching topic..."):
        research = search_topic(topic)

    with st.spinner("Generating script..."):
        script = generate_script(topic, research)

    formatted = format_script(script)

    st.subheader("Generated Script")

    st.write(formatted)