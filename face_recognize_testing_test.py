"""
Usage:
  face_recognize.py -i <test_image>
  
Options:
  -h, --help                     Show this help
  -i, --test_image =<test_image> Test image
"""

from copyreg import pickle
import face_recognition
import docopt
from sklearn import svm
import os
import cv2
from datetime import datetime
import pickle
import mark_attendance

attendanceSheet = set()

def addId(name):
    attendanceSheet.add(name)
    
    
    """     with open('Attendance.csv','a+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                f.writelines(f'{name}\n') """
            
    now = datetime.now() 
    dtString = now.strftime('%H:%M:%S')
    
    mark_attendance.updateAttendance(attendanceSheet,dtString)

def face_recognize_test(test):
    
    clf = pickle.load(open('attendance_model.sav','rb'))
    
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
        addId(student_name)
        print(student_name)
    cv2.imshow('Webcam', cv2.cvtColor(test_image,cv2.COLOR_BGR2RGB))
    while(1):
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
               break

def main():
    args = docopt.docopt(__doc__)
    test_image = args["--test_image"]
    face_recognize_test(test_image)
  
if __name__=="__main__":
    main()