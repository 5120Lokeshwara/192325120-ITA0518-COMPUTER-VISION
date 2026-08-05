import cv2

image = cv2.imread("Sample.jpg")

height, width = image.shape[:2]

bigger_image = cv2.resize(image, (int(width*3.0), int(height*3.0)))
smaller_image = cv2.resize(image, (int(width*0.5), int(height*0.5)))

cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image', bigger_image)
cv2.imshow('Smaller Image', smaller_image)

cv2.imwrite("M:\\COMPUTER VISION\\Lab Sessions\\py\\Bigger_image.jpg", bigger_image)
cv2.imwrite("M:\\COMPUTER VISION\\Lab Sessions\\py\\Smaller_image.jpg", smaller_image)

cv2.waitKey(0)
cv2.destroyAllWindows()