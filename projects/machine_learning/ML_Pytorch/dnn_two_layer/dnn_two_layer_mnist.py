from matplotlib.figure import Figure
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


def load_data():
    mnist_folder = ".\\"
    mnist = thv.datasets.MNIST(mnist_folder, download=True)
    
    print('MNIST dataset: ', next(iter(mnist)))
    X, y = mnist.data, mnist.targets
    print('X Shape: ', X.shape)
    print('y Shape: ', y.shape)
    print('Class labels: ', np.unique(y))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=1, shuffle=True, stratify=y)

    print('X_train Shape: ', X_train.shape)
    print('X_test Shape: ', X_test.shape)
    print('y_train Shape: ', y_train.shape)
    print('y_test Shape: ', y_test.shape)

    X_train_norm = (X_train - th.mean(X_train.float())) / (th.std(X_train.float()))
    X_test_norm = (X_test - th.mean(X_test.float())) / (th.std(X_test.float()))

    fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True)
    ax = ax.flatten()
    for i in range(10):
        ax[i].imshow(X_train[i], cmap='Greys')
        ax[i].set_xticks([])
        ax[i].set_yticks([])
        ax[i].set_title(f'{y_train[i]}')
    plt.tight_layout()
    fig.suptitle('First 10 training samples')
    plt.show()
    print('-'*50)

     # Creates a dataset and dataloader
    X_train_ds = TensorDataset(X_train_norm, y_train)
    th.manual_seed(50)

    X_train_dl = DataLoader(X_train_ds, batch_size=2, shuffle=True)
    return X_train_dl, X_test_norm, y_test

class Model(nn.Module):

    # Initializes model units
    def __init__(self, input_size=0, hidden_units=16, output_size=0):
        super().__init__()
        self.l0 = nn.Flatten()
        self.l1 = nn.Linear(input_size, hidden_units)
        self.l2 = nn.Sigmoid()
        self.l3 = nn.Linear(hidden_units, output_size)
        self.l4 = nn.Softmax(dim=1)

    # Computes net input for given sample
    def forward(self, X):
        X = self.l0(X)
        X = self.l1(X)
        X = self.l2(X)
        X = self.l3(X)
        X = self.l4(X)
        return X


# Trains a given model for number of epochs
def train(model, X_dl, epochs=0, lr=0.001):
    th.manual_seed = 50 
    acc_hist = [0] * epochs 
    loss_hist = [0] * epochs

    loss_fn = nn.CrossEntropyLoss()
    optimizer = th.optim.Adam(model.parameters(), lr=lr)
    acc = []

    for epoch in range(epochs):
        batch_num = 0
        for X_batch, y_batch in X_dl:
            batch_num += 1
            X_preds = model(X_batch)
            loss = loss_fn(X_preds, y_batch)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            loss_hist[epoch] += (loss.item() * y_batch.size()[0])
            correct = (th.argmax(X_preds, dim=1) == y_batch)
            acc_hist[epoch] += (correct.float().sum())
            print(f'Epoch: {epoch+1:03d}/{epochs:03d}'
                  f' | Batch: {batch_num:03d} '
                  f' | Batch Loss: {(loss_hist[epoch] / len(X_dl.dataset)):.4f}'
                  f' | Batch Acc: {(acc_hist[epoch] / len(X_dl.dataset))*100:.4f}'
                  )
        
        acc.append(correct.sum())
        loss_hist[epoch] = loss_hist[epoch] / len(X_dl.dataset)
        acc_hist[epoch] = acc_hist[epoch] / len(X_dl.dataset)
        print(f'Epoch: {epoch+1:03d}/{epochs:03d} '
              f' || Epoch Loss: {loss_hist[epoch]:.4f} '
              f' || Epoch Acc: {acc_hist[epoch]*100:.4f}')
    return loss_hist, acc_hist




if __name__ == '__main__':

    msg = '''
             TWO-LAYER DNN MODEL ON MNIST DATASET 
             WITH 10 HANDWRITTEN DIGITS 0-9 (LABELS)
    '''
    hm.func_title(msg)

    # Loads dataset as a dataloader
    X_train_dl, X_test_norm, y_test = load_data()

    # Initialize model unit parameters
    input_size = X_test_norm.shape[1] * X_test_norm.shape[2]
    hidden_units = 16 
    output_size = len(np.unique(y_test.numpy()))
    model = Model(input_size, hidden_units, output_size)
    print(model)
    print('-'*50)

    epochs = 10
    loss_hist, acc_hist = train(model, X_train_dl, epochs=epochs, lr=0.001)

    # Evaluates model on test dataset
    y_preds = model.forward(X_test_norm)
    correct = (th.argmax(y_preds, dim=1) == y_test).sum()
    test_acc = correct / X_test_norm.shape[0]
    print(f'Test Acc: {test_acc*100:.4f}')
    print('-'*50)

    # Plots loss curve for training dataset
    fig = plt.figure(figsize=(12,5))
    ax = fig.add_subplot(1,2,1)
    ax.plot(range(epochs), loss_hist, lw=3)
    ax.set_xlabel('Epochs', size=15)
    ax.set_ylabel('', size=15)
    ax.set_title('Loss Curve Training dataset', size=15)

    # Plots accuracy curve for training dataset
    ax = fig.add_subplot(1,2,2)
    ax.plot(range(epochs), acc_hist, lw=3)
    ax.set_xlabel('Epochs', size=15)
    ax.set_ylabel('Accuracy', size=15)
    ax.set_title('Accuracy Curve Training dataset', size=15)
    plt.tight_layout()
    plt.show()

    # Saves model
    model_path = '.\\models\\dnn_two_layer_mnist.pth'
    th.save(model, model_path)
    print(f'Model Saved to models\dnn_two_layer_mnist.pth!')

