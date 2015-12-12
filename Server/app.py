import webapp2


class DecisionWithoutId(webapp2.RequestHandler):
  def post(self):
    self.response.out.write('without')


class DecisionWithId(webapp2.RequestHandler):
  def get(self, identifier):
    self.response.out.write('with')


app = webapp2.WSGIApplication([
  ('/decision/([^/]+)/?', DecisionWithId),
  ('/decision/?', DecisionWithoutId)
], debug=True)