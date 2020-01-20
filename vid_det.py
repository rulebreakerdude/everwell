import cv2 as cv2
import numpy as np

def testFace(input_vid,frame_no):
	cap = cv2.VideoCapture(input_vid)
	cap.set(1,frame_no)
	ret, frame = cap.read()#got the frame in variable frame, ret is True if the operation was successful
	if(not ret):
		print("Unable to read frame, maybe an erro with filename?")
		return False
	face_cascade = cv2.CascadeClassifier('/mnt/d/Desktop/ever_pro/virt/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('/mnt/d/Desktop/ever_pro/virt/lib/python3.5/site-packages/cv2/data/haarcascade_eye.xml')
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#gray contains the grayscale of the chosen frame
	cv2.imwrite('intermediate_one.jpg',gray)
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)#faces has face co-ordinates if detected in frame
	print(faces,len(faces))
	if(len(faces)==0):
		print('No Faces detected')
		return False
		
	if(len(faces)>2):
		print('More than two Faces detected')
		return False
		
	for (x,y,w,h) in faces:
		frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray,1.3,10)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imwrite('test_frame_'+str(frame_no)+'.jpg',frame)
	cap.release()
	return True

print("Enter the video file name with extension eg: joey.mp4\nVideo Name:")
input_video=input()
print(testFace(input_video,150))