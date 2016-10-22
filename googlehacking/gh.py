#coding=UTF-8
import requests
from bs4 import BeautifulSoup as bs
import datetime
def readUrl():
	returnvalue = []
	
	with open('address.txt','r') as f:
		addresses = f.readlines()
		
	for url in addresses:
		returnvalue.append(url.strip('\n'))
	
	return returnvalue
		
		
def readKeyword():
	returnvalue = []
	with open('keyword.txt','r') as f:
		keyword = f.readlines()
		
	for word in keyword:
		returnvalue.append(word.strip('\n'))

	return returnvalue
	
def outputResult(res,filename):
	soup = bs(res.text,'html.parser')
	result = soup.find_all('div',{'id':'resultStats'})
	print result[0].text
	
	if result[0].text!='':
		with open(filename+".txt",'a+') as f:
			f.write(result[0].text.encode("utf-8")+'\n'+res.url.encode('utf-8')+'\n\n')
	else:
		print "NoResult"
		

if __name__=='__main__':

	urllist= readUrl()
	keywordlist = readKeyword()
	filename = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
	print filename
	for i in urllist:
		for j in keywordlist:
			searchpattern = i + '+' + j
			res = requests.get("https://www.google.com.tw/search?q=site:"+searchpattern+"&oq=site:"+searchpattern)
			outputResult(res,filename)

	
	
	
		

	