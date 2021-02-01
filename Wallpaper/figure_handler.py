import requests
from bs4 import BeautifulSoup as bs
import re
import os
from datetime import datetime

URL = 'https://www.bing.com/'
img_path = './Wallpaper/assets/images/'

def get_figure_name():
    bing_html = requests.get(URL)
    soup = bs(bing_html.text, 'html.parser')
    figures = soup.find('div', class_= 'img_cont')
    figure_content = figures['style']
    name = re.search('(?<=id=)[0-9a-zA-Z._-]*', figure_content)
    name = name.group(0)
    texts = name.split('_')
    name = texts[0] + '_' + texts[1]
    name = 'https://cn.bing.com/th?id=' + name + '_UHD.jpg'
    return name

def releaseSpace():
    files = os.listdir(img_path)
    if len(files) > 90:
        os.remove(img_path + files[0])
    print(files)

def download(img_url):
    print(os.getcwd())
    img = requests.get(img_url)
    now = datetime.now()
    time = now.strftime("%Y%m%d")
    with open(img_path + time + '.jpg','wb') as f:
        f.write(img.content)
