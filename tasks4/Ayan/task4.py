import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/List_of_open_government_data_sites"
headers = {}  # To get header; google search 'what is my user agent'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    search_response = response.content

soup = BeautifulSoup(search_response, 'html.parser')
# HTML parser is used since we are scraping html table

with open("output1.html", "w", encoding="utf8") as file:
    file.write(str(soup))

tab = soup.find_all("table", {"class": "wikitable"})
# We use wikitable, because all tables has this class


og_table = tab[1]

with open("output3.html", "w", encoding="utf8") as file:
    file.write(str(tab[1]))

fo = open("res.csv", "w", newline="")
csvwriter = csv.writer(fo)
csvwriter.writerow((("govermrnt", "website", "portal_name")))

# iterating over table classes
for row in og_table.tbody.find_all('tr'):
    # Find all data for each column
    columns = row.find_all('td')
    if (columns != []):
        goverment = columns[0].text.strip()
        website = columns[1].text.strip()
        portal_name = columns[2].text.strip()
        # print(goverment, website, portal_name)
        csvwriter.writerow((goverment, website, portal_name))