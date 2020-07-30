# DecisionTreeRegressor
Decision Tree Regressor

Setting up Enviornment  
```pipenv numpy pandas scipy sklearn ipykernel matplotlib```  
```python -m ipykernel install --user --name env-name --display-name "display-name(Python3)"```  

# UPER  
**UNDERSTAND**  
A decision tree is a predictive modeling approach that separates data into classes using a top down appraoch, with broader classes at the top and more specific classes as you travel down the tree.  
There are two types of problems you can use a decision tree to solve: *classification* and *regression* problems. Classification trees predict a discrete or categorical class label, such as ```dog``` or ```cat```. Regression trees predict a continuious quanitiy or numeric output, such as ```$35.98``` or ```11.41 inces```. This distinction is also important to note that the metrics used to contruct (choosing how the variavles at each step split) classification and regression trees are different.  
Examples used for classification trees include Gini impurity, Information gain (Entropy), and Chi-square. The [sklearn.tree.DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) uses  gini or entropy as the criteria to measure the quality of a split. For regression trees, Variance reduction is used as the metric. The [sklearn.tree.DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor) use mean squared error (MSE), friedman mse, and mean absoulte error.  
For this project I will focus on implementing my own python class for a regression decision tree.

**PLAN**  
Because of the overall structure of a decision tree, I plan to create a Node class. If a node is able to split, it will always create two children. Therefore, I will need a method to find the best splitting point as we go down the tree. This method will need to loop through all the features, calculate the ```mse```, and return the feature with the smallest mse. In addition to the Node class, I will create the DTRegression class. I will need a ```fit``` statement and a ```predict``` method that accepts an observation and returns a prediction.

**EXECUTE**  
The ```DTRegressor``` class relies the numpy library and the Node class to fit data and make a prediction on new data. It takes in two parameters, X and y. X represents an array of features where each row is an observation or sample and each column is a differnt feature. The y array are the true values observed for each observation. For example if we were trying to predict hosing prices, number of room and square feet would be features and the target or y would be the actual price of the home.  This input might look like X = [[3, 1500]], y =[100000], where the home has 3 bedrooms, 1500 square feet and is valued at $100,000. The
index of X corresponds with the same index of y.  
 The ```Node``` class is a helper class that executes splitting the decision tree. For regression trees, some measure of variance is used as a metric to determine how the tree 
 will branch off. In this case I used standard deviation. The ```find_split``` method finds
 the best split in each columns (or for each feature). And the ```find_best_split``` finds 
 at which row for each feature does the best split occur. The best fit will have the smallest variance. Therefore, the split that minimizes the standard deviation of the node is picked. If the lowest std is still higher than the previous node, the node does not split. This means we are at the terminal node of the tree. If we want to make a prediction, the ```predict``` method starts at the root node and work is way down to the terminal node and return the predicted y value.

 **REFLECT**  
 The result of my decision tree seems to work, and all cases are accounted for (can input multiple features). However, the tree could perform better. Without the time contraint of four days, I would have loved to spend more time in the Plan step. Mainly, beacuse many difffernt sources for regression trees use differnt metrics for their criteria for splitting the tree. Sklearn used mean squared error, while other common metrics I came across were standard deviation, reduction in variance, root mean square error, and sum of the squared residuals. I first desired to follow along with the sklearn model to see how accurate my tree was, but I could not figure out how they were calculating the mse for each split. Therfore, I went with another option of splitting my tree based on standard deviation.

 Helpful Links  
 https://www.youtube.com/watch?v=g9c66TUylZ4  
 https://www.youtube.com/watch?v=7VeUPuFGJHk
