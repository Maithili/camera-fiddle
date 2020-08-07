import cv2

class baseDescriptor:
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

class briefDescriptor (baseDescriptor):
	def __init__(self, parameters={}):
		super().__init__()
		self.extractor = cv2.xfeatures2d.BriefDescriptorExtractor_create()

	def compute(self):
		# descriptor is size of keypoints x 32
		self.get_keypoints, self.descriptors = self.extractor.compute(self.image, self.keypoints)
