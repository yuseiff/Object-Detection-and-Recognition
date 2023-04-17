import cv2,os
import pyttsx3 as pyv
os.system('cls')

cam=cv2.VideoCapture(0)

known_names=[]
engine=pyv.init()
Class_Names=[]
class_path='Files/coco.names'

with open(class_path,'rt') as f:
        Class_Names=f.read().strip('\n').split('\n')
while True:
    ret, vid= cam.read()
    vid=cv2.resize(vid,(800,500))
   
    
    file1_path='Files/frozen_inference_graph.pb'
    file2_path='Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    
    net=cv2.dnn_DetectionModel(file1_path,file2_path)
    
    net.setInputSize(320,230)
    net.setInputScale(1.0/127.5)
    net.setInputMean((127.5,127.5,127.5))
    net.setInputSwapRB(True)
    
    Class_Ids,confs,bbox=net.detect(vid,confThreshold=0.6)
    
    for Class_id, confidence, box in zip(Class_Ids,confs,bbox):
        
        cv2.rectangle(vid,box,(0,255,0),thickness=3)
        cv2.putText(vid,Class_Names[Class_id-1],(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        if Class_Names[Class_id-1] not in known_names:
            engine.say(Class_Names[Class_id-1])
            engine.runAndWait()
            known_names.append(Class_Names[Class_id-1])
        
    cv2.imshow('Window',vid)
    
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
    