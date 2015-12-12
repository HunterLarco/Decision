import webapp2
from json import loads, dumps
import datetime

from models import Decision, Option


def parameters(*params):
  def decorator(func):
    def helper(self, *args, **kwargs):
      body = loads(self.request.body)
      for param in params:
        if not param in body:
          return self.error(400)
        kwargs[param] = body[param]
      return func(self, *args, **kwargs)
    return helper
  return decorator


def openendpoint(func):
  def helper(self, *args, **kwargs):
    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, OPTIONS'
    self.response.headers['Access-Control-Allow-Credentials'] = 'true'
    self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    self.response.headers['Content-Type'] = 'application/json'
    return func(self, *args, **kwargs)
  return helper


class DecisionWithoutId(webapp2.RequestHandler):
  @openendpoint
  @parameters('title', 'expiration', 'options', 'data')
  def post(self, title=None, expiration=None, options=None, data=None):
    entity = Decision()
    
    entity.title = title
    entity.data = data
    entity.options = map(lambda x: Option(title=x), options)
    entity.setAge(expiration)
    
    entity.put()
    
    self.response.out.write(dumps({
      'identifier': entity.identifier()
    }))


class DecisionWithId(webapp2.RequestHandler):
  @openendpoint
  def get(self, decisionIdentifier):
    entity = Decision.getByIdentifier(decisionIdentifier)
    if entity is None:
      return self.error(406)
    
    self.response.out.write(dumps({
      'identifier': entity.identifier(),
      'title': entity.title,
      'data': entity.data,
      'expiration': entity.getAge(),
      'options': map(lambda option: {
        'title': option.title,
        'votes': option.votes
      }, entity.options)
    }))


class Votes(webapp2.RequestHandler):
  @openendpoint
  def get(self, decisionIdentifier, optionIndex):
    entity = Decision.getByIdentifier(decisionIdentifier)
    if entity is None:
      return self.error(406)
    
    option = entity.options[int(optionIndex)]
    self.response.out.write(dumps({
      'votes': option.votes
    }))
  
  @openendpoint
  def post(self, decisionIdentifier, optionIndex):
    entity = Decision.getByIdentifier(decisionIdentifier)
    if entity is None:
      return self.error(406)
    
    option = entity.options[int(optionIndex)]
    option.votes += 1
    entity.put()
    


app = webapp2.WSGIApplication([
  ('/decision/([^/]+)/votes/([^/]+)?', Votes),
  ('/decision/([^/]+)/?', DecisionWithId),
  ('/decision/?', DecisionWithoutId)
], debug=True)