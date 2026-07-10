import cv2 as cv

load_path = "data/raw/images/construction"
img = cv.imread(load_path + "/construction_004.jpg")

# mouse callback function
def drawfunction(event,x,y,flags,param):
   if event == cv.EVENT_LBUTTONDBLCLK:
      cv.circle(img,(x,y),20,(255,255,255),-1)

img = cv.resize(img, (350,350))
cv.namedWindow('image')
cv.setMouseCallback('image',drawfunction)

while True:
    cv.imshow("image", img)
    key = cv.waitKey(1)
    if key == 27:
        break
cv.destroyAllWindows()

