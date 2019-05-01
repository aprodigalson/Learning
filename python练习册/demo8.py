from bs4 import BeautifulSoup
import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response.read(), 'html.parser')
print(soup.body.text)

# demo9
links = soup.findAll('a')
for link in links:
    print(link['href'])
