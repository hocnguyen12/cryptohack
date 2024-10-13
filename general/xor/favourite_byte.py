import base64
import codecs
from Cryptodome.Util import number as nb

def xor_cipher(data, key):
    """
    XOR cipher for a single-byte key
    """
    return bytes([b ^ key for b in data])

text = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encrypted_data = bytes.fromhex(text)

for key in range(256):
    decrypted_data = xor_cipher(encrypted_data, key)
    try:
        decrypted_text = decrypted_data.decode('ascii')
        if 'crypto' in decrypted_text or 'CRYPTO' in decrypted_text:
            print(f'Key: {key}')
            print(decrypted_text)
    except UnicodeDecodeError:
        continue
