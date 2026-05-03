🎬 Movie Information Extractor
A Streamlit web app that uses Mistral AI and LangChain to extract structured movie information from a plain-text paragraph.

What It Does
Paste any paragraph describing a movie, and the app will extract and return:

Title
Release Year
Genre
Director
Cast
Rating
Summary


Tech Stack
ToolPurposeStreamlitWeb UILangChainPrompt chaining & output parsingMistral AILLM (mistral-large-latest)PydanticStructured output schemapython-dotenvAPI key management

Project Structure
project/
├── app.py           # Main Streamlit app
├── .env             # API keys (not committed)
└── requirements.txt

Setup & Installation
1. Clone the repo
bashgit clone <your-repo-url>
cd <project-folder>
2. Install dependencies
bashpip install streamlit langchain langchain-mistralai pydantic python-dotenv
3. Add your Mistral API key
Create a .env file in the root directory:
MISTRAL_API_KEY=your_api_key_here
4. Run the app
bashstreamlit run app.py

How to Use

Open the app in your browser (usually http://localhost:8501)
Paste a paragraph about any movie into the text area
Click Extract
View the extracted movie details as structured JSON


Example Input
The Dark Knight, released in 2008, is a superhero crime thriller directed by Christopher Nolan.
Starring Christian Bale as Batman alongside Heath Ledger's iconic Joker, the film holds
a 9.0 rating on IMDb. It is widely regarded as one of the greatest films ever made.
Example Output
json{
  "title": "The Dark Knight",
  "release_year": 2008,
  "genre": ["Superhero", "Crime", "Thriller"],
  "director": "Christopher Nolan",
  "cast": ["Christian Bale", "Heath Ledger"],
  "rating": 9.0,
  "summary": "A superhero crime thriller widely regarded as one of the greatest films ever made."
}

Notes

Requires a valid Mistral AI API key
Output quality depends on how descriptive the input paragraph is
Fields like release_year, director, and rating are optional and may be null if not mentioned
