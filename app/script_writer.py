import google.generativeai as genai # type: ignore
from config.config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def generate_script(topic, research):

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are a YouTube Shorts script writer.

Topic: {topic}

Research:
{research}

Write a 45 second YouTube Shorts script.

Structure:
Hook
Main Points
Ending Call To Action
"""

    response = model.generate_content(prompt)

    return response.text