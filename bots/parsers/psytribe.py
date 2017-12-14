import base64
import copy
import psycopg2
import json
import time
import datetime
from urllib.error import HTTPError
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import pandas as pd
import config
from grab import Grab
from grab.spider import Task, Spider

class PsyTribeSpider(Spider):
    """Somesite parser."""

    base_url = "http://psytribe.org"
    initial_urls = [base_url + "/"]
    upload_dir = "static/images/"


    def task_initial(self, grab, task):  # pylint: disable=unused-argument
        """Initial task."""
        print("Loaded psytribe main page")
        for elem in grab.doc.select(config.Psytribe.event_path):
            info = {}
            link = elem.select(config.Psytribe.link_path).text()
            date = elem.select(config.Psytribe.date_path).text()
            img_path = elem.select(config.Psytribe.img_path).text()
            title = elem.select(config.Psytribe.title_path).text()
            info['link'] = self.base_url + link
            info['date'] = date
            info['title'] = title
            info['img'] = self.base_url + img_path
            yield Task('load_info', url=self.base_url + link,
                        info=copy.deepcopy(info))


    def task_load_info(self, grab,          # pylint: disable=unused-argument
                       task, **kwargs):     # pylint: disable=unused-argument
        """ Обработка собственно карточки """
        time.sleep(1)
        info_list = {}
        html = self.load_content(task.info.get('link'))
        img_path = self.upload_image(task.info.get('img'))
        date = self.format_date(task.info.get('date'))
        info_list['title'] = task.info.get('title')
        info_list['date'] = date
        info_list['image'] = img_path
        info_list['link'] = task.info.get('link')
        info_list['content'] = html
        info_list['author'] = "parser"
        info_list['tags'] = json.dumps([config.Psytribe.tag])
        info_list['published'] = False
        info_list['price'] = "none"
        print(info_list)

      
    @staticmethod
    def format_img_path(img_path):
        """Format image path."""
        img_info = {}
        splited = img_path.split(".")
        #get extension
        ext = splited[len(splited)-1]
        name = str(base64.b64encode(img_path.encode('utf-8')))
        img_info['ext'] = ext
        # срезаем лишние символы
        img_info['name'] = name[2:-3]
        return img_info


    def check_date(self, date):
        """Check date is valid."""
        splited = date.split('-')
        if len(splited) < 1:
            print('fuck u')
            return

        dotted = splited[1].split('.')
        if len(dotted) < 2:
            print("There is less then two items in list", dotted)
            return

        dotted.pop(0)
        dotted.insert(0, splited[0])
        return self.create_date(dotted)


    @staticmethod
    def create_date(date_list):
        """Create date from list with length = 3"""
        date_list.reverse()
        date_string = date_list[0] + "-" + date_list[1] + "-" + date_list[2]
        date = pd.to_datetime(date_string)
        return date


    def format_date(self, date):
        """Date format."""
        splited = date.split(' ')
        if len(splited) > 1:
            for item in splited:
                dotted = item.split('.')
                if len(dotted) < 2:
                    print("There is less then two items in list", dotted)
                    return
                return self.create_date(dotted)
        else:
            return self.check_date(date)


    def load_content(self, url):
        """Load content from url"""
        grabber = Grab()
        grabber.go(url)
        html = grabber.doc.select(config.Psytribe.article_path).html()
        return self.clear_html(html)


    @staticmethod
    def clear_html(html):
        """Clear unnecessary tags"""
        soup = BeautifulSoup(html, "html.parser")
        for iframe in soup.findAll('iframe'):
            iframe.decompose()
      
        for link in soup.findAll('a', 'bbc_link'):
            link.decompose()

        return str(soup)



    def upload_image(self, img_path):
        """Upload image to dir."""
        img_info = self.format_img_path(img_path)
        target_path = (self.upload_dir +
                       config.Psytribe.tag +
                       "_" +
                       img_info.get('name') +
                       '.' +
                       img_info.get('ext'))
        try:
            urlretrieve(img_path, target_path)
            return target_path
        except FileNotFoundError as err:
            print(err)   # something wrong with local path
        except HTTPError as err:
            print(err)  # something wrong with url


if __name__ == "__main__":
    BOT = PsyTribeSpider()
    BOT.run()