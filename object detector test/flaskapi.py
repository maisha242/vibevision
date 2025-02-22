from flask import Flask, request
import soundfromimage

app = Flask(__name__)

@app.route('/call_function', methods=['GET'])
def call_function():
    # You can retrieve any parameters from the GET request if needed
    param = request.args.get('param', default=None)

    # Call the function from another file
    soundfromimage.main()
    
    # Return the result as a response to the GET request
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
