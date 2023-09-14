from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(150), nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    important = db.Column(db.Boolean, nullable=False)
