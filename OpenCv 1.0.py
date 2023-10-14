import cv2
cap = cv2.VideoCapture(0)               # image capture function with camera no as attribute

while True:

     status , photo = cap.read()          #click the photo function
     cv2.imwrite('gaurav.png',photo)     #save the photo to python program where to save after esc button press
     cv2.imshow('my image',photo)        # open the photo
     if cv2.waitKey(1) == 27:            #wait for 1 sec or 27 is no for esc (when enter esc window close)
              break



cv2.destroyAllWindows()                #window destoy after esc button
cap.release()
