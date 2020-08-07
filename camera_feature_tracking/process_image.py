import cv2
from . import feature_detector
from . import feature_descriptor

def process_image(image):
	myDetector = feature_detector.detectorShitomasi()
	myDetector.set_image(image)
	myDetector.detect()
	kps = myDetector.get_keypoints()
	myDetector.set_descriptor(feature_descriptor.briefDescriptor())
	desc = myDetector.get_descriptors()
	myDetector.draw()
	return ({"keypoints":kps, "descriptors":desc, "image":image})
