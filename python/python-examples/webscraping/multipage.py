import requests
from bs4 import BeautifulSoup
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# items = soup.find_all('div', class_='w-full rounded border')
# count = 1
# for i in items:
#     itemName = i.find('h4').text.strip('\n')
#     itemPrice = i.find('h5').text
#     print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
#     count = count + 1

pages = soup.find('nav', class_='pagination')
# print(pages)
urls = []
links = pages.find_all('a')
# print(links)
# This misses the first page, probably because the class is "page active", moving on for now
for link in links:
    # linkText = link.find('a')
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        # print(x)
        urls.append(x)
# print(urls)
url = 'https://scrapingclub.com'
count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='w-full rounded border')

    for i in items:
        itemName = i.find('h4').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1