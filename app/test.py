import requests

BASE_URL = "http://127.0.0.1:8000"
TOKEN = "Bearer SuperSecretToken"
HEADERS = {"Authorization": TOKEN}

# Test 1: Add an album
album = "reputation"
album_url = f"{BASE_URL}/add-album/{album}"

print(f"Sending request to add album: {album}")
response = requests.get(album_url, headers=HEADERS)

print("Status Code:", response.status_code)
print("Response:", response.text)
print("-" * 50)

# Test 2: Get rating for a song
song = "Delicate"
rating_url = f"{BASE_URL}/get-rating/{song}"

print(f"Sending request to get rating for song: {song}")
response = requests.get(rating_url, headers=HEADERS)

print("Status Code:", response.status_code)

try:
    response_json = response.json()
    if isinstance(response_json, dict) and "rating" in response_json:
        if response_json["rating"] == 0:
            print("Response: This song is not rated yet.")
        else:
            print("Response:", response_json)
    else:
        print("Response:", response_json)
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON. Response text:", response.text)

print("-" * 50)

# Test 3: Rate a song
song_to_rate = "Delicate"
rating_value = 5
rate_song_url = f"{BASE_URL}/rate-song/{song_to_rate}"

print(f"Sending request to rate song: {song_to_rate} with rating: {rating_value}")
response = requests.post(rate_song_url, headers=HEADERS, params={"rating": rating_value})

print("Status Code:", response.status_code)

try:
    response_json = response.json()
    print("Response:", response_json)
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON. Response text:", response.text)

print("-" * 50)

# Test 4: Get rating for a song
song = "Delicate"
rating_url = f"{BASE_URL}/get-rating/{song}"

print(f"Sending request to get rating for song: {song}")
response = requests.get(rating_url, headers=HEADERS)

print("Status Code:", response.status_code)

try:
    response_json = response.json()
    if isinstance(response_json, dict) and "rating" in response_json:
        if response_json["rating"] == 0:
            print("Response: This song is not rated yet.")
        else:
            print("Response:", response_json)
    else:
        print("Response:", response_json)
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON. Response text:", response.text)

print("-" * 50)

# Test 5: Get all songs
all_songs_url = f"{BASE_URL}/get-all-songs"

print("Sending request to get all songs")
response = requests.get(all_songs_url, headers=HEADERS)

print("Status Code:", response.status_code)

try:
    response_json = response.json()
    print("Response:", response_json)
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON. Response text:", response.text)

print("-" * 50)

# Test 6: Unauthorized Access (wrong token)
print("Sending unauthorized request...")
bad_headers = {"Authorization": "Bearer WrongToken"}
response = requests.get(rating_url, headers=bad_headers)

print("Status Code:", response.status_code)
print("Response:", response.text)
print("-" * 50)