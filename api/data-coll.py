
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/dipamsen/Wikipedia-Scraper/main/filtering/filtered.csv")
df.head()

# df.drop(['Unnamed: 0'], axis=1, inplace=True)

name = df["name"].to_list()
mass = df["mass"].to_list()
radius = df["radius"].to_list()
dist = df["distance"].to_list()
gravity = df["gravity"].to_list()


final_star_list = []

temp_dict = {}
for i in range(0, len(name)):
  temp_dict["name"] = name[i]
  temp_dict["mass"] = mass[i]
  temp_dict["radius"] = radius[i]
  temp_dict["distance"] = dist[i]
  temp_dict["gravity"] = gravity[i]
  final_star_list.append(temp_dict)
  temp_dict = {}
print(final_star_list)
