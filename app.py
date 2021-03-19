from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.Clientes import Cliente, Endereco


@app.route('/')
def index():
    return 'Ola, mundo'


@app.route('/clientes', methods=['GET'])
def get_clientes():
    #clientes = Cliente.query.join(Endereco, Cliente.endereco_id == Endereco.id).all()
    clientes = Cliente.query.all()
    #clientes = Cliente.query.join(Endereco, Cliente.endereco_id == Endereco.id).add_columns(Endereco.rua).all()
    print(clientes)
    return jsonify([i.serialize() for i in clientes])


@app.route('/enderecos', methods=['GET'])
def get_enderecos():
    enderecos = Endereco.query.all()
    print(enderecos)
    return jsonify([i.serialize() for i in enderecos])


@app.route('/endereco/<id>', methods=['GET'])
def get_endereco(id):
    endereco = Endereco.query.filter_by(id=id).first()
    print(endereco)
    return jsonify(endereco.serialize())



if __name__ == '__main__':
    app.run(debug=True)
