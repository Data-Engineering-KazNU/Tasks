import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_open_government_data_sites"
headers = {}  #To get header; google search 'what is my user agent'
response=requests.get(url,headers = headers)

if response.status_code == 200:
    search_response = response.content

soup=BeautifulSoup(search_response,'html.parser')


with open("output1.html", "w",encoding='utf8') as file:
    file.write(str(soup))
    
tab = soup.find_all("table",{"class":"wikitable"})
print(tab[1])


with open("output3.html", "w",encoding='utf8') as file:
    file.write(str(tab[1]))
