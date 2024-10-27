import pandas as pnd
import random as rnd

squirel=pnd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241027.csv")
data =(squirel["Primary Fur Color"].value_counts())

df = pnd.DataFrame(data)
df.to_csv("squirrel_count.csv")