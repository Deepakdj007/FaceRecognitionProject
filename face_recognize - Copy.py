"""
Usage:
  face_recognize.py -d <train_dir> -i <test_image>
  
Options:
  -h, --help                     Show this help
  -d, --train_dir =<train_dir>   Directory with 
                                 images for training
  -i, --test_image =<test_image> Test image
"""
import face_recognition
import docopt
from sklearn import svm
import os
import cv2
from datetime import datetime

def markAttendance(name):
    with open('Attendance.csv','a+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'{name}, {dtString}\n')
  
def face_recognize(dir, test):
    # Training the SVC classifier
    # The training data would be all the 
    # face encodings from all the known 
    # images and the labels are their names
    encodings = []
    names = []
  
    # Training directory
    if dir[-1]!='/':
        dir += '/'
    train_dir = os.listdir(dir)
  
    # Loop through each person in the training directory
    for person in train_dir:
        pix = os.listdir(dir + person)
  
        # Loop through each training image for the current person
        for person_img in pix:
            # Get the face encodings for the face in each image file
            face = face_recognition.load_image_file(
                dir + person + "/" + person_img)
            face_bounding_boxes = face_recognition.face_locations(face)
  
            # If training image contains exactly one face
            if len(face_bounding_boxes) == 1:
                face_enc = face_recognition.face_encodings(face)[0]
                # Add face encoding for current image 
                # with corresponding label (name) to the training data
                encodings.append(face_enc)
                names.append(person)
            else:
                print(person + "/" + person_img + " can't be used for training")
  
    # Create and train the SVC classifier
    clf = svm.SVC(gamma ='scale')
    clf.fit(encodings, names)
  
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
        markAttendance(student_name)
        print(student_name)
    cv2.imshow('Webcam', cv2.cvtColor(test_image,cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
  
def main():
    args = docopt.docopt(__doc__)
    train_dir = args["--train_dir"]
    test_image = args["--test_image"]
    face_recognize(train_dir, test_image)
  
if __name__=="__main__":
    main()