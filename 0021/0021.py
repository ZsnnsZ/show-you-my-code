import os
from hashlib import sha256
from hmac import HMAC


def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8)  # 8 bytes = 64 bits.

    if not isinstance(password, str):
        password = str(password)

    result = password.encode('utf-8')

    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result

def validate_password(hashed, input_password):
    # print(encrypt_password(input_password, salt=hashed[:8]))
    return hashed == encrypt_password(input_password, salt=hashed[:8])

if __name__ == '__main__':
    password = 123456
    hashed = encrypt_password(password)
    # if not validate_password(hashed, password):
    #     print('succeed!')
    # else:
    #     print('wrong!')
    print(hashed)
