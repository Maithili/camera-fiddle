import cv2
from feature_descriptor import featureDescriptor
from utils import *

class briefDescriptor (featureDescriptor):
	def __init__(self, parameters={}):
		super().__init__()
		self.extractor = cv2.xfeatures2d.BriefDescriptorExtractor_create()

	def compute(self):
		# descriptor is size of keypoints x 32
		self.get_keypoints, self.descriptors = self.extractor.compute(self.image, self.keypoints)
		