
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import copy
from linear_discriminant_analysis import LDA
from hepmethds import HepMethds as hm

class NeuralNetMLP:
    # Initializes neural net model
    def __init__(self, num_features, num_hidden, num_classes, random_seed=50):
        super().__init__()
        self.num_classes = num_classes

        # Hidden layer
        rgen = np.random.RandomState(random_seed)
        self.weight_h = rgen.normal(loc=0.0, scale=0.1, size=(num_hidden, num_features))
        self.bias_h = np.zeros(num_hidden)

        # Output layer
        self.weight_out = rgen.normal(loc=0.0, scale=0.1, size=(num_classes, num_hidden))
        self.bias_out = np.zeros(num_classes)

    # Conducts a forwards pass of neural network
    def forward(self, X):
        z_h = np.dot(X, np.transpose(self.weight_h)) + self.bias_h
        a_h = sigmoid(z_h)

        z_out = np.dot(a_h, np.transpose(self.weight_out)) + self.bias_out
        a_out = sigmoid(z_out)
        return a_h, a_out

    # Conducts a backward pass of neural network
    def backward(self, X, a_h, a_out, y):
        # dLoss/outWeight = dloss/OutAct * dOutAct/dOutNet * dOutNet/dOutWeight
        # dLoss/hiddenWeight = dloss/hiddenAct * dhiddenAct/dhiddenNet * dhiddenNet/dOutWeight
        #####################################
        ####### Output Layer Weights ########
        #####################################

        # Output layer loss gradient for weight and bias unit
        onehot_y = int_to_onehot(y, a_out.shape[1])
        d_loss__d_a_out = (2 * (onehot_y - a_out) ) / X.shape[0]
        d_a_out__d_z_out = a_out * (1 - a_out)
        delta = d_loss__d_a_out * d_a_out__d_z_out
        d_z_out__d_w_out = a_h

        # Hidden layer loss gradient for weight and bias unit
        d_loss__d_w_out = np.dot(np.transpose(delta), d_z_out__d_w_out)
        d_loss__d_b_out = np.sum(delta, axis=0)
        d_z_out__d_a_h = self.weight_out
        d_loss__d_a_h = np.dot(delta, d_z_out__d_a_h)
        d_a_h__d_z_h = a_h * (1 - a_h)
        d_z_h__d_w_h = X
        d_loss__d_w_h = np.dot(np.transpose(d_loss__d_a_h + d_a_h__d_z_h), d_z_h__d_w_h)
        d_loss__d_b_h = np.sum(d_loss__d_a_h + d_a_h__d_z_h, axis=0)

        return d_loss__d_w_h, d_loss__d_b_h, d_loss__d_w_out, d_loss__d_b_out


# Logistic sigmoidal activation function
def sigmoid(z):
    return 1/(1 + np.exp(np.clip(-z, -255, 255)))

# Convert class labels into one hot encoding representation
def int_to_onehot(y, num_labels):
    arr = np.zeros(shape=(y.shape[0], num_labels))
    for indx, num in enumerate(y):
        arr[indx, num] = 1
    return arr

# Generates batches of training dataset
def mbatch_generator(X, y, minbatch_size):
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    for start_indx in range(0, indices.shape[0] - minbatch_size + 1, minbatch_size):
        #batch_indx = indices[start_indx: start_indx + minbatch_size] 
        batch_indx = start_indx + minbatch_size
        yield X[start_indx:batch_indx], y[start_indx:batch_indx]


# Computes model accuracy and error 
def compute_mse_and_acc(nnet, X, y, num_labels, minbatch_size):
    mse = 0
    acc = 0
    error = 0
    num_examples = 0
    correct_predictions = 0
    mgen = mbatch_generator(X, y, minbatch_size)
    for i, (X_train_min, y_train_min) in enumerate(mgen):
        _, probas = nnet.forward(X_train_min)
        predicted_labels = np.argmax(probas, axis=1)
        onehot_y = int_to_onehot(y_train_min, num_labels)

        error += np.mean((onehot_y - probas).astype('f') ** 2)
        num_examples += y_train_min.shape[0]
        correct_predictions += (predicted_labels == y_train_min).sum()

    mse = error / i
    acc = correct_predictions / num_examples
    return mse, acc

