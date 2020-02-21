#!/usr/bin/python3
"""
main.py
Run to continuously capture images and save them to the flashdrive.
Running main.py will:
    (1) create a new directory on the flash drive
    (2) periodically save captures to the created directory
"""

import os
from datetime import datetime

# Configure drive directory in /etc/fstab
drive_dir = "/media/usbdrive"
data_dir_top = os.path.join(drive_dir, "timelapse")
data_dir = os.path.join(data_dir_top, datetime.now().strftime("From%m-%d-%Y,%Hh-%Mm-%Ss"))
print("Creating new directory", data_dir)

try:
	os.makedirs(data_dir)
except OSError as e:
	import errno
	if e.errno != errno.EEXIST: # data dir already exists
		raise
	pass


# Begin capturing data
output_str = os.path.join(data_dir, "image%06d.jpg")

from datetime import timedelta
import subprocess

# raspistill tl parameter configures the interval between shots in the timelapse
tl = int(timedelta(minutes=5)/timedelta(milliseconds=1))

# Uncomment to set a timeout after which raspistill will cease taking pictures
# t = int(timedelta(hours=8)/timedelta(milliseconds=1))

# A timeout of zero will cause raspistill to continue the timelapse in perpetuity
t = 0

print("Beginning timelapse...")
process = subprocess.Popen(["raspistill", "-t", str(t), "-tl", str(tl), "-o", output_str])
process.wait()

