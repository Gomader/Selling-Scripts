import os

import pandas as pd

from blue_ocean_words_processing.config import BlueOceanWordQueryConfig


def read_raw_files():
    data = None
    for filename in os.listdir(BlueOceanWordQueryConfig.RAW_DATA_FOLDER):
        if filename.endswith('csv'):
            if data is not None:
                data._append(pd.read_csv(os.path.join(BlueOceanWordQueryConfig.RAW_DATA_FOLDER, filename),
                                         encoding='utf-8'))
            else:
                data = pd.read_csv(os.path.join(BlueOceanWordQueryConfig.RAW_DATA_FOLDER, filename),
                                   encoding='utf-8')
    return data


if __name__ == '__main__':
    read_raw_files()
