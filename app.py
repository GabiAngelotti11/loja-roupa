from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)
app.secret_key = 'minha-senha'

usuarios_db = {
    'admin@fatec.sp.gov.br': {'id': 1, 'nome': 'usuario', 'senha': '123', 'celular': '123456789', 'nivel_acesso': 'usuario'}}

produtos_db = {'nome_produto': {'preco': 0, 'descricao': '', 'categoria': '','quantidade': 0}}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        user = usuarios_db.get(email)
        if user and user['senha'] == senha:
            session['usuario_logado'] = {'email': email, 'nome': user['nome']}
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('index'))
        else:
            flash('E-mail ou senha incorretos!', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('index'))

@app.route('/cadastrar_usuarios', methods=['GET', 'POST'])
def cadastrar_usuarios():
    if 'usuario_logado' not in session:
        flash('Você precisa estar logado para acessar esta página!', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        celular = request.form.get('celular')
        data_nascimento = request.form.get('data_nascimento')
        cpf = request.form.get('cpf')
        nivel_acesso = request.form.get('nivel_acesso')
        cep = request.form.get('cep')
        endereco = request.form.get('endereco')
        numero = request.form.get('numero')
        complemento = request.form.get('complemento')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')

        if email in usuarios_db:
            flash('Este e-mail já está cadastrado!', 'warning')
        else:
            usuarios_db[email] = {
                'nome': nome, 'senha': senha, 'celular': celular, 
                'data_nascimento': data_nascimento, 'cpf': cpf, 
                'nivel_acesso': nivel_acesso, 'cep': cep, 
                'endereco': endereco, 'numero': numero, 
                'complemento': complemento, 'cidade': cidade, 'estado': estado
            }
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('index'))
        
    return render_template('cadastrar_usuarios.html')

@app.route('/listar_usuarios')
def listar_usuarios():
    if 'usuario_logado' not in session:
        flash('Você precisa estar logado para acessar esta página!', 'danger')
        return redirect(url_for('index'))

    if 'usuario_logado' not in session:
        flash('Você precisa estar logado para acessar esta página!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('listar_usuarios.html', usuarios=usuarios_db)

@app.route('/excluir_usuario/<email>', methods=['POST'])
def excluir_usuario(email):
    if 'usuario_logado' not in session:
        flash('Você precisa estar logado para acessar esta página!', 'danger')
        return redirect(url_for('index'))

    if email in usuarios_db:
        del usuarios_db[email]
        flash('Usuário excluído com sucesso!', 'success')
    else:
        flash('Usuário não encontrado!', 'danger')

    return redirect(url_for('listar_usuarios'))

@app.route('/cadastrar_produtos', methods=['GET', 'POST'])
def cadastrar_produtos():

    if 'usuario_logado' not in session:
        flash('Você precisa estar logado para acessar esta página!', 'danger')
        return redirect(url_for('index'))
    if request.method == 'POST':
        nome_produto = request.form.get('nome_produto')
        preco = request.form.get('preco')
        descricao = request.form.get('descricao')
        quantidade = request.form.get('quantidade')
        categoria = request.form.get('categoria')

        if nome_produto in produtos_db:
            flash('Este produto já está cadastrado!', 'warning')
        else:
            produtos_db[nome_produto] = {
                'preco': preco, 'descricao': descricao, 'categoria': categoria, 'quantidade': quantidade
            }
            flash('Produto cadastrado com sucesso!', 'success')
            return redirect(url_for('index'))
    return render_template('cadastrar_produtos.html')

@app.route('/listar_produtos')
def listar_produtos():
    if 'usuario_logado' not in session:
        flash('Você precisa estar logado para acessar esta página!', 'danger')
        return redirect(url_for('index'))
    return render_template('listar_produtos.html', produtos=produtos_db)

@app.route('/excluir_produto/<nome_produto>', methods=['POST'])
def excluir_produto(nome_produto):
    if 'usuario_logado' not in session:
        flash('Você precisa estar logado para acessar esta página!', 'danger')
        return redirect(url_for('index'))

    if nome_produto in produtos_db:
        del produtos_db[nome_produto]
        flash('Produto excluído com sucesso!', 'success')
    else:
        flash('Produto não encontrado!', 'danger')

    return redirect(url_for('listar_produtos'))

if __name__ == '__main__':
    app.run(debug=True)