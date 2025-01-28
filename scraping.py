import re

import requests
import bs4


resource = requests.get('https://www.iplocation.net/')
#print(resource.text)
#span_tag = re.findall(r'<span class="table-ip4-home">.*?</span',
                      #resource.text, re.DOTALL)
#print(span_tag[0][len('<span class="table-ip4-home">'):-len('</span')].strip())

soup = bs4.BeautifulSoup(resource.text, features='lxml')
span_ip = soup.find('span',class_='table-ip4-home')
print(span_ip.text.strip())
