from flask import Flask,render_template,Response
#video straming 
#using python opencv package
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frame():
        while True:
             #Read the camera frame
            success,frame=camera.read()
            if not success:
                break
            else:
                ret,buffer=cv2.imencode('.jpg',frame)
                frame=buffer.tobytes()
            yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n')
        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
    
    
    '''
    OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library.
    It provides a wide range of functions and tools for various computer vision tasks, such as image and video processing, 
    object detection, face recognition, optical character recognition (OCR), camera calibration, and more.

OpenCV was originally developed by Intel and later supported by Willow Garage and Itseez (which was later acquired by Intel as well). The library is written in C++ and offers interfaces for various programming languages, including Python and Java.

Key features of OpenCV include:

Image Processing: OpenCV offers a plethora of image processing functions, such as filtering, edge detection, color space conversion, morphology, and histogram analysis.

Computer Vision Algorithms: The library provides implementations of various computer vision algorithms, including feature detection (e.g., SIFT, SURF), object tracking, image stitching, and camera calibration.

Machine Learning: OpenCV includes machine learning algorithms and tools, such as support vector machines (SVM), k-nearest neighbors (k-NN), and decision trees. It also integrates with other machine learning libraries like TensorFlow and PyTorch.

Object Detection and Tracking: OpenCV includes pre-trained models and functions for object detection, face detection, and tracking using techniques like Haar cascades and deep learning-based methods.

GUI Tools: OpenCV provides tools for creating graphical user interfaces (GUIs) to visualize and interact with image and video data.

OpenCL and CUDA Support: OpenCV can leverage hardware acceleration through OpenCL and CUDA, allowing for faster computation on supported GPUs.

Cross-Platform: OpenCV is designed to work on various operating systems, including Windows, macOS, Linux, Android, and iOS.

OpenCV is widely used in both academic and industrial settings for research, development, and practical applications in fields like robotics, computer vision, augmented reality, self-driving cars, medical imaging, and more. Its comprehensive set of functionalities makes it a valuable tool for anyone working with image and video data and wanting to perform advanced computer vision tasks.
    '''