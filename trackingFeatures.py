#!/usr/bin/python

from os import listdir
import cv2
import numpy
from matplotlib import pyplot as plt

MAX_FRAMES = 5

def features_callback(image):
	grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	corners = cv2.goodFeaturesToTrack(grayImage, 25,0.1,10)
	corners = numpy.int0(corners)
	for i in corners:
		x,y = i.ravel()
		cv2.circle(image,(x,y),10,255,-1)
	plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
	plt.show()

def test_run_video(callback_list):
	video = cv2.VideoCapture('carVideo/testVid.MOV')
	frame_count = 1
	while(video.isOpened()):
		ret, frame = video.read()
		for fx in callback_list:
			fx(frame)
		frame_count = frame_count + 1
		if (frame_count > MAX_FRAMES):
			break

def test_run_images(callback_list):
	files = sorted(listdir('testData/'))
	frame_count = 1
	for file in files:
		image = cv2.imread('testData/'+file)
		for fx in callback_list:
			fx(image)
		frame_count = frame_count + 1
		if (frame_count > MAX_FRAMES):
			break

def main():
	callback_list = [features_callback]
	test_run_video(callback_list)
	test_run_images(callback_list)

if __name__ == "__main__":
	main()