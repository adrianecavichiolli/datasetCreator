from LabeledImage import LabeledImage

class LabeledImageFactory:
	def __init__(self, getLabelFunction, grayscale):
		self.getLabelFunction = getLabelFunction
		self.grayscale = grayscale
		
	def create(self, img, filename):
		return LabeledImage(img, filename, self.getLabelFunction(filename), self.grayscale)
	
