"""
Parsing https://context.reverso.net/
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urled import encode, decode


def strip(text):
		"""
		Removes all spaces and line breaks from text
		"""
		return text.replace("  ", "").replace("\n", "")

def interpretation(html, num=0):
		"""
		Displays translation depending on part of speech
		"""
		return [strip(i.text) for i in html.find('div', {'id':'translations-content'}).find_all('a', {'data-pos-index':num})]


def parse(site):
		"""
		Parses the site and returns parts of speech, translation with examples and the resulting page
		"""
		user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
		headers={'User-Agent':user_agent,}
		request = Request(site, None, headers)
		html = BeautifulSoup(urlopen(request).read(), features="lxml").find('div', {'class':'left-content'})
		buttons = [strip(i.text) for i in html.find('div', {"id":"pos-filters"}).find_all('button')	]
		interpretations = interpretation(html)
		result = [strip(i.find_all('span')[0].text[:-1]+' - '+i.find_all('span')[-1].text[:-1]) for i in html.find_all('div', {'class':'example'})]	
		return buttons, interpretations, result, html


if __name__ == '__main__':
		word =  'change'
		site = 'https://context.reverso.net/перевод/английский-русский/'+word
		result = parse(encode(site)) 
		print(result)
