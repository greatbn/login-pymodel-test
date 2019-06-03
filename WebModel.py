"""
Model-Based Security Testing Web
"""

import requests

mode = 'Initializing'  # can't call it 'state', that has special meaning
usersLoggedIn = list()

login_url = 'http://localhost:5000/login'

def Initialize():
    global mode
    mode = 'Running'

def InitializeEnabled():
    return mode == 'Initializing'


def Login(user, passwd):
    try:
        body = {
            'username': user,
            'password': passwd
        }
        r = requests.post(login_url, json=body)
        if r.content == 'Correct':
            global mode
            mode = 'LogedIn'
        return r.content
    except Exception as err:
        print(err)

def LoginEnabled(user, passwd):
    return (mode == 'Running' and user not in usersLoggedIn)



state = ('mode',)

actions = (Login, Initialize)


users = ['VinniPuhh', 'OleBrumm', 'user1']
passwords = ['Correct', 'Incorrect', 'password1']

domains = { Login: {'user': users, 'passwd': passwords}}

enablers = { Initialize:(InitializeEnabled,), Login: (LoginEnabled,)}


def Reset():
    global mode
    mode = 'Initializing'
