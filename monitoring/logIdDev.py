from cryptography.fernet import Fernet
import os
import json

key = Fernet.generate_key()
#print("La llave es: " + str(key))

def encryptId(id, role, dateOfCreation, clinicHistoryId):
    textToEncrypt = str(id) + ',' + str(role) + ',' + str(dateOfCreation) + ',' + str(clinicHistoryId)
    cipher_suite = Fernet(b'QeOzYI2XSk2tAiz1IAcdYnUrEGJzGPbsfwHeXIU4Ecw=')
    ciphered_text = cipher_suite.encrypt(textToEncrypt.encode('utf-8'))
    with open('id.json', 'w') as f:
        data = {}
        listIds = []
        listIds.append(ciphered_text.decode('utf-8'))
        data[clinicHistoryId] = listIds
        json.dump(data, f)
    return ciphered_text

def decryptId(position, key):
    with open('id.json', 'r') as f:
        data = json.load(f)
        cipher_suite = Fernet(key)
        ciphered_list = data.get(position)
        unciphered_list = []
        for i in ciphered_list:
            descifrado = cipher_suite.decrypt(i.encode('utf-8'))
            unciphered_list.append(descifrado.decode('utf-8'))
        return unciphered_list

#ciphered_text = encryptId('123456789', 'doctor', '2020-10-10', '11')
#print(ciphered_text)

#ciphered_text2 = encryptId('987654321', 'doctor', '2020-10-10', '12')
#print(ciphered_text2)

#unciphered_text = decryptId('11',  b'QeOzYI2XSk2tAiz1IAcdYnUrEGJzGPbsfwHeXIU4Ecw=')
#print(unciphered_text)

#unciphered_text2 = decryptId('12',  b'QeOzYI2XSk2tAiz1IAcdYnUrEGJzGPbsfwHeXIU4Ecw=')
#print(unciphered_text2)

# Falta: 1. Conectar con el POST de la API. 