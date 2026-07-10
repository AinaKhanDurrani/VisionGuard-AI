import cv2 as cv
import numpy as np

class Camera:
    
    def __init__(self,source = 0):
        self.cap = None
        self.source = source
    
    def open(self,)-> bool:      
        self.cap = cv.VideoCapture(self.source)
        return self.cap.isOpened()
           
        
    def is_open(self)-> bool:   
        return self.cap is not None and self.cap.isOpened()   
           
    
    def get_source(self)->int | str:
        return self.source
        
            
    def read(self, )-> tuple[bool, np.ndarray|None]:
        if not self.is_open():
            return False, None 
        ret, frame = self.cap.read()        
       
        if not ret:
            return False, None
        
        return ret, frame
    
    def get_resolution(self)-> tuple[int,int]|None:
        if self.is_open():
            width = int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH)) 
            height = int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))        
            return  (width, height)          
        else:
             return  None
              

                
    def get_fps(self)-> int | None:
        if self.is_open():
            fps = int(self.cap.get(cv.CAP_PROP_FPS))            
            return  fps           
        else:
            return  None
                
    def release(self) -> bool:
        if self.is_open():
            self.cap.release()  
            self.cap = None
            return True            
        else:
            return False
            
