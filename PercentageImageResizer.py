class PercentageImageResizer:
    def __init__(self, imageResizer, percentageSize):
        self.imageResizer = imageResizer
        self.percentageSize = percentageSize
    
    def __call__(self, image):
        if (self.percentageSize == 1):
            return image
        
        rows, cols = image.shape[0], image.shape[1]
        newRowSize = int(self.percentageSize * rows)
        newColSize = int(self.percentageSize * cols)
            
        return self.imageResizer.resize(image, (newRowSize, newColSize))

