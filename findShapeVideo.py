import cv2
import numpy as np

def outline(img):
    if img is None:
        return None

    #calculate the average color of img
    height, width, _ = np.shape(img)
    avg_color_per_row = np.average(img, axis=0)
    avg_colors = np.average(avg_color_per_row, axis=0)
    int_averages = np.array(avg_colors, dtype=np.uint8)
    average_image = np.zeros((height, width, 3), np.uint8)
    average_image[:] = int_averages + 50  # Adding offset
    #subtract the average color to the original img
    image = cv2.subtract(img, average_image)
    
    #blur the image
    blurred_image = cv2.GaussianBlur(image, (11, 11), 0)
    #gray scale the image
    gray = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)
    #set all pixels above a certain color threshold to white
    _, threshold = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY)
    #detect contours in image
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        #ensure contour is reasonable for a shape
        if cv2.contourArea(contour) < 1000:
            continue
        #calculate center of contour at moments
        M = cv2.moments(contour)
        if M['m00'] != 0:
            X = int(M["m10"] / M["m00"])
            Y = int(M["m01"] / M["m00"])
            #display contours and centers and locations
            cv2.circle(img, (X, Y), 7, (255, 255, 255), -1)
            cv2.drawContours(img, [contour], 0, (0, 0, 255), 6)
            text = f"({X}, {Y})"
            cv2.putText(img, text, (X + 10, Y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1, cv2.LINE_AA)

    return img

#initialize VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('outlineVideo.mp4', fourcc, 20, (1920, 1080))

#initialize VideoCapture
vid = cv2.VideoCapture("PennAir 2024 App Dynamic.mp4")

#take each frame of the video and apply outline function
def extract_frames(video, writer):
    count = 0
    while True:
        success, frame = video.read()
        if not success:
            break
        processed_frame = outline(frame)
        if processed_frame is not None:
            resized_frame = cv2.resize(processed_frame, (1920, 1080))
            writer.write(resized_frame)
            count += 1
            print(f"Processed frame {count}")


extract_frames(vid, video_writer)

vid.release()
video_writer.release()
cv2.destroyAllWindows()
