import warnings
import json
from time import sleep
import glob
import logging 
import re 
from dejavu import *
from dejavu.recognize import FileRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("djv.cnf") as f:
    config = json.load(f)

if __name__ == '__main__':
 
	# create a Dejavu instance
	djv = Dejavu(config)
	
	# Recognize audio from a file
	song = djv.recognize(FileRecognizer, "/sdcard/test.amr")
	print "From file we recognized: %s\n" % song

	
	