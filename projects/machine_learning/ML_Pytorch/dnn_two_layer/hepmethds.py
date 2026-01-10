import requests
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math


class HepMethds:
    """ Helper functions for ML models 
    """

    def download_file(url, dir_file='iris.txt'):
        """ Download file with a given url '
        """
        if not os.path.isfile(dir_file):
            file_url = url 
            dir_file = dir_file
            response = requests.get(url)
            if response.status_code == 200:
                with open(dir_file, "wb") as fb:
                    fb.write(response.content)
                print("File successfully downloaded!")
            else:
                print(f"Error download not complete error-{response.status_code}")
        else:
            print(f'File {dir_file} exits!')


    # Decision region function 
    def plot_decision_region(X, y, classifier, resolution=0.02):
        """Plot decision regions for ML model

        Parameters
        ----------
        X: {array-like}, shape=[no_examples, no_features]
        training matrix where 
        no_examples is the number of training examples,
        no_features is the features number per training example

        y: array-like, shape=[no_examples]
        Target values

        classifier: trained ML model
        """

        # Setup color and marker
        colors = ['red', 'blue', 'gray', 'cyan', 'green']
        marker = ['s', 'o', '>', '^', 'v']
        cmap = ListedColormap(colors[:len(np.unique(y))])

        # Plots decision surface
        x1_min = ((X[:, 0].min()) - 1)
        x1_max = ((X[:, 0].max()) + 1)
        x2_min = ((X[:, 1].min()) - 1)
        x2_max = ((X[:, 1].max()) + 1)

        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
        pred = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        pred = pred.reshape(xx1.shape)
        plt.contourf(xx1, xx2, pred, alpha=0.3, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())

        # Plots features with scatter graph
        for indx, clx in enumerate(np.unique(y)):
            plt.scatter(x=X[y == clx, 0], 
                        y=X[y == clx, 1], 
                        edgecolor='black',
                        marker=marker[indx],
                        c=colors[indx],
                        label=f"Class {indx}",
                        alpha=0.8)

    # Generates scatter plot for given dataset and labels
    def plot_scatter(X, 
                     y, 
                     labelx='Feature 1', 
                     labely='Feature 2', 
                     title='Feature Distribution of Class Labels 0 and 1'):

    # Scatter Plot of dataset with class labels 0 and 1
        markers = ['s', 'o', 'x']
        colors = ['red', 'blue', 'cyan']

        for indx, cl in enumerate(np.unique(y)):
            plt.scatter(x=X[y == cl, 0],
                        y=X[y == cl, 1],
                        c=colors[indx],
                        marker=markers[indx],
                        edgecolors='black',
                        label=f'Class {cl}')
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.title(title)
        plt.tight_layout()
        plt.legend(loc='best')
        plt.show()

    # Displays model title info 
    def func_title(msg):
        print('#'*len(msg)*2)
        print('-'*len(msg)*2)
        print(msg)
        print('#'*len(msg)*2)
        print('-'*len(msg)*2)
























































''' 
##### multi plots

        # print(np.array([xx1.ravel(), xx2.ravel()]).shape)

        #pred_vec = np.array([xx1.ravel(), xx2.ravel()])

        # print(pred_vec.shape)

        # if pred_vec.shape[0] == classifier.weight_.shape[0]:
        #     pred = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        # else:
        #     weight_dim = int((pred_vec.shape[0] * pred_vec.shape[1]) / classifier.weight_.shape[0])
        #     print(weight_dim)
        #     print(classifier.weight_.shape[0])
        #     pred_vec = pred_vec.reshape((weight_dim, classifier.weight_.shape[0]))
        #     pred = classifier.predict(pred_vec)


'''