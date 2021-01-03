from collections import Counter
import re
from bs4 import BeautifulSoup
import urllib.request  as urllib2 
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = 'http://en.wikipedia.org/wiki/Albert_Einstein'
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl)
dem = soup.findAll('p') #find paragraphs
word_counts = Counter()
stopwords = frozenset(('A', 'AN', 'THE'))
for i in dem:    # loop for each para
    words = re.findall(r'\w+', i.text)
    cap_words = [word.upper() for word in words if not word.upper() in stopwords]
    word_counts.update(cap_words)
print (word_counts)