from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate

load_dotenv()

prompt = ChatPromptTemplate.from_messages([("system","""
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
Short Summary: ...""")
,("human",""" 
extract information from the paragraph:
{paragraph}
""")]
)

para = input("Provide your paragraph")

model = ChatMistralAI(
    model='mistral-large-latest'
)

final_prompt = prompt.invoke({"paragraph":para})
response = model.invoke(final_prompt)
print(response.content)