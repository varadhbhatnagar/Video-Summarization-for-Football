

from imutils.object_detection import non_max_suppression
import numpy as np
import pytesseract
import argparse
import cv2
import os
#directory=
for filename in os.listdir():
    if filename.endswith(".jpg"):
    	print(filename)
    	myCmd = "python text_recognition.py --east frozen_east_text_detection.pb --image "+ filename + " --padding 0.05"
    	os.system(myCmd)


