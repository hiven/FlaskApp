from app import db

class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    notes = db.Column(db.String, nullable=True)

    def __init__(self, name, notes):
        self.name = name
        self.notes = notes

    def __repr__(self):
        return '<id {}>'.format(self.id)