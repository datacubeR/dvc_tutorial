import json

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


from config import Config

X_test = pd.read_csv(Config.FEATURES_PATH / 'test_features.csv')
y_test = pd.read_csv(Config.FEATURES_PATH / 'test_labels.csv')

model = joblib.load(Config.MODELS_PATH / 'model.joblib')
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:,1]

output = dict( test_accuracy = accuracy_score(y_test, y_pred),
    test_recall = recall_score(y_test, y_pred, average='macro'))

with open(Config.METRICS_PATH, 'w') as outfile:
    json.dump(output, outfile)

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix for NBA Positions.")
plt.xlabel("Posiciones Predichas")
plt.ylabel("Posiciones Reales")
plt.savefig('conf_mat.png')