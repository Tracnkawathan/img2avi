# img2avi

## description

Convert sequential image files to an .AVI video file.
Make any number of pictures files with consecutive numeric name, like `0001.png`, `0002.png`, `0003.png`, ...
And then, put every pictures into the `./input` folder. Finally execute this `main.py` script.
This program sorts the input pictures by names and make an avi video named `./out.avi`.
you also can change the input and output file path or fps by the command line options.

![https://raw.github.com/wiki/Tracnkawathan/img2avi/demo.gif](https://raw.github.com/wiki/Tracnkawathan/img2avi/demo.gif)

This tool is implemented just for my studying, thanks!

## Requirement

This tool requires python 3 and OpenCV.
if you don't have OpenCV yet, just install it by using `pip`.
```
$ pip install opencv-python
```

## Usage

By default, This program will check `./input` folder and make `./out.avi` file as an output.
FPS of the output will be 20 by default.

```
$ python3 main.py
$ python3 main.py --fps 60 --input <path/to> --out <path/to/output.avi>
```

You can use debug mode if you want to check whether the sequence of the output is right or not.
press `0` key on the image window to show next frame.

```
$ python3 main.py --debug
```

If you want more infomation, you can see help by `-h` option.

```
$ python3 main.py -h
```

## Install

Please `git clone` this repo. Thank you!
```
$ git clone https://github.com/Tracnkawathan/img2avi.git
```
