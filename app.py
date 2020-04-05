from flask import Flask, request, jsonify
import numpy as np
import pickle as p


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)


if __name__ == '__main__':
    model1 = p.load(open('rf_model_1.pickle', 'rb'))
    model2 = p.load(open('rf_model_2.pickle', 'rb'))
    model3 = p.load(open('rf_model_3.pickle', 'rb'))
    app.run(debug=True, host='0.0.0.0')
