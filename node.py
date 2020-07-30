# python node.py
import numpy as np

class Node:
    '''
    Node helper class to divide each node into two
    child nodes by separating the data by it's index
    '''
    def __init__(self, X, y, index):
        self.X = X 
        self.y = y
        self.index = index 
        self.samples = len(index)
        self.features = X.shape[1]
        self.value = np.mean(y[index])
        self.score = float('inf')
        self.find_split()
        
        
    def find_split(self):
        # find the best feature to split on
        for feature in range(self.features): 
            self.find_best_split(feature)

        # if terminal node, do not split
        if self.is_terminal: 
            return

        # use the feature to separate the 
        # data into two children nodes
        x = self.split_feature
        left = np.nonzero(x <= self.split)[0]
        right = np.nonzero(x > self.split)[0]
        self.left = Node(self.X, self.y, self.index[left])
        self.right = Node(self.X, self.y, self.index[right])


    def find_best_split(self, feature_index):
        # select feature column
        x = self.X.values[self.index, feature_index]

        # for each observation in row
        for sample in range(self.samples):
            # separate the data by each observation
            left = x <= x[sample]
            right = x > x[sample]
            # find the weighted averge score 
            score = self.get_score(left, right)
            # store lowest score in self.score
            if score < self.score:
                self.feature_index = feature_index
                self.score = score
                # store feature and observation
                # where score is minimized
                self.split = x[sample]
                

    def get_score(self, left, right):
        y = self.y[self.index]
        left_std = y[left].std()
        right_std = y[right].std()
        # weighted average of the standard deviations
        score = (left_std * left.sum()) + (right_std * right.sum())
        return score
                

    @property
    def split_feature(self): 
        # split at this row and column
        feature = self.X.values[self.index,self.feature_index]
        return feature
                
                
    @property
    def is_terminal(self): 
        # terminal node has no score
        # set to infinity
        return self.score == float('inf')                


    def predict(self, x):
        # retrun array of predicition for each X observation
        predict = np.array([self.predict_row(xi) for xi in x])
        return predict


    def predict_row(self, xi):
        # start with root node
        if self.is_terminal: 
            return self.value
        # decide if we need to travel left or right
        # continue until reach terminal node
        # return the value
        node = self.left if xi[self.feature_index] <= self.split else self.right
        return node.predict_row(xi)