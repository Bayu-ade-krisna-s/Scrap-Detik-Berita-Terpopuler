import pandas as pd
import requests
from bs4 import BeautifulSoup

title = []
date = []
link = []

url = 'https://www.detik.com/terpopuler/news?utm_source=detiknews&utm_medium=desktop'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

container = soup.find_all('h3',{'class':'media__title'})

url = []
for item in container:
    url.append(item.find('a').get('href'))

for i in url:
  response = requests.get(i)
  soup = BeautifulSoup(response.content,'html.parser')

  try:
    title.append(soup.find('h1',{'class':'detail__title'}).get_text().replace('\n        ',''))
  except:
    title.append('')
  try:
    date.append(soup.find('div',{'class':'detail__date'}).get_text())
  except:
    date.append('')
  try:
    link.append(soup.find('link',{'rel':'amphtml'}).get('href'))
  except:
    link.append('')


output = {
    "Title":title,
    "Date" :date,
    "Link" :url
}

df = pd.DataFrame(output)
df.to_csv('scrap-detik-berita-terpopuler.csv',index=False)