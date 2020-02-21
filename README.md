# About
The rasperry pi comes with a command `raspistill` which automatically captures images at regular intervals.

This repository provides a service to start timelapse capture on pi boot, to stitch the images into a video, and to display everything via a local server.

# Installation

* Configure systemd to run the timelapse service on system boot:
    * Edit `timelapse_capture.service` so that `ExecStart` points to your copy of main.py
    * Copy `timelapse_capture.service` into `/etc/systemd/system`
    * Run `systemctl enable timelapse_capture`
    * Run `systemctl start timelapse_capture`
