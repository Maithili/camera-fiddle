import cv2
from detector_shitomasi import detectorShitomasi

def main():
	myDetector = detectorShitomasi()
	img = cv2.imread('pic.jpg')
	myDetector.set_image(img)
	myDetector.detect()
	myDetector.draw()

if __name__ == "__main__":
	main()