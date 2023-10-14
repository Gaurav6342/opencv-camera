import cv2

cap = cv2.VideoCapture(0)  # image capture function with camera number as attribute
count = 0  # initialize a counter for saving images with different names

while True:
    status, photo = cap.read()  # click the photo function
    cv2.imshow('my image', photo)  # open the photo
    if cv2.waitKey(1) == 27:  # wait for 1 sec or 27 is the code for esc (when enter esc window close)
        break

    # Save the image with a different name in each iteration
    count += 1
    cv2.imwrite(f'gaurav_{count}.png', photo)

cv2.destroyAllWindows()  # window destroy after esc button
cap.release()
