import requests
from tabulate import tabulate
from bs4 import BeautifulSoup as bss

pl=[]
myurl="https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy%2C4io&page="
for i in range(1,5):
	s=requests.get(myurl+str(i))
	print('[+] done fetching websites')
	soup = bss(s.text, features='html.parser')
	for a in soup.findAll('a',href=True,attrs={'class':"_31qSD5"}):
		name=a.find('div', attrs={'class':'_3wU53n'}).text
		price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'}).text
		specsList=a.find('ul', attrs={'class':'vFw0gD'})
		specs=specsList.find('li',attrs={'class':"tVe95H"}).text
		offerS=a.find('div',attrs={'class':'VGWI6T'})
		if offerS==None:
			offer=' '
		else:
			offer=offerS.span.text
		if len(offer)==6:
			offer='0'+offer
		pl.append([name,price,specs,offer])

print(tabulate(sorted(pl,key=lambda x:x[3],reverse=True),["Device","Price","Specs","Offer"],"fancy_grid"))

