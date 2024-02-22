#2.1.3 DataFrame

import pandas as pd



dataframe = pd.read_csv("GTAV.csv")

print(dataframe)

print(dataframe["author_num_reviews"].mean())
print(dataframe["author_playtime_last_two_weeks"].max())
print(dataframe["author_playtime_at_review"].median())
print(dataframe["author_playtime_forever"].min())
print(dataframe[dataframe["author_playtime_forever"]>10000])
print(dataframe[dataframe["author_num_games_owned"]>1])

