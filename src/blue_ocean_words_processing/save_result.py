import logging
import os

import pandas as pd

from blue_ocean_words_processing.config import BlueOceanWordQueryConfig

logger = logging.getLogger(__name__)


def save_result(data):
    logger.info("Saving results...")
    if os.path.exists(BlueOceanWordQueryConfig.RESULT_FILE_NAME):
        logger.info('Result file exists, deleting...')
        os.remove(BlueOceanWordQueryConfig.RESULT_FILE_NAME)

    title = list()
    search_popularity = list()
    online_words = list()
    subway_price = list()
    conversion_rate = list()
    tianmao_rate = list()

    for row in data:
        title.append(row[0])
        search_popularity.append(row[1])
        online_words.append(row[2])
        subway_price.append(row[3])
        conversion_rate.append(row[4])
        tianmao_rate.append(row[5])

    df = pd.DataFrame({
        '搜索词': title, '搜索人气': search_popularity, '在线商品数': online_words,
        '直通车参考价': subway_price, '转化率': conversion_rate, '猫店占比': tianmao_rate
    })

    df.to_excel(BlueOceanWordQueryConfig.RESULT_FILE_NAME, index=False)
    logger.info('Save results finished.')
