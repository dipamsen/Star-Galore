import pandas as pd

df = pd.read_csv("./final_data.csv")
# print(df)
# Convert AU to Light Years
distances = df['distance']
for i, dist in enumerate(distances):
  try:
    distances[i] = float(dist) * 1.58125e-5
    df['gravity'][i] = float(df['gravity'][i])
  except:
    distances[i] = None

df = df[df['distance'].notna()]
df = df[df['gravity'].notna()]
df = df[df['gravity'] != 'unknown']
# Filter
df = df[df['distance'] <= 100]
df = df[df['gravity'] > 150]
df = df[df['gravity'] < 300]

df.to_csv("filtered.csv", index=False)

print(df)
