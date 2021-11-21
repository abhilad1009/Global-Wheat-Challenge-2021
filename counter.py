import pandas as pd

data=pd.read_csv("submission_v0.csv")

print(data.groupby(['domain']).count())


