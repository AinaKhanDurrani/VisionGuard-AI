import cv2
import os


load_path = "data/raw/images/construction"
save_path = "data/processed/images/construction"



img = cv2.imread(load_path + "/construction_004.jpg")
img = cv2.resize(img, (500,500) )



cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()