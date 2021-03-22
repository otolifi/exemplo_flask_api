from app import db
from flask import url_for, session



class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    endereco = db.relationship('Endereco')
    endereco_id = db.Column(db.Integer, db.ForeignKey('enderecos.id'), nullable=False)
    telefone = db.relationship('Telefone')
    telefone_id = db.Column(db.Integer, db.ForeignKey('telefones.id'), nullable=False)
    
    pets = db.relationship('Pet', secondary='pets_has_clientes', backref='clientes')
    '''pets = db.relationship('Pet', secondary='pets_has_clientes', lazy='subquery', backref=db.backref('clientes', lazy=True))'''
    '''pets = db.relationship('Pet', secondary='pets_has_clientes', lazy='subquery', backref=db.backref('clientes', lazy=True))'''

    def __repr__(self):
        return f"<Cliente {self.nome}, Endereço {self.endereco}>"

    def serialize(self):
        return {"id": self.id,
                "nome": self.nome,
                "endereco": self.endereco.serialize(),
                "telefone": self.telefone.serialize(),
                #"pets": self.pets.serialize_list()
                }

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    raca = db.Column(db.String(45), nullable=False)
    porte = db.Column(db.String(10), nullable=False)
    genero = db.Column(db.String(1), nullable=False)
    especie = db.Column(db.String(15), nullable=False)


    #clientes = db.relationship('Cliente', secondary='pets_has_clientes', backref='pets')
    '''
    clientes = db.relationship('Cliente', secondary='pets_has_clientes', lazy='subquery',
        backref=db.backref('pets', lazy=True))'''

    def __repr__(self):
        return f"<Pet {self.nome}>" #, Cliente {self.cliente.serialize()}

    def serialize(self):
        return {"id": self.id,
                "nome": self.nome,
                "raca": self.raca}
    
    


pets_has_clientes = db.Table('pets_has_clientes',
    db.Column('cliente_id', db.Integer, db.ForeignKey('clientes.id'), primary_key=True),
    db.Column('pet_id', db.Integer, db.ForeignKey('pets.id'), primary_key=True)
)

class Endereco(db.Model):
    __tablename__ = 'enderecos'
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(60), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(45), nullable=False)
    cidade = db.Column(db.String(45), nullable=False)
    uf = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return f'<Endereco {self.rua}>'

    def serialize(self):
        return {"id": self.id,
                "rua": self.rua,
                "cidade": self.cidade}


class Telefone(db.Model):
    __tablename__ = 'telefones'
    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String(11), nullable=False, unique=True)

    def __repr__(self):
        return f'<Telefone {self.telefone}>'

    def serialize(self):
        return {"id": self.id,
                "telefone": self.telefone}



