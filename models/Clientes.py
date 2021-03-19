from app import db
from flask import url_for


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    endereco = db.relationship('Endereco')
    endereco_id = db.Column(db.Integer, db.ForeignKey('enderecos.id'), nullable=False)

    def __repr__(self):
        return f"<Cliente {self.nome}, Endereço {self.endereco}>"

    def serialize(self):
        return {"id": self.id,
                "nome": self.nome,
                "endereco": self.endereco.serialize()}


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
