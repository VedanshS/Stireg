import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.realpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path,'rb') as f:
                    dbx.files.upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))

def main():
    access_token = 'ETlWzY8-UGUAAAAAAAAAAe3-Bor428omUjevAGIas5xO76OtmvAPf4FGQbUog8Lx'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer: "))
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.uploadFile(file_from,file_to)

if __name__ == "__main__":
    main()