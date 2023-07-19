import cv2

# Configurable Parameters
source = "camera.jpg"
destination = "new-camera.png"
scale_percentage = 200

# Image load
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# image new height and width
new_width = int(src.shape[1] * scale_percentage / 100)
new_height = int(src.shape[0] * scale_percentage / 100)

# Generating the image
output = cv2.resize(src, (new_width, new_height))

# Writing the image
cv2.imwrite(destination, output)