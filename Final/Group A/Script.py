import requests
import csv
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"class": "wikitable"})
og_table = table

fo = open("res.csv", "w", newline="")
csvwriter = csv.writer(fo)
csvwriter.writerow((("Year(January)", "Population (thousands)", "Rural", "Urban", "Source")))

for row in og_table.tbody.find_all('tr'):
    columns = row.find_all('td')
    if (columns != []):
        first = '01-01-' + columns[0].text.strip()
        second = columns[1].text.strip()
        third = columns[2].text.strip().replace('n/a', "null")
        fourth = columns[3].text.strip().replace('n/a', "null")
        fifth = columns[4].text.strip()
        csvwriter.writerow((first, second, third, fourth, fifth))
print("complete")