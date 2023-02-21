from prophet import Prophet
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    "C:/Users/choij/OneDrive/Desktop/MachineLearningProjects/AQI Analysis/app/data_date.csv")
df_US = df.loc[df["Country"] == "United States of America"]

df_US = df_US.loc[df_US['Date'].drop_duplicates(keep='first').index, :]

df_US["Year"] = pd.DatetimeIndex(df_US["Date"]).year
df_US = df_US[["Date", "AQI Value"]]
df_US = df_US.rename(columns={"Date": "ds", "AQI Value": "y"})

print(df_US.head())

model = Prophet()
model.fit(df_US)

# Days forcast
future = model.make_future_dataframe(periods=100, freq="D")

predictions = model.predict(future)

futureFigure = model.plot(predictions)
futureFigure.savefig("TimeSeriesDay.png")
# Months forecast
future2 = model.make_future_dataframe(periods=100, freq="M")

predictions2 = model.predict(future2)

futureFigure2 = model.plot(predictions2)
futureFigure2.savefig("TimeSeriesMonth.png")
plt.show()
