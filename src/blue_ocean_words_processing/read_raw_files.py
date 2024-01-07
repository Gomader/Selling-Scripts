import csv
import logging
import os

from tqdm import tqdm

from blue_ocean_words_processing.config import BlueOceanWordQueryConfig

logger = logging.getLogger(__name__)


def read_raw_files():
    logger.info('Reading raw data files...')
    data = list()
    for filename in tqdm(os.listdir(BlueOceanWordQueryConfig.RAW_DATA_FOLDER), desc='Reading raw data files...'):
        if filename.endswith('csv'):
            with open(os.path.join(BlueOceanWordQueryConfig.RAW_DATA_FOLDER, filename), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                data.extend(list(reader)[1:])
    logger.info('Finished reading raw data files.')
    return data


if __name__ == '__main__':
    read_raw_files()
