import collections
import random
import codecs
import math
from IPython.display import display
from IPython.display import HTML

# Distance Measures

# compute the Euclidean distance between the two sample data vectors
def euclidean_distance(sample_profile1, sample_profile2):
    distance = float(0)
    for i in range(len(sample_profile1)):
        distance += float(pow((sample_profile1[i] - sample_profile2[i]), 2))
    return math.sqrt(distance)


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
        # find the k nearest neighbors
        distances = [] # keeps track of the distance to each sample in the training set
        for train_sample in self.train_set:
	    # compute the distance between the gene expression profiles of the two samples
            distance = distance_metric(test_sample.get_gene_profile(), train_sample.get_gene_profile())
            distances.append((distance, train_sample))
        distances.sort()
        nearest_neighbors = distances[:k] # keep the closest k samples
        # take a majority vote on their labels
        votes = {}
        for neighbor in nearest_neighbors:
            sample = neighbor[1] # access the sample
            label = sample.get_label()
            if not label in votes:
                votes[label] = 0
            votes[label] += 1
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
