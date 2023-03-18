import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/List_of_open_government_data_sites"
headers = {}  #To get header; google search 'what is my user agent'
response=requests.get(url,headers = headers)

if response.status_code == 200:
    search_response = response.content

soup=BeautifulSoup(search_response,'html.parser')


with open("output1.html", "w",encoding='utf8') as file:
    file.write(str(soup))
    
tab = soup.find_all("table",{"class":"wikitable"})
#list of tables 

# this is just for analysis will be removed later
with open("output3.html", "w",encoding='utf8') as file:
    file.write(str(tab[1]))

og_tabl1 = tab[1]
#getting the second table 

#creating csv to add our values
fo = open("result.csv","w",newline="")
csvwriter =  csv.writer(fo)
#calling writerow to add our headers
csvwriter.writerow((["government","website","portal_name"]))
#iterating over table values as td
for row in og_tabl1.tbody.find_all('tr'):
    #find all data fro each column
    columns = row.find_all('td')
    if (columns != []):
        government = columns[0].text.strip()
        website = columns[1].text.strip()
        portal_name = columns[2].text.strip()
        #creating result.csv 
        #adding values
        csvwriter.writerow((government,website,portal_name))



