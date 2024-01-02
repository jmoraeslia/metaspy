from flask import Flask, render_template, request, redirect, url_for
from get_data import process_img  

app = Flask(__name__)


@app.route('/index.html', methods=['POST', 'GET'])
def file_up():
    
   

    return render_template('index.html')



# sources of research
@app.route('/ref')
def references():
    return render_template('ref.html')

if __name__ == '__main__':
    app.run(debug=True)
