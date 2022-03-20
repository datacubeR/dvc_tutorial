import pandas as pd

from config import Config
import yaml

with open('params.yaml') as file:
    params = yaml.safe_load(file)['features']


Config.FEATURES_PATH.mkdir(parents=True, exist_ok=True)

train_df = pd.read_csv(Config.DATASET_PATH / 'train.csv')
test_df = pd.read_csv(Config.DATASET_PATH / 'test.csv')


def featurize(df):
    df.query('Tm != "TOT"', inplace = True)
    X = df.drop(columns = params['remove'])
    y = df.Pos
    
    return X,y 

X_train, y_train = featurize(train_df)
X_test, y_test = featurize(test_df)

X_train.to_csv(Config.FEATURES_PATH / 'train_features.csv', index = None)
X_test.to_csv(Config.FEATURES_PATH / 'test_features.csv', index = None)

y_train.to_csv(Config.FEATURES_PATH / 'train_labels.csv', index = None)
y_test.to_csv(Config.FEATURES_PATH / 'test_labels.csv', index = None)
