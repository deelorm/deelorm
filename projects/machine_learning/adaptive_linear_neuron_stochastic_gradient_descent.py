
import numpy as np
import os 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import hepmethds as hm
import copy

class AdalineSGD:
    """Adaline Stochastic Gradient Descent Classifier.

    Parameters
    ----------
    eta: float
    Learning rate for epoch (normally between 0.0 and 1.0)

    n_iter: int 
    Number of passes over training data (epoch)

    random_state: int 
    Random number generator seed for random weight and shuffle number initialization

    is_shuffle: bool (default: True)
    Flag for whether training example should be shuffled

    Attributes
    ----------
    weight_: 1d-array
    weight unit for each update

    bias_: scalar
    bias unit for each update

    losses_: list
    average mean square error loss function values over all training examples for each epoch
    """
    
    # Constructor for initializing parameters
    def __init__(self, eta=0.1, n_iter=50, random_state=1, is_shuffle=True):
        self.eta = eta 
        self.n_iter = n_iter 
        self.random_state = random_state 
        self.is_shuffle = is_shuffle
        self.w_initialize = False
        self.examples_count = 0
        self.correct_pred = 0

    def fit(self, X, y):
        """Fittng training data to model using Stochastic Gradient Descent

        Parameters
        ----------
        X: {array-like}, shape=[no_examples, no_features]
        training vector, where 
        no_examples is the training examples number, 
        no_features is the features in the training example number

        y: array-like. shape=[no_examples]
        Training vector

        Returns:
        self: object
        """

        # Initializes weight and bias unit
        self._initialize_weights(X.shape[1])
        self.losses_ = []
        avg_error = 0

        # Passes over training data
        for _ in range(self.n_iter):
            if self.is_shuffle:
                X, y = self._shuffle(X, y)
            losses = []
            for x, target in zip(X, y):
                losses.append(self._update_weights(x, target))
            avg_error = np.mean(losses)
            self.losses_.append(avg_error)

            print(f'Epoch: {_+1:03d}/{self.n_iter:03d}'
                  f'| Train Acc: {(self.correct_pred/self.examples_count) * 100:.2f}% '
                  f'| MSE: {avg_error:.4f}')
        return self

    # Fit training model without reinitialization of weights
    def _partial_fit(self, X, y):
        self.losses_ = []
        losses = []
        if not self.w_initialize:
            self._initialize_weights(X, y)
        if X.ravel().shape[0] > 1:
            for x, target in zip(X, y):
                losses.append(self._update_weights(x, target))
            self.losses_.append(np.mean(losses))
        else:
            self._update_weights(x, target)
        return self

    # Shuffles datasets and labels
    def _shuffle(self, X, y):
        regen_shuffle = np.random.RandomState(self.random_state)
        regen_permutation = regen_shuffle.permutation(y.shape[0])
        return X[regen_permutation], y[regen_permutation]

    # Initializes weight and bias unit
    def _initialize_weights(self, wsize):
        regen = np.random.RandomState(self.random_state)
        self.weight_ = regen.normal(loc=0.0, scale=0.1, size=wsize)
        self.bias_ = np.float64(0.0)
        self.w_initialize = True

    # Updates weight and bias unit
    def _update_weights(self, x, target):
        output = self.activation(self.net_input(x))
        error = target - output
        self.weight_ += self.eta * 2 * np.dot(error, x)
        self.bias_ += self.eta * 2 * error
        loss = (error ** 2)
        self.examples_count = self.examples_count + 1
        pred = self.predict(x)
        self.correct_pred = self.correct_pred + (target == pred)
        return loss

    def net_input(self, X):
        """ Calculates Net Input for Given Training Data, Bias and Weight """
        return np.dot(X, self.weight_) + self.bias_

    def activation(self, X):
        """ Identity Function of Net Input """
        return X

    def predict(self, X):
        """ Predict Class Label for Training Example """
        return np.where(self.activation(self.net_input(X)) >= 0.5, 1, 0)

def load_data():
    # Checks if file exists
    file = f"{os.getcwd()}\iris.txt"
    if not os.path.isfile(file):
        #Loading iris dataset from archive
        iris_archive = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        hm.HepMethds.download_file(iris_archive)
    else:
        print("Iris dataset exists.")

    iris_path = "C:\\Users\\denni\\Downloads\\dev\\domain\\Python\\ML_Pytorch_Scikit_Learn\\ML_Pytorch\\ML_Pytorch\\iris.txt"
    
    # Reads csv file
    df = pd.read_csv(iris_path, header=None, encoding='utf-8')
    #print(df.tail)

    #Extracting class labels 
    y = df.iloc[:100, 4].values
    y = np.where(y == 'Iris-setosa', 0, 1)

    # Extracting sepal length and petal length
    X = df.iloc[:100, [0,2]].values
    return X, y


######################################################################################
###############                  USGAGE OF                      ######################
###############             ADALINE    CLASSIFIER               ######################
###############            STOCHASTIC  GRADIENT DESCENT         ######################
######################################################################################

# Loads training data
X, y = load_data()

# Model fitting with feature standardization
X_std = copy.copy(X)
X_std[:,0] = (X[:, 0] - np.mean(X[:, 0])) / np.std(X[:, 0])
X_std[:,1] = (X[:, 1] - np.mean(X[:, 1])) / np.std(X[:, 1])

# Decision region and covergence plots
adap_model_sgd= AdalineSGD(eta=0.01, n_iter=15).fit(X_std, y)
hm.HepMethds.plot_decision_region(X_std, y, adap_model_sgd)
plt.xlabel('Sepal length [standardized]')
plt.ylabel('Petal length [standardized]')
plt.title("Adaline Stochastic Gradient Descent with Iris Dataset")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()

plt.plot(range(1, len(adap_model_sgd.losses_) + 1), adap_model_sgd.losses_, marker="s")
plt.title("Mean Square Error  Against Epoches")
plt.xlabel("Number of Iterations")
plt.ylabel("Mean Square Error Losses")
plt.title("Loss Curve Adaline Stochastic Gradient Descent with Iris Dataset")
plt.tight_layout()
plt.show()