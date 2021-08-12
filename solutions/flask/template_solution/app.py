from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Form page to submit text
@app.route('/')
def submission_page():
    return render_template('index.html')

# My prediction app
@app.route('/prediction', methods=['POST'] )
def predict():
    with open("model.pkl", 'rb') as f:
        model = pickle.load(f)
        X = np.array([request.form['sepal_length'],
                      request.form['sepal_width'],
                      request.form['petal_length'],
                      request.form['petal_width']]).astype(float).reshape(1, -1)
        probs = model.predict_proba(X)
    page = f'''Predicted probabilities:
    <table>
        <tr><th>species</th><th>probability</th></tr>
        <tr><td>iris setosa</td><td>{probs[0][0]:.2f}</td></tr>
        <tr><td>iris versicolor</td><td>{probs[0][1]:.2f}</td></tr>
        <tr><td>iris virginica</td><td>{probs[0][2]:.2f}</td></tr>
    </table>'''

    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
