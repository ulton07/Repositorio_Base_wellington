from flask import Flask, request, render_template

app = Flask(__name__)

# Página inicial explicando como usar
@app.route("/")
def index():
    return render_template("index.html")

#Primeira Rota é soma
@app.route("/soma")
def subtrair():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    return {"resultado": v1 + v2}

# Segunda é subtrair 
@app.route("/subtrair")
def subtrair():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    return {"resultado": v1 - v2}

# Terceira é multiplicar
@app.route("/multiplicar")
def multiplicar():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2,", 0))
    return {"resultado": v1 * v2}

# Terceira é dividir 
@app.route("/dividir")
def dividir():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 1)) #evita divisão por zero
    if v2 == 0:
        return {"error": "Divisão por zero não é permitida"}
    return {"resultado": v1 / v2}

# 🚨🚨🚨🚨🚨🚨🚨🚨🚨 Não mexa aqui, pois isso que executa o arquivo 🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨
if __name__ == "__main__":
    app.run(debug=True)


