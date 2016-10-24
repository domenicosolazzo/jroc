from flask import Blueprint

ner = Blueprint(
    'ner',
    __name__
)

import views
