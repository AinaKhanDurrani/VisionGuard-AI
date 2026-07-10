import numpy as np

class Visualizer:
              
    def draw(self, results ) ->np.ndarray:
        annotated_frame = results[0].plot()
        
        return annotated_frame
    