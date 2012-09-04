from flask import Flask
from modoverflow.database import db_session

app = Flask(__name__)
app.secret_key = 'fooooooo'
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

import modoverflow.routes
