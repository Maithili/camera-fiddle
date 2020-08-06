#!/usr/bin/python3

import cv2
from detector_shitomasi import detectorShitomasi
from brief_descriptor import briefDescriptor

def main():
	myDetector = detectorShitomasi()

	img = cv2.imread('pic.jpg')
	myDetector.set_image(img)
	myDetector.detect()
	myDetector.set_descriptor(briefDescriptor())
	desc = myDetector.get_descriptors()
	print(desc.shape)
	myDetector.draw()

if __name__ == "__main__":
	main()