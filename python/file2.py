import csv
import pandas as pd
data = pd.read_csv("quant.csv")
print(data)
data['col3']=[0,0,0,0];
data.to_csv("quant.csv",index=False)
p=pd.read_csv("quant.csv")
print(p)
