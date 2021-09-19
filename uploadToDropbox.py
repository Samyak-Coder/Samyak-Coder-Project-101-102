import dropbox
class TransferData:
    def __init__ (self, accessToken):
        self.accessToken = accessToken
    
    def uploadFiles(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        f = open(fileFrom, 'rb')
        dbx.files_upload(f.read(), fileTo)

def main():
    accessToken = 'bgYLbqBYtCoAAAAAAAAAARQGoGc2CzGZhdULZI--NXwg9wXj4nEJnjZS-07Kt4Hs'
    transferData = TransferData(accessToken)
    fileFrom = input("Enter the patj")
    fileTo = "/test2/tesst"
    # this is the full path to upload the file to, including the name that you want wish to be called once uploaded
    transferData.uploadFiles(fileFrom, fileTo)
    print("File has been moved")

main()