# Fits model
def train(nnet, X_train, y_train, X_valid, y_valid, num_epochs, learning_rate):
    mse = []
    nnet_train_acc = []
    nnet_valid_acc = []
    for e in range(num_epochs):
        for (features, targets) in mbatch_generator(X_train, y_train, minbatch_size=100):
            a_h, a_out = nnet.forward(features)
            
         
            d_loss__d_w_h, d_loss__d_b_h, d_loss__d_w_out, d_loss__d_b_out = \
                nnet.backward(features, a_h, a_out, targets)

            nnet.weight_h += learning_rate * d_loss__d_w_h.astype('f') 
            nnet.bias_h += learning_rate * d_loss__d_b_h.astype('f')  
            nnet.weight_out += learning_rate * d_loss__d_w_out.astype('f') 
            nnet.bias_out += learning_rate * d_loss__d_b_out.astype('f') 

        train_mse, train_acc = \
        compute_mse_and_acc(nnet, 
                            X_train, 
                            y_train, 
                            num_labels=np.unique(y_train).shape[0], 
                            minbatch_size=100)

        valid_mse, valid_acc = \
        compute_mse_and_acc(nnet, 
                            X_valid, 
                            y_valid, 
                            num_labels=np.unique(y_train).shape[0], 
                            minbatch_size=100)

        mse.append(train_mse)
        nnet_train_acc.append(train_acc  *100)
        nnet_valid_acc.append(valid_acc  *100)

        print(f'Epoch: {e+1:03d}/{num_epochs:03d} '
              f'| MSE: {train_mse:.4f} '
              f'| Train Acc: {train_acc*100:.2f}% '
              f'| Valid Acc: {valid_acc*100:.2f}%')
    return mse, nnet_train_acc, nnet_valid_acc
        
# Standardizes dataset
def std_x(X):
        for i in range(len(X[0])):
            if np.std(X[:, i]) != 0:
                X[:,i] = (X[:, i] - np.mean(X[:, i])) / np.std(X[:, i])
            else:
                X[:,i] = (X[:, i])
        return X

# LDA feature extraction functions
def extract_features(X, y, title, dim=4):
    lda = LDA(dim)

    # Standardizes dataset and computes mean vector
    X_train_trans = lda.standardize_input(X)
    mvector = lda.mvector_gen(X_train_trans, y)

    # Computes within  and between classes scatter matrixes
    smatrixw = lda.smatrixw(X_train_trans, y)
    smatrixb = lda.smatrixb(X_train_trans, y)

    # Computes eigen pair values
    eigen_pair = lda.eig_decomp(smatrixw, smatrixb)

    # Generates linear discriminant ratio plot
    lda.exp_discriminant_plot(eigen_pair, title=title)

    # Computes projection matrix and transforms dataset
    w = lda.projmatrix_gen(eigen_pair, y)
    X_train_trans = lda.projmatrix_perf(X_train_trans, w)

    return X_train_trans

# Computes initial error values
def mse(y, probas, num_labels):
    onehot_y = int_to_onehot(y, num_labels)
    return np.mean((onehot_y - probas) ** 2)

# Computes initial accuracy values
def acc(y, probas):
    preds = np.argmax(probas, axis=1)
    return np.mean(y == preds)


def load_mnist():
    # Fetches dataset 
    X,y = fetch_openml("mnist_784", version=1, return_X_y=True)

    X = X.values
    y = y.astype(int).values

    '''
    # Display first 10 random images
    fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True)
    ax = ax.flatten()
    for i in range(10):
        img = X[y == i][0].reshape(28, 28)
        ax[i].imshow(img, cmap='Greys')
        ax[i].set_xticks([])
        ax[i].set_yticks([])
    plt.tight_layout()
    plt.show()

    # Display first 10 random images of digit 8
    fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True)
    ax = ax.flatten()
    for i in range(10):
        img = X[y == 8][0].reshape(28, 28)
        ax[i].imshow(img, "Greys")
        ax[i].set_xticks([])
        ax[i].set_yticks([])
    plt.tight_layout()
    plt.show()
    '''

    # Splits X, y datasets into train, val and test datasets
    X_temp, X_test, y_temp, y_test = train_test_split(X, 
                                                      y, 
                                                      test_size=10000, 
                                                      random_state=123, 
                                                      stratify=y)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, 
                                                      y_temp, 
                                                      test_size=5000, 
                                                      random_state=123, 
                                                      stratify=y_temp)
    # Display shape of X, y split datasets
    print("X_train", X_train.shape)
    print("y_train", y_train.shape)
    print("X_test", X_test.shape)
    print("y_test", y_test.shape)
    print("X_val", X_val.shape)
    print("y_val", y_val.shape)
    print("")

    return X_train, X_val, y_train, y_val, X_test, y_test



