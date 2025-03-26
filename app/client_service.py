import requests
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

BUSINESS_SERVICE_URL = "http://localhost:8002"
DB_SERVICE_URL = "http://localhost:8001"
TOKEN = "SuperSecretToken"

headers = {
    "Authorization": "Bearer SuperSecretToken"
}

@app.get("/")
def read_root():
    return {"message": "This is a client service. A client can: 1) add some album to a playlist; 2) get all songs in a playlist; 3) rate a song (a new one or the one from a database); 4) get a song`s rating (that is in a database)"}

@app.get("/add-album/{album}")
def get_songs(album: str, authorization: str = Header(None)):
    """Fetch songs from a Taylor Swift album via Business Logic Service."""
    if not authorization or authorization.strip() != f"Bearer {TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    if album.lower() in [
        "taylor swift", "red", "fearless", "speak now", "reputation",
        "lover", "midnights", "evermore", "folklore", "1989"
    ]:
        response = requests.get(f"{BUSINESS_SERVICE_URL}/songs/{album}")
        if response.status_code == 200:
            songs = response.json()
            for song in songs:
                result = rate_song(song, 0, authorization)
                print(result)
            return f"{album} was added to your Taylor Swift playlist!"
    else:
        return "Such an album does not exist. Try again :("

@app.post("/rate-song/{song}")
def rate_song(song: str, rating: int, authorization: str = Header(None)):
    """Rate a song via Database Service."""
    if not authorization or authorization.strip() != f"Bearer {TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    response = requests.post(f"{DB_SERVICE_URL}/rate/{song}", params={"rating": rating})
    return response.json()

@app.get("/get-rating/{song}")
def get_rating(song: str, authorization: str = Header(None)):
    """Retrieve song rating from Database Service."""
    if not authorization or authorization.strip() != f"Bearer {TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    response = requests.get(f"{DB_SERVICE_URL}/rating/{song}")
    response_json = response.json()

    if response_json["rating"] == 0:
        return "This song is not rated yet."
    return response.json()

@app.get("/get-all-songs")
def get_all_songs(authorization: str = Header(None)):
    """Retrieve all songs from Database Service."""
    if not authorization or authorization.strip() != f"Bearer {TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    response = requests.get(f"{DB_SERVICE_URL}/all-songs")
    return response.json()

@app.get("/health")
def health_check():
    """Status check."""
    return {"status": "ok"}
