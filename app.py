from flask import Flask
from flask import render_template, request, url_for, session, redirect

import auth
from messages import *

app = Flask(__name__)
app.secret_key = b'aj(>,m&*@#NxmaiOxH23Kkmlb128($'

def is_logged_in():
    '''If 'username' is in the session as a key, return True.
    Otherwise, return False.'''
    return 'username' in session


@app.route("/")
@app.route("/messages/")
def show_messages():
    '''To do: If the user is logged in, render the 'messages.html' template
    together with the user's messages ('inbox').
    If the user is NOT logged in, redirect to the login page.'''
    if is_logged_in():
        user_messages = get_messages(session['username'])
        return render_template('messages.html', user_messages=user_messages)
    else:
        return redirect(url_for('login'))


@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        # Login was successful:
        if auth.login(username, password):
            session['username'] = username
            return redirect(url_for('show_messages'))
        else:
            return render_template('login.html')
    else:
        print('login with GET')
        return render_template('login.html')


@app.route("/logout/")
def logout():
    session.pop('username', None)
    return redirect(url_for('show_messages'))


@app.route("/message/<int:id>/")
def show_message(id):
    '''To do: find the given message by its id.
    Then display it in a rendered template.'''
    message = get_message(id)
    return render_template('message.html', message=message)


@app.route("/message/compose/", methods=["GET", "POST"])
def compose():
    if request.method == 'GET':
        users = auth.get_users()
        users.remove(session['username'])
        print(users)
        return render_template('compose.html', users=users)
    elif request.method == 'POST':
        message_data = request.form
        message_repacked = {'to': message_data['to'], 'from': message_data['from'], 'subject': message_data['subject'], 'body': message_data['body'], 'id': get_next_id(get_all_messages())}
        add(message_repacked)
        return redirect(url_for('show_messages'))
        '''To do: 'unpack' the form data, and process it:
        1. Prepare the data in an appropriate data structure
        2. Save the data to your data store (Make use of existing functions
            you may have)
        3. Once the data is saved to file, redirect to the /messages/ page.'''
@app.route("/messages/sent/")
def show_sent_messages():
    '''To do: If the user is logged in, render the 'messages.html' template
    together with the user's messages ('inbox').
    If the user is NOT logged in, redirect to the login page.'''
    user_messages = get_sent_messages(session['username'])
    return render_template('sent.html', user_messages=user_messages)