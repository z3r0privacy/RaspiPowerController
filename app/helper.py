from flask import flash

messages = []

def clearPermMessags():
    messages.clear()

def addPermMessage(msg):
    messages.append(msg)

def flashPermMessages():
    for msg in messages:
        flash(msg, 'perm')

def calculateSetValue(failSafe, mode):
    # failsafe    mode    result
    # 0           0       0
    # 0           1       1
    # 1           0       1
    # 1           1       0
    return failSafe != mode

def calculateCurrentStatus(failSafe, status):
    # failsafe    status  result
    # 0           0       0
    # 0           1       1
    # 1           0       1
    # 1           1       0
    return failSafe != status