import numpy as np
import os 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from hepmethds import HepMethds as hm


class Perceptron:
    """Perceptron Classifier.

    Parameters
    ----------
    eta: int 
    learning rate (between 0.0 and 1.0)

    n_iter: int 
    number of passes over the training data (epoches)

    random_state: float
    random number generator seed 
    

    Attributes
    ----------
    weight: [array like]
    weights after fitting

    bias: scalar
    bias unit after fitting

    errors_: list
    number of mispredictions in each epoch
    """

    # Constructor for initializing parameters
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter 
        self.random_state = random_state


    def fit(self, X, y):
        """Model Training.

        Parameters
        ----
        X: [array like], shape=[no_examples, no_features],
        X is the training vector
        where no_examples is the number of examples in the training vector,
        no_features is the feature size

        y: [array like], shape=[no_examples]
        Target variable

        Returns
        self: object
        """
        
        # Initializes weight and bias unit
        rgen = np.random.RandomState(self.random_state)
        self.weight_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.bias_ = np.float64(0.0)
        self.errors_ = []

        # Passes over training data
        for _ in range(self.n_iter):
            errors = 0
            correct_pred = 0
            no_examples = 0
            for x, target in zip(X, y):
                output = self.predict(x)
                change = self.eta * (target - output)
                self.weight_ = self.weight_ + change * x
                self.bias_ = self.bias_ + change
                errors = errors + int(change != 0.0)
                correct_pred = correct_pred + (target == output)
                no_examples = no_examples + 1
            self.errors_.append(errors)

            print(f'Epoch: {_+1:03d}/{self.n_iter:03d}'
                  f'| Train Acc: {(correct_pred/no_examples) * 100:.2f}% '
                  f'| Error: {(errors/no_examples):.4f}')
        return self

    def net_input(self, X):
        """Calculates the net input"""
        return np.dot(X, self.weight_) + self.bias_

    def predict(self, X):
        """Predicts class label"""
        return np.where(self.net_input(X) < 0.0, 0 , 1)

# Decision region function 
def plot_decision_region(X, y, classifier, resolution=0.02):
    # Setup color and marker
    colors = ['red', 'blue', 'gray', 'cyan', 'green']
    marker = ['s', 'o', '>', '^', 'v']
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # Plot decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    pred = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    pred = pred.reshape(xx1.shape)
    plt.contourf(xx1, xx2, pred, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for indx, clx in enumerate(np.unique(y)):
        plt.scatter(x=X[y == clx, 0], 
                    y=X[y == clx, 1], 
                    edgecolor='black',
                    marker=marker[indx],
                    c=colors[indx],
                    label=f"Class {indx}",
                    alpha=0.8)


######################################################################################
###############                  USGAGE OF                      ######################
###############             PERCEPTRON CLASSIFIER               ######################
######################################################################################

# Loading iris dataset from archive
s = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
hm.download_file(s, dir_file='iris.txt')

df = pd.read_csv('iris.txt', header=None, encoding='utf-8')
#print(df.tail)

# Extracting class labels 
y = df.iloc[:100, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)

# Extracting sepal length and petal length
X = df.iloc[:100, [0,2]].values

# Generates feature scatter plot
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='s', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='o', label='Versicolor')
# Label axes and show plot
plt.xlabel("Sepal length [cm]")
plt.ylabel("Petal length [cm]")
plt.title('Iris Features: Sepal length and Sepal width')
plt.legend(loc="upper left")
plt.show()

# Initializing the Perceptron model and fitting the model
petron = Perceptron(eta=0.1, n_iter=50)
petron = petron.fit(X, y)

# Plot of epoches number and number of updates
plt.plot(range(1, len(petron.errors_) + 1), petron.errors_, marker='s')
plt.xlabel('Number of epoches')
plt.ylabel('Number of mispredictions')
plt.title('Error Curve Over Epochs')
plt.show()

# Generates decision surface
plot_decision_region(X, y, classifier=petron)
plt.xlabel("Sepal length [cm]")
plt.ylabel("Petal length [cm]")
plt.title('Decision Surface For Perceptron Model With Iris Features')
plt.legend(loc='upper left')
plt.show()
    

































