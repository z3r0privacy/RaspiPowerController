from flask import Flask
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
bootstrap = Bootstrap(app)

relais = [
    {
        'name':'Radio',
        'isCurrentlyOn': True,
        'pinNumber':26
    },
    {
        'name':'Relais 2',
        'isCurrentlyOn': False,
        'pinNumber':27
    },
    {
        'name':'Relais 3',
        'isCurrentlyOn': False,
        'pinNumber':28
    }
]

from app import routes