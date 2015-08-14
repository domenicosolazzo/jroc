from flask import Blueprint 

tagger = Blueprint(
    'tagger',
    __name__
)

import views
