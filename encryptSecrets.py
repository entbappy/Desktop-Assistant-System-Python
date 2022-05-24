from desktop_entity_layer.encryption.encrypt_confidential_data import EncryptData

def secure_credentials():
    obj = EncryptData()
    key = input("Do you want to generate a new key? (y/n)")
    if key == 'y':
        obj.generateKey()
        print("Key has been generated! Save this key into your environment variable: SECRET_KEY & run this file again")
        return

    else:
        obj.generate_your_encrypted_email_password()
        atlas = input("Do you have atlas cluster credentials? (y/n) ")
        if atlas == 'y':
            obj.generate_your_encrypted_atlas_cluster_user_password()
        else:
            print("You can add atlas cluster credentials later, You can use local mongodb")
        return


if __name__ == '__main__':
    secure_credentials()