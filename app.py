import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load API key
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="AI Prompt Optimizer",
    page_icon="🤖"
)

st.title("🤖 AI Prompt Optimizer")
st.write("Turn a simple prompt into a clear and effective AI prompt.")

if not api_key:
    st.error("API key not found ❌")
    st.stop()

client = Groq(api_key=api_key)

with st.form("prompt_form"):
    user_prompt = st.text_input(
        "Enter your prompt:",
        placeholder="Example: Tell me about RAG"
    )

    submitted = st.form_submit_button("✨ Optimize Prompt")

if submitted:

    if not user_prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()

    system_prompt = """
You are an expert prompt engineer.

Your job is to improve the user's raw prompt.

Analyze the user's prompt and make it clearer,
more specific, and more useful for an AI model.

Structure the improved prompt using:

1. Role
2. Task
3. Context
4. Audience
5. Output Format
6. Constraints

Do not change the user's original goal.

Return:

ROLE:
TASK:
CONTEXT:
AUDIENCE:
OUTPUT FORMAT:
CONSTRAINTS:

FINAL IMPROVED PROMPT:
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content

    st.subheader("✨ Improved Prompt")
    st.write(result)

if st.button("✨ Optimize Prompt"):

    if not user_prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()

    system_prompt = """
You are an expert prompt engineer.

Your job is to improve the user's raw prompt.

Analyze the user's prompt and make it clearer,
more specific, and more useful for an AI model.

Structure the improved prompt using:

1. Role
2. Task
3. Context
4. Audience
5. Output Format
6. Constraints

Do not change the user's original goal.

Return:

ROLE:
TASK:
CONTEXT:
AUDIENCE:
OUTPUT FORMAT:
CONSTRAINTS:

FINAL IMPROVED PROMPT:
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content

    st.subheader("✨ Improved Prompt")
    st.write(result)