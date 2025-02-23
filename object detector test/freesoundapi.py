import requests
import webbrowser
import config
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import threading
import time

# Your Beatoven API token
BASE_URL = 'https://public-api.beatoven.ai'

app = Flask(__name__)
CORS(app)

authurl = "https://freesound.org/apiv2/oauth2/authorize/"
tokenurl = "https://freesound.org/apiv2/oauth2/access_token/"
callbackurl = "http://localhost:5001/callback"  # Make sure this is the same as on Freesound API

access_token = None

@app.route("/")
def home():
    auth_redirect_url = (
        f"{authurl}?client_id={config.freesound_id}&response_type=code&redirect_uri={callbackurl}"
    )
    webbrowser.open(auth_redirect_url)
    return "Moving to Freesound for authentication..."

@app.route("/callback")
def callback():
    global access_token
    auth_code = request.args.get("code")

    if not auth_code:
        return jsonify({"error": "No authorization code received."}), 400

    payload = {
        "client_id": config.freesound_id,
        "client_secret": config.freesound_key,
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": callbackurl
    }

    response = requests.post(tokenurl, data=payload)

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data["access_token"]
        
        frontend_url = f"http://localhost:3000?access_token={access_token}"
        return redirect(frontend_url)
    else:
        return jsonify({"error": "Error getting access token", "details": response.text}), 400


@app.route("/get_access_token", methods=["GET"])
def get_access_token():
    global access_token
    if access_token:
        return jsonify({"access_token": access_token})
    else:
        return jsonify({"error": "Access token not available"}), 400

# Create a new track with the specified prompt
def create_track(prompt):
    try:
        response = requests.post(
            f'{BASE_URL}/api/v1/tracks',
            headers={'Authorization': f'Bearer {config.beatoven_key}', 'Content-Type': 'application/json'},
            json={'prompt': {'text': prompt}}
        )

        if response.status_code == 200:
            data = response.json()
            print('Track created:', data)
            return data['tracks'][0]  # Track ID
        else:
            return None
    except Exception as e:
        print(f"Error creating track: {e}")
        return None

# Compose the track using the track ID
def compose_track(track_id):
    try:
        response = requests.post(
            f'{BASE_URL}/api/v1/tracks/compose/{track_id}',
            headers={'Authorization': f'Bearer {config.beatoven_key}', 'Content-Type': 'application/json'},
            json={'format': 'wav', 'looping': False}
        )

        if response.status_code == 200:
            data = response.json()
            print('Composition started:', data)
            return data['task_id']  # Return task ID
        else:
            return None
    except Exception as e:
        print(f"Error composing track: {e}")
        return None

# Check the composition status
def check_composition_status(task_id):
    try:
        response = requests.get(
            f'{BASE_URL}/api/v1/tasks/{task_id}',
            headers={'Authorization': f'Bearer {config.beatoven_key}'}
        )

        if response.status_code == 200:
            data = response.json()
            print('Composition status:', data)

            if data['status'] == 'composed':
                return data['meta']['track_url']  # Return the track URL when composed
            else:
                print('Track is still being composed.')
                return None
        else:
            return None
    except Exception as e:
        print(f"Error checking composition status: {e}")
        return None

@app.route("/generate_and_play", methods=["POST"])
def generate_and_play():
    try:
        # Step 1: Create the track with the provided prompt
        prompt = request.json.get("prompt")
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        
        track_id = create_track(prompt)
        if not track_id:
            return jsonify({"error": "Failed to create track"}), 500

        # Step 2: Compose the track
        task_id = compose_track(track_id)
        if not task_id:
            return jsonify({"error": "Failed to start composition"}), 500

        # Step 3: Check the composition status
        track_url = None
        while not track_url:
            track_url = check_composition_status(task_id)
            if not track_url:
                time.sleep(5)  # Wait for 5 seconds before checking again

        return jsonify({"track_url": track_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def run_flask():
    app.run(port=5001, debug=True, use_reloader=False)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    time.sleep(1)

    webbrowser.open("http://localhost:5001")

    flask_thread.join()
