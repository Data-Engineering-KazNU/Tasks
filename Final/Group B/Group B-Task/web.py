import requests
from bs4 import BeautifulSoup
import csv
url = "https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan"
headers = {}  #To get header; google search 'what is my user agent'
response=requests.get(url,headers = headers)

if response.status_code == 200:
    search_response = response.content

soup=BeautifulSoup(search_response,'html.parser')
#HTML parser is used since we are scraping html table

with open("output1.html", "w", encoding="utf8") as file:
    file.write(str(soup))
    
tab = soup.find_all("table",{"class":"wikitable"})
#We use wikitable, because all tables has this class

og_table=tab[0]

print(og_table)
with open("output3.html", "w", encoding="utf8") as file:
    file.write(str(tab[1]))


fo=open(r"C:\Users\USER\Desktop\Data\tasks\tasks4\bekbolat\valsample.csv", "w" , newline="")
csvwriter= csv.writer(fo)
csvwriter.writerow((("year", "population", "rural", "urban","source" )))


#iterating over table classes
for row in og_table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    if(columns != []):
        year = "01-01-" + columns[0].text.strip() 
        population = columns[1].text.strip()
        rural = columns[2].text.strip().replace("n/a", " ")
        urban = columns[3].text.strip().replace("n/a", " ")
        source = columns[4].text.strip()
        #print(year,population, portal_name)
        csvwriter.writerow((year,population,rural,urban,source))
