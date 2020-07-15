from flask import render_template, redirect, url_for, request, flash
from app import app, relais

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', relais=relais)

@app.route('/toggleRelais', methods=['POST'])
def toggleRelais():
    rel = request.form['relaisName']
    print(rel + ' should be toggled')
    
    toggledSuccessfully = False
    found = False
    for r in relais:
        if r['name'] == rel:
            r['isCurrentlyOn'] = not r['isCurrentlyOn']
            toggledSuccessfully = True
            break

    if toggledSuccessfully:
        flash("Relais '" + rel + "' toggled successfully", 'success')
    elif not found:
        flash("Relais named '" + rel + "' not found", 'error')
    else:
        flash("Unknown error while trying to toggle relais '" + rel + "'", 'error')

    return redirect(url_for('index'))