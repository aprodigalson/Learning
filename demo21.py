import os
import hashlib


def encrypt_password(password):
    salt = os.urandom(8)
    r = hashlib.sha256(password.encode()+salt).hexdigest()
    return salt, r


def check_password(u, password):
    salt = u['salt']
    return hashlib.sha256(password.encode()+salt).hexdigest() == user['password']


user = {'password': '', 'salt': b''}

raw_password = 'password'

user['salt'], user['password'] = encrypt_password(raw_password)
result = check_password(user, raw_password)

print(result)


# use md5 to encrypt
db = {}


def get_md5(password):
    a = hashlib.md5()
    a.update(password.encode('utf-8'))
    return a.hexdigest()


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


def login(username, password):
    b = get_md5(password + username + 'the-Salt')
    print(b)
    if b == db[username]:
        return True
    return False


un = "guyueyu"
psd = "password"
register(un, psd)
print(db)
print(login(un, psd))