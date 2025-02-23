from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
import soundfromimage
import time

app = Flask(__name__)

# Allow all origins
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/call_function', methods=['GET'])
def call_function():
    # Retrieve any parameters from the GET request if needed
    param = request.args.get('param', default=None)

    def stream_event():
        last_chunk = None  # To track the previous chunk

        for chunk in soundfromimage.main():
            if chunk != None:
                # Emit the collision name as a message
                if (last_chunk == None):
                    last_chunk = chunk
                if (last_chunk != None and chunk != last_chunk):
                    yield f"data: {chunk}\n\n"  # Send chunk (nameCollision) as a message to the client



    return Response(stream_event(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run()
