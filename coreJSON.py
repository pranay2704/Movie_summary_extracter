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
    release_year : Optional[int]
    genre : List[int]
    director : Optional[str]
    cast : List[str]
    rating : Optional[float]
    summary : str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([('system',
                                            
"""Extract movie information from the paragraph 
{format_instructions}
"""),
("human", """{paragraph}""")
])

para = input("Provide your paragraph")

model = ChatMistralAI(
    model='mistral-large-latest'
)

final_prompt = prompt.invoke({'paragraph':para,
                              'format_instructions':parser.get_format_instructions})

response = model.invoke(final_prompt)
print(response.content)