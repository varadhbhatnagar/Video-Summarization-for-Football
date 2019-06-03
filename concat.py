#ocr_output
#yc_output
#audio_output
BASE_PATH = "C:\\Users\dark_knight\Desktop\AIT\Projects\VideoSummarization\\Transfer_Learning\\"
from moviepy.editor import VideoFileClip, concatenate_videoclips
ocr =[line.rstrip('\n') for line in open(BASE_PATH + 'ocr_output.txt')]
yc =[line.rstrip('\n') for line in open(BASE_PATH + 'yc_output.txt')]
au =[line.rstrip('\n') for line in open(BASE_PATH+'audio_output.txt')]

final_ans=[]
final_cap=[]
for x in ocr:
	final_ans.append(int(x))
	final_cap.append("subs")
for x in yc:
	final_ans.append(int(x))
	final_cap.append("yellow_card")
for x in au:
	final_ans.append(int(x))
	final_cap.append("important_events")	


yx=sorted(zip(final_ans, final_cap))
minutes=0
seconds=0
f = open("subt.SRT", "a")
count=1

clips=[]
for x in range(0,len(yx)):
	if yx[x][1]=="important_events":
		clip = VideoFileClip(BASE_PATH + "\\Video\\"+"2_HQ.mkv").subclip(final_ans[x]-30, final_ans[x]+30)
		clips.append(clip)
		f.write(str(count))
		f.write("\n")
		f.write("00:"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)+",000 --> "+"00:"+str(minutes+1).zfill(2)+":"+str(seconds).zfill(2)+",000 --> ")
		f.write("\nImportant Events...")
		f.write('\n\n')
		minutes=minutes+1
		count=count+1


	if yx[x][1]=="yellow_card":
		clip = VideoFileClip(BASE_PATH + "\\Video\\"+"2_HQ.mkv").subclip(final_ans[x]-30, final_ans[x]+10)
		clips.append(clip)
		pmin=minutes
		psec=seconds
		seconds=seconds+40
		if seconds>60:
			minutes=minutes+1
			seconds=seconds%60
		f.write(str(count))
		f.write("\n")
		f.write("00:"+str(pmin).zfill(2)+":"+str(psec).zfill(2)+",000 --> "+"00:"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)+",000 --> ")
		f.write("\nYellow Cards...")
		f.write('\n\n')
		count=count+1

	if yx[x][1]=="subs":
		clip = VideoFileClip(BASE_PATH + "\\Video\\"+"2_HQ.mkv").subclip(final_ans[x]-10, final_ans[x]+10)
		clips.append(clip)
		pmin=minutes
		psec=seconds
		seconds=seconds+20
		if seconds>60:
			minutes=minutes+1
			seconds=seconds%60
		f.write(str(count))
		f.write("\n")
		f.write("00:"+str(pmin).zfill(2)+":"+str(psec).zfill(2)+",000 --> "+"00:"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)+",000 --> ")
		f.write("\nSubstitution...")
		f.write('\n\n')
		count=count+1
	x=x+1
f.close()
final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("final_video.mp4")

