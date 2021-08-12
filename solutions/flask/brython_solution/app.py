from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Form page to submit text
@app.route('/')
def submission_page():
    return render_template('index.html')


@app.route('/predict', methods=['POST'] )
def predict():
    user_data = request.json

    with open("model.pkl", 'rb') as f:

        model = pickle.load(f)
        X = np.array([user_data['sepal_length'],
                      user_data['sepal_width'],
                      user_data['petal_length'],
                      user_data['petal_width']]).astype(float).reshape(1, -1)
        probs = model.predict_proba(X)

        return jsonify({'setosa': probs[0][0],
                        'versicolor': probs[0][1],
                        'virginica': probs[0][2]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
