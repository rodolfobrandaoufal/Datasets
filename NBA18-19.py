import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing



path='/home/rb/Github/Datasets'
os.chdir(path)

df = pd.read_csv('NBA_data.csv')
df1=df.drop(columns=["TEAM","GP","W","L"])
normalized_df=(df1-df1.min())/(df1.max()-df1.min())

df['RATE'] = normalized_df['PTS']*normalized_df['REB']*normalized_df['AST']*normalized_df['STL']*normalized_df['BLK']/normalized_df['TOV']
print(df.sort_values(by=['RATE'], ascending=False).head(10))

TEAM=df['TEAM']
PTS=df['PTS']
REB=df['REB']
AST=df['AST']
TOV=df['TOV']
STL=df['STL']
BLK=df['BLK']
RATE=df['RATE']

fig1, ax = plt.subplots()
plt.scatter(TEAM, PTS)
plt.xticks(rotation=70)
ax.set_ylabel('PTS')
ax.set_title('PTS')

fig2, ax = plt.subplots()
plt.scatter(TEAM,REB)
plt.xticks(rotation=70)
ax.set_ylabel('REB')
ax.set_title('REB')

fig3, ax = plt.subplots()
plt.scatter(TEAM, AST)
plt.xticks(rotation=70)
ax.set_ylabel('AST')
ax.set_title('AST')

fig4, ax = plt.subplots()
plt.scatter(TEAM, TOV)
plt.xticks(rotation=70)
ax.set_ylabel('TOV')
ax.set_title('TOV')

fig5, ax = plt.subplots()
plt.scatter(TEAM,STL)
plt.xticks(rotation=70)
ax.set_ylabel('STL')
ax.set_title('STL')

fig6, ax = plt.subplots()
plt.scatter(TEAM, BLK)
plt.xticks(rotation=70)
ax.set_ylabel('BLK')
ax.set_title('BLK')

fig7, ax = plt.subplots()
plt.scatter(TEAM, RATE)
plt.xticks(rotation=70)
ax.set_ylabel('RATE')
ax.set_title('RATE')

plt.show()