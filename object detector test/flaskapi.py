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
        # for chunk in soundfromimage.main():
        #     if (chunk != None):
        #         yield chunk + "\n"
        #     else:
        #         break

        for i in range(1, 20):
            yield str(i) + "\n"
    return Response(stream_event(), mimetype="text/event-stream")

    # Return the result as a response to the GET request
    #return jsonify({"result": result})

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