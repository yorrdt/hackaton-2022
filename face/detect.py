import cv2
import time

import variables
import compare


def detectFace(net, frame, conf_threshold=0.7):
    
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], False, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            face = frame.copy()
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 300)), 4)
            # cv2.putText(frame, "%.2f" % (confidence * 100), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
            
            top=x1
            right=y1
            bottom=x2-x1
            left=y2-y1
            
            face = face[right:right+left, top:top+bottom]
            if (variables.saveFrame == True):
                cv2.imwrite(variables.admin_path + "face%d.jpg" % variables.countOfAdmins, face)
                variables.countOfAdmins += 1
                cv2.imshow("savedFace", face)
                variables.saveFrame = not variables.saveFrame
                # print("face was saved")
            
            # cv2.imshow("Recognized Face", face)
            
            if (variables.compareFrameAndFace == True):
                compare.compareFaces(face)
                variables.compareFrameAndFace = not variables.compareFrameAndFace
                # compare.compareFaces(net, frame)
                

    return frame, bboxes