from app import models, db
import datetime


d = models.Decision("test this decision",datetime.datetime.now(),[])
o = models.Option("this is an option", d)


db.session.add(d)
db.session.add(o)
db.session.commit()