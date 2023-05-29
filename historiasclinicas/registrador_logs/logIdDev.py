from cryptography.fernet import Fernet
import os
import json

key = Fernet.generate_key() 
#print("La llave es: " + str(key))

def encryptId(id, role, dateOfCreation, clinicHistoryId):
    textToEncrypt = str(id) + ',' + str(role) + ',' + str(dateOfCreation) + ',' + str(clinicHistoryId)
    cipher_suite = Fernet(b'QeOzYI2XSk2tAiz1IAcdYnUrEGJzGPbsfwHeXIU4Ecw=')
    ciphered_text = cipher_suite.encrypt(textToEncrypt.encode('utf-8'))
    with open('./registrador_logs/id.json', 'r') as f:
        data = json.load(f)
    with open('./registrador_logs/id.json', 'w') as f:
        if clinicHistoryId in data:
            listIds = list(data.get(clinicHistoryId))
            listIds.append(ciphered_text.decode('utf-8'))
            data[clinicHistoryId] = listIds
        else:
            listIds = []
            listIds.append(ciphered_text.decode('utf-8'))
            data[clinicHistoryId] = listIds
        json.dump(data, f)
    return ciphered_text

def decryptId(position, key):
    with open('./registrador_logs/id.json', 'r') as f:
        data = json.load(f)
        cipher_suite = Fernet(key)
        ciphered_list = data.get(position)
        unciphered_list = []
        for i in ciphered_list:
            descifrado = cipher_suite.decrypt(i.encode('utf-8'))
            unciphered_list.append(descifrado.decode('utf-8'))
        return unciphered_list

def decryptId2(mensaje, key):
    cipher_suite = Fernet(key)
    unciphered_text = (cipher_suite.decrypt(mensaje))
    return cipher_suite.decrypt(mensaje.encode('utf-8'))
 
#print(decryptId2('gAAAAABkVeKBLEbPXdNaadx6yTwP0_09CCobTxm8DOtj2JgFNAXxhESrbDz8H5196gvIy3Foix763DD0g1ncJFIblWDPcvHCzN7MDatLei3ZHTBV6wOR_a3yUupFzsOBNDJZSFe7et_1', b'QeOzYI2XSk2tAiz1IAcdYnUrEGJzGPbsfwHeXIU4Ecw='))
