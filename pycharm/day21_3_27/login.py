import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(username, passwd):
    passwd_md5 = hashlib.md5()
    passwd_md5.update(passwd.encode('utf-8'))
    passwd_db = passwd_md5.hexdigest()
    for user, password in db.items():
        if user == username and password == passwd_db:
            return True
    return False


print(login('michael', '123456'))
