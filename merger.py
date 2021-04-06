import csv
import pandas as pd
import io

headers = ["name", "mass", "radius", "distance"]

df = pd.read_csv("./brown-dwarfs.csv")
df = df[df['mass'].notna()]
df = df[df['radius'].notna()]
df['radius'] = df['radius'] * 0.102763  # Convert to Solar Radius
df['mass'] = df['mass'] * 0.000954588  # Convert to Solar Mass

print(df[headers])


df2 = pd.read_csv("./brightstars.csv")

with io.open("merged.csv", "w", encoding="utf-8", newline='') as f:
  csvW = csv.writer(f)
  csvW.writerow(headers)
  csvW.writerows(df[headers].iloc)
  csvW.writerows(df2.iloc)
