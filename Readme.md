# 🎬 Movie Information Extractor

A clean Streamlit web app that uses **Mistral AI**, **LangChain**, and **Pydantic** to turn a plain-text movie description into structured JSON.

Paste any paragraph about a movie, click **Extract**, and the app returns key details such as the title, release year, genre, director, cast, rating, and a short summary. The app is designed around schema-based extraction, which makes the output predictable and easy to use in downstream applications [page:2][page:1].

## Features

- Extracts structured movie metadata from unstructured text.
- Returns consistent JSON output for easy inspection or reuse.
- Uses a schema-driven approach with Pydantic validation for cleaner results [page:2].
- Supports Mistral models through the `langchain-mistralai` integration package [page:1].
- Keeps secrets out of source code by loading the API key from a `.env` file, which is a common security best practice for app configuration [web:4][page:1].

## Extracted Fields

The app can return the following fields when they are present in the input text:

- `title`
- `release_year`
- `genre`
- `director`
- `cast`
- `rating`
- `summary`

Some fields may be `null` or empty if the paragraph does not mention them clearly.

## Tech Stack

| Tool | Purpose |
|------|---------|
| Streamlit | Web interface for entering movie descriptions and viewing output |
| LangChain | Prompt orchestration and structured extraction workflow [page:2] |
| Mistral AI | LLM used for movie information extraction via `mistral-large-latest` [page:1] |
| Pydantic | Structured schema definition and validation [page:2] |
| python-dotenv | Environment variable loading for local development |

## Project Structure

```text
project/
├── app.py              # Main Streamlit app
├── .env                # API keys (not committed)
└── requirements.txt    # Python dependencies
```

## How It Works

1. The user pastes a paragraph describing a movie.
2. Streamlit sends the input into the extraction workflow.
3. LangChain uses a structured-output pattern so the response follows a predefined schema instead of free-form text [page:2].
4. The schema is validated and returned as clean JSON.

This pattern is useful because structured output reduces brittle text parsing and gives the application predictable fields that can be consumed directly by code [page:2].

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Install dependencies

```bash
pip install streamlit langchain langchain-mistralai pydantic python-dotenv
```

The Mistral integration for LangChain is provided through the `langchain-mistralai` package [page:1].

### 3. Add your API key

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_api_key_here
```

A valid `MISTRAL_API_KEY` is required to access Mistral models [page:1].

### 4. Run the app

```bash
streamlit run app.py
```

By default, Streamlit apps usually open locally at `http://localhost:8501/`.

## Usage

1. Open the app in your browser.
2. Paste a paragraph describing a movie into the text area.
3. Click **Extract**.
4. Review the structured JSON response.

## Example Input

```text
The Dark Knight, released in 2008, is a superhero crime thriller directed by Christopher Nolan. Starring Christian Bale as Batman alongside Heath Ledger's iconic Joker, the film holds a 9.0 rating on IMDb. It is widely regarded as one of the greatest films ever made.
```

## Example Output

```json
{
  "title": "The Dark Knight",
  "release_year": 2008,
  "genre": ["Superhero", "Crime", "Thriller"],
  "director": "Christopher Nolan",
  "cast": ["Christian Bale", "Heath Ledger"],
  "rating": 9.0,
  "summary": "A superhero crime thriller widely regarded as one of the greatest films ever made."
}
```
## Requirements

A minimal `requirements.txt` can look like this:

```txt
streamlit
langchain
langchain-mistralai
pydantic
python-dotenv
```

## Notes

- A valid Mistral AI API key is required for the app to work [page:1].
- Output quality depends on how descriptive the input paragraph is.
- Optional fields such as `release_year`, `director`, and `rating` may be missing if they are not stated in the source text.
- Setting model temperature to `0` is a practical choice when you want more consistent extraction behavior.

## Future Improvements

- Add form validation and user-friendly error messages.
- Show missing fields explicitly in the UI.
- Support poster extraction or external movie database enrichment.
- Add export options such as JSON download.
- Save extraction history with session state.

## License

Add your preferred license here, such as MIT.
