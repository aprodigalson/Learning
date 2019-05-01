import os
import requests
from pyquery import PyQuery


class DownLoadImage(object):
    def __init__(self):
        self.urls = list()
        self.url = 'http://tieba.baidu.com/p/2166231880'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) Chrome/59.0.3071.109 Safari/537.36'
        }
        self.s = requests.session()
        self.s.headers.update(self.headers)

    def get_image_url(self):
        response = self.s.get(self.url)
        doc = PyQuery(response.content.decode())
        images = doc.find('img.BDE_Image')
        for img in images.items():
            self.urls.append(img.attr('src'))

    def save(self):
        directory = 'picture'
        if not os.path.exists(directory):
            os.mkdir(directory)
        for i in range(len(self.urls)):
            url = self.urls[i]
            response = self.s.get(url)
            filename = directory + '/' + 'img' + str(i) + '.jpg'
            with open(filename, 'wb') as file:
                file.write(response.content)

    def download(self):
        self.get_image_url()
        self.save()


d = DownLoadImage()
d.download()
