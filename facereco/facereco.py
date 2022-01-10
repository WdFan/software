import cv2
import dlib
import matplotlib.pyplot as plt
import numpy as np
import time

def FaceRecognize():
    # 定义人脸检测器
    detector = dlib.get_frontal_face_detector()
    # 定义人脸关键点检测器
    predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")
    #打开摄像头
    camera = cv2.VideoCapture(0)
    st = 0
    en = 0
    while(True):
        # 读取一帧图像
        ret,img = camera.read()
        #判断图片读取成功
        start_time = time.time()
        if ret:
            # 检测到的人脸
            faces = detector(img, 0)
            # 如果存在人脸
            if len(faces):
                print("Found %d faces in this image." % len(faces))
                for i in range(len(faces)):
                    landmarks = np.matrix([[p.x, p.y] for p in predictor(img, faces[i]).parts()])
                    for point in landmarks:
                        pos = (point[0, 0], point[0, 1])
                        cv2.circle(img, pos, 1, color=(0, 255, 255), thickness=3)
            else:
                print('Face not found!')
     #       cv2.putText(img, "FPS {0}" .format(str(1.0 / (time.time() - start_time))), (40, 40), 3, 1, (255, 0, 255), 2)
            cv2.imshow('Face',img)
            #如果按下q键则退出
            if cv2.waitKey(100) & 0xff == ord('q') :
                break
    camera.release()
    cv2.destroyAllWindows()

FaceRecognize()