# web.py
from flask import Flask, render_template, request
from get_data import get_metadata

app = Flask(__name__)

# process file received
@app.route('/', methods=['POST', 'GET'])
def up_file():
    if 'file' not in request.files:
        return "try again;"

    filename = request.files['file']



# sources of research
@app.route('/ref')
def references():
    return render_template('/ref.html')
if __name__ == '__main__':
    app.run(debug=True)
