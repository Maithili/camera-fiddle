import cv2
from utils import *

class featureDescriptor:
	def __init__(self, parameters={}):
		self.extractor = None
		self.image = None
		self.keypoints = []
		self.descriptors = []
		self.params = {}

	def set_image(self, img):
		self.image = img

	def set_keypoints(self, keypoints):
		self.keypoints = keypoints

	def compute(self):
		pass

	def get_descriptors(self):
		return self.descriptors