import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_s_curve
from sklearn.manifold import MDS
from tqdm import tqdm

    
def scatter_3d(X, y):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.hot)
    ax.view_init(10, -70)
    ax.set_xlabel("$x_1$", fontsize=18)
    ax.set_ylabel("$x_2$", fontsize=18)
    ax.set_zlabel("$x_3$", fontsize=18)
    plt.show(block=False)
    
if __name__ == "__main__":
    
    
    X, Y = make_s_curve(n_samples = 500,
                           noise = 0.1,
                           random_state = 42)
    scatter_3d(X,Y)
