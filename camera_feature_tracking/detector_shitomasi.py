import cv2
from feature_detector import featureDetector
from utils import *

class detectorShitomasi (featureDetector):
	def __init__(self, parameters={}):
		super().__init__()
		default_params = {'max_corners':25, 'quality_level':0.01, 'min_distance':10, 'block_size':3}
		self.params = overwrite_parameters(parameters, default_params)
		
	def detect(self):
		corners = cv2.goodFeaturesToTrack(self.grayimage,self.params['max_corners'],self.params['quality_level'],self.params['min_distance'],blockSize=self.params['block_size'])
		self.keypoints = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=self.params['block_size']) for f in corners]