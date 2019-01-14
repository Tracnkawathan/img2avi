#!/usr/bin/env python3
# -*- encode: utf-8 -*-
# @Author   : A.Ohta
# @Version  : 1.0.0
"""main.py: Convert sequential image files to an .AVI video file.
"""

import re
import glob
import argparse
import cv2


def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def main():
    # argparse
    parser = argparse.ArgumentParser(
        description="Convert sequential image files to an .AVI video file.\n\n\
        Make any number of pictures files with consecutive numeric name, like 0001.png, 0002.png, ...\n\
        And then, put every pictures into the ./input folder. Finally execute this main.py script.\n\
        This program sorts the input pictures by names and make an ./avi video named out.avi.\n\
        you also can change the input and output file path or fps by the command line options.")

    parser.add_argument("--debug", action='store_true', default=False,
                        help="Enable debug mode if this is set. default=False")
    parser.add_argument("--fps", type=int, action='store', nargs='?', default=20,
                        help="Fps of the output avi file. default=20")
    parser.add_argument("--input", type=str, action='store', nargs='?', default='./input',
                        help="the directory path of the input folder. default=\'./input\'")
    parser.add_argument("--out", type=str, action='store', nargs='?', default='./out.avi',
                        help="File name of the output video. default=\'./out.avi\'")
    args = parser.parse_args()

    # make an input list from the input folder.
    filelist = sorted(glob.glob(args.input+'/*'), key=numericalSort)

    # define the codec and create the VideoWriter object.
    # determine height and width of the video from the first frame size.
    headframe = cv2.imread(filelist[0])
    head_height, head_width, _ = headframe.shape
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    out = cv2.VideoWriter(args.out, fourcc, args.fps,
                          (head_width, head_height))

    # print how to operate for debug mode.
    if args.debug is True:
        print("# Debug mode will display every frame pictures.")
        print("# Press 0 on the display window if you want to see next.")

    # read images and write into the video.
    for filename in filelist:
        # Grab a first frame
        frame = cv2.imread(filename)
        height, width, _ = frame.shape

        if (height != head_height) or (width != head_width):
            print("Image size does not match with the first frame.")
            print("Check this file: ", filename)
            print("Converting incomplete.")
            break

        # Write into the video
        out.write(frame)

        # debug mode
        if args.debug is True:
            print("[debug] showing:", filename)
            cv2.imshow('color', frame)
            cv2.waitKey(0)

    # Cleanup
    out.release()
    print("The video is generated at: ", args.out)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
