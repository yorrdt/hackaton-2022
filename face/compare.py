import cv2
import numpy as np
import os
import variables


def compareFaces(frame):

    face_path = variables.admin_path + "face2.jpg"
    if os.path.exists(face_path):
        admin_face = cv2.imread(face_path)
    else:
        print("Face not found")
        return
    
    net = cv2.dnn.readNetFromTorch("models/nn4.small2.v1.t7")
    
    face_img = cv2.imread(face_path)
    face_blob = cv2.dnn.blobFromImage(face_img, 1./255, (96, 96), (0, 0, 0), True, False)
    net.setInput(face_blob)
    face_representation = net.forward()

    frame_blob = cv2.dnn.blobFromImage(frame, 1./255, (96, 96), (0, 0, 0), True, False)
    net.setInput(frame_blob)
    frame_representation = net.forward()
    
    # print(os.listdir(variables.admin_path))
    
    norm = cv2.norm(face_representation, frame_representation)
    if cv2.norm(face_representation, frame_representation) < 0.60:
        print(f"verified: {norm}")
        return True
    else:
        print(f"unverified: {norm}")
        return False
    