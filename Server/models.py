from google.appengine.ext import ndb
from datetime import datetime


class IdentifiedModel(ndb.Model):
  def identifier(self):
    return self.key.id()
  
  @classmethod
  def getByIdentifier(cls, identifier):
    return cls.get_by_id(identifier)


class ExpiringLink(IdentifiedModel):
  expiration = ndb.DateTimeProperty (indexed=True)
  
  @classmethod
  def create(cls, expiration):
    entity = cls(expiration=expiration)
    entity.put()
    return expiration
  
  @classmethod
  def use(cls, identifier):
    entity = cls.getByIdentifier(identifier)
    if entity == None:
      return False
    
    self.key.delete()
    return entity.expiration > datetime.now()
    

class Option(IdentifiedModel):
  title = ndb.TextProperty    (indexed=False)
  votes = ndb.IntegerProperty (indexed=False)


class Decision(IdentifiedModel):
  title      = ndb.TextProperty       (indexed=True )
  expiration = ndb.DateTimeProperty   (indexed=True )
  data       = ndb.PickleProperty     (indexed=False)
  options    = ndb.StructuredProperty (Option, indexed=False, repeated=True)