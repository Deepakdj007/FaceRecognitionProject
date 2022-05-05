from copyreg import pickle
import face_recognition
import docopt
from sklearn import svm
import os
import cv2
from datetime import datetime
import pickle
import mark_attendance
import csv
from tkinter import Tk   
from tkinter.filedialog import askopenfilename

attendanceSheet = set()

def addId(attendanceSheet):
    
    """
    with open('Attendance.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerow(list(attendanceSheet))
        
    """
            
    #now = datetime.now() 
    #dtString = now.strftime('%H:%M:%S')
    
    mark_attendance.updateAttendance(attendanceSheet)
    

def face_recognize_test(test):
    
    clf = pickle.load(open('F:\Deepak_Jose_RSET\FaceRecognitionProject\_attendance_model.sav','rb'))
    
    # Load the test image with unknown faces into a numpy array
    test_image = face_recognition.load_image_file(test)
  
    # Find all the faces in the test image using the default HOG-based model
    face_locations = face_recognition.face_locations(test_image)
    no = len(face_locations)
    print("Number of faces detected: ", no)
  
    # Predict all the faces in the test image using the trained classifier
    print("Found:")
    test_image_encodings = face_recognition.face_encodings(test_image)
    for i in range(no):

        x1 = face_locations[i][3]
        y1 = face_locations[i][0]
        x2 = face_locations[i][1]
        y2 = face_locations[i][2]
        

        
        test_img_encoding = test_image_encodings[i]
        name = clf.predict([test_img_encoding])
        student_name = name[0]

        cv2.rectangle(test_image,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.putText(test_image,student_name,(x1+6,y2+25),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
        

        attendanceSheet.add(student_name)
        print(student_name)
    addId(attendanceSheet)
    
  
    cv2.imshow('Webcam', cv2.cvtColor(test_image,cv2.COLOR_BGR2RGB))
    while(1):
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
               break


def main():
    Tk().withdraw()
    test_image = askopenfilename()
    face_recognize_test(test_image)
    print("Attendnance marked")
  
if __name__=="__main__":
    main()