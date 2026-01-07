
import numpy as np
import os 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import hepmethds as hm
import copy

class Adaline:
    """Adaptive Linear Neuron Gradient Descent Classifier.

    Parameters
    ----------
    self.eta: float
    learning rate (between 0.0 and 1.0)

    self.n_iter: int
    number of passes over training data (epoches)

    self.random_state: int
    random number generator seed for random weight initialisation (reproducibilty)

    Attributes
    ----------
    self_weight_: 1-dimensional array
    weights after each epoch 

    self_bias: scalar 
    bias value after each epoch

    losses_: list
    mean square error loss function values per epoch 
    """

    # Constructor for initializing parameters
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
         self.eta = eta 
         self.n_iter = n_iter 
         self.random_state = random_state 

    def fit(self, X, y):
        """Fitting Adaline Model to Training Data.

        Parameters
        ----------
        X: {Array like}, shape=[no_examples, no_features],
        training array, where 
        no_examples is the number of training examples,
        no_features is the numbeer of features in the training example 

        y: array like, shape={no_examples},
        Target values

        Returns:
        self: object
        """

        # Initializes weight and bias unit
        regen = np.random.RandomState(self.random_state)
        self.weight_ = regen.normal(loc=0.0, scale=0.1, size=X.shape[1])
        self.bias_ = np.float64(0.0)
        self.losses_ = []

        # Passes over training data
        for _ in range(self.n_iter):
            correct_pred = 0
            no_examples = int(X.shape[0])

            net_input = self.net_input(X)
            output = self.activation(net_input)
            error = (y - output)
            self.weight_ += self.eta * 2 * np.dot(error, X) / (X.shape[0])
            self.bias_ += self.eta * 2 * np.mean(error) 
            losses = np.mean(error ** 2)
            self.losses_.append(losses) 
            correct_pred = correct_pred + (y == self.predict(X)).sum()

            print(f'Epoch: {_+1:03d}/{self.n_iter:03d}'
                  f'| Train Acc: {(correct_pred/no_examples) * 100:.2f}% '
                  f'| MSE: {losses:.4f}')
        return self

    # Net input of model
    def net_input(self, X):
        return np.dot(X, self.weight_) + self.bias_

    # Identity function 
    def activation(self, X):
        return X

    # Model prediction
    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.5, 1, 0)

# Loads dataset
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

    # Extracting class labels 
    y = df.iloc[:100, 4].values
    y = np.where(y == 'Iris-setosa', 0, 1)

    # Extracting sepal length and petal length
    X = df.iloc[:100, [0,2]].values
    return X, y


######################################################################################
###############                  USGAGE OF                      ######################
###############             ADALINE    CLASSIFIER               ######################
###############                GRADIENT DESCENT                 ######################
######################################################################################

# Loads training data
X, y = load_data()

# Model fitting and subplots for suboptimal learning rates
fig, ax = plt.subplots(nrows= 1, ncols= 2, figsize=(12, 4))
adap_model1 = Adaline(eta=0.1, n_iter=15).fit(X, y)
ax[0].plot(
    range(1, len(adap_model1.losses_) + 1), 
    np.log10(adap_model1.losses_), 
    marker="s", 
    c="red")
ax[0].set_title("Loss Curve Adaline Learning with rate of 0.1")
ax[0].set_xlabel("Number of Epochs")
ax[0].set_ylabel("Log(Mean Square Error)")

adap_model2 = Adaline(eta=0.0001, n_iter=15).fit(X, y)
ax[1].plot(
    range(1, len(adap_model2.losses_) + 1), 
    adap_model2.losses_, 
    marker="o", 
    c="blue")
ax[1].set_title("Loss Curve Adaline Learning with rate of 0.0001")
ax[1].set_xlabel("Number of Epochs")
ax[1].set_ylabel("Mean Square Error")
plt.show()

# Model fitting with feature standardization
X_std = copy.copy(X)
X_std[:,0] = (X[:, 0] - np.mean(X[:, 0])) / np.std(X[:, 0])
X_std[:,1] = (X[:, 1] - np.mean(X[:, 1])) / np.std(X[:, 1])

# Decision region and covergence plots
adap_model_std = Adaline(eta=0.5, n_iter=15).fit(X_std, y)
hm.HepMethds.plot_decision_region(X_std, y, adap_model_std)
plt.xlabel('Sepal length [standardized]')
plt.ylabel('Petal length [standardized]')
plt.title("Adaline Gradient Descent Decison Surface")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()

plt.plot(
    range(1, len(adap_model_std.losses_) + 1), 
    adap_model_std.losses_, 
    marker="s")
plt.title("Mean Square Error Against Epoches")
plt.xlabel("Number of Iterations")
plt.ylabel("Mean Square Error Losses")
plt.tight_layout()
plt.show()




