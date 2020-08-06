import cv2
import numpy
import matplotlib.pyplot as plt

class featureDetector:
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
		for keypt in self.keypoints:
			x = int(round(keypt.pt[0]))
			y = int(round(keypt.pt[1]))		
			cv2.circle(self.image, (x,y), int(round(keypt.size)), color=(255,0,0))
		plt.imshow(cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB))	
		plt.show()
