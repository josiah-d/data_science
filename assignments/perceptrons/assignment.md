# Perceptrons
- [Perceptrons](#perceptrons)
  - [Introduction](#introduction)
  - [Basic](#basic)
    - [Part 1: Installation, and Introduction to Keras](#part-1-installation-and-introduction-to-keras)
    - [Part 2: Loading data and baseline model](#part-2-loading-data-and-baseline-model)
      - [Initial inspection](#initial-inspection)
      - [Baseline model](#baseline-model)
    - [Part 3: Logistic Regression with Keras](#part-3-logistic-regression-with-keras)
  - [Advanced](#advanced)
    - [Part 4: Logistic regression in parallel](#part-4-logistic-regression-in-parallel)
    - [Part 5: Perceptrons: Logistic regression with hidden features](#part-5-perceptrons-logistic-regression-with-hidden-features)
  - [Extra Credit](#extra-credit)
    - [Part 6: Installation for PCs with NVIDIA GPUs that wish to use the GPU to speed up training.](#part-6-installation-for-pcs-with-nvidia-gpus-that-wish-to-use-the-gpu-to-speed-up-training)

## Introduction

Multilayer neural networks are a current hot-topic in machine learning. The multilayer perceptron was the first standardized architecture.  In this assignment, you will learn to tune a [multilayer perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron) model.

There are many libraries for using neural networks, but there isn't yet a single standard.  [Tensorflow](https://www.tensorflow.org/) is used by many, with [Keras](https://keras.io/) as one of the official APIs.

## Basic

### Part 1: Installation, and Introduction to Keras

We'll be installing Keras and Tensorflow using a Docker container.  You could install Tensorflow natively (see [here](https://www.tensorflow.org/install/pip)) but Tensforflow typically causes downgrades in the Anaconda environment, and it has screwed up students'  Anaconda distribution in the past.

**NOTE** If you have a PC with an NVIDIA GPU, and you want to train on it (highly recommended if you're pursuing a neural-net based capstone project), then you'll want to install `nvidia-docker` instead.  Go to the end of this assignment (the bottom of this page) and follow the install directions there.

So, on with the Docker install:
* Go to the home directory in your Terminal.  

  ```bash
  $ cd ~
  ```

* Start a Jupyter server on a `Docker` instance with Tensorflow 2.0 installed. This will pull the image from Docker Hub and make a container named `tensorflow`.


**It is very important to ensure that no local jupyter notebook process is using the port 8888. Otherwise your password/token will be invalid.**

    ```bash
    $ docker run -it --name tensorflow -p 8888:8888 -v "$PWD":/tf tensorflow/tensorflow:2.0.0a0-py3-jupyter
    ```
  * After starting up the `docker` container and running the `Jupyter` notebook, you'll see a printout like:
    ```
    ...
    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-10-open.html
    Or copy and paste one of these URLs:
        http://(ae4038ed94a3 or 127.0.0.1):8888/?token=e305929f1dca3ae69707f9a67d6467bd92ce3c1d6521919c
    ```
    
    The hex number after `token=` is a password you need to access the notebook. In this case, it is `e305929f1dca3ae69707f9a67d6467bd92ce3c1d6521919c`, but yours will be different.
  * Go to `http://localhost:8888` and enter in the password when prompted.
  * If you use the above Docker command, the working directory will map to directory `/tf` in the container. The working directory of the Jupyter notebook in the container is `/tf`, and a useful Python script for this assignment in the `src` directory of this repository. Make sure that the `src` directory is in the Jupyter notebook's Python path, one way or another.
  * If you close the notebook, to re-run the container by typing 
    ```bash
    $ docker start -a tensorflow
    ```
* This Docker image (and the resulting container) has `numpy`, `keras`, and `tensorflow` packages.  However, it's lacking `pandas` and `sklearn`.  If you want to use them in this assignment, you'll have to access the container from the command line to install them.  Here's how you do that.  
  ```bash
  $ docker exec -it tensorflow /bin/bash
  ```
  Then from within the container:
  ```bash
  # pip install -U scikit-learn  
  # pip install pandas
  ```
* For this assignment you have a couple of workflow options.  You could work in the Jupyter notebook.  Or, you can access the Tensorflow container from Terminal (as you did above) so that you can run a script from the command line.
> First, you need to run `docker container ls` to find out the running container's name. Let's call it `container_name`.
* Then, to do this, in your Terminal access the running container in the bash shell using:
    ```bash
    $ docker exec -it container_name /bin/bash
    ```
  Then from within the container:
  ```bash
  # python mlp.py
  ```  
  Or:
  ```bash
  # ipython
  In [1]: run mlp.py
  ```

* Briefly read some example code for Multilayer Perceptron (the standard neural network) at http://keras.io/examples/. Note that these examples may be out of date.  If you want to run the examples in the link, you need to import `keras` and supporting modules differently than what's shown in the examples.  Specifically, they need to be imported from `tensorflow`:

    ```python
    from tensorflow import keras
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout, Activation
    from tensorflow.keras.optimizers import SGD
    ```

### Part 2: Loading data and baseline model

> In this part, you are encouraged to start a notebook to finish the tasks. As always, a lot of Googling is required. You are not supposed to understand everything completely to finish this part.


In the Docker-backed Jupyter notebook/Terminal/Ipython console, use the `load_and_condition_MNIST_data` function in `src/mlp.py` to load a train and test set of images of hand-drawn digits.

#### Initial inspection

```python
from mlp import load_and_condition_MNIST_data
X_train, y_train, X_test, y_test, y_train_onehot = load_and_condition_MNIST_data()
```

1. The shape of `X_train` is (n_samples, n_features). How many samples are there in the training set? How many in the test set? How many features are there per sample?

2. You may have noticed that each sample "image" is a row from the `X` matrix - it's a 1-dimensional array. Speculate on why this is a convenient way to store images.

3. Inspect a few of the sample images. (You may find the `np.reshape` and `ax.imshow` methods useful.) Inspect some of the corresponding labels from the labels `y_train`; you'll find that they're simply a number corresponding to the digit depicted in the image.

```python
fig, ax = plt.subplots()
ax.imshow(X_train[0].reshape(28,28));
```


Look at the `y_train_onehot` labels. What's going on there? We'll get to that soon.

Our task is to use X_train and y_train to make a model that will accurately predict the labels in X_test.

#### Baseline model

If we conceptualize each image sample as a 1-dimensional vector, we can use any multiclass model available. For example, we could simply train a single decision tree:

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
yhat = clf.predict(X_test)
print(accuracy_score(y_test, yhat))
```

If you run this, you'll find a single decision tree can classify hand-drawn digits with about 88% accuracy. Pretty good for being so simple. That's the score to beat.

Take a moment to discuss with your partner what each split in the decision tree means, and what it means for a decision tree to classify an image.

### Part 3: Logistic Regression with Keras

Maybe the simplest possible model in Keras a neural network with a single unit and no hidden layer:

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
np.random.seed(42)

n_samples, n_feats = X_train.shape

model = Sequential() # sequence of layers

denselayer = Dense(units=1,
                input_dim=n_feats,
                kernel_initializer='uniform',
                activation='sigmoid')

model.add(denselayer)
```

1. Build this model, and **without training it**, use the `.predict(X_test)` method to predict the output label of the test set. What is the shape of the output of `predict`? Speculate about why this works, even if you haven't trained the model.

2. The output of this model is the activation of a single "neuron" (aka "unit"), as a function of all 784 input pixel features. The output of the neuron is `activation_function( m*x+b )`, where `activation_function` is function specified in the `denselayer` layer, and `m` and `b` are the `.weights` and `.bias` members of the layer. Manually obtain the neuron's weight and bias, and use the pseudocode `activation_function( m*x+b )` to calculate the neuron's response to the first test example `X_test[0]`. 

Now, find the output of a logistic regression model using `m` as the `beta` and `X_test[0]` as `x_i`. How to they compare?

3. The current model can't do multiclass prediction - it can only predict a single thing. Let's use it to predict if an image is a '1'. Create a binary label set `yone_train` and `yone_test` for images that are ones, and then train it like this:

```
from tensorflow.keras.metrics import Precision, Recall
model.compile(loss='binary_crossentropy', optimizer="sgd", metrics=[Precision(), Recall()] ) 

model.fit(X_train, yone_train, epochs=10, batch_size=5000, verbose=1,
              validation_split=0.1)
```

Take a look at the `weight` and `bias` parameters of the `denselayer`. Have they changed? Now that you've considered the relationship of this neuron to logistic regression, how would you relate training this model to training a logistic regression model? (Consider taking the neuron's `weight` vector, reshaping it into a square, and rendering an image of it.)

## Advanced

### Part 4: Logistic regression in parallel

Keras allows us to perform logistic regression _in parallel_ for a large number of target classes:

```python
np.random.seed(42)

n_samples, n_feats = X_train.shape

model = Sequential() # sequence of layers

denselayer = Dense(units=10,
                input_dim=n_feats,
                kernel_initializer='uniform',
                activation='sigmoid')

model.add(denselayer)

model.compile(loss='categorical_crossentropy', 
              optimizer="sgd", metrics=["accuracy"] )
```

1. Compile and train this model. What test accuracy does it converge to? Is it good or bad?

2. Use the model to find a probabilistic prediction on any item in `X_test`. What is the _sum of probabilities_ for every predicted class?

You'll notice the predictions are hot garbage (with an accuracy around 20%), and that the class probabilities for every class sum to more than 1.0.

One solution is to apply a function to the neuron outputs that normalizes the vector such that it's constrained to add up to 1.0, and then on a loss from _that_ function.

3. Change the `activation` argument to "softmax", and retrain the model. What is the test accuracy? What is the sum of classification probabilities for all classes, for a single prediction?

Extra credit: train with a large `batch` argument in `.fit`, and make pictures of the unit weights reshaped into 28x28 images.

### Part 5: Perceptrons: Logistic regression with hidden features

A perceptron is an architecture whereby an input is classified into a number of features; features that are actually unknown when model training begins. Then, logistic regression (or softmax regression) using the _hidden features_ as inputs is used to find the final class probabilities. This architecture is called a "perceptron", "multiplayer perceptron", or "MLP". Here's how to define an MLP with 300 neurons in one hidden layer, using Keras:

```python
np.random.seed(42)

n_samples, n_feats = X_train.shape

model = Sequential() # sequence of layers

hidden_units = 300
n_classes = 10

hidden_layer = Dense(units=hidden_units,
                input_dim=n_feats,
                kernel_initializer='constant',
                activation='sigmoid')

output_layer = Dense(units=n_classes,
                input_dim=hidden_units,
                kernel_initializer='uniform',
                activation='softmax')

model.add(hidden_layer)
model.add(output_layer)
```

1. Compile and train this model on the MNIST dataset. The 'adam' optimizer tends to do well. What kind of accuracy do you get? 
2. Vary the hyperparameters. Choose differnet activations, kernal initializers, hidden units, optimizers, and optimizer parameters. To access optimizer parameters, instantiate optimizer objects from `tensorflow.keras.optimizers`. Can you get a better accuracy than 94%?

This task might feel a little like looking for a needle in a haystack.  Perhaps you can think of an automated approach instead of a manual brute force search? (but with some intuition the brute force search will get you there, too.)  Keras has a [wrapper](https://keras.io/scikit-learn-api/) for the scikit-learn API where you can interface with GridSearch.  See this [blog post.](https://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/)

3. When you have a very good accuracy, make a picture of the weights associated with the hidden layers.

Hint: do this, 
```python
hidden_unit_i = 0
plt.imshow(hidden_layer.weights[0].numpy()[:,hidden_unit_i].reshape(28,28))
```

Speculate on what this might mean.

## Extra Credit

### Part 6: Installation for PCs with NVIDIA GPUs that wish to use the GPU to speed up training.  

1) Go [here](https://github.com/NVIDIA/nvidia-docker) and follow the directions to install `nvidia-docker`.
2) Check that it works:  
   ```bash
   $ docker run --gpus all nvidia/cuda:9.0-base nvidia-smi
   ```
3) Download an image, make a container and a volume:
   ```
   $ cd ~
   $ docker run --gpus all -it --name tensorflow-gpu -p 8888:8888 -v "$PWD":/tf tensorflow/tensorflow:latest-gpu-py3-jupyter
   ```

As discussed in Part 1, you can work with the container in a Jupyter notebook or from terminal.
