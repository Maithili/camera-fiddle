import cv2
import numpy
import matplotlib.pyplot as plt
from . import utils

class baseDetector:
	def __init__(self):
		self.image = None
		self.grayimage = None
		self.keypoints = []
		self.params = {}

	def set_image(self, image):
		self.image = image
		if(len(image.shape) == 2):
			print('Grayscale image detected!')
			self.grayimage = self.image
		else:
			if (len(image.shape) == 3):
				self.grayimage = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
			else:
				print('Unknown image format!')

	# needs overriding
	def detect(self):
		pass

	def get_keypoints(self):
		return self.keypoints

	def set_descriptor(self, descriptor):
		self.descriptor = descriptor

	def get_descriptors(self):
		if not len(self.keypoints):
			print('Cannot extract descriptors without keypoints!')
			return
		self.descriptor.set_image(self.image)
		self.descriptor.set_keypoints(self.keypoints)
		self.descriptor.compute()
		descriptors = self.descriptor.get_descriptors()
		return descriptors

	def draw(self):
		if not len(self.image):
			print('Cannot draw without an image!')
			return
		# cv2.drawKeypoints(self.image, self.keypoints, self.image, flags=4)
		for keypt in self.keypoints:
			x = int(round(keypt.pt[0]))
			y = int(round(keypt.pt[1]))		
			cv2.circle(self.image, (x,y), int(round(keypt.size)), color=(0,0,255), thickness = 2)
		plt.imshow(cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB))	
		plt.show()

class detectorShitomasi (baseDetector):
	def __init__(self, parameters={}):
		super().__init__()
		default_params = {'max_corners':25, 'quality_level':0.1, 'min_distance':10, 'block_size':5}
		self.params = utils.overwrite_parameters(parameters, default_params)
		
	def detect(self):
		corners = cv2.goodFeaturesToTrack(self.grayimage,self.params['max_corners'],self.params['quality_level'],self.params['min_distance'],blockSize=self.params['block_size'])
		self.keypoints = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=self.params['block_size']) for f in corners]