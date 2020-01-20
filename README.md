# Everwell
Mini project for Everwell 

All requirements for running this poject can be found in requirements.txt
To run the project, you must have python 3.* installed on the machine.
As a best practice, we will install this project in its own virtual environment.

1. Clone the repository
2. Navigate to everwell/ and in a terminal window inside everwell run -> virtualenv -p python3 virt (this will create a virtual environment called virt inside everwell)
3. Activate the environment, run -> source virt/bin/activate (to exit anytime, run -> deactivate)
4. Run -> pip3 install -r requirements.txt (To install the dependencies)
5. Run -> python vid_det.py (script to input video and apply face detection)
6. Input the name of video file (including the extension)
7. Choose 1. too apply face detection test.

The progam outputs in case of
1. Face detection
  a. Face_detection_intermediate.jpg: Grayscale image of the extracted frame
  b. Face_detection_final.jpg: Final image with detected faces (may not be generated for rejected cases)
2. Backgroun Subtractor
  a. Subtracted_background.jpg: Foreground mask found using MOG2
