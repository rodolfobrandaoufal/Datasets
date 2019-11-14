import pandas as pd
import numpy as np

url = 'https://github.com/rodolfojbrandao/Datasets/blob/master/NBA_data.csv'
df = pd.read_csv(url, error_bad_lines=False)
print(df)