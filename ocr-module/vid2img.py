import cv2
BASE_PATH = "C:\\Users\dark_knight\Desktop\AIT\Projects\VideoSummarization\\Transfer_Learning"
vidcap = cv2.VideoCapture(BASE_PATH + "\\Video\\"+'2_HQ.mkv')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 25 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)