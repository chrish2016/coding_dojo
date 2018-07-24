from flask import Flask
from flask_bcrypt import Bcrypt, check_password_hash, generate_password_hash

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'ThisIsSecretKey'

# password = 'hunter2'
# pw_hash = bcrypt.generate_password_hash(password)
# print pw_hash

# candidate = 'seet'
# bcrypt.check_password_hash(pw_hash, candidate)

pw_hash = generate_password_hash('hunter2', 10)
check_password_hash(pw_hash, 'hunter2')
if True:
     print "true"
else: print "false"

print pw_hash