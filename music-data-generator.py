import glob
import eyed3
import json
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--directory", required=True,
	help="Music Directory")
ap.add_argument("-o", "--output", required=True,
	help="Output file path")

args = vars(ap.parse_args())
files =glob.glob(args["directory"]+"/*.mp3")


data={}
for file in files:
	data[file]={}
	music=eyed3.load(file)
	data[file]['content']=music.tag.title+"|"+music.tag.artist+"|"+str(music.tag.recording_date)
	

with open(args["output"]+".json","wb") as f:
	json.dump(data,f)
	print " Music data saved successfully in %s" %  args["output"]+".json"