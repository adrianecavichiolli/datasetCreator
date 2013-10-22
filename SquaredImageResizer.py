class SquaredImageResizer:
    def __init__(self, imageResizer, newSize):
        self.imageResizer = imageResizer
        self.newSize = (newSize, newSize)
    
    def resize(self, image):
        if (image.shape[0] == self.newSize[0] and 
           image.shape[1] == self.newSize[1]):
            return image
        
        rows, cols = image.shape[0], image.shape[1]
        difference = abs(rows - cols)
        start = difference / 2
        
        if rows > cols:
            imgToResize = image[start:start+cols, :]
        elif cols > rows:
            imgToResize = image[:, start:start+rows]
        else:
            imgToResize = image
            
        return self.imageResizer.resize(imgToResize, self.newSize)