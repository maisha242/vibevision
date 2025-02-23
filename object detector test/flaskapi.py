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

    # Call the function from another file
    def stream_event():
        last_chunk = None  # Keep track of the last chunk

        for chunk in soundfromimage.main():
            if chunk != None and chunk != last_chunk:  # Check if the chunk is different from the last one
                yield chunk + "\n"
                last_chunk = chunk  # Update last_chunk to the current chunk
            else:
                break

    return Response(stream_event(), mimetype="text/event-stream")

@app.route('/stream', methods=['GET'])
def call_stream():
    def event_stream():
        count = 0
        while True:
            time.sleep(1)
            yield f"data: Hello {count}\n\n"
            count += 1
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run()
