import collections
import random
import codecs
from IPython.display import display
from IPython.display import HTML

class Sample:

  def __init__(self, label, microarray):
    self.label = label
    self.microarray = microarray

  def __str__(self):
    return str(self.label) + ': ' + self.attr

  def get_label(self):
    return self.label

  def get_microarray(self):
    return self.microarray

class Data:

  def __init__(self, matrix_path='data/Renal_cell_carcinoma_Matrix.txt', label_path='data/Renal_cell_carcinoma_label-11.txt'):
    data = []
    labels = [int(line.strip()) for line in open(label_path)]
    f = open(matrix_path)
    index = 0
    for line in f:
      micro = line.strip().split(' ')
      micro = map(int, micro)
      data.append(Sample(labels[index], micro))
      index += 1
    # shuffle the data
    random.shuffle(data)
    # split the data into a train and test set
    train_size = int(len(data) * 0.66)
    self.train = data[:train_size]
    self.test = data[train_size + 1:]

  def get_train(self):
    return self.train

  def get_test(self):
    return self.test


def analyze_results(labelled_data):
  correct = [1 if l == d.get_label() else 0 for d, l in labelled_data]
  total = len(correct)
  acc = (correct.count(1) * 100.0) / total
  print 'Accuracy: %.2f%%' % acc