######################################################################################
######################################################################################
###############                    USGAGE OF                    ######################
###############                 NEURAL NET MLP                  ######################
###############             WITH LDA FEATURE EXTRACTION         ######################
######################################################################################
###################################################################################### 

if __name__ == "__main__":
    np.random.seed(50)
    X_train, X_val, y_train, y_val, X_test, y_test = load_mnist()

    model = NeuralNetMLP(num_features=28*28,
                         num_hidden=50,
                         num_classes=10)

    _, probas = model.forward(X_val)
    model_mse = mse(y_val, probas, num_labels=10)
    model_acc = acc(y_val, probas)

    # Computes initial error and accuracy values
    print(f"Initial MSE: {model_mse:.2f}")
    print(f"Inital Acc: {model_acc * 100:.2f}%")
    print('')

    # Standardizes dataset
    X_train_cp = copy.copy(X_train)
    X_val_cp = copy.copy(X_val)
    X_train_std = std_x(X_train_cp)
    X_val_std = std_x(X_val_cp)

    # # Fits model
    mod_mse, mod_train_acc, mod_val_acc = train(model, 
                                                X_train_std, 
                                                y_train, 
                                                X_val_std, 
                                                y_val, 
                                                num_epochs=1000, 
                                                learning_rate=0.8)

    # # Generates error curve
    plt.plot(range(len(mod_mse)), mod_mse)
    plt.ylabel("Mean Squared Error")
    plt.xlabel("Epochs")
    plt.tight_layout()
    plt.show()

    # # Generates accuracy curve
    plt.plot(range(len(mod_train_acc)), mod_train_acc, label='Train Acc')
    plt.plot(range(len(mod_val_acc)), mod_val_acc, label='Valid Acc')
    plt.ylabel("Model Accuracy {%}")
    plt.xlabel("Epochs")
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.show()
    print('Model fitting with original dataset completed!')

    print('*'*50)
    print('*'*50)
    print('Model Fitting with Extracted Dataset')
    print('*'*50)
    print('*'*50)

    # Extract features
    X_train_trans = extract_features(X_train, 
                                     y_train, 
                                     title='Training dataset', 
                                     dim=X_train.shape[1])
    X_val_trans = extract_features(X_val, 
                                   y_val, 
                                   title='Validation dataset', 
                                   dim=X_val.shape[1])

    model1 = NeuralNetMLP(num_features=X_train_trans.shape[1],
                         num_hidden=50,
                         num_classes=10)






















































    ########################################################################################################
    ########################################################################################################
    ########################################################################################################
    ########################################################################################################

    # fits model with data
    # mod_mse_trans, mod_train_acc_trans, mod_val_acc_trans = train(model1, 
    #                                            X_train_trans, 
    #                                            y_train, 
    #                                            X_val_trans, 
    #                                            y_val, 
    #                                            num_epochs=100, 
    #                                            learning_rate=0.8)


    # # Generates loss curve
    # plt.plot(range(len(mod_mse_trans)), mod_mse_trans)
    # plt.ylabel("Mean Squared Error")
    # plt.xlabel("Epochs")
    # plt.tight_layout()
    # plt.show()

    # Generates accuracy curve
    # plt.plot(range(len(mod_train_acc_trans)), mod_train_acc_trans, label='Train Acc')
    # plt.plot(range(len(mod_val_acc_trans)), mod_val_acc_trans, label='Valid Acc')
    # plt.ylabel("Model Accuracy {%}")
    # plt.xlabel("Epochs")
    # plt.legend(loc="lower right")
    # plt.tight_layout()
    # plt.show()





    














