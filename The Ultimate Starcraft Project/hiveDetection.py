from PIL import ImageGrab
import numpy as np
import cv2

hive_cascade = cv2.CascadeClassifier("hive_cascade.xml")
while(True):
    img = ImageGrab.grab(bbox=(400,400,1200,1260)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    hives = hive_cascade.detectMultiScale(frame)
    print "Found {0} hives!".format(len(hives))
    for (x,y,w,h) in hives:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()