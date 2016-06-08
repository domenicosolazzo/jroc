# -*- coding: UTF-8 -*-
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

# Gives you some handy tools for debugging errors. This includes a web-based stack trace and interactive Python console for errors.
DEBUG=os.environ.get("DEBUG", False)

# Tag manager type: tag-nostat-bm.sh, tag-bm.sh, tag-nostat-nn.sh
OBT_TYPE = os.environ.get('OBT_TYPE', 'tag-bm.sh')

# This is a secret key that is used by Flask to sign cookies. It’s also used by extensions like Flask-Bcrypt.
# You should define this in your instance folder to keep it out of version control. You can read more about instance folders in the next section.
# This should be a complex random value.
SECRET_KEY=os.environ.get("SECRET_KEY", "youshouldchangethis")

# Basic auth (only if both username and password are set)
if os.environ.get('BASIC_AUTH_USERNAME', None) and os.environ.get('BASIC_AUTH_PASSWORD', None):
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME','')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD','')
    # If set to True, makes the whole site require HTTP basic access authentication.
    BASIC_AUTH_FORCE = True
