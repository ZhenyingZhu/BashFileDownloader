import os
import urllib
import urllib2

from bs4 import BeautifulSoup

base_url = 'http://www.lanzhong.net/youxi1/index1.htm'

root_page = urllib2.urlopen(base_url).read()
soup = BeautifulSoup(root_page, "lxml")

print soup.prettify()

# # Get Folder
# home = os.path.expanduser("~")
# downloadFolder = os.path.join(home, 'Downloads', 'files')
# if not os.path.exists(downloadFolder):
#     os.makedirs(downloadFolder)


# fileName = os.path.join(downloadFolder, '1ARCY.ZIP')
# urllib.urlretrieve("http://cd.textfiles.com/pslv3nv10/GAMES/DOS/MVP/1ARCY.ZIP", fileName)

