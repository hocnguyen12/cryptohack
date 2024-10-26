"""
    Privacy-Enhanced Mail ? challenge
"""

from Crypto.PublicKey import RSA

with open("privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem", "rb") as f:
    data = f.read()
    mykey = RSA.import_key(data)
    print(f"flag : {mykey.d}")
