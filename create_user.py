import mysql.connector
import hashlib

users = [
    ('user1', 'password1'),
    ('user2', 'password2')
]

try:
    conn = mysql.connector.connect(
        user='app',
        password='sapham',
        host='127.0.0.1',
        database='app'
    )
    cur = conn.cursor()

    sql = """
    DROP TABLE users
    """
    print("Drop table users if exists")
    cur.execute(sql)
    print("Create table users")
    sql = """
    CREATE TABLE IF NOT EXISTS `users`(
        `id` int(11) not null auto_increment primary key,
        `username` varchar(100) not null,
        `password` varchar(100) not null
    )
    """

    cur.execute(sql)
    
    print("Insert user to table users")

    for user in users:
        password = hashlib.md5(user[1]).hexdigest()
        sql = """
        INSERT INTO users(username, password)
        VALUES ('{}', '{}')
        """.format(user[0], password)
        cur.execute(sql)
    
    conn.commit()
    # cur = conn.cursor()
    sql = """
    SELECT * from users
    """
    cur.execute(sql)
    for (id, username, password) in cur:
        print "{} {}".format(username, password)
except mysql.connector.Error as err:
    print(err)
finally:
    conn.close()