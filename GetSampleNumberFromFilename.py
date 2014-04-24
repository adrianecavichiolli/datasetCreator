import re

class GetSampleNumberFromFilename:
    def __init__(self):
        self.regex = re.compile("[^_]*_(.*)_")

    def __call__(self, image):
        return self.regex.match(image.getFilename()).group(1)
