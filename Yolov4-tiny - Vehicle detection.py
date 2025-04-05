import cv2
import numpy as np

# Load YOLOv4-tiny
net = cv2.dnn.readNet("C:\\Users\\lucid\\OneDrive\\Desktop\\microproccessor\\yolov4-tiny.weights", "C:\\Users\\lucid\\OneDrive\\Desktop\\microproccessor\\yolov4-tiny.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def detection(frame):
    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    vehicle_count = len(indexes)  # Count the number of vehicles detected
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'Vehicle {vehicle_count}', (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame

def capturescreen(camera_index):
    realtimevideo=cv2.VideoCapture(camera_index)
    while realtimevideo.isOpened():
        ret, frame = realtimevideo.read()
        controlkey = cv2.waitKey(1)
        if ret:
            vehicleframe = detection(frame)
            cv2.imshow('Vehicle' + str(camera_index), vehicleframe)
        else:
            break
        if controlkey == ord('q'):
            break
    realtimevideo.release()

for i in range(4):
    capturescreen(i)

cv2.destroyAllWindows()
