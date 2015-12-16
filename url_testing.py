import os
import urllib
import urllib2

from bs4 import BeautifulSoup

# Get Folder
home = os.path.expanduser("~")
downloadFolder = os.path.join(home, 'Downloads', 'files')
if not os.path.exists(downloadFolder):
    os.makedirs(downloadFolder)


# Analysis page structure
html = urllib2.urlopen('http://cd.textfiles.com/pslv3nv10/GAMES/DOS/MVP/').read()
soup = BeautifulSoup(html, "lxml")
print soup.title.string
for link in soup.find_all('a'):
    print(link.get('href'))

# Retrive file
# fileName = os.path.join(downloadFolder, '1ARCY.ZIP')
# urllib.urlretrieve("http://cd.textfiles.com/pslv3nv10/GAMES/DOS/MVP/1ARCY.ZIP", fileName)