import os
import dropbox
from dropbox.files import WriteMode


def main():
    accesstoken = ''
    transferData = TransferData(access_token)

    filefrom = str(input("Enter the folder path to transfer : "))
    fileto = input("Enter full path of file to upload to dropbox: ")  

    transferData.upload_file(file_from,file_to)
    print("The file has been moved")

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        
        for root, dirs, files in os.walk(filefrom):

            for filename in files:
                
                localpath = os.path.join(root, filename)

                relativepath = os.path.relpath(localpath, file_from)
                dropboxpath = os.path.join(fileto, relative_path)
               
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))



main()