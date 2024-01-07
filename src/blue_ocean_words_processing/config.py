import os
import re

from configs.config import Config


class BlueOceanWordQueryConfig:
    # 标题字数
    TITLE_LENGTH = 10
    # 搜索人气
    SEARCH_POPULARITY = 500
    # 在线商品数
    ONLINE_GOODS_NUMBER = 10000
    # 转化率
    CONVERSION_RATE = 0.01
    # 直通车
    SUBWAY_REFERENCE_PRICE = 1.5
    # 天猫占比
    TIANMAO_RATE = 0.8

    WORD_ROOT_FILE = os.path.join(Config.BLUE_OCEAN_WORDS_PROCESSING_FOLDER, 'word_root.txt')
    OUTPUT_FOLDER = os.path.join(Config.BLUE_OCEAN_WORDS_PROCESSING_FOLDER, 'output')
    RAW_DATA_FOLDER = os.path.join(Config.BLUE_OCEAN_WORDS_PROCESSING_FOLDER, 'raw_data')
    RESULT_FILE_NAME = os.path.join(OUTPUT_FOLDER, 'output.xlsx')

    FORBIDDEN_WORDS = re.compile(r'三只松鼠|apm|美团|会员|香奈儿|西太后|成人|最|火影忍者|周大福')
