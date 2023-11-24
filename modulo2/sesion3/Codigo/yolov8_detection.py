# -*- coding: utf-8 -*-

from ultralytics import YOLO
import cv2 as cv
import os
import argparse
import sys


#Initialize the parameters
confThreshold=0.4 #Confidence threshold
iouThreshold=0.5 #Intersection over union threshold
#load a pretrained model (trained on COCO, which include 80 pre-trained classes.)
model = YOLO('yolov8m-seg.pt')

parser=argparse.ArgumentParser(description='Object Detection using YOLOv8 in OPENCV')
parser.add_argument('--image',help='Path to image file.')
parser.add_argument('--video', help='Path to video file')
args=parser.parse_args()

print(model.names)

if (args.image):
    #Open the image file
    if not os.path.isfile(args.image):
        print("Input image file",args.image,"doesn't exist")
        sys.exit(1)
    cap=cv.VideoCapture(args.image)
    outputFile=args.image[:-4]+'yolo_out8m-seg.jpg'
elif (args.video):
    #Open the video file
    if not os.path.isfile(args.video):
        print("Input video file",args.image,"doesn't exist")
        sys.exit(1)
    cap=cv.VideoCapture(args.video)     
    outputFile=args.video[:-4]+'yolo_out8m-seg.avi'
else:
    #Webcam input
    cap=cv.VideoCapture(0)
    outputFile="yolo_out8m-seg.avi"

winName='Deep learning object detection in OpenCV'
cv.namedWindow(winName,cv.WINDOW_NORMAL)

#Get the video writer initialized to save the output video
if (not args.image):
    vid_writer=cv.VideoWriter(outputFile,cv.VideoWriter_fourcc('M','J','P','G'),5,(round(cap.get(cv.CAP_PROP_FRAME_WIDTH)),round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
    
while cv.waitKey(1)<0:
    
    
    #get frame from the video
    hasFrame, frame = cap.read()
    
    #Stop the program if reached end of video
    if not hasFrame:
        print("Done processing !!!")
        print("Output file is stored as ", outputFile)
        cv.waitKey(3000)
        break
    
    img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    #results = model.predict(frame,classes=[0,2],conf=0.75)
    results = model.predict(frame,conf=confThreshold,iou=iouThreshold,save=False)
    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    
    #Write the frame with the detection boxes
    if (args.image):
        cv.imwrite(outputFile,annotated_frame)
    else:
        vid_writer.write(annotated_frame)
    cv.imshow(winName,annotated_frame)

cap.release()
cv.destroyAllWindows()
if (not args.image):
    vid_writer.release()

