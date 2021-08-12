# Flask assignment solutions

For this assignment you will turn create a website using flask based on a machine-learning problem, ideally your capstone project.

The solutions are bare-bones websites using a predictive model based on the iris dataset. The user can enter the dimensions of the flower and the app will return the probability it is each of three different species. In each case the model is a random-forest classifier. The websites are fairly similar. None are pretty.

They differ in the approach to web-programming. The first (in `template_solution/`) uses jinja2 templates and web forms, so when the user clicks the button a POST request is made to return a new page. This doesn't require as much understanding of web programming, but is limited and is an outdated approach, far from how web programming is done today. It's a good approach if you don't expect to do more than this.

The second (in `javascript_solution/`) uses javascript, jQuery, and Ajax. When the user clicks the button a javascript function runs on the browser to find the value of the relevant fields and send them back to the server as json. The server sends back the probabilities (rather than a whole new page) and another javascript function puts those in a table. This is best if you are comfortable with web technologies, know a little about javascript,  and want more than just a simple prediction.

The third solution (in `brython_solution/`) is similar, but rather than javascript uses a version of python called [brython](https://brython.info/) that is converted to javascript on the fly in the browser. This may be more accessible if you don't have the time to learn a new language but want to make a powerful website.

To run any of the solutions, first go to the appropriate directory and run `python fit_model.py`. That will create a pickled model (`model.pkl`). Then run `python app.py` and go to `localhost:8080` on your browser.