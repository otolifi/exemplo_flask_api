from flask import Flask, jsonify, request, session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.Clientes import Cliente, Endereco, Telefone, Pet, pets_has_clientes


@app.route('/clientes')
def get_clientes():
    lista = dict()
    result = Cliente.query.join(pets_has_clientes).all()
    #print(result)
    for x in result:
        lista[str(x.id)] = x.serialize()
        #print('x=', x.nome)
        for pet in x.pets:
            print('pet=', pet.serialize())
            lista[str(x.id)][str(pet.id)] = pet.serialize()
    #print(lista)
    return lista


@app.route('/')
def index():
    return 'Ola, mundo'

'''
@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    print(clientes)
    return jsonify([i.serialize() for i in clientes])
    '''


@app.route('/enderecos', methods=['GET'])
def get_enderecos():
    enderecos = Endereco.query.all()
    print(enderecos)
    return jsonify([i.serialize() for i in enderecos])


@app.route('/endereco', methods=['POST'])
def novo_endereco():
    
    data = request.get_json()
    #endereco = Endereco(request.get_json())
    print(data['rua'])
    endereco = Endereco(rua=data['rua'], cep=data['cep'], bairro=data['bairro'], cidade=data['cidade'], uf=data['uf'])
    
    db.session.add(endereco)
    db.session.commit()

    return "ok"


@app.route('/pets/<id>', methods=['GET'])
def get_pets_by_id(id):
    pets = Pet.query.filter_by(id=id)
    print(pets)
    return jsonify([i.serialize() for i in pets])


@app.route('/pets', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    print(pets)
    return jsonify([i.serialize() for i in pets])


@app.route('/endereco/<id>', methods=['GET'])
def get_endereco(id):
    endereco = Endereco.query.filter_by(id=id).first()
    print(endereco)
    return jsonify(endereco.serialize())


@app.route('/teste')
def get_teste():
    end = get_pets()
    print(end)

    return end



if __name__ == '__main__':
    app.run(debug=True)
