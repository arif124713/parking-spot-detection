import os
import cv2
import numpy as np
import pandas

from util import empty_or_not, get_parking_spots_bboxes

video_path='./parking_1920_1080_loop.mp4'
mask = './mask_1920_1080.png'
mask = cv2.imread(mask, 0)
cap= cv2.VideoCapture(video_path)
connected_components=   cv2.connectedComponentsWithStats(mask,4, cv2.CV_32S)
spots= get_parking_spots_bboxes(connected_components)

while True:
    ret, frame= cap.read()
    not_empty = 0
    empty = 0


    for spot in spots:
        x,y,w,h= spot
        spot_crop= frame[y:y + h, x:x + w, :]
        spot_status= empty_or_not(spot_crop)


        if spot_status:
            not_empty+=1
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            empty+=1
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        total = not_empty + empty

    cv2.putText(frame, str((f"available slots are {not_empty}/{total}")), (100, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0,0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

