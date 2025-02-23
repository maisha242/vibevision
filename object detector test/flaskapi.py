from flask import Flask, request
from flask_cors import CORS
import soundfromimage

app = Flask(__name__)

# Allow all origins
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/call_function', methods=['GET'])
def call_function():
    # Retrieve any parameters from the GET request if neededpyt
    param = request.args.get('param', default=None)

    # Call the function from another file
    result = soundfromimage.main()

    # Return the result as a response to the GET request
    return result

if __name__ == "__main__":
    app.run()