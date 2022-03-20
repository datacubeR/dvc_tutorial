import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

from config import Config

import yaml

with open('params.yaml') as file:
    params = yaml.safe_load(file)['train']

Config.MODELS_PATH.mkdir(parents=True, exist_ok=True)

X_train = pd.read_csv(Config.FEATURES_PATH / 'train_features.csv')
y_train = pd.read_csv(Config.FEATURES_PATH / 'train_labels.csv')

model = LogisticRegression(C = params['C'], max_iter=params['max_iter'], random_state=Config.RANDOM_SEED)
model.fit(X_train, y_train.to_numpy().ravel())

joblib.dump(model, Config.MODELS_PATH / params['model_name'])
