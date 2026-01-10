
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from hepmethds import HepMethds as hm
from sklearn.model_selection import train_test_split
from logistic_regression_sgd import LogisticRegressionSGD as lgsd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import copy


class LDA:
    ''' Linear Discriminant Analysis Function 

    Parameters
    ----------
    dim: scalar
    number of features in dataset
    '''

    # Constructor for initializing parameters
    def __init__(self, dim):
        self.dim = dim
        self.mvector = []

    # Standardizes datasets
    def standardize_input(self, X):
        for i in range(len(X[0])):
            if np.std(X[:, i]) != 0:
                X[:, i] = ((X[:, i] - np.std(X[:, i])) / np.mean(X[:, i]))
            else:
                X[:,i] = (X[:, i])
        return X

    # Generates mean vector on class label basis 
    def mvector_gen(self, X, y):
        for label in np.unique(y):
            self.mvector.append((np.mean(X[y == label, :], axis=0)))
        self.mvector = np.array(self.mvector, dtype=np.float64)
        return self.mvector

    # Generates within class scatter matrix
    def smatrixw(self, X, y):
        matrixw = np.zeros((self.dim, self.dim))
        for label in np.unique(y):
            matrixw += np.cov(np.transpose(X[y == label, :]))
        return matrixw

    # Generates between class scatter matrix
    def smatrixb(self, X, y):
        overall_mean = np.mean(X, axis=0)
        overall_mean = overall_mean.reshape((self.dim, 1))
        matrixb = np.zeros((self.dim, self.dim))
        for label, mrow in zip(np.unique(y), self.mvector):
             n = X[y == label,: ].shape
             mrow = mrow.reshape((self.dim, 1))
             rcomp = mrow - overall_mean
             matrixb += (n[0] * np.dot(rcomp, np.transpose(rcomp)))
        return matrixb

    # Computes eigen pair 
    def eig_decomp(self, smatrixw, smatrixb):
        matrix_det = np.linalg.det(smatrixw)
        if matrix_det == 0:
            matrixwb = np.dot(smatrixw, smatrixb)
        else:
            matrixwb = np.dot(np.linalg.inv(smatrixw), smatrixb)
        eigen_val, eigen_vec = np.linalg.eig(matrixwb)
        eigen_pair = [ [np.abs(eigen_val[i]), eigen_vec[:, i]] for i in range(len(eigen_val)) ]
        eigen_pair = sorted(eigen_pair, key=lambda i:i[0], reverse=True)
        return eigen_pair

    # Computes projection matrix
    def projmatrix_gen(self, eigen_pair, y):
        fsize = len(np.unique(y))
        fterm = []

        if len(np.unique(y)) == 2:
            w = np.hstack((eigen_pair[0][1][:, np.newaxis], eigen_pair[1][1][:, np.newaxis]))
        else:
            for i in range(fsize - 1):
                fterm.append(np.array(eigen_pair[i][1]))
            w = np.hstack([i[:, np.newaxis] for i in fterm])
        return w

    # Tranforms dataset with projection matrix
    def projmatrix_perf(self, X, w):
        return np.dot(X, w.astype(np.float64))

    # Generates linear discriminant ratio plot
    def exp_discriminant_plot(self, eigen_pair, title='Training dataset'):
        eigen_total = sum([eigen_pair[i][0] for i in range(len(eigen_pair))])
        exp_discriminant = [eigen_pair[i][0]/eigen_total for i in range(len(eigen_pair))]
        cumsum = np.cumsum(exp_discriminant).tolist()
        eigen_val = [i[0] for i in eigen_pair]

        pltx = [i for i in range(1, len(eigen_pair) + 1)]
        plt.bar(pltx, 
                exp_discriminant, 
                align='center', 
                label='Individual Discriminant', color='blue')

        plt.step(pltx, 
                 cumsum, 
                 where='mid', 
                 label='Cumulative Discriminant', color='red')
        plt.xlabel('Linear Discriminant')
        plt.ylabel('Linear Discriminant Ratio')
        plt.title(title)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show() 

    # Loads dataset
    def load_data(self):
        # Download or load dataset
        hm.download_file('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',
                     dir_file='wine_data.txt')
        X_data = pd.read_csv('wine_data.txt', encoding='utf-8')

        # Extracts training examples of first two class labels
        X_data = np.array(X_data, dtype='f').tolist()
        X_data_cp = []
        for i in range(len(X_data)):
            if X_data[i][0] != 3.0:
                X_data_cp.append(X_data[i])

        for i in range(len(X_data_cp)):
            if X_data_cp[i][0] == 1.0:
                X_data_cp[i][0] = 0
            elif X_data_cp[i][0] == 2.0:
                X_data_cp[i][0] = 1

        # Converts list into numpy array
        X_data = copy.copy(X_data_cp)
        X_data = np.array(X_data, dtype='f')
        X = X_data[:, 1:14]
        y = X_data[:, 0].astype(int)
        
        print('-'*50)
        print('Shape of X_data', X_data.shape)
        print('Class Labels', np.unique(y))
        print('Class Label Count', np.bincount(y))
        print('X shape', X.shape)

        # Performs training, test dataset splits
        X_train, y_train, X_test, y_test = train_test_split(X, 
                                                            y, 
                                                            test_size=0.3, 
                                                            random_state=1, 
                                                            stratify=y)
        print("")
        print('X_train', X_train.shape)
        print('y_train', y_train.shape)
        print('X_test', X_test.shape)
        print('y_test', y_test.shape)
        return X_train, y_train, X_test, y_test
   


