from pathlib import Path
import yaml

with open('params.yaml') as file:
    params = yaml.safe_load(file)

class Config:
    RANDOM_SEED = params['base']['random_seed']
    ASSETS_PATH = Path('./assets')
    FILE_PATH = ASSETS_PATH / 'original_data' / params['data']['file_name']
    DATASET_PATH = ASSETS_PATH / 'data' 
    FEATURES_PATH = ASSETS_PATH / 'features'
    MODELS_PATH = ASSETS_PATH / 'models'
    METRICS_PATH = ASSETS_PATH / 'metrics.json'