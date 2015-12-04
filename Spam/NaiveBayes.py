__author__ = 'gp'

import sys;
import math;

class NaiveBayes:

    def __init__(self,smooth):
        self.labelCounts = None;
        self.labelProbs  = {};
        self.priors      = None;
        self.vocab       = set();
        self.smooth      = smooth;

    def train(self, emails):
        self.computeLabel(emails);
        self.computePriors(len(emails));
        #Compute the total number of word positions per label.
		#Create a set of all words in our vocabulary.
        positions = {}
        for label in self.labelCounts:
            total = 0;
            for word in self.labelCounts[label]:
                total = total + self.labelCounts[label][word];
                self.vocab.add(word);
            self.positions.update({label:total});
        self.computeWordProbs(positions);

    def predict(self, email):
        classifier = None;
        prob = -(sys.maxint);
        for label in self.labelProbs:
            p = self.priors[label];
            for word in email.getWords():
                #Uses additive logs since probabilities are so small they will
				#often drop to about 0 when multiplied together. Also support
				#case for when word doesn't exist.
                if(word in self.labelProbs[label]):
                    p = p + math.log(self.labelProbs[label][word] * email.getWords()[word]);
                else:
                    p = p + math.log(self.labelProbs[label][""]) * email.getWords()[word];

            if(prob < p):
                classifier = label;
                prob = p;

        return classifier;

    def computeLabelCounts(self, emails):
        for e in emails:
            if(not(e.getLabel() in self.labelCounts)):
                temp_obj = {};
                self.labelCounts.update({e.getLabel():temp_obj});

            #Update a total count of labels seen.
            if(e.getLabel() in self.priors):
                self.priors.update({e.getLabel():self.priors[e.getLabel()] + 1.0});
            else:
                self.priors.update({e.getLabel():1.0});

            #Update the count of each word seen per label
            for word in e.getWords():
                counts = self.labelCounts[e.getLabel()];
                if(word in counts):
                    counts.update({ word: e.getWords()[word] + counts[word]});
                else:
                    counts.update({word: e.getWords()[word]})

    def computePriors(self, total):
        for label in self.priors:
            self.priors.update({label:self.priors[label]/total});

    def computeWordProbs(self,positions):
        for label in self.labelCounts:
            probs = {};

            #Denominator is: N * (|Vocabulary| + 1) * smooth.
            den = positions[label] + self.smooth *(len(self.vocab) + 1);
            for word in self.labelCounts[label]:
                num =  self.labelCounts[label][word] + self.smooth;
                probs.update({word : num/den});

            #Default probability for when the word doesn't exist in the vocab.
            probs.update({"" : self.smooth/den});
            self.labelProbs.update({label : probs});

