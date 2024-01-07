import logging
import re

from blue_ocean_words_processing.config import BlueOceanWordQueryConfig

logger = logging.getLogger(__name__)


def sort_data(data):
    logger.info('Sorting data...')
    data.sort(key=lambda x: x[1], reverse=True)


def basic_processing(raw_data):
    logger.info('Start basic processing...')
    data = list()
    titles = list()
    for row in raw_data:
        temp = list()

        # 标题字数卡点
        if len(row[0]) > BlueOceanWordQueryConfig.TITLE_LENGTH or \
                re.search(BlueOceanWordQueryConfig.FORBIDDEN_WORDS, row[0]) or row[0] in titles:
            continue
        titles.append(row[0])
        temp.append(row[0])

        # 搜索人气卡点
        if (search_popularity := float(row[1])) < BlueOceanWordQueryConfig.SEARCH_POPULARITY:
            continue
        temp.append(round(search_popularity, 2))

        # 在线商品数卡点
        if row[13] == '-':
            temp.append(0)
        elif (online_words := int(row[13])) > BlueOceanWordQueryConfig.ONLINE_GOODS_NUMBER:
            continue
        else:
            temp.append(online_words)

        # 直通车参考价卡点
        if row[9] == '-':
            temp.append(0)
        elif (subway_price := float(row[9])) > BlueOceanWordQueryConfig.SUBWAY_REFERENCE_PRICE:
            continue
        else:
            temp.append(round(subway_price, 2))

        # 支付转化率卡点
        if row[10] == '-':
            temp.append(0)
        elif (conversion_rate := float(row[10].replace('%', '')) / 100) < BlueOceanWordQueryConfig.CONVERSION_RATE:
            continue
        else:
            temp.append(round(conversion_rate, 2))

        # 猫店占比卡点
        if row[11] == '-':
            temp.append(0)
        elif (tianmao_rate := float(row[11].replace('%', ''))) / 100 > BlueOceanWordQueryConfig.TIANMAO_RATE:
            continue
        else:
            temp.append(round(tianmao_rate, 2))

        data.append(temp)
    logger.info('Finished processing.')
    return data


def run(raw_data):
    logger.info('Starting process blue ocean words...')
    data = basic_processing(raw_data=raw_data)
    sort_data(data=data)
    logger.info('Finished processing blue ocean words.')
    return data


if __name__ == '__main__':
    run()
