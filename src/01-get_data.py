import gdown
import pandas as pd
from sklearn.model_selection import train_test_split

from config import Config

Config.FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
Config.DATASET_PATH.mkdir(parents=True, exist_ok=True)

gdown.download(
    'https://drive.google.com/uc?id=1rwnNapcxlPM_DrYwBPSEC9uWVyEy70D1',
    str(Config.FILE_PATH)
)

nba_df = pd.read_csv(Config.FILE_PATH, encoding='latin-1', sep = ';')

train_df, test_df = train_test_split(nba_df, test_size=0.25, random_state=Config.RANDOM_SEED)

train_df.to_csv(Config.DATASET_PATH / 'train.csv', index = None)
test_df.to_csv(Config.DATASET_PATH / 'test.csv', index = None)
