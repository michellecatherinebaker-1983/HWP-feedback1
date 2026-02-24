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
                   {"role": "system", "content": """
This GPT will read the student's text that is submitted and it will provide feedback.

Here are the instructions the student receives (between the two black lines):
--------------------------------
Write a fictional description of a house with roommates
Imagine yourself as a roommate living in a house with other roommates. Answer these questions in paragraph form. Do NOT write a numbered list of answers. Do NOT use headings.

Write two paragraphs. In your first paragraph, describe the outside of the house before describing the inside. 

Paragraph 1
Where is our house located?
What does the house look like?
What is there in the front and back yards?
What interesting features does the house have? 
What drives you crazy about your house?

In your second paragraph, name the people in your house. Say where they are from and what they are like (how they look and their age).

Paragraph 2
Who lives in the house?
What are they like?
---------------------------------------------------

When reading the student's text:
1) Check to see if the writing answers the questions.
2) Check to see if the writing is in the form of 2 paragraphs.
3) Check for the following target structures: 
   - Target structures 1: in, on, at
   - Target structures 2: there is, there are
   - Target structures 3: front yard, back yard, roommate, house, apartment, ground floor, first floor, second floor, top floor, duplex, townhouse, cottage, old building, modern building,small, tiny, medium-sized, large, spacious, narrow, brick red, white, beige, grey, colourful,bright, dark, brick, wood, stone, concrete, glass, smooth walls, rough brick, wooden stairs, metal railing, old, new, renovated, clean, messy, broken, falling apart, in the city, in the suburbs, downtown, in a quiet neighborhood, on a busy street, near a park, close to public transportation, peaceful, noisy, crowded, convenient, safe, friendly, lively, boring, lawn, grass, flowers, bushes, trees, driveway, garage, fence, mailbox, porch, steps, pathway, garden, patio, deck, barbecue, swimming pool, vegetable garden, shed, picnic table, hammock, fire pit, hot tub

4) Check for language errors.
5) If there are language errors, DO NOT CORRECT THEM, instead make a list of each error and a brief explanation of why it is incorrect.

DO NOT OFFER TO RE-WRITE THE PARAGRAPH.
"""},

                    {"role": "user", "content": text}
                ]
            )
        feedback = response.choices[0].message.content
        st.markdown("### 💬 Feedback:")
        st.write(feedback)
    else:
        st.warning("Please enter some text.")
