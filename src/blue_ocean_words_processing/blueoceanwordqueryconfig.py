import os

from configs.config import Config


class BlueOceanWordQueryConfig:
    # 标题字数
    TITLE_LENGTH = 10
    # 搜索人气
    SEARCH_POPULARITY = 500
    # 在线商品数
    ONLINE_GOODS_NUMBER = 20000
    # 转化率
    CONVERSION_RATE = 0.01
    # 直通车
    SUBWAY_REFERENCE_PRICE = 2
    # 天猫占比
    TIANMAO_RATE = 0.4

    WORD_ROOT_FILE = os.path.join(Config.BLUE_OCEAN_WORDS_PROCESSING_FOLDER, 'word_root.txt')
    OUTPUT_FOLDER = os.path.join(Config.BLUE_OCEAN_WORDS_PROCESSING_FOLDER, 'output')
    RAW_DATA_FOLDER = os.path.join(Config.BLUE_OCEAN_WORDS_PROCESSING_FOLDER, 'raw_data')
