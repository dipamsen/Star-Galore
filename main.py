from bs4 import BeautifulSoup
import csv
import requests
import io


url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

data = []
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

headers = ["Name", "Distance (light years)", "Mass", "Radius"]
rows = list(soup.find(
    "table", attrs={"class", "wikitable"}).find("tbody").find_all("tr"))
rows.pop(0)
for row in rows:
  td_tags = row.find_all("td")
  name = (td_tags[1].text).strip().replace("\n", "")
  dist = (td_tags[3].text).strip().replace("\n", "")
  mass = (td_tags[5].text).strip().replace("\n", "")
  radi = (td_tags[6].text).strip().replace("\n", "")
  data.append([name, dist, mass, radi])

with io.open("new-data.csv", "w", encoding="utf-8", newline='') as f:
  csvw = csv.writer(f)
  csvw.writerow(headers)
  csvw.writerows(data)
