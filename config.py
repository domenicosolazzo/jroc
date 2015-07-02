# -*- coding: UTF-8 -*-
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

# Gives you some handy tools for debugging errors. This includes a web-based stack trace and interactive Python console for errors.
DEBUG=os.environ.get("DEBUG", False)

# This is a secret key that is used by Flask to sign cookies. It’s also used by extensions like Flask-Bcrypt.
# You should define this in your instance folder to keep it out of version control. You can read more about instance folders in the next section.
# This should be a complex random value.
SECRET_KEY=os.environ.get("SECRET_KEY", "youshouldchangethis")
