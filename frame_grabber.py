# -*- coding: utf-8 -*-
# Grab frames from video by OpenCV.

import os
import sys
import cv2

def grab_frames(video, start, end, outfile_name):
    print(f'Starting from frame {start} to {end}')
    for i in range(int(video.get(cv2.CAP_PROP_FRAME_COUNT))):
        success, img = video.read()
        if not success: 
            print(f'Fail at frame: {i}')
            continue
        if i < start:   continue;
        if i > end:     break;
        cv2.imwrite(f'{outfile_name}-{i:4d}.png', img)



if __name__ == '__main__':
    video = cv2.VideoCapture(sys.argv[1])
    fps = video.get(cv2.CAP_PROP_FPS)
    start = int(input('Start Second: ')) * fps
    end = int(input('End Second: ')) * fps
    
    path = os.path.dirname(sys.argv[1])
    name = os.path.basename(sys.argv[1]).split('.')[0]
    os.chdir(path)
    if not os.path.isdir(name):
        os.mkdir(name)
    os.chdir(name)

    grab_frames(video, start, end, name)
