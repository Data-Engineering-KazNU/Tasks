import csv

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_open_government_data_sites"
headers = {}  #To get header; google search 'what is my user agent'
response=requests.get(url,headers = headers)

if response.status_code == 200:
    search_response = response.content

soup=BeautifulSoup(search_response,'html.parser')

with open('output1.html', 'w') as file:
    file.write(str(soup.encode('utf8')))

tab = soup.find_all('table', {'class':'wikitable'})

og_table = tab[1]


with open("output3.html", "w") as file:
    file.write(str(tab[1]))

#creatging result.csv to add our values
fo = open('result.csv' , 'w' , newline='')
csvwriter = csv.writer(fo)
#calling writerow one time to add csv headers
csvwriter.writerow(('government', 'website', 'portal_name'))

for row in og_table.tbody.find_all('tr'):
    # Find all data for each column
    columns = row.find_all('td')
    if(columns != []):
        government = columns[0].text.strip()
        website = columns[1].text.strip()
        portal_name = columns[2].text.strip()
        # print(government,website,portal_name)
        # adding values
        csvwriter.writerow ((government, website, portal_name))