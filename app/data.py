import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "C:/Users/choij/OneDrive/Desktop/MachineLearningProjects/AQI Analysis/app/data_date.csv")
df_US = df.loc[df["Country"] == "United States of America"]

df_US = df_US.loc[df_US['Date'].drop_duplicates(keep='first').index, :]


# df_US.index = df_US["Date"]
# del df_US["Date"]
df_US["Year"] = pd.DatetimeIndex(df_US["Date"]).year
# print(df_US.head())
# print(df_US.tail())
fig = plt.plot(df_US["Date"], df_US["AQI Value"])
plt.xlabel('Date')
plt.ylabel("AQI Value")
plt.xticks([0, 64], labels=["2022-07-21", "2023-1-12"])
plt.savefig("data.png")
