from flask import Flask, request
import sys
# Constants
PORT = 8081

sys.stdout.flush()
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/hello', methods = ['GET', 'POST'])
def process_hello():
    if request.method == 'GET':
        hello_recipient = 'world'
        if 'name' in request.args:
            hello_recipient = request.args.get('name')
        output_string = "Hello, {}!".format(hello_recipient)
        return (output_string, 200)
    elif request.method == 'POST':
        output_string = 'This method is unsupported.'
        status_code = 405
        return (output_string, status_code)

@app.route('/check', methods = ['GET', 'POST'])
def process_check():
    if request.method == 'GET':
        output_string = "All is well!"
        status_code = 200
        return (output_string, status_code)
    elif request.method == 'POST':
        output_string = 'This method is unsupported.'
        status_code = 405
        return (output_string, status_code)

if __name__ == "__main__":
    app.run(port=PORT, host='0.0.0.0')
