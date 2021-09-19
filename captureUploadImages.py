import cv2
import dropbox
import time
import random
print("Get ready with your project which needs to be captured...")
print("3")
print("2")
print("1")
startTime = time.time()
def takeSnapshot():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True 
    while(result):
        #read the frames while camera is on
        ret, frame = videoCaptureObject.read()
        #cv2.imwrite function is used to save an image to any storage device
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        startTime = time.time
        result = False
    return img_name
    print("Snapshot taken")
    #release the camera
    videoCaptureObject.release()
    #close all the windows that might be open while the process
    cv2.destroyAllWindows()

def upload_file(img_name):
    accessToken = "Ea1pT-BrzFYAAAAAAAAAAUnALPZz4j_DFRXGz8r-HgopYZ6nCwh-1l9kT10Qne1a"
    file = img_name
    fileFrom = file
    fileTo = "/Projects/" + (img_name)
    dbx = dropbox.Dropbox(accessToken)
    
    with open(fileFrom, "rb") as f:
        dbx.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=5):
            name = takeSnapshot()
            upload_file(name)

main()