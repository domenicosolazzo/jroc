from flask import Flask
from entities import entities
from tagger import tagger
from exceptions import make_json_app

app = Flask(__name__, instance_relative_config=True)
# Load configuration file (config.py)
app.config.from_object('config')
# Load configuration from the instance folder
app.config.from_pyfile('config.py')

# Exceptions will be returned as json responses
app = make_json_app(app)

# Puts the API blueprint on api.U2FtIEJsYWNr.com.
app.register_blueprint(entities, url_prefix='/entities')
app.register_blueprint(tagger, url_prefix='/tagger')

if __name__ == '__main__':
    app.run()
