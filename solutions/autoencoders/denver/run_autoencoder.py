import numpy as np
from tensorflow.keras.datasets import fashion_mnist
from autoencoder_keras import Autoencoder
import matplotlib.pyplot as plt
import assignment_soln as a


if __name__ == '__main__':
    # Import data
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

    # Prepare input
    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

    # Keras implementation
    autoencoder = Autoencoder(x_train.shape[1], 2)
    autoencoder.train(x_train, x_test, 256, 50)
    encoded_imgs = autoencoder.getEncodedImage(x_train)
    decoded_imgs = autoencoder.getDecodedImage(encoded_imgs)

    # Keras implementation results
    plt.figure(figsize=(20, 4))
    for i in range(10):
        # Original
        subplot = plt.subplot(2, 10, i + 1)
        plt.imshow(x_test[i].reshape(28, 28))
        plt.gray()
        subplot.get_xaxis().set_visible(False)
        subplot.get_yaxis().set_visible(False)

        # Reconstruction
        subplot = plt.subplot(2, 10, i + 11)
        plt.imshow(decoded_imgs[i].reshape(28, 28))
        plt.gray()
        subplot.get_xaxis().set_visible(False)
        subplot.get_yaxis().set_visible(False)
    plt.savefig('results.png')

    # Question 9
    d_ind_cat = a.assign_index_to_category_name()
    d_cat_ind = {v: k for k, v in d_ind_cat.items()}
    indices_per_category = {cat: a.indices_for_category(cat, y_train) 
                            for cat in range(0,10)}
    fig_name = 'autoencoder_2_components.png'
    axis_labels = ('Autoencoder code 1', 'Autoencoder code 2')
    a.plot_2d_transformed_data(encoded_imgs, y_train, d_ind_cat, axis_labels, fig_name)

    # Question 10
    centroids = a.get_centroids_and_centroid_images(x_train, encoded_imgs, indices_per_category)
    d_centroids, d_centroids_ae, d_centroid_images, d_ind_centroids = centroids
    centroid_images = [d_centroid_images[cat].reshape(28,28) for cat in range(0,10)] 
    fig_name = 'autoencoder_centroid_images.png'
    a.plot_images_in_lst(centroid_images, fig_name)

    # Question 11
    reconstructed_images = [] 
    for cat in range(0,10):
        reconstructed_images.append(decoded_imgs[d_ind_centroids[cat]].reshape(28,28))
    fig_name = 'reconstructed_images_from_2_autoencoder_components.png'
    a.plot_images_in_lst(reconstructed_images, fig_name)
