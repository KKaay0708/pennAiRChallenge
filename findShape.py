import cv2 
import numpy as np 

#load the image into img
img = cv2.imread('PennAir 2024 App Static.png') 

#calculate the average color of img
height, width, _ = np.shape(img)
avg_color_per_row = np.average(img, axis=0)
avg_colors = np.average(avg_color_per_row, axis=0)
int_averages = np.array(avg_colors, dtype=np.uint8)
average_image = np.zeros((height, width, 3), np.uint8)
average_image[:] = int_averages + 40 # Adding offset
#subtract the average color to the original img
image = cv2.subtract(img, average_image)

#blur the image
blurred_image = cv2.GaussianBlur(image, (11, 11), 0)
#gray scale the image
gray = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY) 
#set all pixels above a certain color threshold to white
_, threshold = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY) 
#detect contours in image
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

i = 0
for contour in contours: 
	if i == 0: 
		i = 1
		continue
	#ensure contour is reasonable for a shape
	area = cv2.contourArea(contour)
	if area < 1000: continue
	#calculate center of contour at moments
	M = cv2.moments(contour)
	if M['m00'] != 0:
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		#display contours and centers and locations
		cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
		cv2.drawContours(img, [contour], 0, (0, 0, 255), 5) 
		text = f"({cX}, {cY})"
		cv2.putText(img, text, (cX + 10, cY - 10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)

#show and write final image
cv2.imshow('outline image', img) 
cv2.imwrite('outlineImage.png', img)

cv2.waitKey(0) 
cv2.destroyAllWindows() 