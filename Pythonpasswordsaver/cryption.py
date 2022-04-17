from cryptography.fernet import Fernet
import sqlite3
import mariadb
import sys
import numpy as np

def generate_key():
    key = Fernet.generate_key()

    return key


def load_key():
    return generate_key()


def encrypt_pass(password):
    key = load_key()
    a = key
    encoded_password = password.encode()
    f = Fernet(key)
    print(a)
    print(type(a))
    encrypted_password = f.encrypt(encoded_password)


    return encrypted_password, a


def decrypt_pass():
    try:
        connection = mariadb.connect(
            user = 'root',
            password = 'Kesandzsm3354',
            host = 'database-1.czrchfylrgcw.us-east-1.rds.amazonaws.com',
            port = 3306,
            database = 'pass1'
            )  
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1) 

    veritabani_sec = connection.cursor()
    veritabani_sec.execute("""SELECT password, privateKey  FROM userpass LIMIT 0,1 """)
    data = veritabani_sec.fetchall()

    passw = data[0][0]
    key = data[0][1]

    connection.commit()
    connection.close()
    f = Fernet(key)
    decrypted = f.decrypt(passw)
    depass = decrypted.decode()
    return depass


def decrypt2():
    try:
        connection = mariadb.connect(
            user = 'root',
            password = 'Kesandzsm3354',
            host = 'database-1.czrchfylrgcw.us-east-1.rds.amazonaws.com',
            port = 3306,
            database = 'pass1'
            )  
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1) 

    veritabani_sec = connection.cursor()
    veritabani_sec.execute("""SELECT password, privateKey  FROM ppass """)
    data = veritabani_sec.fetchall()
    # print(data)

    vt = connection.cursor()
    vt.execute("SELECT COUNT(password) FROM ppass ")
    data2 = vt.fetchall()
    son = data2[0][0]

    liste1 = []
    liste2 = []

    i = 0
    while i < son  :
        passw = data[i][0]
        key = data[i][1]
        liste1.append(passw)
        liste2.append(key)

        i=i+1





    j = 0
    real = []
    while j < son :
        f = Fernet(liste2[j])
        decrypted = f.decrypt(liste1[j])
        depass = decrypted.decode()
        real.append(depass)
        j = j + 1
    connection.commit()
    connection.close()

    return real

