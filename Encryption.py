from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import time
import pumongo
from pumong import MongoClient
import datetime
from datetime import datetime
import random

cluster = MongoClient(
    'mongodb+srv://test1:123@cluster0.hfj9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['Flame']
collection = db['arjdoroteo']

def aes_userdata():
    key = b'1234567890qwertyuiopasdfghjklzxc'
    iv = b'1q2w3e4r5t6y7u8i'
    
    plainName = b'Adrian Robert Doroteo'
    plainLocation = b'14.466762,120.974886'
    plainData = plainName + b',' + plainLocation
    
    cipher = AES.new(key,AES.MODE_CBC,iv)
    
    cipherText = cipher.encrypt(pad(plainData,AES.block_size))
    
    with open('cipher_file','wb') as c_file:
        c_file.write(key)
        c_file.write(iv)
        c_file.write(cipherText)
        
    return (cipherText)

def mongodbUpload(temp, co, gas, date_time, cipherText):
    post = {'User Info': cipherText, 'Date and Time': date_time, 'Temperature': temp, 'CO': co, 'LPG': gas}
    collection.insert_one(post)
    print('Uploaded')
    
x = True

temp_limit = 125
co_limit = 100
gas_limit = 10000

timer = 5

cipherText = aes_userdata()

while x == True:
    temp = random.randint(15,125)
    co = random.randint(0,100)
    gas = random.randint(0,10000)
    
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S") 
    if temp >= temp_limit or co >= co_limit or gas >= gas_limit:
        mongodbUpload(temp, co, gas, date_time, cipherText)
        if timer == 0:
            print('Timer Done!')
            timer = 5
            
    elif time == 0:
        mongodbUpload(temp, co, gas, date_time, cipherText)
        print('Timer Done!')
        timer = 5
        
    timer -= 1
    time.sleep(1)
    print(timer)
    print('Temp: ' + str(temp) + ' CO: ' + str(C0) + ' LPG: ' + str(gas)) 
