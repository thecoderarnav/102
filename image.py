import cv2 as cv
import time
import random
import dropbox

start_time = time.time()
def take_snapshot():
    number = random.randint(0, 100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        img_name = "img"+ str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False

    return img_name   

    print("Screenshot Taken") 

    videocaptureobject.release()
    cv2.destroyAllWindows()

def upload_files(img_name):
    access_token = "YvEuTejtuXQAAAAAAAAAAaK1BM1h9ht6KfX0mfzxxm86xD9VX8Zz8ovr1WSpki3e"
    file = img_counter
    file_from = file
    file_to = "/newfolder1/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as F:
        dbx.files_upload(F.read(), file_to, mode = dropbox.files.WriteMode.override)

        print("File Has Been Uploaded")
    
def main():
     while(True):
         if ((time.time()-start_time)>= 2):
             name = take_snapshot()
             upload_files(name)       
main()