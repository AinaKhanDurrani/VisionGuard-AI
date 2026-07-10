from ultralytics import YOLO
from ultralytics.engine.results import Results


class Detector:
    
    def __init__(self, model = "yolo11n.pt"):
        self.model = YOLO(model)        
    
    def detect(self , frame )->  list[Results]|None:
        if frame is None:
            return None 
        
        return self.model(frame)
           
        
            