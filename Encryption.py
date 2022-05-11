from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
iv = get_random_bytes(16)
plainText = b'Your mission should you choose to accept it is to impeach the President of the Philippines'
cipher = AES.new(key,AES.MODE_CBC,iv)

cipherText = cipher.encrypt(pad(plainText, AES.block_size))

with open('cipher_file', 'wb') as c_file:
    c_file.write(key)
    c_file.write(iv)
    c_file.write(cipherText)

