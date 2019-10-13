# import time
import pymongo
import re
import os
import requests
from urllib.parse import urlencode
from config import *
# from json.decoder import JSONDecodeError
from hashlib import md5
from multiprocessing import Pool

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]


def get_page(offset, keyword):
    """
    获取网页功能
    :param offset: 
    :param keyword: 
    :return: 
    """
    # 构建头信息
    headers = {
        'authority': 'www.toutiao.com',
        'cookie': 'csrftoken=42fe0d3ed62ce1864f9e93d188b8216c; tt_webid=6745417947265140236; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6745417947265140236; s_v_web_id=2d5cd7dc47c10cb9a807857623b95e4f; __tasessionId=09n44ztnq1570873949244',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # timestamp = int(round(time.time() * 1000))
    # print(timestamp)获取时间戳
    # 构建参数
    data = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': '0',
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',

    }
    base = 'https://www.toutiao.com/api/search/content/?'
    url = base + urlencode(data)
    try:
        # verify：证书验证
        response = requests.get(url=url, headers=headers)

        if response.status_code == requests.codes.ok:
            # 返回爬取的内容
            # print(response.json())
            return response.json()
    except requests.ConnectionError as e:
        print('Error occurred', e.args)
    return None


def get_images(text):
    """
    解析网页内容
    :param text: 
    :return: 
    """
    if text.get('data'):
        datas = text.get('data')
        for data in datas:
            if not data.get('title'):
                continue
            # 获取标题
            title = re.sub('[\t]', '', data.get('title'))
            if not data.get('image_list'):
                continue
            # 获取图片列表
            images = data.get('image_list')

            for image in images:
                # 构造图的url，将缩略图改为大图
                if 'pgc-image' in image.get('url'):
                    origin_image = re.sub('list.*?pgc-image', 'large/pgc-image', image.get('url'))
                else:
                    origin_image = re.sub('list', 'large', image.get('url'))
                # 返回生成器，包括标题与图片url
                yield {
                    'image': origin_image,
                    'title': title,
                }


def save_image(item):
    """
    保存图片功能
    :param item: 
    :return: 
    """
    if not item.get('image'):
        return
    # 图片路径
    image_path = os.path.join('image_壁纸', item.get('title'))
    if not os.path.exists(image_path):
        try:
            # 有的文章标题做目录不合法
            os.makedirs(image_path)
        except OSError as e:
            print("error:", e.args)
    try:
        res = requests.get(item.get('image'))
        if requests.codes.ok == res.status_code:
            # 存储路径
            file_path = os.path.join(image_path, '{file_name}.{file_suffix}'.format(
                file_name=md5(res.content).hexdigest(),
                file_suffix='jpg'
            ))
            # 写入图片
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(res.content)
                print('Dowloaded image: ', file_path)
            else:
                print('Already Downloaded image: ', file_path)
    except Exception as e:
        print('Error:', e.args)


def save_image_mongo(result):
    """
    保存到mongodb中
    :return: 
    """
    if db[MONGO_TABLE].insert(result):
        print('Successfully Saved to Mongo', result)
        return True
    return False


def main(offset):
    # keyword = '街拍'
    text = get_page(offset, KEYWORD)
    if text == None:
        return
    # 循环导出图集
    for image in get_images(text):
        # print("1")
        # save_image(image)
        save_image_mongo(image)


def run():
    # 构建翻页功能
    # page_start = 0
    # page_end = 1
    groups = (x * 20 for x in range(GROUP_START, GROUP_END + 1))
    # 多进程爬取
    pool = Pool()
    pool.map(main, groups)
    pool.close()
    pool.join()


if __name__ == '__main__':
    run()
