import hashlib
import mysql.connector
import os

from flask import Flask, request


app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if "username" not in data:
        return "username is required", 400
    if "password" not in data:
        return "password is required", 400
    print(data)
    conn = mysql.connector.connect(
        user=os.environ.get('MYSQL_USER', 'app'),
        password=os.environ.get('MYSQL_PASSWORD', 'sapham'),
        host=os.environ.get('MYSQL_HOST', '127.0.0.1'),
        database=os.environ.get('MYSQL_DATABASE', 'app')
    )
    try:
        user = data['username']
        passwd = data['password']

        cur = conn.cursor()
        sql = """
        SELECT * from users where username='{}'
        """.format(user)
        cur.execute(sql)
        for (id, username, password) in cur:
            if password == hashlib.md5(passwd).hexdigest():
                return 'Correct'
        return 'Incorrect'
    except mysql.connector.Error as err:
        print(err)
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")