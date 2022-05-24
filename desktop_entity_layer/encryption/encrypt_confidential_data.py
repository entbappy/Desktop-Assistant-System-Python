'''
Author: BOKTIAR AHMED BAPPY
Designation: Data Scientist
Date: 14/04/2022
Email: 1. boktiar@ineuron.ai  2. entbappy73@gmail.com
'''


import sys
import os
from cryptography.fernet import Fernet
from desktop_utils_layer.utils import CommonUtils
from desktop_exception_layer.exception import GenericException as EncyptException
import yaml


class EncryptData:

    def __init__(self):
        try:
            self.configs = CommonUtils().read_yaml('config.yaml')

        except Exception as e:
            encrypt_exception = EncyptException(
                "Failed during loading yaml file in module [{0}] class [{1}] method [{2}]"
                    .format(self.__module__, EncryptData.__name__,
                            self.__init__.__name__))
            raise Exception(encrypt_exception.error_message_detail(str(e), sys)) from e


   
    def generateKey(self):
        """
        Generates a key and save it into a file
        """
        try:
            key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(key)
            return key
        except Exception as e:
            raise Exception(e) from e


    def load_key(self):
        """
        Return secret key from environment variable:
        """
        try:
            key = os.environ.get('SECRET_KEY')
            return key
        except Exception as e:
            raise Exception(e) from e




    def encrypt_message(self,message,key=None):
        """
        Encrypts a message
        """
        try:
            encoded_message = message.encode()
            if key is None:
                key=self.load_key()
            f = Fernet(key)
            encrypted_message = f.encrypt(encoded_message)

            return encrypted_message

        except Exception as e:
            raise Exception(e) from e



    def decrypt_message(self,encrypted_message,key=None):
        """
        Decrypts an encrypted message
        """
        try:
            if key is None:
                key=self.load_key()
            f = Fernet(key)
            decrypted_message = f.decrypt(encrypted_message).decode("utf-8")
            return decrypted_message

        except Exception as e:
            raise Exception(e) from e


    
    def generate_your_encrypted_email_password(self):
        """
        Generates a password for email and encrypt it
        """
        try:
            password = input("Enter your email password: ")
            key = self.load_key()
            encrypted_password = self.encrypt_message(password,key)

            self.configs['EMAIL_CONFIG']['YOUR_EMAIL_PASS'] = encrypted_password

            with open('config.yaml', 'w') as f:
                    yaml.dump(self.configs, f)
            
            print("Your encrypted email password is saved")
        
        except Exception as e:
            raise Exception(e) from e

    


    def generate_your_encrypted_atlas_cluster_user_password(self):
        """
        Generates an user & password for atlas cluster and encrypt it
        """
        try:
            cluster_username = input("Enter your atlas cluster username: ")
            cluster_pass = input("Enter your atlas cluster password: ")
            
            key = self.load_key()
      
            encrypted_username = self.encrypt_message(cluster_username,key)
            encrypted_pass = self.encrypt_message(cluster_pass,key)

            self.configs['DATABASE_CONFIG']['ATLAS_CLUSTER_USERNAME'] = encrypted_username
            self.configs['DATABASE_CONFIG']['ATLAS_CLUSTER_PASSWORD'] = encrypted_pass

            with open('config.yaml', 'w') as f:
                    yaml.dump(self.configs, f)
            
            print("Your encrypted user & password are saved")
        
        except Exception as e:
            raise Exception(e) from e


    
    