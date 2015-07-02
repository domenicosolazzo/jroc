from flask import Flask
from entities import entities
from tagger import tagger
from exceptions import make_json_app

app = Flask(__name__)
app = make_json_app(app)
# Puts the API blueprint on api.U2FtIEJsYWNr.com.
app.register_blueprint(entities, url_prefix='/entities')
app.register_blueprint(tagger, url_prefix='/tagger')
#app.debug = True

if __name__ == '__main__':
    #app.debug = True
    app.run()
