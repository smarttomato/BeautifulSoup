import requests
import json
from bs4 import BeautifulSoup
import os

part_one_path = '/home/zhangzhimeng/github/BeautifulSoup/three bodies/第一部/'
part_two_path = '/home/zhangzhimeng/github/BeautifulSoup/three bodies/第二部/'
part_three_path = '/home/zhangzhimeng/github/BeautifulSoup/three bodies/第三部/'


def get_contents():
    for i in range(282, 318):
        url = 'http://www.shizongzui.cc/santi/' + str(i) + '.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        bs = BeautifulSoup(response.text, 'lxml')
        title = bs.find_all('h1')
        content = bs.find('div', attrs={'class': 'bookcontent clearfix'})
        content = str(content).replace('<br/>', '\n')
        bs1 = BeautifulSoup(content)
        content = bs1.text
        if os.path.exists(part_one_path):
            with open(part_one_path+title[1].get_text()+'.txt', 'w') as f:
                f.write(content)
                print(str(i)+':finished')
        else:
            os.mkdir(part_one_path)
            with open(part_one_path+title[1].get_text()+'.txt', 'w') as f:
                f.write(content)

    for j in range(318, 368):
        url = 'http://www.shizongzui.cc/santi/' + str(j) + '.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        bs = BeautifulSoup(response.text, 'lxml')
        title = bs.find_all('h1')
        content = bs.find('div', attrs={'class': 'bookcontent clearfix'})
        content = str(content).replace('<br/>', '\n')
        bs1 = BeautifulSoup(content)
        content = bs1.text
        if os.path.exists(part_two_path):
            with open(part_two_path+title[1].get_text()+'.txt', 'w') as f:
                f.write(content)
                print(str(j)+':finished')
        else:
            os.mkdir(part_two_path)
            with open(part_two_path+title[1].get_text()+'.txt', 'w') as f:
                f.write(content)
    for k in range(368, 417):
        url = 'http://www.shizongzui.cc/santi/' + str(k) + '.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        bs = BeautifulSoup(response.text, 'lxml')
        title = bs.find_all('h1')
        content = bs.find('div', attrs={'class': 'bookcontent clearfix'})
        content = str(content).replace('<br/>', '\n')
        bs1 = BeautifulSoup(content)
        content = bs1.text
        if os.path.exists(part_three_path):
            with open(part_three_path + title[1].get_text() + '.txt', 'w') as f:
                f.write(content)
                print(str(k) + ':finished')
        else:
            os.mkdir(part_three_path)
            with open(part_three_path + title[1].get_text() + '.txt', 'w') as f:
                f.write(content)


if __name__ == '__main__':
    get_contents()
