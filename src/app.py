from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lista-clientes")
def listaClientes():
    return render_template("ListaClientes.html")

@app.route("/nuevo-cliente")
def nuevoCliente():
    return render_template("NuevoCliente.html")