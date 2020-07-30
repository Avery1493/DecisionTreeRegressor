# DecisionTreeRegressor
Decision Tree Regressor

Setting up Enviornment  
```pipenv numpy pandas scipy sklearn ipykernel matplotlib```  
```python -m ipykernel install --user --name env-name --display-name "display-name(Python3)"```  

# UPER  
**UNDERSTAND**  
A decsion tree is a predictive modeling approach that separates data into classes using a top down appraoch, with broader classes at the top and more specific classes as you travel down the tree.  
There are two types of problems you can use a decsion tree to solve: *classification* and *regression* problems. Classifiaction trees predict a discrete or categorical class label, such as ```dog``` or ```cat```. Regression trees predict a continuious quanitiy or numeric output, such as ```$35.98``` or ```11.41 inces```. This distinction is also important to note that the metrics used to contruct (choosing how the variavles at each step split) classification and regression trees are different.  
Examples used for classification trees include Gini impurity, Information gain (Entropy), and Chi-square. The [sklearn.tree.DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) uses  gini or entropy as the criteria to measure the quality of a split. For regression trees, Variance reduction is used as the metric. The [sklearn.tree.DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor) use mean squared error (MSE), friedman mse, and mean absoulte error.  
For this project I will focus on implementing my own python class for a regression decision tree. I will use MSE as my splitting metric and will create a ```fit``` and ```predict``` method.

**PLAN**  
Because of the overall structure of a decsion tree, I plan to create a Node class. If a node is able to split, it will always create two children. Therefore, I will need a method to find the best splitting point as we go down the tree. THis method will need to loop through all the features, calculate the ```mse```, and return the feature with the smallest mse. In addition to the Node class, I will create the DTRegression class. I will need a ```fit``` statement and a ```predict``` method that accepts an observation and returns a prediction.

**EXECUTE**
