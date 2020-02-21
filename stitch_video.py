#!/usr/bin/python3
import os
import subprocess

top_dir = "/media/usbdrive/timelapse"
subdirs = os.listdir(top_dir)
print("Listing {}".format(top_dir))
for i, d in enumerate(subdirs):
    print("[{}] {}".format(i, d))
ans = int(input("Choose a source directory (e.g. 2): "))
chosen_dir = subdirs[ans]

data_dir = os.path.join(top_dir, chosen_dir)
out_path = os.path.join(data_dir, "timelapse.mp4")
infiles_path = os.path.join(data_dir, "image%06.jpg")
print("Making timelapse {}...".format(out_path))

# Uncomment to use ffmpeg library
"""
process = subprocess.Popen([
    "ffmpeg",
    "-framerate", "25", # fps
    "-i", os.path.join(data_dir, "image%06d.jpg"), # infiles
    "-c:v", "libx264", # codec
    "-profile:v", "high", # high quality
    "-crf", "20", # constant quality mode
    "-pix_fmt", "yuv420p", # use YUV pixel format and 4:2:0 Chroma subsampling
    out_path
])
"""

os.chdir(data_dir)
process = subprocess.Popen("avconv -r 10 -i image%06d.jpg -r 10 -vcodec libx264 -vf scale=1280:720 timelapse.mp4", shell=True)

process.wait()
print("Done.")
