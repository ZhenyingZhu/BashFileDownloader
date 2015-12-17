import os
import urllib
import urllib2

from bs4 import BeautifulSoup

base_url = 'http://cd.textfiles.com/directory.html'

root_page = urllib2.urlopen(base_url).read()
soup = BeautifulSoup(root_page, "lxml")

print soup.get_text()