import cv2 as cv2
import numpy as np

def testFace(input_vid,frame_no):
	cap = cv2.VideoCapture(input_vid)
	cap.set(1,frame_no)
	ret, frame = cap.read()#got the frame in variable frame, ret is True if the operation was successful
	cap.release()
	if(not ret):
		print("Unable to read frame, maybe an erro with filename?")
		return False
	return detectFace(frame,1)
	
def detectFace(frame,mode):
	face_cascade = cv2.CascadeClassifier('/mnt/d/Desktop/ever_pro/virt/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('/mnt/d/Desktop/ever_pro/virt/lib/python3.5/site-packages/cv2/data/haarcascade_eye.xml')
	if(mode==1):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#gray contains the grayscale of the chosen frame
	if(mode==2):
		gray = frame#the frame is already grayscale
	cv2.imwrite('Face_detection_intermediate.jpg',gray)#saving grayscale frame
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)#faces has face co-ordinates if detected in frame
	if(len(faces)==0):
		print('No Faces detected')
		return False
		
	for (x,y,w,h) in faces:#marking the faces found
		frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray,1.3,10)
		for (ex,ey,ew,eh) in eyes:#applying eye detection inside faces
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imwrite('Face_detection_final.jpg',frame)
	
	if(len(faces)>2):#we still want to show the detected faces hence moving this down
		print('More than two Faces detected')
		return False
	
	return True
	
def createBackgroundSubtractor(input_vid,frame_no):
	cap = cv2.VideoCapture(input_vid)
	fgbg = cv2.createBackgroundSubtractorMOG2()
	current_frame=0
	while(current_frame<frame_no):
		ret, frame = cap.read(current_frame)
		fgmask=fgbg.apply(frame)
		current_frame+=1
	'''
	cap.set(1,frame_no)
	ret, frame = cap.read()
	cap.set(1,frame_no+1)
	ret, frame_plus_1 = cap.read()
	fgmask=cv2.cvtColor(cv2.absdiff(frame_plus_1,frame),cv2.COLOR_BGR2GRAY)
	#fgmask = fgbg.apply(frame)
	'''
	cv2.imwrite('Subtracted_background.jpg',fgmask)
	detectFace(fgmask,2)
	cap.release()

test=0
print("Enter the video file name with extension eg: joey.mp4\nVideo Name:")
input_video=input()
while(test < 4):
	print("Enter the test you want to use.\n1. Face Detection\n2. Background Subtraction\n3. Exit program")
	test=int(input())
	if(test==1):
		print(testFace(input_video,150))
	elif(test==2):
		createBackgroundSubtractor(input_video,150)
	else:
		test=4








