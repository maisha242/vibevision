import requests
import webbrowser
import config
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS  # Import CORS to enable cross-origin requests
import threading
import time

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
        
        frontend_url = f"http://localhost:3001?access_token={access_token}"  #front end on 3000 
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
    
@app.route("/search", methods=["POST"])
def search_sounds():
    global access_token
    if not access_token:
        return jsonify({"error": "Access token not available"}), 400

    data = request.get_json()

    query = data.get("query")  # required

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    search_url = "https://freesound.org/apiv2/search/text/"

    headers = {"Authorization": f"Bearer {access_token}"}
    params = {
        "query": query,
        "fields": "id,name,tags,previews"  
    }

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code == 200:
        search_result = response.json()

        if search_result["count"] > 0:
            first_result = search_result["results"][0]

            # Extract the preview MP3 URL (you can choose between low and high quality)
            preview_url = first_result["previews"].get("preview-hq-mp3")  # HQ MP3
            if not preview_url:
                preview_url = first_result["previews"].get("preview-lq-mp3")  # LQ MP3 as fallback

            if preview_url:
                return jsonify({"sound_name": first_result["name"], "preview_url": preview_url})
            else:
                return jsonify({"error": "No preview URL available"}), 400
        else:
            return jsonify({"error": "No results found"}), 404

    else:
        return jsonify({"error": "Error with Freesound search", "details": response.text}), 400


def run_flask():
    app.run(port=5001, debug=True, use_reloader=False)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    time.sleep(1)

    webbrowser.open("http://localhost:5001")

    flask_thread.join()
