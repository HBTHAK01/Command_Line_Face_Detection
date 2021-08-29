import cv2
import sys
import matplotlib
import matplotlib.pyplot as plt

from argparse import ArgumentParser

import app

def main():
    haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    parser = ArgumentParser()
    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    args = parser.parse_args()

    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        input_image = cv2.imread(args.image, 0)

    function_call = app.detect_faces(haar_cascade_face, input_image)
    plt.imshow(app.convertToRGB(function_call))
    cv2.imwrite("output.png", function_call)
    
if __name__ == "__main__":
    main()