"""
Usage:
  face_recognize.py -d <train_dir>
  
Options:
  -h, --help                     Show this help
  -d, --train_dir =<train_dir>   Directory with 
                                 images for training
"""
import face_recognition
import docopt
from sklearn import svm
import os
import cv2
import pickle

  
def face_recognize_train(dir):
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
    pickle.dump(clf, open('attendance_model.sav','wb'))
    print("Model Saved")
  
  
def main():
    args = docopt.docopt(__doc__)
    train_dir = args["--train_dir"]
    face_recognize_train(train_dir)
  
if __name__=="__main__":
    main()