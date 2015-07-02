# Gives you some handy tools for debugging errors. This includes a web-based stack trace and interactive Python console for errors.
DEBUG=False

# This is a secret key that is used by Flask to sign cookies. It’s also used by extensions like Flask-Bcrypt.
# You should define this in your instance folder to keep it out of version control. You can read more about instance folders in the next section.
# This should be a complex random value.
SECRET_KEY="secret_key"

# If you’re using Flask-Bcrypt to hash user passwords, you’ll need to specify the number of “rounds” that the algorithm executes in hashing a password. If you aren’t using Flask-Bcrypt, you should probably start. The more rounds used to hash a password, the longer it’ll take for an attacker to guess a password given the hash.
# The number of rounds should increase over time as computing power increases.
BCRYPT_LEVEL = 12
