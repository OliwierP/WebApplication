import hashlib
import os
import random

"""
"""

def hash_passwd(passwd, n=32):
    """
	Funkcja hash_passwd sluzy do generowanie soli oraz hasha
	
	Parameters
	----------
	passwd(): haslo
	n(int): gorna granica zakresu liczb z posrod ktorych losowana jest liczba dla soli

	Returns
	-------
	_salt(int): sol
	_hash(int): hash
    """
    _salt = os.urandom(n)
    _hash = hashlib.pbkdf2_hmac("sha256", passwd.encode("utf-8"), _salt, 100000)
    return _salt, _hash

