import sys
import os

sys.path.append("../Active_Learning")

from Active_Learning import ActiveLearning


a = ActiveLearning("uncertainty_least_confident")
a.sample(X=None, y=None, n_sample=1)

