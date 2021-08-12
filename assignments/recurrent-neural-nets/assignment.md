# Recurrent Neural Networks

- [Recurrent Neural Networks](#recurrent-neural-networks)
  - [Introduction](#introduction)
  - [Basic](#basic)
    - [Part 1: Read about LSTM](#part-1-read-about-lstm)
  - [Advanced](#advanced)
    - [Part 2: Forecast time-series data](#part-2-forecast-time-series-data)

## Introduction

The LSTM (Long Short-Term Memory) variant of recurrent neural networks has been deployed in speech recognition products by Google, Apple, and Microsoft. If you are trying to model a sequence where important context occurs much earlier, there is a good chance you'll want to use an LSTM.

## Basic

### Part 1: Read about LSTM

The first part of this assignment is **not** coding. It's reading this [excellent blog post](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) by Christopher Olah and answering the following questions.

1. What problem do standard recurrent neural networks have that LSTMs seek to address?

2. Contrast the repeating module in a standard recurrent neural net with that of an LSTM.

3. In an LSTM module:
   a) What holds the information?
   b) What structures add or remove information?

4. Describe how an LSTM module:
   a) Updates its state.
   b) Determines what to output.

## Advanced

### Part 2: Forecast time-series data

In the `src` folder you'll find an `lstm.py` file and a `run_lstm.py` file. These files are slightly modified versions of Jakob Aungiers code you can find [here](https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction). In his [blog](http://www.jakob-aungiers.com/articles/a/LSTM-Neural-Network-for-Time-Series-Prediction) you can read how he used an LSTM to:

1. Learn a sine wave, and then
2. Predict the rise and fall of the S&P 500.
   Your assignment is to play with and try to understand this code. Some things to look out for include:

- The use of argument parsing. When you execute the code from them main directory, you tell your code to analyze either the **sine** wave data or the S&P 500 data: `$ python src/run_lstm.py sine`. Make sure that you can answer the following questions.
  - How the data is split into train and test sets.
  - How the target is determined.
  - How the model architecture is defined.
  - The hyperparameters that are needed to get good performance on the sine wave.
  - The hyperparameters required to get good performance on the S&P 500.

If you have time, find your own times series data set and see if some version of this architecture works for predicting your data.
