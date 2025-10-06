from flask import Flask, render_template,request

app = Flask(__name__)

#principal
@app.route("/")
def ola():
    return "ola mundo!, ulton e amigos"

#contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

# hobbies
@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")

# Jogos
@app.route("/jogos")
def jogos():
    jogos = ["gta 5","call of duty", "free fire"]
    return render_template("jogos.html", jogos = jogos)


if __name__ == '__main__':
    app.run(debug=True)