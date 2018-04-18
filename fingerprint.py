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
	with open("/sdcard/Tutorials/audio-fingerprinting/data.json") as f:
	    files = json.load(f)
	# Fingerprint all the mp3's in the directory we give it
	
	for fl in files:
	    print files[fl]["content"]
	    djv.fingerprint_file(fl,files[fl]["content"])


	
	