#!/usr/bin/python

from urllib.request import urlopen
from xml.etree import ElementTree as ET

test_feed = "https://www.archlinux.org/feeds/news/"

class Item():
    def __init__(self):
        self.title = ""
        self.link = ""
        self.description = ""
        self.pubDate = ""
        self.guid = ""

class Channel():
    def __init__(self):
        self.url = "" # actual rss feed url
        self.title = "" # title tag
        self.link = "" # link tag
        self.description = "" # desc tag
        self.items = [] # channel's 'item' childs

class RssMgr():
    def __init__(self):
        self._feeds = dict() # (k: internal name, v: Channel() object)

    def add_channel(self, name, url):
        """
        Add the channel to the channels list if :
            - name doesn't already exist in the list
            - the url points to a valid rss document
        """
        pass

    def get_channels(self):
        """
        Load the channels list from the database
        """
        pass


def showcase():
    page = urlopen(test_feed)
    if page.status == 200:
        content = page.read()
        page.close()
        root = ET.fromstring(content)
        rssobj = {}
        rssobj['url'] = test_feed
        rssobj['version'] = root.get('version')
        ch = root.find('channel')
        rssobj['channel'] = {}
        rssobj['channel']['title'] = ch.find('title').text
        rssobj['channel']['link'] = ch.find('link').text
        rssobj['channel']['desc'] = ch.find('description').text
        print(rssobj)


def showcae2():
    """ Showing what the RssMgr API should look like. """
    mgr = RssMgr()
    mgr.add_feed("Arch Linux", "https://www.archlinux.org/feeds/news/")
    afeed = mgr.get("Arch Linux") # maybe mgr["Arch Linux"]
    print("%s : %d items." % (afeed.title, len(afeed.items)))

