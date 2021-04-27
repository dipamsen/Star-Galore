rj = 0.10049
mj = 3.7752e+57
# M(*) = Solar Mass
# MJ = Jupiter Mass

import pandas as pd

df = pd.read_csv("./merged.csv")


data = []
for i in range(255):
  data.append(df.iloc[i].to_list())

gravities = []
for star in data:
  try:
    star[1] = star[1].replace(",", "")
    star[1] = float(star[1]) * 1.989e+30
    star[2] = float(star[2]) * 6.957e+8
    mass = star[1]
    rad = star[2]
    gravity = (mass / rad * rad) * 6.67e-11
    gravities.append(gravity)
  except:
    gravities.append("unknown")

df['gravity'] = gravities
df.to_csv("final_data.csv", index=False)
