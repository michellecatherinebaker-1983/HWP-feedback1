# save this as feedback_gpt.py
import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


st.title("📝 ESL Feedback Assistant")
st.write("Paste your text below and get feedback on grammar, structure, and clarity.")

text = st.text_area("Your writing:", height=200)

if st.button("Get Feedback"):
    if text.strip():
        with st.spinner("Analyzing..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an ESL feedback assistant. Analyze grammar, vocabulary, and sentence structure, categorize errors, and give clear improvement suggestions."},
                    {"role": "user", "content": text}
                ]
            )
        feedback = response.choices[0].message.content
        st.markdown("### 💬 Feedback:")
        st.write(feedback)
    else:
        st.warning("Please enter some text.")
