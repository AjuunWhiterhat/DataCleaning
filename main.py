import pandas as pd
import csv

df = pd.read_csv("merged_dataset.csv")
df = df.dropna(axis=0, how="all")
df.drop("Unnamed: 4",axis=1,inplace=True)

df = df.rename({
    'name.1':'Dwarf Star name',
    'distance.1':"Dwarf Distance",
    'mass.1':'solar mass',
    'radius.1':'solar radius'
},axis='columns')

print(df.columns)

df.to_csv("main.csv")

