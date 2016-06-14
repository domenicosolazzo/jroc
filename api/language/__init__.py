from flask import Blueprint

language = Blueprint(
    'language',
    __name__
)

import views
