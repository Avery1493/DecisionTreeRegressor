# python DTRegressor.py
from node import Node
import pandas as pd
import numpy as np

class DTRegressor():
    '''
    X: array like shape (n_samples, n_features)
    y: array like shape (n_samples) -- true values for X
    '''
    def fit(self, X, y):
        # fit tree based on X features and y target
        # using helper class Node
        # and an index represented by len of y
        self.tree = Node(X, y, np.array(range(len(y))))
        return self
    
    def predict(self, X):
        return self.tree.predict(X.values)



if __name__ == "__main__":
    data = {"dosage": [10,20,35,5,15], "age": [32,56,44,62,25], "drug_effective": [98,0,6,44,88]}
    df = pd.DataFrame(data=data)
    target = df["drug_effective"]
    features = df.drop(columns='drug_effective')
    tree = DTRegressor()
    tree.fit(features,target)
    preds = tree.predict(features)
    print(preds)
