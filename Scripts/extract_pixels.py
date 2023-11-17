import cv2
import numpy as np
def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            bgr_color = image[y, x]
            rgb_color = cv2.cvtColor(np.array([[bgr_color]]), cv2.COLOR_BGR2RGB)[0][0]
            print(f"Pixel coordinates: ({x}, {y}), Color: ({rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]})")

# Load an image file
image = cv2.imread("crop-ex.jpg")
# Create a window to display the image
cv2.namedWindow("Image")

# Set the mouse callback function
cv2.setMouseCallback("Image", mouse_callback)

# Display the image on the window
cv2.imshow("Image", image)

# Wait for a key press to exit
cv2.waitKey(0)

# Destroy the window and free up resources
cv2.destroyAllWindows()