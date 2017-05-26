from PIL import ImageGrab
import numpy as np
import cv2
i = 1
while(True):
    img = ImageGrab.grab(bbox=(1920/2,1080/2,1060,640)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    imageName = "negs/negative"+str(i)+".jpg"
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(imageName, frame)
    cv2.imshow("test", frame)
    i = i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()