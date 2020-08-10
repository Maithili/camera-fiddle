#!/usr/bin/python3

from os import listdir
import cv2
import numpy
from matplotlib import pyplot as plt

from camera_feature_tracking import *
from track_camera_frames import *

MAX_FRAMES = 1600

def match(frame1, frame2):
	bf = cv2.BFMatcher_create(crossCheck = True)
	matches = bf.knnMatch(frame1["descriptors"],frame2["descriptors"], k=1)
	matchesImage = cv2.drawMatchesKnn(frame1["image"],frame1["keypoints"],frame2["image"],frame2["keypoints"],matches,None)
	plt.imshow(cv2.cvtColor(matchesImage,cv2.COLOR_BGR2RGB))	
	plt.show()
	return matches

def test_run_video():
	video = cv2.VideoCapture('testVid.MOV')
	frame_count = 1
	previous_frame = {}
	while(video.isOpened()):
		if(frame_count % 500 == 0):
			ret, image = video.read()
			current_frame = process_image(image)
			if(previous_frame):
				# diff = current_frame["image"]-previous_frame["image"]
				# plt.imshow(diff)
				# plt.show()
				matches = match(current_frame, previous_frame)
				kp_pairs = get_keypoint_pairs(matches, previous_frame, current_frame)
				F = eight_point_match(kp_pairs[:8])
				# for pair in kp_pairs:
				# 	check_F(pair,F)
				# F = eight_point_match(kp_pairs[-8:])
				# for pair in kp_pairs:
				# 	check_F(pair,F)
			previous_frame = current_frame
		frame_count = frame_count + 1
		if (frame_count > MAX_FRAMES):
			break

def get_keypoint_pairs(matches, previous_frame, current_frame):
	keypoint_pairs = []
	if(not(matches)):
		print("Got no matches!!")
	for m in matches:
		if len(m) ==1:
			keypoint_pairs.append((current_frame["keypoints"][m[0].trainIdx].pt, previous_frame["keypoints"][m[0].queryIdx].pt))
	return keypoint_pairs

# def test_run_images():
# 	files = sorted(listdir('testData/'))
# 	frame_count = 1
# 	previous_frame = {}
# 	for file in files:
# 		image = cv2.imread('testData/'+file)
# 		current_frame = process_image(image)
# 		if(previous_frame):
# 			matches = match(current_frame, previous_frame)
# 			print(matches)

# 		previous_frame = current_frame
# 		frame_count = frame_count + 1
# 		if (frame_count > MAX_FRAMES):
# 			break

def main():
	test_run_video()
	# test_run_images()

if __name__ == "__main__":
	main()