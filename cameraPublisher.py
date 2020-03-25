from io import BytesIO
from picamera import PiCamera
from PIL import Image

test_mode = False

class piCamPublisher:
	
	def __init__(self):
		self.__stream = BytesIO()
		self.__camera = PiCamera()
		self.__callback_list = []
	
	def add_callback(self, callback):
		self.__callback_list += [callback]
		
	def run(self):
		if test_mode:
			test_run(self.__callback_list)
			return
		try:
			for foo in self.__camera.capture_continuous(self.__stream, format='jpeg'):
				self.__stream.truncate()
				self.__stream.seek(0)
				image = Image.open(self.__stream)
				for fx in self.__callback_list:
					fx(image)
		finally:
			print('CLOSING SHIT!')
			self.__stream.close()


## below for testing
from time import sleep
from datetime import datetime as dt
from os import listdir

def test_callback(image):
	print(dt.now())

def test_run(callback_list):
	files = sorted(listdir('testData/'))
	for file in files:
		image = Image.open('testData/'+file)
		for fx in callback_list:
			fx(image)
