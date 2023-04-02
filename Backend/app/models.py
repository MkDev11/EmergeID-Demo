from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idme_id = db.Column(db.String(100), nullable=False, unique=True)
    did = db.Column(db.String(100), nullable=False, unique=True)
    image_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User id={self.id} idme_id={self.idme_id} did={self.did} image_url={self.image_url}>"
