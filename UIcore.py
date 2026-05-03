import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert at extracting useful movie information from a paragraph.

Extract the following details if available:
- Movie name
- Cast
- Main characters
- Director
- Setting
- Genre
- Release year

Also generate a short summary in 1 to 2 sentences.

If any field is missing, write "Not mentioned".

Return the answer in this exact format:

Movie Name: ...
Cast: ...
Main Characters: ...
Director: ...
Setting: ...
Genre: ...
Release Year: ...
Short Summary: ..."""),
    ("human", """
extract information from the paragraph:
{paragraph}
""")
])

model = ChatMistralAI(model='mistral-large-latest')

st.title("Movie Info Extractor")

paragraph = st.text_area("Provide your paragraph", height=200)

if st.button("Extract"):
    if paragraph.strip():
        with st.spinner("Extracting..."):
            final_prompt = prompt.invoke({"paragraph": paragraph})
            response = model.invoke(final_prompt)
            st.text(response.content)
    else:
        st.warning("Please enter a paragraph.")