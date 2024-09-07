# pennAiRChallenge

For Static Image Case:
1. Clone the repository to Github Desktop
2. Open in Visual Studio Code
3. Given Static Image is already included, so simply running the code should display and write the final product image

Provide a brief explanation of your approach and any challenges faced:

The approach begins with reading the image, calculating average color of the image as a whole, subtracting the average color of the image from the original image, blurring the image, grey scaling the image, setting a threshold for each pixel to either become black or white, calculating the contours of the image, ensuring the area of the contours are a shape to reduce drawing the wrong contours, drawing the valid contours, calculating the centers, displaying the centers and locations, and finally showing and writing the image.  Essentially the image becomes black and white to allow the contours to be better detected.

Challenges included detecting the different colors in image and video mode that were difficult to detect like the green trapezoid, blue triangle, etc.  To overcome this challenge, the threshold and blurring numbers were tinkered with and the average color was subtracted to negate the noise from the messy background.  Working on the hard challenge, the dark blue was difficult to detect, and therefore the contrast and saturation were tinkered with, however neither worked.  The image was then equalized, however that also did not work.

For Video Case:
1. Clone the repository to Github Desktop
2. Open in Visual Studio Code
3. Download Given Video linked: [https://drive.google.com/file/d/1yY7xvWigyv9UQOOSgaDck_8a4I1QCjiH/view?usp=sharing](url)
5. Add the downloaded video to the same folder in Visual Studio Code
6. Run the code and run the new file written to the folder

Video Case Result:
[https://drive.google.com/file/d/128Zoe20vZ5RvEA4Zk7LEyYQhtxt5TDoc/view?usp=sharing
](url)
