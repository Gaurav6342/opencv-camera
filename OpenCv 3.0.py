

import cv2
import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image, ImageTk

def capture_and_save():
    global count
    status, photo = cap.read()
    count += 1
    cv2.imwrite(f'gaurav_{count}.png', photo)

def update():
    status, photo = cap.read()
    if status:
        # Convert the BGR image to RGB format
        image = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)

        # Convert the image to PIL format
        image = PIL.Image.fromarray(image)

        # Create a PhotoImage object
        photo_image = ImageTk.PhotoImage(image=image)

        # Update the label with the new PhotoImage
        label.config(image=photo_image)
        label.image = photo_image

        # Call update function after 10 milliseconds
        root.after(10, update)

# Create a Tkinter window
root = tk.Tk()
root.title("Capture Image")

# Create a button to capture and save an image
capture_button = ttk.Button(root, text="Capture", command=capture_and_save)
capture_button.pack(pady=10)

# Create a label to display the OpenCV window
label = ttk.Label(root)
label.pack()

# OpenCV setup for capturing video frames
cap = cv2.VideoCapture(0)
count = 0  # initialize a counter for saving images with different names

# Start the update function
update()

# Start the Tkinter main loop
root.mainloop()

# Close OpenCV window and release the camera when the Tkinter window is closed
cv2.destroyAllWindows()
cap.release()
