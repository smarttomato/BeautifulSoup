#抓取平凡的世界内容

import requests
from bs4 import BeautifulSoup
import re

folder_path = '/home/zhangzhimeng/github/BeautifulSoup/'
url = 'http://www.pingfandeshijie.net/di-'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
part_info = ['yi', 'er', 'san']
chapter_info = range(1, 55)
for part in part_info:
    for chapter in chapter_info:
        current_url = url + part + '-bu-' + str('%02d' % chapter) + '.html'
        result = requests.get(current_url, headers=headers)
        result.encoding = 'utf-8'
        soup = BeautifulSoup(result.text, 'lxml')
        h1 = soup.find('h1')
        print(h1.get_text())
        p = soup.find_all('p')
        for k in p:
            print(k.get_text())
            if '下一章' in k.get_text():
                break
            content = k.get_text()
            if re.match('第一部', h1.get_text()):
                with open(folder_path + '第一部.txt', 'a+') as f:
                    f.write(content + '\n')
            elif re.match('第二部', h1.get_text()):
                with open(folder_path + '第二部.txt', 'a+') as f:
                    f.write(content + '\n')
            elif re.match('第三部', h1.get_text()):
                with open(folder_path + '第三部.txt', 'a+') as f:
                    f.write(content + '\n')





