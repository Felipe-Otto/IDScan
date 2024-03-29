from flask import Flask
from flask_restful import Api
from Document.DocumentRest import Document

app = Flask(__name__)
api = Api(app)

api.add_resource(Document, '/document')

if __name__ == '__main__':
    app.run(debug=True)