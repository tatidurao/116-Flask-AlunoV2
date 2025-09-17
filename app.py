# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/index")
def home():
    nome = "Kaiowa" # escreva seu nome
    idade = "14" # escreva sua idade
    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def home1():
    nome = "Louis" # escreva seu nome
    idade = "32" # escreva sua idade
    return render_template('pai.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/mae")
def home2():
    nome = "Preguiça de pensar um nome" # escreva seu nome
    idade = "31" # escreva sua idade
    return render_template('mae.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo
@app.route("/amigo")
def home3():
    nome = "David" # escreva seu nome
    idade = "14" # escreva sua idade
    return render_template('amigo.html' , nome = nome , idade = idade)

# adicione outras rotas, se você quiser

# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
