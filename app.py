from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta que recibe un dato y lo procesa
@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    return f"Has ingresado: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)
