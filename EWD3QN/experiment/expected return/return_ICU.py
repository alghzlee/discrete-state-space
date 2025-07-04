import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    EWD3QN = np.load('../../EWD3QN/EWD3QN.npy', allow_pickle=True)
    x_length_list = list(range(len(EWD3QN)))
    ax = plt.figure()

    plt.plot(x_length_list, EWD3QN, '-', color='r', label='EWD3QN')
    font1 = {'family': 'Arial', 'weight': 'normal'}
    plt.legend(prop=font1)
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], fontname="Arial")
    plt.yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24], fontname="Arial")
    plt.xlabel("Epochs", font1)
    plt.ylabel("Expected return", font1)
    plt.show()
 
