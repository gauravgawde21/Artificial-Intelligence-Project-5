__author__ = 'gp'

from Email import Email
from NaiveBayes import NaiveBayes

class Classifier:

    def init_process(self):
        smooth      = 1
        smooth      = input('Enter smoothing parameter')

        #Parse training and test data into sets.
        trainEmails = self.parseEmails("./DataSet/train");
        testEmails  = self.parseEmails("./DataSet/test");

        #Train the data and then predict the classifier
        nb = NaiveBayes(smooth);
        nb.train(trainEmails);
        correctPred = 0;

        for e in testEmails:
            if(e.getLabel() == nb.predict(e)):
                correctPred = correctPred + 1

        #Print accuracy statistics
		self.computeAccuracy(correctPred, len(testEmails));

    def parseEmails(self,fileName):
        emails = {};
        with open(fileName) as f:
            for line in f:
                eid       = line.split( )[0];
                label     = line.split( )[1];
                email_obj = Email(eid, label);
                word      = line.split( )[2];
                count     = line.split( )[3];
                email_obj.addWord(word,count);
                emails.add(email_obj);
        return emails;

    def computeAccuracy(self,matches,total):
        print "Test-Data Prediction Statistics";
        print "-------------------------------";
        print "Matches::",matches;
        print "Accuracy::",round((100.0 * (matches / total)),2);
