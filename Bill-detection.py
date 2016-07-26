# USAGE
# python list_detector.py --image images/cat_01.jpg --cascade cascade.xml

# import the necessary packages
from imutils import paths
import argparse
import sys
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to the input image")
ap.add_argument("-c", "--cascade",
	default="cascade.xml",
	help="path to list detector haar cascade")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
for imagePath in paths.list_images(args["images"]):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier(args["cascade"])
    rects = detector.detectMultiScale(gray, scaleFactor=2.5, minNeighbors=2, minSize=(170, 170))

    

    for (i, (x, y, w, h)) in enumerate(rects):
	cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
        #roi_gray = gray[y:y+h, x:x+w]
       # roi_color = img[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
	cv2.putText(image, "list #{}".format(i + 1), (x, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
        sys.stdout=open("test.txt","a")
        print "I found {0} lists in that image".format(i + 1)
        print('\n')

# show the detected list images
	cv2.imshow("images", image)
	cv2.waitKey(600)



  


