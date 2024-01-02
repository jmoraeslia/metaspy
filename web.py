from flask import Flask, render_template, request
from get_data import process_img  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_img', methods=['POST'])
def process_img_route():
    
    if 'mainFile' not in request.files:
        return "Nenhuma imagem foi enviada."

    imagem = request.files['mainFile']

    
    resultado = process_img(imagem)

    
    return render_template('index.html', resultado=resultado)

@app.route('/ref')
def references():
    return render_template('ref.html')

if __name__ == '__main__':
    app.run(debug=True)
