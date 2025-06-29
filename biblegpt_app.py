import os
import streamlit as st

# Load API key
api_key = os.environ.get("OPENAI_API_KEY")

st.set_page_config(page_title="BibleGPT", page_icon="🙏")
st.title("Wisdom - Ask your Bible Question")

# Show video
video_path = "vidu-video-2839536230959578.mp4"
if os.path.exists(video_path):
    st.video(video_path)
else:
    st.warning(f"Video file {video_path} not found.")

# Continue with question input
question = st.text_input("Enter your Bible question:")

if question:
    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful Bible assistant who only answers using the Bible."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        st.write("**BibleGPT says:**")
        st.write(answer)
