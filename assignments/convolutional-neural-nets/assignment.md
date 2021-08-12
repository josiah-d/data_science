# Convolutional Neural Networks
- [Convolutional Neural Networks](#convolutional-neural-networks)
  - [Basic](#basic)
    - [Part 1: MNIST Classification](#part-1-mnist-classification)
      - [Read The code](#read-the-code)
      - [Tunning suggestions](#tunning-suggestions)
  - [Advanced](#advanced)
    - [Part 2: Cats and Dogs.](#part-2-cats-and-dogs)
  - [Extra credit](#extra-credit)
    - [Part 3: Upgrade the code syntax.](#part-3-upgrade-the-code-syntax)
## Basic

### Part 1: MNIST Classification
You will be revisiting the MNIST digits but with a more formidable 
image classification tool:  a convolutional neural net.  Take the pre-existing code
in `src/cnn.py` and tune it to improve performance. You should be able to get 
above 90%+ accuracy.

#### Read The code

Read the `src/cnn.py` code to understand the structure of the code. Feel free to copy it into Jupyter notebook to examine the structure of the neural network.

#### Tuning suggestions
1. Changing the activation functions. Explore the choices of activation functions. Hints: Andrej Karpathy's favorite is `relu`.
2. There are several other hyperparameters to fine tune. For example,
   1. `batch_size`. Try values from `[32, 64, 256, 512]`, etc. If your computer has large memory, try even larger batch size.
   2. `nb_epoch`. Can increase to like `3` or `4`.
   3. `nb_filters`. Number of input filters. Choose from `[12, 16, 32]`.
   4. `kernel_size`. Try `[3,3]` or `[5,5]`.

Note that the solution is not unique.
## Advanced

### Part 2: Cats and Dogs.

You are going to build a neural network model to classify dogs and cats.

1. Read this [blog](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html) for the syntax of Keras.

The [`src/starter_part2.py`](src/starter_part2.py) provides you with a runnable example. However, the dataset is very limited. It is there so it can run.

Download the full dataset from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats/). Change the `batch_size` to increase training speed. Make sure that you properly, manually ok, split the trainning and validation sets.

Your task is to learn from the [community](https://www.kaggle.com/c/dogs-vs-cats/notebooks) to increase the accuracy to **80%+** on your validation set.


> Hint: be aware of the desired directory structures.
```
data/
    train/
        dogs/
            dog001.jpg
            dog002.jpg
            ...
        cats/
            cat001.jpg
            cat002.jpg
            ...
    validation/
        dogs/
            dog003.jpg
            dog004.jpg
            ...
        cats/
            cat003.jpg
            cat004.jpg
            ...

```

## Extra credit
### Part 3: Upgrade the code syntax.

2. Read this [blog](https://keras.io/guides/transfer_learning/) for the updated syntax of using keras. Change the starter code with the latest syntax.
> This assignment is an important lesson that also teaches you how to migrate codebase.


