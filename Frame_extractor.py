import csv
import glob
import sys
import os
import os.path
from subprocess import call

"""Extracting can be done with ffmpeg:
    `ffmpeg -i video.mpg -vf fps=30/1 image-%04d.jpg`
"""

print('sys.argv[0] =', sys.argv[0])
pathname = os.path.dirname(sys.argv[0])
dir_path = os.path.abspath(pathname)


def extract_files():

    dataset_location = os.path.join(dir_path,"Fine-Grained Video Classification","Dogs_test")
    class_folders = glob.glob(os.path.join(dataset_location,"*"))
    for vid_class in class_folders:
        class_files = glob.glob(os.path.join(vid_class,"*.mp4"))
        for vid_path in class_files:
            video_parts = get_video_parts(video_path=vid_path)
            classname, filename_no_ext, filename, file_path_no_ext = video_parts
            src = os.path.join(dataset_location, classname, filename)
            os.mkdir(file_path_no_ext)
            dest = os.path.join(file_path_no_ext,'thumb%04d.jpg')
            call(["ffmpeg", "-i", src,"-vf","fps=20/1", dest])

def get_video_parts(video_path):
    """Given a full path to a video, return its parts."""
    file_path_no_ext = video_path.split('.')[0]
    parts = video_path.split(os.path.sep)
    filename = parts[-1]
    filename_no_ext = filename.split('.')[0]
    classname = parts[-2]

    return classname, filename_no_ext, filename, file_path_no_ext

def main():
    extract_files()

if __name__ == '__main__':
    main()