from app.database import db 

class Dulce(db.Model):
    __tablename__ = 'dulces'
    
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    sabor = db.Column(db.String(50), nullable=False)
    origen = db.Column(db.String(50), nullable=False)
    # Inicializa la clase 'Dulce'
    def __init__(self, marca, peso, sabor, origen):
        self.marca = marca
        self.peso = peso
        self.sabor = sabor
        self.origen = origen
    # Guarda un dulce en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()
    # Obtiene todos los dulces de la base de datos
    @staticmethod
    def get_all():
        return Dulce.query.all()
    # Obtiene un dulce por su ID
    @staticmethod
    def get_by_id(id):
        return Dulce.query.get(id)  #return Dulce.query.get(id) 
    # Actualiza un dulce en la base de datos
    def update(self, marca=None, peso=None, sabor=None, origen=None):
        if marca is not None:
            self.marca= marca
        if peso is not None:
            self.peso = peso
        if sabor is not None:
            self.sabor = sabor
        if origen is not None:
            self.origen = origen
        db.session.commit()
    # Elimina un dulce de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()