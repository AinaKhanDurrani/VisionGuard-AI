from ultralytics import YOLO
import cv2 as cv

import os

video = "data/raw/videos/traffic/traffic_002.mp4"
save_path = "data/processed/videos"

model = YOLO('yolo11n.pt')

cap = cv.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    if not ret:
        break
    
    result = model(frame)
    
    img = result[0].plot()
    
    img = cv.resize(img, (550,450))
    
    cv.imshow("traffic video",img)
    
    key = cv.waitKey(50)
    
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
    

