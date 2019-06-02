"""
Model-Based Security Testing Web
"""

import mysql.connector
import hashlib

mode = 'Initializing'  # can't call it 'state', that has special meaning
usersLoggedIn = list()


def Initialize():
    global mode
    mode = 'Running'

def InitializeEnabled():
    return mode == 'Initializing'


def Login(user, passwd):
    try:
        conn = mysql.connector.connect(
            user='app',
            password='sapham',
            host='127.0.0.1',
            database='app'
        )
        cur = conn.cursor()
        sql = """
        SELECT * from users where username='{}'
        """.format(user)
        print(sql)
        cur.execute(sql)
        for (id, username, password) in cur:
            if password == hashlib.md5(passwd):
                usersLoggedIn.append(user) 
                return 'Correct'
        return 'Incorrect'
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
