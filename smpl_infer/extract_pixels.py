import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Pixel coordinates: ({x}, {y})")

# Load an image file
image = cv2.imread("frame0.0001.jpg")
print(image.shape)
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