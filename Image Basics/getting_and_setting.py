#!/usr/bin/env python

import argparse
import cv2

# use argparse to handle parsing our command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

# loading the actual image off of
# disk and displaying it to us.
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# important to note that OpenCV stores RGB
# channels in reverse order
(b, g, r) = image[0, 0]
print "Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b)

image[0, 0] = (0, 0, 255)

(b, g, r) = image[0, 0]
print "Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b)

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)

cv2.waitKey(0)
