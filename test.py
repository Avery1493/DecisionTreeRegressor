from node import Node 
from DTRegressor import DTRegressor

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.tree import DecisionTreeRegressor, plot_tree


# The Boston Housing Dataset
# load data
X, y = load_boston(return_X_y=True)
columns = ["crime","zone","industry","river","nox_con","rooms","age",
           "distance","highways", "tax", "school","B","lstat"]
house = pd.DataFrame(data=X, columns=columns)
# set features and target
target = y
features = house[["rooms", "age"]]
# Fft Tree
tree = DecisionTreeRegressor()
tree.fit(features,target)



print(tree.predict([[6,65], [2,10]]))
