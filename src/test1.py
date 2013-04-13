import webapp2




class Test1(webapp2.RequestHandler):

    def get(self):
        self.response.content-type
        self.response.out.write("this is something")

app = webapp2.WSGIApplication([('/', Test1)],
                              debug=True)