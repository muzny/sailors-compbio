import collections
import random
import codecs
import math
from IPython.display import display
from IPython.display import HTML

# Distance Measures

# compute the Euclidean distance between the two sample data vectors
def euclidean_distance(sample_profile1, sample_profile2):
   # TODO 1: implement the Euclidean distance function

# Classifiers

class KNearestNeighbors:
    
    """ kNN Classifier """

    def train(self, train_set):
        self.train_set = train_set
        
    def classify(self, test_samples, k, distance_metric):
        labelled_samples = []
        for sample in test_samples:
            guess = self.classify_sample(sample, k, distance_metric)
            labelled_samples.append((sample, guess))
        return labelled_samples
        
    def classify_sample(self, test_sample, k, distance_metric):
        # find the k nearest neighbors of the test sample
        distances = [] # keeps track of the distance to each sample in the training set
        for train_sample in self.train_set:
	    # TODO 2: compute the distance between the gene expression profiles of the two samples
            # TODO 3: store the computed distance and the training sample it corresponds to
        
	distances.sort()
        nearest_neighbors = distances[:k] # keep the closest k samples
        # take a majority vote on their labels
        votes = {}
        for neighbor in nearest_neighbors:
            # TODO 4: implement the body of the loop to count how many votes each label has

        # choose the label with the most votes
        max_votes = 0
        max_label = 0
        for v in votes:
            if votes[v] > max_votes:
                max_label = v
                max_votes = votes[v]
        return max_label


# Evaluation utilities 

# compute the accuracy of the classification results
def evaluate_results(classified_samples):
  correct = [1 if guess == sample.get_label() else 0 for sample, guess in classified_samples]
  total = len(correct)
  acc = (correct.count(1) * 100.0) / total
  print 'Accuracy: %.2f%%' % acc
