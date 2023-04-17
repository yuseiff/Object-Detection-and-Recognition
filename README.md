# Object-Detection
The code is an implementation of an object detection camera using the OpenCV and Pyttsx3 modules in Python. The purpose of the code is to detect objects in real-time using a camera and provide an audible warning to the user in case of any potential danger.

Here is a brief description of what the code does:

Import necessary modules: The code imports the OpenCV and Pyttsx3 modules for image processing and text-to-speech functionality, respectively.

Initialize the camera: The code initializes the camera by creating a VideoCapture object with the camera index set to 0, which is the default camera.

Load pre-trained models: The code loads pre-trained models for object detection from two files - 'frozen_inference_graph.pb' and 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'.

Detect objects: The code uses the pre-trained models to detect objects in real-time by calling the detect() method of the DetectionModel object. The method returns the class IDs, confidence scores, and bounding boxes for the detected objects.

Draw rectangles and display names: The code draws rectangles around the detected objects and displays their names on the video window using the Class_Names list.

Provide an audible warning: The code uses the Pyttsx3 module to provide an audible warning to the user in case of any potential danger. It says the name of the object using the engine.say() method and runs it using the engine.runAndWait() method.

Display the video: The code displays the video window with the detected objects and their names using the cv2.imshow() method.

Close the window: The code waits for the user to press the 'q' key to close the video window using the cv2.waitKey() method.

Overall, the code performs real-time object detection using pre-trained models and provides an audible warning to the user in case of any potential danger. It is a basic implementation of an object detection camera using OpenCV and Pyttsx3 modules in Python.
