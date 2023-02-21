import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "C:/Users/choij/OneDrive/Desktop/MachineLearningProjects/AQI Analysis/app/data_date.csv")
df_US = df.loc[df["Country"] == "United States of America"]

df_US = df_US.loc[df_US['Date'].drop_duplicates(keep='first').index, :]

print(df_US["Status"].value_counts())

categories = ["Good", "Moderate", "Unhealthy",
              "Very Unhealthy", "Unhealthy for Sensitive Groups", "Hazardous"]

good = len(df_US.loc[df_US["Status"] == "Good"])
moderate = len(df_US.loc[df_US["Status"] == "Moderate"])
unhealthy = len(df_US.loc[df_US["Status"] == "Unhealthy"])
veryUnhealthy = len(df_US.loc[df_US["Status"] == "Very Unhealthy"])
unhealthyForSensitiveGroups = len(
    df_US.loc[df_US["Status"] == "Unhealthy for Sensitive Groups"])
hazardous = len(df_US.loc[df_US["Status"] == "Hazardous"])

values = [good, moderate, unhealthy, veryUnhealthy,
          unhealthyForSensitiveGroups, hazardous]
print(values)

fig = plt.bar(categories, values)
plt.xticks(fontsize=4)
plt.savefig("AQIStatus.png")
plt.show()
