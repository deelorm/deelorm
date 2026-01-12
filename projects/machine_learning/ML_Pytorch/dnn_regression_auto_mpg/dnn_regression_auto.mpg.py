
# Modules 
from pydoc import describe
from matplotlib.figure import Figure
from scipy import optimize
from hepmethds import HepMethds as hm
import torch as th
import torchvision as thv 
from sklearn.datasets import load_iris
import numpy as np
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import torch.nn as nn
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd


# DNN Regression model  
class DNNRegresion(nn.Module):
    '''DNN Regression Classifier.

    Generates a DNN Regression model for the Auto-MPG dataset
    Feature set = {Cylinders, Displacement, Horsepower, Weight, Acceleration, Model year, Origin}
    Ground Truth Label = {MPG}

    Parameters
    ----------
    input_size: {array-like}, shape=[no_examples, no_features]
    train matrix where 
    no_examples is the number of training examples in train matrix.
    no_features is the number of features in train matrix

    hidden_unit: int
    number of hidden units for first linear layer

    output_size: int
    number of units in output layer (equivalent to class labels)

    Returns:
    self (model object)
    '''
    
    # Initializes model parameters
    def __init__(self, input_size, hidden_unit, output_size):
        super().__init__()
        self.l1 = nn.Linear(input_size, hidden_unit)
        self.l2 = nn.ReLU()
        self.l3 = nn.Linear(hidden_unit, 4)
        self.l4 = nn.ReLU()
        self.l5 = nn.Linear(4, output_size)
     
    # Conducts forward pass and returns model instance
    def forward(self, X):
        X = self.l1(X)
        X = self.l2(X)
        X = self.l3(X)
        X = self.l4(X)
        X = self.l5(X)
        return X


# Loads train, and test dataset
def load_data():
    dir_name = '.\\datasets\\auto_mpg.txt'
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
    column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 
                    'Weight', 'Acceleration', 'Model year', 'Origin']

    auto_mpg = hm.download_file(url, dir_name)

    df = pd.read_csv('.\\datasets\\auto_mpg.txt',
                     names=column_names, 
                     comment='\t', 
                     sep=' ',
                     skipinitialspace=True,
                     na_values='?'
                     )

    # Drops incomplete rows
    df = df.dropna()
    df = df.reset_index(drop=True)
    df_stats = df.describe().transpose()

    numeric_column_names = ['Cylinders', 
                            'Displacement', 
                            'Horsepower', 
                            'Weight', 
                            'Acceleration']


    # Splits data into test and train sets
    df_train, df_test = train_test_split(df, train_size=0.8, random_state=1)

    # Normalizes dataset
    for col in numeric_column_names:
        mean = df_stats['mean']
        std = df_stats['std']
        df_train[col] = (df_train[col] - mean.loc[col]) / std.loc[col]
        df_test[col] = (df_test[col] - mean.loc[col]) / std.loc[col]

    df_train_std = th.Tensor(np.array(df_train))[:, 1:7]
    df_test_std = th.Tensor(np.array(df_test))[:, 1:7]

    # Creates bucket indexes for model year feature
    modyear_bounds = th.Tensor([73, 76, 79])
    df_train_std[:, 5] = th.bucketize(df_train_std[:, 5], modyear_bounds, right=True)
    df_test_std[:, 5] = th.bucketize(df_test_std[:, 5], modyear_bounds, right=True)

    # Creates a joint dataset for numeric and categorical types
    df_train_origin = th.Tensor(np.array(df_train))[:,7]
    df_test_origin = th.Tensor(np.array(df_test))[:,7]
    X_train = th.cat([df_train_std, df_train_origin.unsqueeze(1)], 1)
    X_test = th.cat([df_test_std, df_test_origin.unsqueeze(1)], 1)

    # Generates class label 
    y_train = th.Tensor(np.array(df_train['MPG']))
    y_test = th.Tensor(np.array(df_test['MPG']))

    print('X_train Shape: ', X_train.shape)
    print('X_test Shape: ', X_test.shape)
    print('y_train Shape: ', y_train.shape)
    print('y_test Shape: ', y_test.shape)

    # Creates dataset and dataloader
    X_train_dataset = TensorDataset(X_train, y_train)
    th.manual_seed(50)
    X_train_dl = DataLoader(X_train_dataset, batch_size=8, shuffle=True)
    print('-'*50)

    return X_train_dl, X_test, y_test        


# Fits training example
def train(model, X_dl, epochs, lr):
    th.manual_seed(50)
    loss_fn = nn.MSELoss()
    optimizer = th.optim.SGD(params=model.parameters(), lr=lr)
    loss_hist_train = [0]*epochs
    print('Fitting model...')
    for epoch in range(epochs):
        for X_batch, y_batch in X_dl:
            pred = model(X_batch)[:, 0]
            loss = loss_fn(pred, y_batch)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            loss_hist_train[epoch] = (loss_hist_train[epoch] +  loss.item())
        loss_hist_train[epoch] = loss_hist_train[epoch] / (len(X_dl))
        print(f'epoch: {epoch+1:03d}/{epochs:03d} '
              f' | loss: {loss_hist_train[epoch]:.4f}')
    print('Model fitting completed...')
    return loss_hist_train
            

if __name__ == '__main__':
    
    print(DNNRegresion.__doc__)

    msg = '''
             DNN REGRSSION ON AUTO MPG DATASET
    '''
    hm.func_title(msg)

    
    # Loads, initializes model and fits model
    X_train_dl, X_test, y_test = load_data()
    input_size = X_test.shape[1]
    output_size = 1
    hidden_unit = 8
    model = DNNRegresion(input_size, hidden_unit, output_size)
    loss_hist_train = train(model=model, X_dl=X_train_dl, epochs=100, lr=0.0001)

    # Plots MSE Error Curve
    fig = plt.figure(figsize=(12,4))
    plt.plot(loss_hist_train)
    plt.xlabel('Epochs')
    plt.title('Multivariate MSE Error Curve for DNN Regression Model')
    plt.ylabel('Loss')
    plt.tight_layout()
    plt.show()

    # Computes Test Error
    loss_fn = nn.MSELoss()
    y_pred = model(X_test)
    loss = loss_fn(y_pred.squeeze(1), y_test)
    print(f'MSE Test Loss: {loss.item():.4f}')
    print(f'MAE Test Loss: {nn.L1Loss()(y_pred.squeeze(1), y_test):.4f}')

    # Saves model
    model_dir = ".\\dnn_regression_classifier.pt"
    th.save(model, model_dir)
    print('Model saved!')

    print('DNN Regression Run Completed!')






