## Premise
You are a contract data scientist/consultant hired by a new e-commerce site to try to weed out fraudsters.  The company unfortunately does not have much data science expertise... so you must properly scope and present your solution to the manager before you embark on your analysis.  Also, you will need to build a sustainable software project that you can hand off to the companies engineers by deploying your model in the cloud.  Since others will potentially use/extend your code you **NEED** to properly encapsulate your code and leave plenty of comments.

## The Data
#### NOTE: This data is VERY sensitive!

It is located in `data/data.zip`.

***Do not share this data with anyone! Do not include the data file in your pull request!***

You will be required to work on the project on campus.


### Deliverables 
* Scoping document (in Markdown)
* Code on private fork of repo on Github
    * proper functions/encapsulation
    * well commented
    * Model description document (see below)
* Flask app with well documented API
    * Needs to query live data from our server (see step 6 below) 
    * Needs to accept input records on POST `/score` endpoint
* Web based front-end to enable quick triage of potential fraud
    * Triage importance of transactions (low risk, medium risk, high risk)
    * Extra: D3 based visualization of data/trend


### The "product" of fraud
Something that you will need to think about throughout this case study is how the product of your client fits into the given technical process.  A few points to note about the case of fraud:

* Failures are not created equal
    * False positives decrease customer/user trust
    * False negatives cost money
        * Not all false negative cost the same amount of money
* Accessibility
    * Other (non-technical) people may need to interact with the model/machinery
    * Manual review

Your model will be used only the first step in the fraud identification process. You do not use the model to declare a ground truth about fraud or not fraud, but simply to flag which transactions need further manual review.  You will be building a triage model of what are the most pressing (and costly) transactions you have seen. It may also be useful to display what factors contribute to a given case being flagged as fraudulent by your model.  

## Day 1: Morning

### Step 1: EDA
Before you start building the model, start with some EDA.

#### [Deliverable]: Look at the data
Start by looking at the data.

1. Load the data with pandas. Add a 'Fraud' column that contains True or False values depending on if the event is fraud. If `acct_type` field contains the word `fraud`, label that point Fraud.

2. Check how many fraud and not fraud events you have.

3. Look at the features. Make note of ones you think will be particularly useful to you.

4. Do any data visualization that helps you understand the data.


#### [Deliverable]: Scoping the problem
Before you get cranking on your model, think of how to approach the problem.

1. What preprocessing might you want to do? How will you build your feature matrix? What different ideas do you have?

2. What models do you want to try?

3. **What metric will you use to determine success?**


### Step 2: Building the Model

#### [Deliverable]: Comparing models
Start building your potential models.

**Notes for writing code:**
* As you write your code, **always be committing** (ABC) to Github!
* Write **clean and modular code**.
* Include **comments** on every method.

*Make sure to get a working model first before you try all of your fancy ideas!*

1. If you have complicated ideas, implement the simplest one first! Get a baseline built so that you can compare more complicated models to that one.

2. Experiment with using different features in your feature matrix. Use different featurization techniques like stemming, lemmatization, tf-idf, part of speech tagging, etc.

3. Experiment with different models like SVM, Logistic Regression, Decision Trees, kNN, etc. You might end up with a final model that is a combination of multiple classification models.

4. Compare their results. Pick a good metric; don't just use accuracy!

## Day 1: Afternoon

#### [Deliverable]: Model description and code
After all this experimentation, you should end up with a model you are happy with.

1. Create a file called `model.py` which builds the model based on the training data.

    * Feel free to use any library to get the job done.
    * Again, make sure your code is **clean**, **modular** and **well-commented**! The general rule of thumb: if you looked at your code in a couple months, would you be able to understand it?

2. In a file called `report.md`, describe your project findings including:
    * An overview of a chosen "optimal" modeling technique, with:
        * process flow
        * preprocessing
        * accuracy metrics selected
        * validation and testing methodology
        * parameter tuning involved in generating the model
        * further steps you might have taken if you were to continue the project.


#### [Deliverable]: Pickled model

1. Use `pickle` to serialize your trained model and store it in a file. This is going to allow you to use the model without retraining it for every prediction, which would be ridiculous.

### Step 3: Prediction script

Take a few raw examples and store them in json or csv format in a file called `test_script_examples`.


#### [Deliverable]: Prediction script

1. Write a script `predict.py` that reads in a single example from `test_script_examples`, vectorizes it, unpickles the model, predicts the label, and outputs the label probability (print to standard out is fine).

    This script will serve as a sort of conceptual and code bridge to the web app you're about to build.

    Each time you run the script, it will predict on one example, just like a web app request. You may be thinking that unpickling the model every time is quite inefficient and you'd be right; we'll remove that inefficiency in the web app.


### Step 4: Database

#### [Deliverable]: Prediction script backed by a database

You'll want to store each prediction the model makes on new examples, which means you'll need a database.

