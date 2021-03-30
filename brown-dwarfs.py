import requests
from bs4 import BeautifulSoup
import io
import csv

page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
soup = BeautifulSoup(page.content, features="html.parser")

field_brown_dwarfs = soup.find_all("table")[4]
headers = ['name', 'constellation', 'right_ascension', 'declination',
           'distance', 'spectral_type', 'mass', 'radius', 'discovery_year']

tr_tags = field_brown_dwarfs.find_all("tr")
tr_tags.pop()

brown_dwarfs = []
for row in tr_tags:
  td_tags = row.find_all("td")
  tmp = []
  for i, val in enumerate(td_tags):
    if(i == 4):
      continue
    tmp.append(val.text.strip())
  brown_dwarfs.append(tmp)

with io.open("brown-dwarfs.csv", "w", encoding="utf-8", newline='') as f:
  csvw = csv.writer(f)
  csvw.writerow(headers)
  csvw.writerows(brown_dwarfs)
