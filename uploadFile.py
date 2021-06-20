import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(fileFrom):
            path = input("Enter folder path")
        f = open(fileFrom, 'rb')
        dbx.files_upload(f.reas(),fileTo,mode=WriteMode('overwrite'))
    
def main():
    access_token = input("Enter access token")
    x = TransferData(access_token)

    fileFrom = input("Enter path to file of whoch you want to upload")
    fileTo = input("Enter path of cloud file you want to transfer the file to")
    
    x.upload(fileFrom,fileTo)
    print("File has been moved to dropbox")


            



        

    

    