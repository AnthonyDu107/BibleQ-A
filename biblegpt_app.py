import os
import streamlit as st
from openai import OpenAI

# Load API key from environment
api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

st.title("BibleGPT - Ask Bible Questions 🙏")

question = st.text_input("Ask your Bible question:")

if question:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful Bible assistant who only answers using the Bible."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        st.markdown("**BibleGPT says:**")
        st.write(answer)
