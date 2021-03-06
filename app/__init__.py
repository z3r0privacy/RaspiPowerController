from flask import Flask, flash
from flask_bootstrap import Bootstrap
from gpiozero import OutputDevice
import os
import yaml
from .pseudoOutputDevice import PseudoOutputDevice
from .helper import addPermMessage, calculateSetValue



app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
if app.secret_key == "CHANGE_ME":
    raise Exception("default key not changed")

bootstrap = Bootstrap(app)

relais = yaml.safe_load(open(os.environ.get('APP_CONFIG')))['relais']
for i in range(len(relais)):
    try:
        relais[i]['device'] = OutputDevice(relais[i]['pin'], active_high=False, initial_value=calculateSetValue(relais[i]['failSafe'], relais[i]['startValue']))
    except:
        print("Only PseudoOutputDevice loaded for relais " + relais[i]['name'])
        addPermMessage("Only PseudoOutputDevice loaded for relais " + relais[i]['name'])
        relais[i]['device'] = PseudoOutputDevice(relais[i]['pin'])


""" relais = [
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
] """

from app import routes