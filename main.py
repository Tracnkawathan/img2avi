#!/usr/bin/env python3
# -*- encode: utf-8 -*-
# @Author   : A.Ohta
# @Version  : 1.0.0
"""main.py: Convert sequential image files to an .AVI movie file.
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
    parser = argparse.ArgumentParser()

    parser.add_argument("--debug", action='store_true', default=False,
                        help="enable debug mode if this is set.")

    args = parser.parse_args()

    # make an input list from the input folder.
    filelist = sorted(glob.glob('./input/*'), key=numericalSort)

    # define the codec and create the VideoWriter object.
    # determine height and width of the video from the first frame size.
    headframe = cv2.imread(filelist[0])
    head_height, head_width, _ = headframe.shape

    outpath = './outvideo.avi'
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    fps = 60  # TODO MUST use arguments!
    out = cv2.VideoWriter(outpath, fourcc, fps, (head_width, head_height))

    # print how to operate for debug mode.
    if args.debug is True:
        print("# Debug mode will display every frame pictures.")
        print("# Press 0 on the display window if you want to see next.")
    # for
    for filename in filelist:
        # Grab a first frame
        frame = cv2.imread(filename)
        height, width, _ = frame.shape

        out.write(frame)

        # debug mode
        if args.debug is True:
            print("[debug] showing:", filename)
            cv2.imshow('color', frame)
            cv2.waitKey(0)

    # Cleanup
    out.release()
    print("The video is generated at: ", outpath)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
