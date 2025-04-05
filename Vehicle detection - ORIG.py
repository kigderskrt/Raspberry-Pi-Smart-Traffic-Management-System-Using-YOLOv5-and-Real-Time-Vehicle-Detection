import cv2

vehiclexml=cv2.CascadeClassifier('vehicle.xml')

def detection(frame):
    vehicle=vehiclexml.detectMultiScale(frame,1.15,4)
    for (x,y,w,h) in vehicle:
        cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
        cv2.putText(frame,'Cars',(x+w,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),thickness=2)
    return frame

def capturescreen(camera_index):
    realtimevideo=cv2.VideoCapture(camera_index)
    while realtimevideo.isOpened():
        ret,frame=realtimevideo.read()
        controlkey=cv2.waitKey(1)
        if ret:
            vehicleframe=detection(frame)
            cv2.imshow('Cars'+str(camera_index),vehicleframe)
        else:
            break
        if controlkey==ord('q'):
            break
    realtimevideo.release()

for i in range(4):
    capturescreen(i)

cv2.destroyAllWindows()
