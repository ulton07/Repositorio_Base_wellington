from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']

        return f'usuario: {nome} | senha: {senha}'
    
    return render_template('login.html')





@app.route('/cadstrar',methods=['POST','GET'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        email = request.form['email']

        return f'usuario: {nome} | senha: {senha} | email: {email}'
    
    return render_template('cadastrar.html')


if __name__ == '__main__':
    app.run(debug=True)