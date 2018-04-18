Qpython Audio FingerPrinting
=======================

Implementing audio fingerprting on android using QPython & Dejavu

## Branches
  * **[Master](https://github.com/semirgoldu/qpython-dejavu)** 



## Dependency

1)Qpython
2)Numpy, Scipy, Matplotlib, pydub, pymysql, dejavu python packages
3)Termux for ffmpeg

You can get numpy,scipy and matplotlib packages on qpython by installing AIPY android mobile app from playstore
## Info

Dejavu uses MySQLdb mysql connector by default - in this package we will use pymysql instead with
one minor modifications.

* in pymysql/convertors.py
* line 110 

replace **return u"'%s'" % _escape_unicode(value)**
with **return u"'%s'" % _escape_unicode(u"'"+str(value)+"'")**

To make qpython use ffmpeg from Termux we will modify
pydub slightly.


* pydub/utils.py
* line 161-166 - setting ffmpeg path "/data/data/com.termux/files/usr/bin/ffmpeg"

* pydub/audio_segement.py
* line 504 - setting "/data/data/com.termux/files/usr/lib" as ld library path

**os.environ['LD_LIBRARY_PATH'] = "/data/data/com.termux/files/usr/lib"**
You must **chmod -R 0777 /data/data/com.termux/files/usr/lib** so
that Qpython has access to Termux

* dejavu/database_sql.py
* line 4-5 replace MySQLDb witg pymysql

**import pymysql as mysql**
**from pymysql.cursors import DictCursor**

## Usage

Use fingerprint.py to fingerprint your music directory

Use recognoze.py for recognizing music from db

More documentation on dejavu pypi package