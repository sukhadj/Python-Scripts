from pushbullet import Pushbullet
import cv2 as cv 
import time

decline=["No","no","nah","nahi"]
accept=["yes","Yes","ho"]

pb=Pushbullet("o.ZNw6hKcdp0PXK5uelvBhW307LhAf15hP")

message =pb.push_note("Verification","Did you just logged in?")

flag=False

while time.clock()<=30:
	pushes = pb.get_pushes()
	if pushes[0]["body"] in decline:
		flag=True
		break
	if pushes[0]["body"] in accept:
		break

if flag:
	cap=cap=cv.VideoCapture(0)
	ret,frame=cap.read()
	threat =pb.push_note("threat","Threat detected")	
	if ret:
		cv.imwrite("cache/image.jpg",frame)
		with open("cache/image.jpg","rb") as pic:
			file_data=pb.upload_file(pic,"picture.jpg")
			push =pb.push_file(**file_data)
	else:
		error =pb.push_note("error","Unable to send picture")
else:
	clear =pb.push_note("np","happy computing")