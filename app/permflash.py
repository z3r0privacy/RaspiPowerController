from flask import flash

messages = []

def clearPermMessags():
    messages.clear()

def addPermMessage(msg):
    messages.append(msg)

def flashPermMessages():
    for msg in messages:
        flash(msg, 'perm')