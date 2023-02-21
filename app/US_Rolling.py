import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "C:/Users/choij/OneDrive/Desktop/MachineLearningProjects/AQI Analysis/app/data_date.csv")
df_US = df.loc[df["Country"] == "United States of America"]

df_US = df_US.loc[df_US['Date'].drop_duplicates(keep='first').index, :]

df_US["Rolling AQI"] = df_US["AQI Value"].rolling(2).mean()
df_US = df_US.drop(136)

df_US.index = df_US["Date"]
del df_US["Date"]

print(df_US.head())
print(df_US.tail())

plt.plot(df_US["AQI Value"], label="AQI")
plt.plot(df_US["Rolling AQI"], label="Rolling AQI")
plt.legend()
plt.ylabel("AQI")
plt.xlabel("Date")
plt.xticks([0, 63], labels=["2022-07-22", "2023-1-12"])
plt.savefig("rolling.png")
plt.show()
