
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

class PCA:
    '''Principal Component Analysis Function
    '''
    # Standardizes datasets
    def std_input(self, X):
        for i in range(len(X[0])):
            if np.std(X[:, i]) != 0:
                X[:,i] = (X[:, i] - np.mean(X[:, i])) / np.std((X[:, i]))
            else:
                X[:,i] = X[:,i]
        return X 

    # Computes covariance matrix
    def covariance_matrix(self, x_std):
        return np.cov(x_std)
    
    # Computes eigen pair 
    def eig_decomp(self, x_covariant):
        eigen_val, eigen_vec = np.linalg.eig(x_covariant)
        eigen_pair = ((np.abs(eigen_val[i]), eigen_vec[:, i]) for i in range(len(eigen_val)))
        
        eigen_pair = sorted(eigen_pair, reverse=True, key=lambda i:i[0])
        return eigen_pair

    # Computes projection matrix
    def projmatrix_gen(self, eigen_pair):
        projmatrix_w = np.hstack((eigen_pair[0][1][:, np.newaxis],
                                 eigen_pair[1][1][:, np.newaxis]))
        return projmatrix_w

    # Tranforms dataset with projection matrix
    def projmatrix_perf(self, x_std, projmatrix_w):
        return np.dot(x_std, projmatrix_w)

    # Generates explained discriminant ratio plot
    def exp_var_plot(self, eigen_pair):
        eigen_total = sum([eigen_pair[i][0] for i in range(len(eigen_pair))])
        exp_var = [eigen_pair[i][0]/eigen_total for i in range(len(eigen_pair))]
        cumsum = np.cumsum(exp_var).tolist()
        eigen_val = [i[0] for i in eigen_pair]

        pltx = [i for i in range(1, len(eigen_pair) + 1)]
        
        plt.bar(pltx, 
                exp_var, 
                align='center', 
                label='Individual Variances', color='blue')

        plt.step(pltx, 
                 cumsum, 
                 where='mid', 
                 label='Cumulative Variances', color='red')
        plt.xlabel('Principal Components Index')
        plt.ylabel('Explained Variance Ratio')
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

    # Generates scatter plot for given dataset and test labels
    def plot_scatter(self, X, y, 
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


######################################################################################
###############          USGAGE OF PCA FUNCTION                 ######################
###############      (PRINCIPAL COMPONENT ANALYSIS)             ######################
###############       WITH LOGISTIC REGRESSION CLASSIFIER       ######################
######################################################################################


if __name__ == '__main__':
    #print('-'*50)
    pca = PCA()
    X_train, y_train, X_test, y_test = pca.load_data()
    

    # ------------------- SKLEARN ---------------------------------------
    # sc = StandardScaler()
    # X_train_std = sc.fit_transform(X_train)

    # pca = PCA(n_components=2)
    # X_train_pca = pca.fit_transform(X_train_std)

    # lsd = LogisticRegression(random_state=1, solver='lbfgs')
    # lsd = lsd.fit(X_train_pca, X_test)
    #---------------------------------------------------------------------

    #---------------------------------------------------------------------
    # Standardizes X_train and y_train datasets
    X_train_std = pca.std_input(X_train)
    y_train_std = pca.std_input(y_train)

    # Computes covariance matrix and eigen pairs
    X_cov = pca.covariance_matrix(np.transpose(X_train_std))
    eigen_pair = pca.eig_decomp(X_cov)

    # Plots variances across principal components
    pca.exp_var_plot(eigen_pair)

    # Computes the transformation matrix and transforms datasets
    W = pca.projmatrix_gen(eigen_pair)
    X_train_trans = pca.projmatrix_perf(X_train_std, W)
    X_train_trans = pca.projmatrix_perf(X_train_std, W)

    # Plots scatter plot for transformed dataset
    pca.plot_scatter(X_train_trans, 
                     X_test, labelx='Principal Component 1', 
                     labely='Principal Component 2')

    # Fit logistic model
    lsd = lgsd(eta=0.01, n_iter=100)
    lsd = lsd.fit(X_train_trans, X_test)

    # Plot decision regions
    hm.plot_decision_region(X_train_trans, X_test, classifier=lsd)
    plt.tight_layout()
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Decision surface after PCA feature extraction')
    plt.tight_layout()
    plt.legend(loc='upper left')
    plt.show()

    

 


    



