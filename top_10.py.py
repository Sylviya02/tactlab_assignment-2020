from urllib.request import urlopen
from html.parser import HTMLParser
import json
import collections
class WordsParser(HTMLParser):
	search_tags=['p','div','span','a','h1','h2','h3','h4']
	current_tag=''
	common_words={}
	def handle_starttag(self, tag, attr):
		self.current_tag=tag
	def handle_data(self,data):
		if self.current_tag in self.search_tags:
			for word in data.strip().split():
				common_word=word.lower().replace('.','').replace(':','')
				common_word=common_word.replace(',','')
				common_word=common_word.replace('?','')
				common_word=common_word.replace(';','')
				if (len(common_word)>2 and common_word not in ['the','and','are','you','our','for','any'] and common_word[0].isalpha()):
					try:
						self.common_words[common_word] =+ 1
					except:
						self.common_words.update({common_word:1})
if __name__=='__main__':
	url='https://www.geeksforgeeks.org/analysis-algorithm-set-5-amortized-analysis-introduction/'
	response=urlopen(url)
	html=response.read().decode('utf-8',errors='ignore')
	words_parser=WordsParser()
	words_parser.feed(html)
	words_count=collections.Counter(words_parser.common_words)
	most_common=words_count.most_common(10)
	for word,count in most_common:
		print(word, str(count) + ' times',sep=": ")
	url='https://en.wikipedia.org/wiki/GitHub'
	response=urlopen(url)
	html=response.read().decode('utf-8',errors='ignore')
	words_parser=WordsParser()
	words_parser.feed(html)
	words_count=collections.Counter(words_parser.common_words)
	most_common=words_count.most_common(10)
	for word,count in most_common:
		print(word)
	url='https://en.wikipedia.org/wiki/GitHub'
	response=urlopen(url)
	html=response.read().decode('utf-8',errors='ignore')
	words_parser=WordsParser()
	words_parser.feed(html)
	words_count=collections.Counter(words_parser.common_words)
	most_common=words_count.most_common(10)
	for word,count in most_common:
		print(word)
	url='https://www.geeksforgeeks.org/getting-started-machine-learning/'
	response=urlopen(url)
	html=response.read().decode('utf-8',errors='ignore')
	words_parser=WordsParser()
	words_parser.feed(html)
	words_count=collections.Counter(words_parser.common_words)
	most_common=words_count.most_common(10)
	for word,count in most_common:
		print(word)
        
