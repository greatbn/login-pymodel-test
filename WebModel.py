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
        r = requests.post(url, json=body)
        if r.content == 'Correct':
            print("OK")
            global mode, usersLoggedIn
            usersLoggedIn.append(user)
            mode = 'LogedIn'
        return r.content
    except mysql.connector.Error as err:
        print(err)
    finally:
        conn.close()

def LoginEnabled(user, passwd):
    return (mode == 'Running' and user not in usersLoggedIn)



state = ('mode', 'usersLoggedIn')

actions = (Initialize, Login,)


# users = ['VinniPuhh', 'OleBrumm', 'user1']
# passwords = ['Correct', 'Incorrect', 'password1']

# domains = { Login: {'user': users, 'passwd': passwords}}

enablers = { Initialize:(InitializeEnabled,), Login: (LoginEnabled,)}


def Reset():
    global mode
    mode = 'Initializing'
