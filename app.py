from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_usuarios', methods=['GET', 'POST'])
def cadastrar_usuarios():
    if request.method == 'POST':
        # Process the form data
        pass
    return render_template('cadastrar_usuarios.html')

@app.route('/listar_usuarios')
def listar_usuarios():
    # Fetch and display the list of users
    return render_template('listar_usuarios.html')

@app.route('/cadastrar_produtos', methods=['GET', 'POST'])
def cadastrar_produtos():
    if request.method == 'POST':
        # Process the form data for product registration
        pass
    return render_template('cadastrar_produtos.html')

@app.route('/listar_produtos')
def listar_produtos():
    # Fetch and display the list of products
    return render_template('listar_produtos.html')

if __name__ == '__main__':
    app.run(debug=True)