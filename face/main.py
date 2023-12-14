import cv2
import time

# local modules
import variables
import detect

video_capture = cv2.VideoCapture(0)
time.sleep(2)

# load face detection model
modelFile = "models/res10_300x300_ssd_iter_140000_fp16.caffemodel"
configFile = "models/deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

while True:
    try:
        _, frameOrig = video_capture.read()
        frame = cv2.resize(frameOrig, (640, 480))

        if (variables.detectionEnabled == True):
            frame, bboxes = detect.detectFace(net, frame)

        # cv2.namedWindow('FaceID window', cv2.WINDOW_KEEPRATIO)
        cv2.imshow('FaceID window', frame)
        # cv2.resizeWindow('FaceID window', 320, 240) # 640*480

    except Exception as e:
        print(f'exc: {e}')
        pass

    # key controller
    key = cv2.waitKey(1) & 0xFF
    if key == ord("d"):
        variables.detectionEnabled = not variables.detectionEnabled
        
    if key == ord("s"):
        variables.saveFrame = not variables.saveFrame
        
    if key == ord("c"):
        variables.compareFrameAndFace = not variables.compareFrameAndFace

    if key == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()