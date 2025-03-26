from fastapi import FastAPI, HTTPException, Header
from openai import OpenAI

app = FastAPI()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

@app.get("/")
def read_root():
    return {"message": "This is the business service. It uses an AI model to return all songs in some specific Taylor Swift`s album."} 

@app.get("/songs/{album}")
def get_songs(album: str):
    """Fetch songs from an album using OpenRouter API."""
    completion = client.chat.completions.create(
    extra_body={},
    model="openai/gpt-3.5-turbo-0613",
    messages=[
        {
        "role": "user",
        "content": f"Return me all songs in Taylor Swift album called {album}. Give me all song names in one line separated with ; without any additional information."
        }
    ]
    )
    song_string = completion.choices[0].message.content
    song_list = [song.strip() for song in song_string.split(';')]
    return song_list

@app.get("/health")
def health_check():
    """Status check."""
    return {"status": "ok"}
