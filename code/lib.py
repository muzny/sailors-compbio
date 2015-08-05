import collections
import random
import codecs
from IPython.display import display
from IPython.display import HTML

class Sample:

  """ Represents a single sample in the dataset """

  def __init__(self, class_label, gene_expression_profile):
    self.label = class_label
    self.gene_profile = gene_expression_profile

  def __str__(self):
    return 'Sample with label: ' + str(self.label)

  # returns the class label (i.e. tissue type) of this sample
  def get_label(self):
    return self.label

  # returns the expression data for each gene in the sample
  def get_gene_profile(self):
    return self.gene_profile

class DataSet:

  """ Stores the gene expression dataset """ 

  def __init__(self, matrix_file_path, label_file_path):
    # load class labels from the labels file
    labels_file = open(label_file_path)
    labels = [int(line.strip()) for line in labels_file]
    
    # load gene expression data from the matrix file
    matrix_file = open(matrix_file_path)
    samples = []
    matrix_line_index = 0
    # each line in the file corresponds to a sample
    for line in matrix_file:
      # parse the expression data for each gene in the sample
      gene_profile = map(float, line.strip().split('\t'))
      # store the sample data
      samples.append(Sample(labels[matrix_line_index], gene_profile))
      matrix_line_index += 1
    # shuffle the data to randomize the order of the samples
    random.seed(1)
    random.shuffle(samples)

    # split the data into a train and test set
    train_size = int(len(samples) * 0.66) # 2/3 of the data
    self.train = samples[:train_size]
    self.test = samples[train_size:]

  # returns the samples in the training set
  def get_train_set(self):
    return self.train

  # returns the samples in the test set
  def get_test_set(self):
    return self.test

