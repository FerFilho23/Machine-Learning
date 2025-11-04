import pickle
from pathlib import Path
from flask import Flask, request, jsonify

app = Flask('churn_prediction')

# Load the model
C = 1.0
models_dir = Path(__file__).resolve().parent / 'models'
models_dir.mkdir(exist_ok=True)
model_file = models_dir / f'model_C={C}.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
    print('Loaded model from', model_file)
    
@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    churn = y_pred >= 0.5
    
    result = {
        'churn_probability': float(y_pred[0]),
        'will_churn': bool(churn[0])
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)