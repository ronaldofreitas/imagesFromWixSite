

from bs4 import BeautifulSoup
import requests

url = 'http://bobinex.com.br/images/produtos/'
ext = 'iso'

def listFD(url, ext=''):
    page = requests.get(url).text
    print page
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

source= listFD(url, ext)
#for file in listFD(url, ext):
    #print file


start_sep='src=\"'
end_sep=".jpg\""

result=[]
imagens=[]
tmp=source.split(start_sep)
for par in tmp:
  if end_sep in par:
    result.append(par.split(end_sep)[0])

for line in result:
	imagens.append(line + '.jpg')


'''
import re
import requests
from bs4 import BeautifulSoup

site = 'http://bobinex.com.br/produtos/papel-de-parede/infantario'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
'''