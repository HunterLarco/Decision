from app import db

from datetime import datetime


class Decision(db.Model):
  __tablename__ = 'decision'
  
  identifier = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  expiration = db.Column(db.DateTime)
  creationDateTime = db.Column(db.DateTime)
  options = db.relationship('Option', backref='decision', lazy='dynamic')

  def __init__(self, title, expiration, options, data={}):
    self.title = title
    self.expiration = expiration
    # self.options = options
    # self.data = data
    self.creationDateTime = datetime.utcnow()

  def __repr__(self):
    return 'Decision(title=%s, expiration=%s, identifier=%s)' % (self.title, self.expiration, self.identifier)


class Option(db.Model):
  __tablename__ = 'option'
  
  identifier = db.Column(db.Integer, primary_key=True)
  votes = db.Column(db.Integer, primary_key=True)
  decisionIdentifier = db.Column(db.Integer, db.ForeignKey('decision.identifier'))

  def __repr__(self):
    return '<Option %r>' % (self.body)