### Recurrent neural networks solution, Part 1

The first part of this assignment is **not** coding.  It's reading this [excellent blog post](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) by Christopher Olah and answering the following questions.

1) What problem do standard recurrent neural networks have that LSTMs seek to address?  
*The problem of remembering information far back in a sequence, i.e. long-term dependencies.*

2) Contrast the repeating module in a standard recurrent neural net with that of an LSTM.  
*The repeating module in a standard RNN is simple, usually it's only one layer with a single activation function.  The repeating module for an LSTM has four layers that interact with each other to set the "cell state".*


3) In an LSTM module:  
a) What holds the information?  
*The cell state holds information relevant to influencing the activation of an LSTM layer.*

b) What structures add or remove information?    
*Gates add or remove information from the cell state.*  

4) Describe how an LSTM module:   
a) Updates its state.  
*First, the LSTM needs to determine what it should forget.  This is done by a layer using a sigmoid activation function called the "forget gate layer." The output off the forget layer ranges from 0 to 1, where 0 indicates completely get rid of the information in the cell state, where 1 indicates save all that information.  Next, the LSTM needs to decide what information it should add to the cell state.  This requires two layers and two activation functions.  A sigmoid layer, called the "input gate layer", decides which values to update from options presented by another layer, activated by a hyperbolic tan function. So there are 3 layers associated with updating the state of an LSTM.*

b) Determines what to output.   
*The final layer of the four layer LSTM determines what to output; it will be a filtered version of the updated cell state.  It uses sigmoid followed by the hyperbolic tan activation functions to print out select components of the cell state clamped between -1 and 1.*  
