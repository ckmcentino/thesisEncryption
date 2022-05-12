from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import time
import pymongo
from pymongo import MongoClient
import datetime
from datetime import datetime

cluster = MongoClient('mongodb+srv://test1:123@cluster0.hfj9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['Flame']
collection = db['arjdoroteo']

# Encrypts user's name and location, writes to file, and returns cipher
def aes_userdata():
    key = get_random_bytes(32)
    iv = get_random_bytes(16)
    # plainName = input('Enter Name: ').encode('ascii')
    # plaintLocation = input('Enter Location: ').encode('ascii')
    plainName = b'Adrian Robert Doroteo'
    plainLocation = b'Las Pinas City'
    plainData = plainName +b','+ plainLocation
    cipher = AES.new(key,AES.MODE_CBC,iv)

    cipherText = cipher.encrypt(pad(plainData, AES.block_size))

    with open('cipher_file', 'wb') as c_file:
        c_file.write(key)
        c_file.write(iv)
        c_file.write(cipherText)
    return str(cipherText)

#Uploads data to Mongodb
def mongodbUpload(temp, co, gas, date_time, cipherText):
    post = {'User Info':cipherText,'Date and Time': date_time,'Temperature' : temp, 'CO': co, 'LPG': gas}
    collection.insert_one(post)
    print ('Uploaded')

x = True
temp = 69
temp_limit = 125

co = 50
co_limit = 100

gas = 150
gas_limit = 10000

timer = 5

cipherText = aes_userdata()

while x == True:
    
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    if temp >= temp_limit or co >= co_limit or gas >= gas_limit:
        mongodbUpload(temp, co, gas, date_time, cipherText)
        if timer == 0:
            print('Timer Done!')
            timer = 5

    elif timer == 0:
        mongodbUpload(temp, co, gas, date_time, cipherText)
        print('Timer Done!')
        timer = 5

    timer-= 1
    time.sleep(1)
    print(timer)
