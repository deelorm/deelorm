
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from hepmethds import HepMethds as hm


class LogisticRegressionSGD:
    ''' Stochastic Gradient Descent based Logistic Regression Classifier 
    Parameters
    ----------
    eta: float
    learning rate between 0.0 and 1.0

    n_iter: int 
    number of passes over training examples

    random_state: int 
    random number generator seed for weight initialization

    shuffle: int
    conditional flag for shuffling training dataset

    Attributes
    ----------
    weight_: 1d-array
    weight after fitting

    bias_: scalar 
    bias unit after fitting
    
    losses_: list 
    mean square error function loss values

    '''

    def __init__(self, eta=0.01, n_iter=50, random_state=1, shuffle=True):
        self.eta = eta 
        self.n_iter = n_iter 
        self.random_state = random_state 
        self.shuffle = shuffle 
        self.w_initialized = False
        self.examples_count = 0
        self.correct_pred = 0

    def fit(self, X, y):
        ''' Fits the model

        Parameters
        ---------
        X: {array-like}, shape=[no_examples, no_features],
        training matrix where 
        no_examples is the number of examples in training dataset,
        no_features is the number of features in training dataset

        y: array-like, shape=[no_examples]
        target values where 
        no_examples is the number of examples in training dataset

        Returns: object of the LogisticRegressionSGD classifier
        '''

        # Initialize weights and loss 
        self._initialize_weights_(X.shape[1])
        self.losses_ = []

        # Iterate through training dataset
        for i in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle_(X, y)
            losses = []
            errors = []
            avg_loss = 0
            for x, target in zip(X, y):
                ls, err = self._update_weights_(x, target)
                losses.append(ls)
                errors.append(err)
            avg_loss = np.mean(losses)
            avg_error = np.mean(errors)
            self.losses_.append(avg_loss)

            train_acc = ((self.correct_pred/self.examples_count) * 100)
            print(f'Epoch: {i+1:03d}/{self.n_iter:03d}'
                  f'| Train Acc: {train_acc:.2f}% '
                  f'| Error: {avg_error:.4f}')
        return self

    def partial_fit(self, X, y):
         ''' Updates weight and bias parameters without re-initialization '''
         if not self.w_initialized:
             self._initialize_weights_(X.shape[1])
         if X.ravel().shape[0] > 0:
            for x, targets in zip(X, y):
                self._update_weights_(x, targets)
         else:
            self._update_weights_(X, y)

    def _shuffle_(self, X, y):
        ''' Shuffles training dataset and class labels '''
        p_no = np.random.permutation(len(y))
        return X[p_no], y[p_no]

    def _initialize_weights_(self, s):
        ''' Initializes weights and bias model parameters '''
        rgen = np.random.RandomState(s)
        self.weight_ = rgen.normal(loc=0.0, scale=0.1, size=s)
        self.bias_ = np.float64(0.0)
        self.w_initialized = True

    def _update_weights_(self, x, targets):
        ''' Updates weights and bias model parameter '''
        output = self.net_input(x)
        activation = self.activation(output)
        error = targets - activation
        self.weight_ = self.weight_ + (self.eta * 2 * x * error)
        self.bias_ = self.bias_ + (self.eta * 2 * error)
        loss = (-targets * np.log(activation)) - ((1 - targets) * np.log(1 - activation))

        self.examples_count = self.examples_count + 1
        pred = self.predict(x)
        self.correct_pred = self.correct_pred + (targets == pred)
        return loss, error ** 2

    def net_input(self, X):
        ''' Computes the net input of training  dataset'''
        return np.dot(X, self.weight_) + self.bias_

    def activation(self, z):
        ''' Computes the logistic sigmoid function values  '''
        z = z.astype(float)
        return 1. / (1. + np.exp(np.clip(-z, -255, 255)))

    def predict(self, X):
        ''' Computes the class membership probabilities '''
        return np.where(self.activation(self.net_input(X)) >= 0.5, 1, 0)


# Generates training dataset and class labels
def subset_gen():
    iris = pd.read_csv('iris.txt',
                   header=None,
                   encoding='utf-8')

    iris = iris.values
    X = []
    y = []
    for i in range(len(iris)):
        if (iris[i, 4] == 'Iris-setosa') or (iris[i, 4] == 'Iris-versicolor'):
            X.append(iris[i, 2:4])
            if iris[i, 4] == 'Iris-setosa':
                y.append(0)
            else:
                y.append(1)
    X = np.array(X)
    y = np.array(y)
    return X, y
        

######################################################################################
###############                  USGAGE OF                      ######################
##############         LOGISTIC REGRESSION  CLASSIFIER          ######################
###############            STOCHASTIC  GRADIENT DESCENT         ######################
######################################################################################


if __name__ == '__main__':
    # Generate training examples and class labels
    X, y = subset_gen()

    # Print training examples and class labels 
    print('Shape of Training Dataset', X.shape)
    print('Shape of Train Labels', y.shape)

    # Features Scatter plot 
    hm.plot_scatter(X, y, title='Features Scatter Plot Before Fitting')

    lgsgd = LogisticRegressionSGD(n_iter=50)

    # Print parameter and attribute list for classifier
    #print(lgsgd.__doc__)

    # Fit the model
    lgsgd = lgsgd.fit(X, y)

    # Plot decision regions
    print('Plotting decision regions.....')
    hm.plot_decision_region(X, y, classifier=lgsgd)
    plt.title('LogisticRegressionSGD Decsion Region Plot with Iris Dataset')
    plt.xlabel('Petal length {cm}')
    plt.ylabel('Petal width {cm}')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
    print('Decision Plot Complete!')

    # Plot loss curve
    print('.'*10)
    print('Plotting loss curve.....')
    plt.plot(range(0, len(lgsgd.losses_)), lgsgd.losses_)
    plt.title('LogisticRegressionSGD Loss Curve with Iris Dataset')
    plt.xlabel('Epochs')
    plt.ylabel('Mean Square Error')
    plt.tight_layout()
    plt.show()
    print('Loss Curve Plot Complete!')


