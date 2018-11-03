import base64
import config.app as APP

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

class Enigma:

    @staticmethod
    def encrypt(raw, key = APP.SECRET_KEY):
        ''' Encrypts raw text data using a key '''
        key = SHA256.new(key.encode()).digest()
        raw = Enigma._pad(32, raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    @staticmethod
    def decrypt(enc, key = APP.SECRET_KEY):
        ''' Decrypts encrypted text data using a key '''
        key = SHA256.new(key.encode()).digest()
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return Enigma._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    @staticmethod
    def _pad(bs, s):
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    @staticmethod
    def hash(data):
        ''' creates a presentable salted hash '''
        from werkzeug import generate_password_hash
        verifyHash = ':'.join(generate_password_hash(data).split('$')[1:])
        return verifyHash

    @staticmethod
    def verify(verifyHash, data):
        ''' verifies presentable salted hash '''
        from werkzeug import check_password_hash
        verifyHash = 'pbkdf2:sha256:50000$%s' % ('$'.join(verifyHash.split(':')))
        return check_password_hash(verifyHash, data)