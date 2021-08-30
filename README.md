As we see currently there are lots of applications of face detection, like some of the examples where face detection is used is in smartphone face detection is used to authenticate the identity of the user, face detection is used in home security cameras and so on. So, in this program we use the argparse module for command line interface and pass the name of the image as an argument to it. From that it determines the number of faces in the specified image in the command line and saves the output image with rectangle markings on the faces of that image.

The format to pass the arguments in the command line is:

python main.py -i input1.png , where input1.png is the image_name and you can specify any image_name in which you want to detect faces.