#!/usr/bin/env python
from flask import Flask, session, redirect, url_for, escape, request

PORT_NUMBER = 9998

# Check Configuration section for more details
SESSION_TYPE = 'redis'
app = Flask(__name__)
app.secret_key = 'any random string'
app.config.from_object(__name__)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/login/',methods=["POST","GET"])
def login():
    if (request.method == 'POST'):
        if(request.form['username']=='demo' and request.form['password']=='demo'):
            back = 'Logged in.'
            session['key'] = 'blah'
        else:
            back = 'Login error.'
    else:
        back = '<html><body><form method ="POST" action=".">Username:<input type="text" name="username"><br>Password:<input type="text" name="password"><br><input type="submit"></body></form></html>'
    return back

@app.route('/get/')
def get():
    return session.get('key', 'not set')

app.run(host='0.0.0.0', port=PORT_NUMBER, debug=True)