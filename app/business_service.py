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
    return {"status": "ok"}
