"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    
    ...
    def __init__(self,path):
        self.path = path
        file = open(self.path,"r")
        self.count = 0
        for x in file:
            self.count += 1
        file.close()
        print(f"{self.count} words read")

    def random(self):
        file = open(self.path,"r")
        content = file.readlines()
        random_line = random.randint(0,self.count)
        print(content[random_line])
        file.close()
        








