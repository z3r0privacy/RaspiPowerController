from flask import render_template, redirect, url_for, request, flash
from app import app, relais
from .helper import flashPermMessages, calculateCurrentStatus
import sys

@app.route('/')
@app.route('/index')
def index():
    flashPermMessages()
    return render_template('index.html', relais=relais, isOn=calculateCurrentStatus)

@app.route('/toggleRelais', methods=['POST'])
def toggleRelais():
    rel = request.form['relaisName']
    print(rel + ' should be toggled')
    
    toggledSuccessfully = False
    found = False
    for r in relais:
        if r['name'] == rel:
            found = True
            try:
                r['device'].toggle()
                toggledSuccessfully = True
            except:
                pass
            break

    if toggledSuccessfully:
        flash("Relais '" + rel + "' toggled successfully", 'success')
    elif not found:
        flash("Relais named '" + rel + "' not found", 'error')
    else:
        flash("Unknown error while trying to toggle relais '" + rel + "'", 'error')

    return redirect(url_for('index'))

@app.route('/restartService', methods=['POST'])
def restartService():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return ('', 204)