from fastapi import FastAPI, HTTPException

app = FastAPI()

db = {}

@app.get("/")
def read_root():
    return {"message": "This is a database service where all the songs that a user adds are stored."} 

@app.post("/rate/{song}")
def rate_song(song: str, rating: int):
    """Stores user rating for a song (0-5)."""
    if rating == 0:
        db[song] = rating
        return {"song": song, "rating": rating}

    if rating < 1 or rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5.")

    db[song] = rating
    return {"song": song, "rating": rating}

@app.get("/rating/{song}")
def get_rating(song: str):
    """Retrieves stored rating for a song."""
    if song not in db:
        raise HTTPException(status_code=404, detail="There is no such song in database.")

    return {"song": song, "rating": db[song]}

@app.get("/all-songs")
def get_all_songs():
    """Retrieves all songs in a database."""
    all_songs = []
    for song in db.keys():
        all_songs.append(song)
    return all_songs

@app.get("/health")
def health_check():
    """Status check."""
    return {"status": "ok"}
