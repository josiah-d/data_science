import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from collections import defaultdict
import os

def check_for_plots_dir():
    if not os.path.exists('plots'):
        os.makedirs('plots')

def plot_images_in_lst(image_lst, fig_name):
    check_for_plots_dir()
    nimgs = len(image_lst)
    ncols = int(min(nimgs, 5)) 
    nrows = int(np.floor(nimgs / ncols))
    fig = plt.figure(figsize=(2*ncols, 2*nrows))
    for i in range(nimgs):
        ax = fig.add_subplot(nrows, ncols, i+1)
        ax.imshow(image_lst[i], cmap='gray')
        ax.set_xticks([])
        ax.set_yticks([])
    fig.suptitle(fig_name.split('.')[0], fontsize=16)
    fig.savefig('plots/' + fig_name, dpi=100)
    plt.close()

def assign_index_to_category_name():
    d_ind_cat = {0: 'Tshirt-top',
                 1: 'Trouser',
                 2: 'Pullover',
                 3: 'Dress',
                 4: 'Coat',
                 5: 'Sandal',
                 6: 'Shirt',
                 7: 'Sneaker',
                 8: 'Bag',
                 9: 'Ankle boot'}
    return d_ind_cat


def indices_for_category(ind_category, labels):
    row_indices = np.argwhere(labels == ind_category).flatten()
    return row_indices

def select_nimgs_from_category(images, n, indices_for_category, seed):
    np.random.seed(seed=seed)
    selected_indices = np.random.choice(indices_for_category, size=n, 
                                        replace=False)
    selected_images = images[selected_indices]
    return selected_images

def plot_2d_transformed_data(X_2features, labels, d_ind_cat, axis_labels, fig_name):
    colors = {0: 'blue',
              1: 'green',
              2: 'red',
              3: 'cyan',
              4: 'magenta',
              5: 'yellow',
              6: 'olive',
              7: 'pink',
              8: 'orange',
              9: 'blueviolet'}
    cat_labels = np.array([d_ind_cat[cat] for cat in range(0,10)])
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1,1,1)
    for cat in range(0, 10):
        X_cat = X_2features[labels == cat, :]
        ax.scatter(X_cat[:, 0], X_cat[:, 1], s=4, alpha=0.3, 
               color=colors[cat], label=cat_labels[cat])
    ax.legend(loc='upper left')
    ax.set_xlabel(axis_labels[0])
    ax.set_ylabel(axis_labels[1])
    fig.suptitle(fig_name.split('.')[0], fontsize=16)
    fig.savefig('plots/' + fig_name, dpi=100)
    plt.close()

def get_centroids_and_centroid_images(X, X_transformed, indices_per_category):
    d_centroids = defaultdict(lambda: np.ndarray(0))
    d_ind_centroids = defaultdict(int)
    d_centroids_pca = defaultdict(lambda: np.ndarray(0))
    d_centroid_images = defaultdict(lambda: np.ndarray(0))
    for cat in range(0,10):
        X_cat = X_transformed[indices_per_category[cat]]
        centroid = np.mean(X_cat, axis=0)
        d_centroids[cat] = centroid
        distances = np.linalg.norm(centroid - X_cat)
        ind_smallest_cat = distances.argmin()
        ind_smallest = indices_per_category[cat][ind_smallest_cat]
        d_ind_centroids[cat] = ind_smallest 
        d_centroids_pca[cat] = X_transformed[ind_smallest]
        d_centroid_images[cat] = X[ind_smallest]
    return d_centroids, d_centroids_pca, d_centroid_images, d_ind_centroids



if __name__ == '__main__':
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    # Question 2
    fig_name = 'first_ten_train.png'
    image_lst = [train_images[i] for i in range(0, 10)]
    plot_images_in_lst(image_lst, fig_name)

    # Question 3
    d_ind_cat = assign_index_to_category_name()
    d_cat_ind = {v: k for k, v in d_ind_cat.items()}
    indices_per_category = {cat: indices_for_category(cat, train_labels) 
                            for cat in range(0,10)}
    seed = 1
    n = 10
    selected_images = {cat: select_nimgs_from_category(train_images, n, 
                            indices_per_category[cat], seed)
                            for cat in range(0,10)}
    for cat in range(0, 10):
        fig_name = d_ind_cat[cat] + '.png'
        plot_images_in_lst(selected_images[cat], fig_name)

    # Question 4 
    row_shape = (len(train_images), train_images.shape[1] * train_images.shape[2])
    X_train = train_images.reshape(row_shape) 

    # Question 5
    nc = 2 # number of PCA components
    pca = PCA(n_components=nc) 
    pca.fit(X_train)
    X_train_pca = pca.transform(X_train)
    fig_name = 'PCA_2_components.png'
    axis_labels = ('Principal component 1', 'Principal component 2')
    plot_2d_transformed_data(X_train_pca, train_labels, d_ind_cat, axis_labels, fig_name)

    # Question 6
    centroids = get_centroids_and_centroid_images(train_images, X_train_pca, indices_per_category)
    d_centroids, d_centroids_pca, d_centroid_images, d_ind_centroids = centroids
    centroid_images = [d_centroid_images[cat] for cat in range(0,10)] 
    fig_name = 'representative_centroid_images.png'
    plot_images_in_lst(centroid_images, fig_name)

    # Question 7
    d_reconstructed = defaultdict(lambda: np.ndarray(0)) 
    for cat in range(0,10):
        d_reconstructed[cat] = pca.inverse_transform(d_centroids_pca[cat]).reshape(28,28)
    reconstructed_images = [d_reconstructed[cat] for cat in range(0,10)] 
    fig_name = 'reconstructed_images_from_2_principal_components.png'
    plot_images_in_lst(reconstructed_images, fig_name)
