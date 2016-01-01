import os
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup

base_url = 'http://www.lanzhong.net/youxi1/index1.htm'

root_page = urllib2.urlopen(base_url).read()
soup = BeautifulSoup(root_page, "lxml")

print soup.prettify()

print "=" * 20
for href_tag in soup.find_all('a'):
    link = href_tag.attrs['href']
    print urlparse.urljoin(base_url, link)

# # Get Folder
# home = os.path.expanduser("~")
# downloadFolder = os.path.join(home, 'Downloads', 'files')
# if not os.path.exists(downloadFolder):
#     os.makedirs(downloadFolder)


# fileName = os.path.join(downloadFolder, '1ARCY.ZIP')
# urllib.urlretrieve("http://cd.textfiles.com/pslv3nv10/GAMES/DOS/MVP/1ARCY.ZIP", fileName)

def main():
    print "Hello World"


if __name__ == 'main':
    main()