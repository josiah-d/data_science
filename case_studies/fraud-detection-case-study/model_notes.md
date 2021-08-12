# The Data

This data is **very confidential**. Please take care to not share it outside of Galvanize! 

Training data is in `data/data.zip`. You can uncompress the data file with this command: `unzip data.zip`.

You will need to use this data set to train models, perform model selection, and validate your choices. 

This is event data and your goal is to determine if a record is fraudulent. Start by taking a look at the data. 

What do these columns mean? Many of them won't be useful for you, so a big part of the task is feature identification and extraction. You can use Beautiful Soup and NLP techniques to get features out of the description column.

The label is derived from the `acct_type` feature. There are a few different possibilities for this value, but all we care about is fraud or not fraud. If the `acct_type` field contains the word `fraud`, label that data point as `fraud`. Otherwise, `not fraud`. 


# Build your model

Build a really dumb model first as your baseline.  This serves two purposes:

  - The dumb model serves as a baseline for comparison.  Potential improvements must improve on the baseline to be considered.
  - The dumb model serves as a stub component for code development.  If your team is working in parallel on modeling and infrastructure, you can decide on an interface, and then use that interface for your dumb model.  This gives your infrastructure team a working example to use.

The last point is especially important, please reflect upon it and digest.


# Saving your model

After some exploratory analysis, you'll land on a model you're happy with (or is at least good enough). It's okay if some of your exploratory analysis code isn't pretty, but your production code which interfaces with your dashboard model building code should be maintainable.

Now we'd like to build the model once and save it so we do not have to repeat the time consuming process of transformation and training. We can save python objects with the `pickle` module.

Here's how you can do some pickling:

```python
import numpy as np
import pickle

class MyModel():

    def fit():
        pass

    def predict_proba():
        return np.random.uniform()


def get_data(datafile):
    ....
    return X, y

if __name__ == '__main__':
    X, y = get_data('data/data.json')
    model = MyModel()
    model.fit(X, y)
    with open('model.pkl', 'wb') as f:
        # Write the model to a file.
        pickle.dump(model, f)
```

Now I can reload the model from the pickle file and use it to predict! No need to retrain :)

```python
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

model.predict_proba(...)
```
