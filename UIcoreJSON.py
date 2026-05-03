import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ('system', """Extract movie information from the paragraph\n{format_instructions}"""),
    ("human", "{paragraph}")
])

model = ChatMistralAI(model='mistral-large-latest')

st.title("Movie Information Extractor")

para = st.text_area("Provide your paragraph")

if st.button("Extract"):
    if para:
        final_prompt = prompt.invoke({
            "paragraph": para,
            "format_instructions": parser.get_format_instructions()
        })
        response = model.invoke(final_prompt)
        movie = parser.parse(response.content)
        st.json(movie.model_dump())
    else:
        st.warning("Please enter a paragraph.")