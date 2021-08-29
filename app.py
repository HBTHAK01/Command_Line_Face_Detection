import cv2
import matplotlib.pyplot as plt

def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def detect_faces(cascade, test_image, scaleFactor = 1.1):
    image_copy = test_image.copy()
    # gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    faces_cascade = cascade.detectMultiScale(image_copy, scaleFactor = scaleFactor, minNeighbors = 5)
    print('Faces found in the given image is: ', len(faces_cascade))

    for (x, y, w, h) in faces_cascade:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 10)

    return image_copy

