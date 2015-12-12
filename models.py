from app import db


class Decision(db.Model):
  identifier = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  expiration = db.Column(db.DateTime)
  creationDateTime = db.Column(db.DateTime)

  def __init__(self, title, expiration, options, data={}):
    self.title = title
    self.expiration = expiration
    # self.options = options
    # self.data = data
    self.creationDateTime = datetime.utcnow()

  def __repr__(self):
    return 'Decision(title=%s, expiration=%s, identifier=%s)' % (self.title, self.expiration, self.identifier)
