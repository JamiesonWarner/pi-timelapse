#!/usr/bin/python3

import os
import errno

drive_dir = "/media/usbdrive"
data_dir_top = os.path.join(drive_dir, "timelapse")
for name in os.listdir(data_dir_top):
	data_dir = os.path.join(data_dir_top, name)
	try:
		os.rmdir(data_dir)
	except OSError as e:
		if e.errno == errno.ENOTEMPTY:
			continue

