# Transfer Learning

- [Transfer Learning](#transfer-learning)
  - [Introduction](#introduction)
  - [Basic](#basic)
    - [Part 1: Data](#part-1-data)
    - [Part 2: Simple ConvNet](#part-2-simple-convnet)
  - [Advanced](#advanced)
    - [Part 3: Transfer Model](#part-3-transfer-model)

## Introduction

Today we're going to train a convnet to recognize desserts using transfer learning, then compare it to a simple convnet. This exercise is quite memory and CPU intensive so **close any unnecessary programs before you begin.**


> Please also make sure that you upgraded Tensorflow to 2.0+. The solution was tested with the following versions.

```csv
tensorflow==2.3.1
tensorflow-estimator==2.3.0
```
## Basic

### Part 1: Data

> Estimated time of completion: 5 mins.

Inspect the `data/` folder. To make it easy to load images into Keras, it's been split into a training and validation folders, with an additional holdout set to evaluate model performance at the end.

### Part 2: Simple ConvNet

> Estimated time of completion: 30 mins.

1. Using the `create_model` function in `simple_cnn.py` (this is the same ConvNet you built in the CNN assignment), create a keras model. Use 100x100x3 (100 pixels square with channels for RGB) as the input size while testing to save time, but we will increase this later.
2. Previously, we used `model.fit()` to run the model. However, the `fit()` method will load all of your data into memory, which is generally unusable for large datasets. To deal with this, we'll be using data generators, which load data on the fly. The keras ImageDataGenerator also makes it easy to implement data augmentation, which we can use to increase our validation accuracy.  
   Make two image data generators: one for training data and one for validation. for both, use the Xception preprocessor, which performs a couple quick scaling and transformation operations.

    ```python
    from keras.applications.xception import preprocess_input
    ```

You can decide what image augmentation to use in the training datagen, but don't use augmentation in the validation datagen as we want that to be indicative of real world inputs to our model.

3. Using your image datagens, use flow_from_directory to make two generators, one for training and one for validation. Start with target_size 100x100 and batch_size 16.

4. Compile model using your favorite optimizer.
5. Run your model for a few epochs using the `fit_generator` method. `steps_per_epoch` is generally equal to the number of training images / batch_size, and validation steps is number of validation images / batch_size

6. After you've gotten that to work, add a tensorboard callback so you can monitor training status

7. The model at the end of training session is not necessarily the best model! To fix this, we will add another callback that saves our best model to disk for use later. Use `keras.callbacks.ModelCheckpoint` to make a callback and pass it to the `fit_generator`. You can use `save_best_only=True` to prevent saving tons of models on your computer.

8. Finally, let's evaluate our model on the holdout set.
   First, load your best model from disk:

    ```python
    from keras.models import load_model
    best_model = load_model(file_path_to_model)
    ```

You can make a `holdout_generator` with `validation_datagen.flow_from_directory` and pass it the holdout folder instead of the validation folder. Then use `model.evaluate_generator()`, which is very similar to `fit_generator` to output the holdout loss and holdout accuracy.

    ```python
    metrics = best_model.evaluate_generator(<your code here>)
    ```

> Checkpoint 1: Congratulations! You just created a very practical set-up for modeling with a ConvNet, where you can read in large datasets with ease, save the best models and monitor the progress on a tensorboard!

## Advanced

### Part 3: Transfer Model

> Estimated time of completion: 60 mins.

1. Create a function that takes Xception (from keras.applications) and adds a new head for our current task onto it. Use a GlobalAveragePooling2D layer and a Dense layer with a softmax activation.

2. Set all of the layers except for the new head to untrainable, then compile it with you favorite optimizer. We want to warm up the head slowly, so use a lower learning rate than you normally would ~(2x to 10x smaller).

3. From here, you can run the warmup phase the same way that you ran the simple model with the generators and the fit_generator method

4. After a few warmup epochs, unfreeze the 14th convolutional block onward, recompile and continue training, again with a low learning rate or an adaptive optimizer.

5. Evaluate your performance on with the transfer model. Is it better than the simple ConvNet?

6. Play around with different hyperparameters, optimizers and even base models (try mobilenet, etc.)

> Checkpoint 2: Nice work! You just performed surgery on a neural network and retrained it to your particular task! This is a really powerful method for image classification.
