import pandas as pd
from matplotlib import pyplot as plt

years=[]
for line in open("ELECTION_ID"):
    id_year = line.strip().split() ##newvar
    year = id_year[1]
    years.append(year)

files = []
for y in years:
    files.append(y + ".csv")

dataframes=[]
for x in files:
    for y in years:
        header = pd.read_csv(f, nrows = 1).dropna(axis = 1)
        d = header.iloc[0].to_dict()
        df = pd.read_csv(f, index_col = 0, thousands = ",", skiprows = [1])
        df.rename(inplace = True, columns = d)
        df.dropna(inplace = True, axis = 1)
        y = df["Year"]
        dataframes.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])
bigframe=pd.concat(dataframes)
print(bigframe)

bigframe["Republican Share"]=bigframe["Republican"].div(newframe["Total Votes Cast"])
