from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


from app import models


@app.route('/decision/', methods=['POST'])
def createDecision():
  admin = User('admin', 'admin@example.com')
  db.session.add(admin)
  db.session.commit()


@app.route('/decision/<identifier>/', methods=['GET'])
def getDecision(identifier=None):
  return 'Hello World!'


@app.route('/decision/<identifier>/votes/', methods=['POST', 'GET'])
def votes(identifier=None):
  return 'Hello World!'


if __name__ == '__main__':
  app.run(debug=True)