from app.detection.detector import Detector
from app.utils.camera import Camera
from app.utils.visualization import Visualizer

import cv2 as cv


def main():
    
    camera = Camera(0)
    detector = Detector()
    visualizer = Visualizer()
    
    if not camera.open():
        print(f"Failed to open camera source: {camera.get_source()}")
        return
        
 
    try:
        while True:                         
            ret, frame = camera.read()  
            if not ret:
                break        

            results = detector.detect(frame= frame)

            annotated_frame = visualizer.draw(results)
       
            cv.imshow("video",annotated_frame)
         
            if cv.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv.destroyAllWindows()
    
    return
       
       

if __name__ == "__main__":
    main()