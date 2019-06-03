import cv2
import os
import sys
BASE_PATH = "C:\\Users\dark_knight\Desktop\AIT\Projects\VideoSummarization\\Transfer_Learning"
VIDEO_PATH = sys.argv[1]
IMP_FRAMES_PATH=sys.argv[2]
count=0
vidcap = cv2.VideoCapture(VIDEO_PATH)
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
    	cv2.imwrite(BASE_PATH+"\\Frames\\"+"image"+str(count)+".jpg", image)
    	f2.write(str(sec)+"\n")   
    return hasFrames

f = open(IMP_FRAMES_PATH, "r")
f2 = open(BASE_PATH + "\\Frames\\"+"timing_map.txt","w")
for line in f:
	fps = vidcap.get(cv2.CAP_PROP_FPS)  
	frameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
	duration = frameCount/fps
	start = int(line.strip())-3;
	end = start+6
	sec = start
	frameRate = 1 # 1 frame every second
	while sec <= end:
	    sec = round(sec, 2)
	    if(sec < 1):
	    	sec = sec + frameRate
	    	continue
	    if( sec > duration ):
	    	sec = sec + frameRate
	    	continue
	    count+=1
	    success = getFrame(sec)
	    sec = sec + frameRate

f.close()
f2.close()
