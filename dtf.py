import json
import requests
import bs4

from fake_headers import Headers


def get_fake_headers():
    return Headers(browser='chrome', os='mac').generate()


response = requests.get('https://dtf.ru/games', headers=get_fake_headers())
soup = bs4.BeautifulSoup(response.text, features='lxml')
news_list = soup.findAll('div', class_='content--short')

parsed_data = []
for news in news_list:
    article_link = news.find('a', class_='content__link')['href']
    response = requests.get(f'https://dtf.ru{article_link}', headers=get_fake_headers())
    article = bs4.BeautifulSoup(response.text, features='lxml')
    title = article.find('h1').text
    time = article.find('time')['datetime']
    text = article.find('article', class_='content__blocks').text

    parsed_data.append({
        'title': title,
        'time': time,
        'link': f'https://dtf.ru{article_link}',
        'text': text,
    })

with open('articles.json', 'w') as f:
    f.write(json.dumps(parsed_data, ensure_ascii=False, indent=4))
 # код ложиться конкретно на последней строчке " ensure_ascii=False, indent=4))" если это не вводить ответ не коректно отображается но работает