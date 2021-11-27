import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):   
        dbx=dropbox.Dropbox(self.access_token)
        f=open (file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token='WdADGtqZlzEAAAAAAAAAATPeHzpB7HoeI9K5uPU4H25htxPzOkV-zmAlOEJsqXeh'
    transferData=TransferData(access_token)
    file_from=input("enter your file path to transfer:-")
    file_to=input("enter the file path where to upload:-")
    transferData.upload_file(file_from,file_to)
    print("success! it has transfered")

main()
