import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.360doc.com/content/15/0408/11/22483181_461495582.shtml'

result = requests.get(url)
result.encoding = 'utf-8'
soup = BeautifulSoup(result.text, 'lxml')
contents = soup.find_all('p')
for content in contents:
    print(re.findall(r'\d、{.*?}:', content, re.S))

