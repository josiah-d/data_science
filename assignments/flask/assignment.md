# Flask

## Introduction

In this assignment you will create a flask application based on your capstone project. This is an open-ended continuation of your work that you are encouraged to continue past this assignment; the steps below are recommendation. All work should be done in the repository for your capstone project, not here.

## Basic

### Part 1: Build a trivial flask app

1. Create a directory called `app`  containing a `.py` file with a flask application. It should have a route for `/`  that  returns a minimal HTML page from the `templates` directory using `render_template`. Run the app and verify it works.

2. Add some content to the HTML relevant to your capstone. Add a title, headers, some text about your project, and an image (located in the `static` directory).

### Part 2: Plan your app

1. Choose something interactive from your project. If you wrote a predictive model, the input might be a data point and the output a target or probability of a label. If it classifies images, imagine inputting an image and returning a label. Recommenders should recommend based on inputs.

Now take whatever idea you had and make it simpler.

2. Save the model used in your app as a pickle file.

3. If your simplified plan has input fields, add these to your template, giving them `id` attributes. If it has outputs, add tags for those. Add a submit button. If you're using forms, place this inside a FORM element.

## Advanced

### Part 3: Connect your app to the model

1. Following the approach in the lecture or the solutions, write the server-side code to load your model, make a prediction, and return the results. Update the template, either adding javascript or brython, or having the form point to the appropriate location.

### Part 4: Make it less simple

Go back to your original idea. Can you make the website do a little more?

### Part 5: Make it pretty

Add CSS or bootstrap to make the formatting more attractive. Add additional text to explain your project. Turn it into something you might show a potential employer.

## Extra Credit

### Part 6: Put it on AWS

Put the app on an AWS server. Make sure to open the appropriate ports so users can access it. Create an Elastic IP and a domain name.

