from cryptography.fernet import Fernet
import os
import json

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encryptId(id, role, dateOfCreation, clinicHistoryId):
    textToEncrypt = id + ',' + role + ',' + dateOfCreation + ',' + clinicHistoryId
    ciphered_text = cipher_suite.encrypt(textToEncrypt.encode('utf-8'))
    if os.path.exists('monitoring\id.json'):
        numLogs = 0
        with open('monitoring\id.json', 'r') as f:
            data = json.load(f)
            numLogs = len(data)
        with open('monitoring\id.json', 'w') as f:
            data[numLogs] = ciphered_text.decode('utf-8')
            json.dump(data, f)
    else:
        with open('monitoring\id.json', 'w') as f:
            data = {}
            data[0] = ciphered_text.decode('utf-8')
            json.dump(data, f)
    return ciphered_text

def decryptId(position):
    with open('monitoring\id.json', 'r') as f:
        data = json.load(f)
        ciphered_text = data.get(position)
        # pasar a bytes en base 64, usando el import base64
        coded_text = ciphered_text.encode('utf-8')
        unciphered_text = (cipher_suite.decrypt(coded_text)).decode('utf-8')
        return unciphered_text

#ciphered_text = encryptId('123456789', 'doctor', '2020-10-10', '11')
#print(ciphered_text)

#ciphered_text2 = encryptId('987654321', 'doctor', '2020-10-10', '12')
#print(ciphered_text2)

unciphered_text = decryptId('0')
print(unciphered_text)

unciphered_text2 = decryptId('1')
print(unciphered_text2)