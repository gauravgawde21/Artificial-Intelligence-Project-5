__author__ = 'gp'

class Email:
    def __init__(self, eid, label):
        self.eid = eid;
        self.label = label;
        self.words = {};

    def geteid(self):
        return self.eid;

    def getLabel(self):
        return self.label;

    def addWord(self,word,count):
        self.words.update(word,count);

    def getWords(self):
        return self.words;