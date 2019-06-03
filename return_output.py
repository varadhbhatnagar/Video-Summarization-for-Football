BASE_PATH = "C:\\Users\dark_knight\Desktop\AIT\Projects\VideoSummarization\\Transfer_Learning"

f = open(BASE_PATH + "\\Frames\\timing_map.txt")
f2 = open(BASE_PATH + "\\Frames\\boolean_map.txt")
f3 = open(BASE_PATH + "\\"+"yc_output.txt","w")
f4 = open(BASE_PATH + "\\"+"audio_output.txt","w")
prev = -1
for row in f:
	row2 = f2.readline()
	if str(row2).strip() == "True" && prev!=-1 && row>=prev+5:
		f3.write(row)
	else:
		f4.write(row)

f.close()
f2.close()
f3.close()
f4.close()	
