import cv2
import time
import os
from PIL import Image
path = 'Images'



# Open the default camera
cam = cv2.VideoCapture(0)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object


counter = 0

while True:
    ret, frame = cam.read()

    counter += 1

    if ret:
        cv2.imshow("Captured", frame)         
        cv2.imwrite(os.path.join(path , "captured_image" + str(counter) + ".png"), frame)  

        cv2.destroyWindow("Captured")       
    else:
        print("Failed to capture image.")

    # Write the frame to the output file

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

    time.sleep(1)

# Release the capture and writer objects
cam.release()
cv2.destroyAllWindows()