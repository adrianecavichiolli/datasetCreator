import re

class FileNumberRegexMatcher:
    def __init__(self, numbers, regex = ".*_(.+)\..*"):
        self.numbers = numbers
        self.regex = re.compile(regex)

    def __call__(self, image):
        match = self.regex.match(image.getFilename())
        if match is not None:
            number = int(match.group(1))
            if number in self.numbers:
                return True
        return False

