import cv2
import os
import tkinter as tk
from tkinter import font as tkFont
from deepface import DeepFace
import glob
import pickledb

images = glob.glob('database/user*.jpg')
count_of_users = len(images)
print(count_of_users, " ", images)

root = tk.Tk()
root.title("Automated wardrobe console")
root.geometry("480x640")
root.resizable(False, False)

helv36 = tkFont.Font(family='Helvetica', size=28, weight='bold')

def verify(frame):
    global count_of_users, images
    count_of_users+=1
    for i in range(1, count_of_users): # first input of true or false
        result = DeepFace.verify(frame, "database/user" + str(i) + ".jpg", "VGG-Face")
        if result["verified"] == True:
            dress_is_appear_window = tk.Tk()
            dress_is_appear_window.title("Automated wardrobe console")
            dress_is_appear_window.geometry("480x640")
            dress_is_appear_window.resizable(False, False)
                
            tk.Label(text="Your clothes are waiting for you in the wardrobe").pack(expand=True)
            
            # TODO: Delete user from DB
               
            dress_is_appear_window.mainloop()
            exit(0)
                
        else:
            # count_of_users+=1
            cv2.imwrite("database/user" + str(count_of_users) + ".jpg", frame);
               
            user_id_window = tk.Tk()
            user_id_window.title("Automated wardrobe console")
            user_id_window.geometry("480x640")
            user_id_window.resizable(False, False)
                
            tk.Label(text="Your number id: " + str(count_of_users)).pack(expand=True)
                
            user_id_window.mainloop()
            exit(0)
                

def start_button_click():
    global count_of_users
    root.destroy()
    
    cascPath = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    db = pickledb.load('database/auto-wardrobe.db', False)
    video = cv2.VideoCapture(0)
    
    while (True):
        ret, frame = video.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=8,
            minSize=(200, 200),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        for (x, y, w, h) in faces:
            if w > 200:
                if count_of_users == 0:
                    count_of_users+=1
                    cv2.imwrite("database/user" + str(count_of_users) + ".jpg", frame[y:y + h, x:x + w]);
                       
                    user_id_window = tk.Tk()
                    user_id_window.title("Automated wardrobe console")
                    user_id_window.geometry("480x640")
                    user_id_window.resizable(False, False)
                        
                    tk.Label(text="Your number id: " + str(count_of_users)).pack(expand=True)
                        
                    user_id_window.mainloop()
                    exit(0)
                verify(frame[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
        if cv2.waitKey(1) == ord('q'):
            break
            
        cv2.imshow("Automated wardrobe console", frame)
    
    video.release()
    cv2.destroyAllWindows()


tk.Button(text="Start", font=helv36, command=start_button_click).pack(expand=True)
root.mainloop()