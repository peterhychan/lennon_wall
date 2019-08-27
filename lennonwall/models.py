from datetime import datetime
from lennonwall import db

class Message(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(50))
	body=db.Column(db.String(200))
	time=db.Column(db.DateTime, default=datetime.utcnow, index=True)