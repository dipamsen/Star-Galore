import pandas as pd

df = pd.read_csv("./merged.csv")

df = df[df['mass'].notna()]
df = df[df['radius'].notna()]
df = df[df['distance'].notna()]

names = df['name']
new_names = []

for name in names:
  new_names.append(name.replace(" [de]", "").replace(" [fr]", ""))

df['name'] = new_names

df.to_csv("./cleaned.csv", index=False)
