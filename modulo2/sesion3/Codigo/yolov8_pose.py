# -*- coding: utf-8 -*-

from ultralytics import YOLO
import cv2 as cv
import os
import argparse
import sys
import numpy as np
import math

def compute_angle(v1, v2):
    # Unit vector.
    v1u = v1 / np.linalg.norm(v1)
    # Unit vector.
    v2u = v2 / np.linalg.norm(v2)
    # Compute the angle between the two unit vectors.
    angle_deg = np.arccos(np.dot(v1u, v2u)) * 180 / math.pi
    return angle_deg

#Initialize the parameters
confThreshold=0.4 #Confidence threshold
iouThreshold=0.5 #Intersection over union threshold
#load a pretrained model (trained on COCO, which include 80 pre-trained classes.)
model = YOLO('yolov8n-pose.pt')

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
    outputFile=args.image[:-4]+'yolo_out.jpg'
elif (args.video):
    #Open the video file
    if not os.path.isfile(args.video):
        print("Input video file",args.image,"doesn't exist")
        sys.exit(1)
    cap=cv.VideoCapture(args.video)     
    outputFile=args.video[:-4]+'yolo_out.avi'
else:
    #Webcam input
    cap=cv.VideoCapture(0)
    outputFile="yolo_out_pose.avi"

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
    results = model.predict(frame,conf=0.6,save=True)
    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    keypoints_frame=[]
    bbox_frame=[]
    height,width,_=frame.shape
    for i in range(len(results[0].keypoints.xyn)):#extract keypoints for each object
        kp_obj_i=results[0].keypoints.xy[i,:].cpu().numpy()[:]
        keypoints_frame.append(kp_obj_i)
        boxes = results[0].boxes
        for box in boxes:
            b = box.xyxy[0].tolist()  # get box coordinates in (top, left, bottom, right) format
            print(b)
            bbox_frame.append(b)

        # To do: represent indexes of key-points
        for j in range(len(kp_obj_i)):
            cv.circle(annotated_frame, (int(kp_obj_i[j,0]), int(kp_obj_i[j,1])), 5, (0,0,255), -1)
            cv.putText(annotated_frame, str(j), (int(kp_obj_i[j,0]), int(kp_obj_i[j,1])), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv.LINE_AA)
        
        # Calcular los vectores
        hip_to_knee_right = kp_obj_i[14] - kp_obj_i[12]
        knee_to_ankle_right = kp_obj_i[16] - kp_obj_i[14]
        
        hip_to_knee_left = kp_obj_i[13] - kp_obj_i[11]
        knee_to_ankle_left = kp_obj_i[15] - kp_obj_i[13]
        
        # Calcular el ángulo
        angle_right = compute_angle(hip_to_knee_right, knee_to_ankle_right)
        angle_left = compute_angle(hip_to_knee_left, knee_to_ankle_left)
        
        # Dibujar el ángulo en la imagen
        cv.putText(annotated_frame, f"Angle right leg: {angle_right:.2f}", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
        cv.putText(annotated_frame, f"Angle left leg: {angle_left:.2f}", (50, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
            
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

