
from Crypto.Cipher import AES
from webapp import app
from base64 import b64encode, b64decode

def encrypt(username):
    if isinstance(username,str):
      username = username.encode("utf-8")
    cipher = AES.new(app.secret_key,AES.MODE_CTR)
    cipher_text = cipher.encrypt(username)
    cipher_text = b64encode(cipher_text).decode("utf-8")
    nonce = b64encode(cipher.nonce).decode("utf-8")
    return "{}.{}".format(cipher_text,nonce)

def decrypt(cookie_value):
    try:
        cipher_text, nonce = cookie_value.split(".")
        nonce = b64decode(nonce)
        cipher_text = b64decode(cipher_text)
        cipher = AES.new(app.secret_key,AES.MODE_CTR, nonce=nonce)
        username = cipher.decrypt(cipher_text)
    except Exception as e:
        print(e)
        username = ""
    return username
