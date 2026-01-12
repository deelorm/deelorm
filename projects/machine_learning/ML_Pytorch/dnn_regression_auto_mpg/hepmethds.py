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