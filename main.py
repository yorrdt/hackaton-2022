import cv2

# need stereocamera here cap_left, cap right
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while (True):

    frame = cap.read()
    
    if frame == False:
        print("frame not found")
        break
    
    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    
    if cv2.waitKey(1) == ord('q'):
        break
        
    cv2.imshow("frame", frame)
    cv2.imshow("blur", blur)
    
video.release()
cv2.destroyAllWindows()