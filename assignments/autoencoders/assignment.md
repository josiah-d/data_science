# Autoencoders

## Basic

### Part 1: Installing Tensorflow
1)  If tensorflow isn't already installed, install it: `pip install tensorflow`

2)  By default, Keras uses tensorflow as its backend.  If for some reason you are using theano, change it back in the keras config file (`~/.keras/keras.json`) by setting `"backend": "tensorflow"`.

### Part 2: Using TensorBoard
TensorBoard is a great visualization tool that can take a lot of the mystery out of what's happening under the hood of neural networks. (Look inside the black box!) We have the ability to use this tool from within keras.

Run the script `src/xor_keras.py`. This will train a simple neural network on a TINY dataset (8 rows!) to model the "XOR" relationship, and is configured to write model logs to TensorBoard.

In order to keep TensorBoard logs, you need to invoke TensorBoard in a list of "callbacks". Callbacks are fed as a list in your `model.fit` step. See excerpts from the code below to see how this is done.

```python
# with your import statements
from keras.callbacks import TensorBoard

# insert lots of code pre-processing and instantiating model, etc.
# ...
# later:
model.compile(loss='mean_squared_error', optimizer=sgd, metrics=["mse"])

# before fit step
# instantiate TensorBoard
# these are my recommended settings for this type of problem- change as necessary
tensorboard = TensorBoard(log_dir='./logs', histogram_freq=2, batch_size=batch_size, write_graph=True, write_grads=True, write_images=True)

model.fit(X, y, batch_size=batch_size, epochs=num_epochs, verbose=1, shuffle=True,
          validation_split = 0.25, callbacks = [tensorboard])
```

See [here](https://keras.io/callbacks/#tensorboard) for more information on the TensorBoard keyword arguments.

You may want to consider also adding an [EarlyStopping](https://keras.io/callbacks/#earlystopping) callback to your callbacks list. This will make your life much easier - you won't have to guess at the number of epochs, and keras will stop automatically when you start to get diminishing returns in performance.

Once you run the code, this will create some TensorBoard logs for you to look at. TensorBoard will continue to dump files from subsequent runs into the same log directory, which will make visualization really confusing! So make sure that as you do this multiple times, you change the name of the log directory you write to or remove the logs entirely if you won't need them again.

Once your model is finished training, you can access the TensorBoard output from the command line like
```bash
tensorboard --logdir=logs
```
Note - you’ll need to specify the path to wherever you saved *your* logs.

You should get some output that looks something like
<br>```TensorBoard 1.5.1 at http://Taryns-MBP:6006```
Copy the web address given and paste into your web browser to start visualizing!
Note, if the given shortcut does not work in your browser, try navigating to `0.0.0.0:6006` instead. `0.0.0.0` references your local machine. The default port for TensorBoard is 6006.

Click on the `Scalars` tab. This will show you the evolution of your model metrics as well as your loss. You can view these as a function of epochs, or time (relative or absolute). Note: relative time and epochs become confusing when you have inadvertently dumped more than one training run into the same log directory, as multiple runs will just lay on top of each other.

Did we need as many epochs as we did? Where does our loss start to level off?

Click on the `Images` tab. If you had this option turned on, you will be able to visualize your weights at each step. You can step forward and backward to see how your weights evolved over time (this will be at the granularity you set when instantiating your TensorBoard object). In this case we don't have too many weights, so you won't have huge weight matrices to look over. Time series models yield particularly interesting looking weights.

Click on `Graphs` to see a visualization of your model architecture. This is very helpful when you start using more complicated cell types and architectures and want to see how data is flowing under the hood!

The `Distributions` tab will show how the distribution of your weights and their gradients are evolving with each step. This is very useful for debugging - i.e. if your model seems to be getting stuck or converging on weird results, you can look at each layer and see what might be the cause. This may also tell if you have layers that are not "contributing" to your model. `Histograms` presents nearly the same information in a different format. Try changing the initializations of your weights and compare these tabs before and after. This should help you visualize how important initializations are and better help you understand what you are seeing in this tab.

The other tabs will not be available to you with data you are using and with the model and settings specified above.

Continue to play around in TensorBoard until you feel comfortable using these tools.

## Advanced
### Part 3: Using Autoencoders
Using your new knowledge about autoencoders, write fill in the stub code in `src/autoencoder.py`, to design an autoencoder with dense layers. For more help on this, see the tutorial [here.](https://blog.keras.io/building-autoencoders-in-keras.html)
The first function in this script loads and scales the MNIST dataset for you.

The second function should return your autocoder model, compiled.

Use the function in `src/plot_reconstruction.py` to examine the reconstructed inputs. If you don't like your results at first, keep tuning your model!

## Extra Credit
### Part 4: Integrate your Autoencoder into a predictive model
Integrate a softmax prediction layer into your trained autoencoder. You can add this at the end of the full autoencoder, or at the end of the encoded (compressed) portion. See [this post](https://keras.io/getting-started/faq/#how-can-i-use-pre-trained-models-in-keras) for help on freezing trained layers in keras.

Using an autoencoder, I was able to get test accuracy of 98% (and keep in mind, we are still not using the "correct" model architecture for images). Can you beat that?
