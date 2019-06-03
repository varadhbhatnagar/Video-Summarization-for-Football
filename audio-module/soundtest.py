from scipy.io import wavfile
import numpy
import matplotlib.pyplot as plt
import math
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor as mp
import sys
BASE_PATH = "C:\\Users\dark_knight\Desktop\AIT\Projects\VideoSummarization\\Transfer_Learning"

filename=BASE_PATH+"\\Video\\2_HQ.mkv"
clip = mp.VideoFileClip(filename)
clip.audio.write_audiofile("theaudio.wav")
sampFreq, snd = wavfile.read('theaudio.wav')

print(snd.dtype)
snd=snd/(2.**15)
print(snd.shape)

shape=int(snd.shape[0])

print(shape/sampFreq)
print(sampFreq)
timeArray = numpy.arange(0, shape, sampFreq)
timeArray = timeArray / sampFreq
persec4=sampFreq/4
#s2 = snd[:,0] 
s2 = snd[: :sampFreq,0]
print(s2.shape)

s2=numpy.square(s2)
s2=numpy.square(s2)
#s2=numpy.square(s2)
#s2=numpy.square(s2)

#s2=numpy.sqrt(s2)
#s2=numpy.sqrt(s2)

'''plt.plot(timeArray, s2, color='k')
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.show()
'''
print(s2)
mean=numpy.mean(s2)
array_of_time=numpy.array(0)
print(timeArray)
t=0
y=numpy.max(s2)
y=y * 0.15
for x in s2:
	if x>y:
		temp_time=int(t)
		array_of_time= numpy.append(array_of_time,temp_time)
		#print(int(t/sampFreq))
	t=t+1
print(array_of_time)
print(numpy.unique(array_of_time))

unique_array_of_time=numpy.unique(array_of_time)
maxi=unique_array_of_time[-1]
final_array=numpy.zeros(maxi+1)
p=maxi
r=maxi

final_ans=unique_array_of_time[unique_array_of_time>0]
with open(BASE_PATH	 + "\\Frames\\"+'frames.txt', 'w') as file:
    for time in final_ans:
        file.write(str(int(time)-20)+"\n")

'''
for x in range(0,len(final_ans)+1):
	ffmpeg_extract_subclip("2_HQ.mkv", final_ans[x]-15, final_ans[x+1]+15, targetname="test.mp4")
	x=x+1
'''