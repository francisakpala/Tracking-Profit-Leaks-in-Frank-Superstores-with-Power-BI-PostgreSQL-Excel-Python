import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
df.to_csv("clean_superstore.csv", index=False)
