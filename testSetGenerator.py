#!/usr/bin/python3

from picamera import PiCamera

MAX_IMAGES = 10

def main():
	with PiCamera() as camera:
		camera.start_preview() 
		input("Press any key to start recording...")
		try:
			for i, filename in enumerate(camera.capture_continuous('testData/image{counter:02d}.jpeg')):
				if i==(MAX_IMAGES-1):
					break
		finally:
			camera.stop_preview()

	
if __name__ == "__main__":
	main()
