import matplotlib.pyplot as plt
import numpy as np

def plot_errors(classified_samples):
  labels = []
  for cs in classified_samples:
    if not cs[0].get_label() in labels:
      labels.append(cs[0].get_label())
  labels.sort()
  # our categories will be the kinds of labels
  # dict classified_label -> list indexed by true label
  num_by_cat = { label : [0] * len(labels) for label in labels}
  label2index = {label : labels.index(label) for label in labels}
  for sample_tuple in classified_samples:
    sample_label = sample_tuple[1]
    true_label = sample_tuple[0].get_label()
    num_by_cat[sample_label][label2index[true_label]] += 1

  ind = np.arange(len(num_by_cat))
  width = 0.35
  handles = []
  label_text = []
  colors = ['r', 'b', 'g', 'y']
  i = 0
  fig = plt.figure(figsize=(10, 8), dpi=100)
  for classified_label in num_by_cat:
    counts = num_by_cat[classified_label]
    label_str = 'Classified as %i' % classified_label
    p1 = plt.bar(ind, counts, width, color=colors[i], label=label_str)
    i += 1
    handles = p1
    label_text.append(label_str)

  plt.ylabel('Count')
  plt.xlabel('True Label')
  plt.title('Labels by true label and classified label')
  
  plt.xticks(ind+width/2., labels)
  plt.legend(handles, labels=label_text, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

  plt.show()
    
