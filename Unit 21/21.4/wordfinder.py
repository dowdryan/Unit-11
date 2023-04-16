import random


class WordFinder:
    def __init__(self, filename):
        """Returns the total number of words found in the given file"""
        dict_file = open(filename)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Uses a for loop to get each line/word, and gets rid of any white spaces in each line"""
        return [word.strip() for word in dict_file]

    def random(self):
        """Picks out and returns a random word from the file"""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Searches for any blank lines/comments and skips them"""
    def parse(self, dict_file):
        return [word.strip() for word in dict_file
                if word.strip() and not word.startswith("#")]
