# FaceRecognitionProject
#### KTU Final Semester Project - Automated Attendance tracking system
![image](https://user-images.githubusercontent.com/54731120/190552127-afc01589-4c90-4eb2-ab63-ffa33ed702f2.png)


## Project Objective

The prime objective of our project is to develop an attendance tracker that uses a
computer vision model to recognize students from images. It is aimed for an academic
environment where faculties find it difficult to take attendance manually. It is designed
to be quick, accurate, reliable and to automate almost all the administrative tasks that
are related to taking attendance and dealing with reports.

## Algorithm

### Pre-processing, Training & Testing
![image](https://user-images.githubusercontent.com/54731120/190550996-0375c3e4-d3b4-48a5-b2c9-2fa48b284105.png)

### Face Recognition

![image](https://user-images.githubusercontent.com/54731120/190551069-acfc0771-7cfa-4ac1-92e4-f160a3935b3c.png)

### Report Generation

![image](https://user-images.githubusercontent.com/54731120/190551097-8cef45db-e07f-4226-af88-a76e2ee1e3a7.png)

### Notification Generation

![image](https://user-images.githubusercontent.com/54731120/190551130-20c394aa-b4eb-47ac-8f70-34083f9d4eef.png)

The final algorithm that was developed relied on a deep learning computer vision model that would recognize faces from different instances (images) of students in the classroom and would send the face labels to the database to mark the attendance. 

**Below are the processes explained in detail:**

* Images (multiple instances) of the students in the classroom will be captured by using a smartphone camera at different angles.

*	After removing noise and other unwanted elements from the images, and scaling (pre-processing), they will be sent over to a deep learning model hosted on a cloud service for multiple face recognition.

*	Different instances of Amazon S3 buckets will be used to store our model, the train and test dataset as well as the instance images. Using open-source pre-trained im- plementation of DLIB’s ResNet-29 face recognition algorithm and a SVM classifier, the model will process the input using the computing resources provided and will generate face labels in-order to mark the attendance in the database.

*	The details on students and faculties will be stored in a cloud database that is deployed using MongoDB Database engine. The queries will be using MongoDB query language (MQL) parsed through Pymongo from the python script.

*	Python data formatting (pandas) visualization (plotly  seaborn) tools will be used for creating visual charts. Report generation will include composing all to a PDF report file using FPDF. For tracking attendance levels of various students, functions with specific parameters are automatically run every day & in specific intervals so that the faculty is notified if there are any low attendance levels for any students.

*	Automatically generated notifications are sent to various students in case of low attendance by the use of services likes SMTP library for e-mail and Twilio API for WhatsApp respectively.

*	Any additional updates to the application will be handled by GitHub as changes committed to the repository will be built in a docker container and uploaded to hosting service as a new docker image.

*	Overall, the web application developed by Django Bootstrap will be communicating with the DL model through API calls endpoints. As there are more than enough computing resources available, the model will be executed much faster than on a local machine and thus deliver attendance reports in seconds.

## Software Requirements

* **OpenCV**: OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine per- ception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.

* **Face Recognition Library (DLIB)**: Dlib is a powerful library having a wide adoption in image processing community similar to OpenCV. Even though it is written in c++, it has a python interface as well. Programmer Adam Geitgey offers a FOSS face recognition API that leverages DLIB’s state-of-the-art face recognition built with deep learning. The model has an accuracy of 99.38 % on the Labeled Faces in the Wild benchmark.

* **Django**: Django is a high-level Python web framework that enables rapid develop- ment of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of back-end web development like authentication, user access levels, database to model forms etc. It is free and open source, has a thriving and active community, great documentation, and many options for API integration.

* **Bootstrap 5.0**: Bootstrap is a free and open-source tool collection for creating respon- sive websites and web applications. It is the most popular HTML, CSS, and JavaScript framework for developing responsive, mobile-first websites.

* **Languages Used:** Python, HTML, CSS, jQuery, NoSQL 

## Proposed Solution - Modular Division

### Module 1: Collection and Pre-processing of Custom Dataset

To train the selected model, we needed to collect dataset from multiple students of dif- ferent classes. 25 images of faces from each student at different angles were taken. From Class 1: 36 students, Class 2: 12 students, Class 3: 12 students. Therefore images from a total of 60 different students were taken to train our model. I.e, a total of 1500 images in the custom dataset. These images were pre-processed in the following ways:

**Compression**: The images were compressed from 4-5 MB to mere 100-200 KB in size for faster and easier processing/training.

**Down-scaling**: The compressed images were then down-scaled from 3840 x 2160 to 540x720 pixels to make them all in a fixed shape for facilitating mini-batch learning.

**Cropping**:    The background and useless features of the face were cropped out leav- ing only the face features to be seen. The resolution was further down-scaled to a fixed 250x333 pixels.

![image](https://user-images.githubusercontent.com/54731120/190551700-089251d6-d03a-4935-b266-de3f766f1b1a.png)
**Images of Students at Different Angles**

![image](https://user-images.githubusercontent.com/54731120/190552228-97305ba3-e32c-44ba-8690-022d4203559f.png)
**Custom Dataset**

### Module 2: Training ResNet model using Custom Dataset

The model was trained on the processed custom dataset. The following are the steps involved in the process:
*	Find the training directory used to store multiple images of different students.
*	For each student folder in the directory:

–	Take one photo at a time, and get the face encoding of each image.

–	Add the face encoding along with the label(name) and store in separate lists.

–	If multiple faces detected in an image ; return error message.

*	Fit the encoding and labels using SVM classifier.
*	After every folder has been iterated through, save the model as a .sav file.

### Module 3: Testing/Deploying the model

To trained model was loaded and tested on a variety of test data collected from class- rooms. The test image includes students sitting in benches as they would in a normal classroom to simulate the real scenario. The output produced through OpenCV was able to draw a bounding box around the faces of all the students and identify them using their IDs. The same test was conducted using images of students in a variety of situations and was able to detect all the students in a given image and mark their attendance in the MongoDB database.

![image](https://user-images.githubusercontent.com/54731120/190552409-b5abce59-908e-46c7-b3d8-690721c9b568.png)
**Test Images at Various Conditions**

![image](https://user-images.githubusercontent.com/54731120/190552450-aec50dab-cc9f-4b5f-a6be-7f89cb27bfb9.png)
**Resultant Image with Bounding Boxes & Labels**
![image](https://user-images.githubusercontent.com/54731120/190552502-1d258b38-5a1d-4971-9948-1f8bf1293d07.png)
**Resultant Image with Bounding Boxes & Labels**
![image](https://user-images.githubusercontent.com/54731120/190552533-a4c0eaf7-bb25-41a2-a687-4ae1336e5ba8.png)
**Resultant Image with Bounding Boxes & Labels**

![image](https://user-images.githubusercontent.com/54731120/190552561-ff4989e7-edf0-4db9-884e-d42d0588d86d.png)
**Marked Attendance in MongoDB Document**

### Module 4: Report Generation

The marked attendances are stored in the MongoDB Database as documents inside different collections. To summarize these attendances at different interval ranges, a report generation feature was introduced. They include a variety of visualizations/graphs using the plotly library. To extract and pre-process the data from the database pandas was used. To generate a PDF report file, the FPDF python library was used. The following are the different reports that could be generated based on the ’From’ and ’To’ date options:

* Daily Reports: ’From’ and ’To’ Date are the same. Shows attendance percentages of students during each period of a particular day.
*	Monthly/Semester-wise Reports: Given the start and end date of a month/semester. Shows a comprehensive attendance report of each student during the particular month/semester.

*	Reports on a Range: Given a random date range, shows a simple visualization report from data extracted on that given range.

![image](https://user-images.githubusercontent.com/54731120/190552684-0343b2bc-c62e-471b-9ede-5eaf65fcca93.png)

### Module 5: Notification Generation

When a particular student’s attendance falls below 75% they can be notified via either E-mail or WhatsApp. On selecting generate notifications, the list of student’s having any of their subjects with low attendance score will be displayed. The faculty can then choose whether to send notifications to the students individually or collectively. The E-mails are sent using the help of SMTPLIB and SSL python libraries. The WhatsApp message is sent using the Twilio REST API. The message content will include the concerned subject name and low attendance score.

![image](https://user-images.githubusercontent.com/54731120/190552727-bdf178e8-307b-4267-896a-ecebe5310d3b.png)
**Email Notification**

![image](https://user-images.githubusercontent.com/54731120/190552762-b45f57a5-d593-47d9-b3e6-8fd435a6ab85.png)
**WhatsApp Notification**

###	Module 6: Web App Development

A web application was developed using Django Bootstrap 5.0 to package all the modules to a complete GUI application. A number of standard features were introduced in the web application to provide a seamless user experience for the user/faculty:
*	User Authentication: Requires User-ID and Password for authentication before any of the features could be accessed. Users have to added by the administrator.

*	Welcome Page: A page describing the product, it’s functionalities & the team behind the development.

*	Mark Attendance: Selecting a Class and a Period will prompt a window for up- loading the classroom photo. After processing, a success message will be displayed along with marked attendance in MongoDB.

*	View Attendance: Selecting a class & a Date will show the following day’s atten- dance in a tabular format.

*	Edit Attendance: Selecting a Class & a Date will show the following day’s atten- dance in a tabular format. Each cell can be edited and the data will be updated in the database upon selecting the submit button.

*	Send Notification: Selecting a Class will show a list of students having low atten- dance scores (¡75%) in any of their enrolled subjects. Notifications can be send using Email or WhatsApp.

*	Generate Report: Selecting a Class, ’From’ & ’To’ dates will generate a PDF report (that includes comprehensive visualizations) that is automatically downloaded.

*	Contact: A contact form is available to lodge complaints/bug reports that will be send directly to the admin when submitted.

![image](https://user-images.githubusercontent.com/54731120/190552887-805c11a0-8ca1-4e8e-925a-5c5322e441ba.png)
**Welcome Page**

![image](https://user-images.githubusercontent.com/54731120/190552908-8594dab7-a861-49a1-81a0-c46ccb046b4c.png)
**Login Page**

![image](https://user-images.githubusercontent.com/54731120/190552931-354236ec-1892-4d2f-a176-ddd8359f2dd5.png)
**View Attendance Input**

![image](https://user-images.githubusercontent.com/54731120/190552964-27fa7c30-b69e-4f47-a566-b91e87871c52.png)
**View Attendance Output**

![image](https://user-images.githubusercontent.com/54731120/190552979-0dbb055e-2ee3-4563-871d-432f703ff31c.png)
**Mark Attendance Input**

![image](https://user-images.githubusercontent.com/54731120/190553001-8d5e06f6-208d-4b64-a907-8a2fe18e64b2.png)
**Edit Attendance Output**

![image](https://user-images.githubusercontent.com/54731120/190553027-579f7025-e8f2-449a-b5f4-52a74dcf6efb.png)
**Send Notification**

![image](https://user-images.githubusercontent.com/54731120/190553070-ea5433ea-3e51-41d9-b7cd-572d79fa3d44.png)
**Send Notification Output**

