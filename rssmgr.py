#!/usr/bin/python

from urllib.request import urlopen
from xml.etree import ElementTree as ET

my_rss_feed = "https://www.archlinux.org/feeds/news/"

page = urlopen(my_rss_feed)
if page.status == 200:
  content = page.read()
  page.close()
  tree = ET.fromstring(content)
  print(tree.tag)