1. Set up a Postgres or MongoDB database that will store each example that the script runs on. You should create a database schema that reflects the form of the raw example data and add a column for the predicted probability of fraud.

2. Write a function in your script that takes the example data and the prediction as arguments and inserts the data into the database.

    Now, each time you run your script, one row should be added to the `predictions` table with a predicted probability of fraud.


## Day 2: Morning

### Step 5: Web App

#### [Deliverable]: Hello World app

1. A request in your browser to `/hello` should display "Hello, World!". Set up a Flask app with a route `GET /hello` to do so. Here's an example app skeleton:

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ''' <p> nothing here, friend, but a link to 
                   <a href="/hello">hello</a> and an 
                   <a href="/form_example">example form</a> </p> '''

@app.route('/hello', methods=['GET'])
def hello_world():
    return ''' <h1> Hello, World!</h1> '''

@app.route('/form_example', methods=['GET'])
def form_display():
    return ''' <form action="/string_reverse" method="POST">
                <input type="text" name="some_string" />
                <input type="submit" />
               </form>
             '''

@app.route('/string_reverse', methods=['POST'])
def reverse_string():
    text = str(request.form['some_string'])
    reversed_string = text[-1::-1]
    return ''' output: {}  '''.format(reversed_string)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
```

Use this [tutorial](http://blog.luisrei.com/articles/flaskrest.html) to for more.

#### [Deliverable]: Fraud scoring service

1. Set up a route `POST /score` and have it execute the logic in your prediction script. You should import the script as a module and call functions defined therein.

    There are two things you'll do to make this all more efficient:

    1. Only unpickle the model once
    2. Only connect to the database once.
    
    Do both in a `if __name__ == '__main__':` block before you call `app.run()` and you can refer to these top-level global variables from within the function. This may require some re-architecting of your prediction module.

    The individual example will no longer be coming from a local file, but instead you will get it by making a request to a server that will give you a data point as a string, which you can parse into JSON. 
You can use `json.loads()` to parse a string to json, which is the reverse process of `json.dumps()`. You'll still need to vectorize it, predict, and store the example and prediction in the database.

### Step 6: Get "live" data

We've set up a service for you that will send out "live" data so that you can see that your app is really working.

To use this service, you will need to make a request to our secure server. It gives a maximum of the 10 most recent datapoints, ordered by `sequence_number`. New datapoints come in every few minutes.

*Warning: you will need to implement the save_to_database method.*

```python
class EventAPIClient:
    """Realtime Events API Client"""
    
    def __init__(self, first_sequence_number=0,
                 api_url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/',
                 api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC',
                 db = None):
        """Initialize the API client."""
        self.next_sequence_number = first_sequence_number
        self.api_url = api_url
        self.api_key = api_key
        
    def save_to_database(self, row):
        """Save a data row to the database."""
        print("Received data:\n" + repr(row) + "\n")  # replace this with your code

    def get_data(self):
        """Fetch data from the API."""
        payload = {'api_key': self.api_key,
                   'sequence_number': self.next_sequence_number}
        response = requests.post(self.api_url, json=payload)
        data = response.json()
        self.next_sequence_number = data['_next_sequence_number']
        return data['data']
    
    def collect(self, interval=30):
        """Check for new data from the API periodically."""
        while True:
            print("Requesting data...")
            data = self.get_data()
            if data:
                print("Saving...")
                for row in data:
                    self.save_to_database(row)
            else:
                print("No new data received.")
            print(f"Waiting {interval} seconds...")
            time.sleep(interval)


# Usage Example

client = EventAPIClient()
client.collect()
```

1. Write a function that periodically fetches new data, generates a predicted fraud probability, and saves it to your database (after verifying that the data hasn't been seen before).

**Make sure your app is adding the examples to the database with predicted fraud probabilities.**

## Day 2: Afternoon

### Step 7: Dashboard

#### [Deliverable]: Web front end to present results

You want to present potentially fraudulent transactions with their probability scores from your model. The transactions should be segmented into 3 groups: low risk, medium risk, or high risk (based on the probabilities).

* Add route in Flask app for a dashboard
* Read data from postgres/mongodb
* Return HTML with the data
    * To generate the HTML from the json data from the database, either just use simple string concatenation or Jinja2 templates.


### Step 8: Deploy!

Use [these instructions](https://github.com/GalvanizeDataScience/project-proposals/blob/master/host_app_on_amazon.md) as your guide if you need one.


* Set up AWS instance
* Set up environment on your EC2 instance
* Push your code to github
* SSH into the instance and clone your repo
* Run Flask app on instance 
* Make it work (debug, debug, debug)
* Profits!


### Extra

* Make your dashboard interactive. Allow a dashboard user to clear or flag fraud events. Come up with other features that might be useful.

* Create a D3 visualization for your web based frontend.  You might want to visualize any number of metrics/data.  Use your creativity to create something that makes sense for a end user in terms of what data you present.
