from LabeledImage import LabeledImage

class LabeledImageFactory:
	def create(self, img, filename):
		return LabeledImage(img, filename, LabeledImage.getLabelFromFilename(filename))