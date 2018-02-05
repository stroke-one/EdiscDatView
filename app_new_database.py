fom flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_populate.datlibs.datlibs import DatReader

import time
tm = time.time()

app = Flask(__name__)
app.config(['SQLALCHEMY_DATABASE_URI']) = 'sqlite:///tmp/test.db'
db = SQLAlchemy(app)