######################################################################################
###############          USGAGE OF LDA FUNCTION                 ######################
###############      (LINEAR DISCRMINANT ANALYSIS)              ######################
###############       WITH LOGISTIC REGRESSION CLASSIFIER       ######################
######################################################################################

if __name__ == '__main__':
    print('-' * 50)
    # #-------------------------------------------------------------
    # # Transforms dataset with linear discriminant analysis function
    lda = LDA(dim=13)
    X_train, y_train, X_test, y_test = lda.load_data()

    # Standardizes X_train and y_train datasets
    X_train_std = lda.standardize_input(X_train)

    # Computes mean vectors for classes and features
    mvector = lda.mvector_gen(X_train_std, X_test)
    smatrixw = lda.smatrixw(X_train_std, X_test)
    smatrixb = lda.smatrixb(X_train_std, X_test)

    # Computes the eigen pair vectors, transformation matrix and transforms datasets
    eigen_pair = lda.eig_decomp(smatrixw, smatrixb)
    lda.exp_discriminant_plot(eigen_pair)
    w = lda.projmatrix_gen(eigen_pair, X_test)
    X_train_trans = lda.projmatrix_perf(X_train_std, w)

    # Generates scatter plot with extracted features
    hm.plot_scatter(X_train_trans, 
                    X_test, labelx='Linear Discriminant 1', 
                    labely='Linear Discriminant 2',
                    title='Linear Discriminant Analysis Plot'
                    )

    # Fits a logistic regression model
    lgd = lgsd(eta=0.5, n_iter=50)
    lgd = lgd.fit(X_train_trans, X_test)

    # Generates decision region plots
    print('Plotting decision regions.....')
    print(X_test.shape)
    hm.plot_decision_region(X_train_trans, X_test, classifier = lgd)
    plt.tight_layout()
    plt.legend(loc='upper left')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
    print('Decision Plot Complete!')

    # Generate loss curve
    print('.'*10)
    print('Plotting loss curve.....')
    plt.plot(range(0, len(lgd.losses_)), lgd.losses_)
    plt.title('Loss Curve Plot after Feature Extraction')
    plt.xlabel('Epochs')
    plt.ylabel('Mean Square Error')
    plt.tight_layout()
    plt.show()
    print('Loss Curve Plot Complete!')
    


