import threading

def xor_cipher(data, key):
    """
    XOR cipher for a given key
    """
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def is_valid_ascii(text):
    """
    Check if the text contains valid ASCII characters and specific substrings
    """
    try:
        decoded_text = text.decode('ascii')
        return 'crypto' in decoded_text or 'CRYPTO' in decoded_text
    except UnicodeDecodeError:
        return False

def find_key_for_length(encrypted_data, key_length):
    for key in range(256 ** key_length):
        key_bytes = key.to_bytes(key_length, 'big')
        decrypted_data = xor_cipher(encrypted_data, key_bytes)
        if is_valid_ascii(decrypted_data):
            print(f'Key: {key_bytes}')
            print(f'Decrypted data: {decrypted_data.decode("ascii")}')
            return

hex_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encrypted_data = bytes.fromhex(hex_string)

# Limiter la longueur de la clé (par exemple, 1 à 4 octets)
key_lengths_to_try = range(1, 5)

# Utiliser threading pour essayer différentes longueurs de clés en parallèle
threads = []

for key_length in key_lengths_to_try:
    print("trying key length of ", key_length)
    thread = threading.Thread(target=find_key_for_length, args=(encrypted_data, key_length))
    threads.append(thread)
    thread.start()

# Attendre que tous les threads se terminent
for thread in threads:
    thread.join()
