## Internet of Things Devices - Time Series Plots
# The Internet of things (IoT) describes the network of physical objects that are embedded with sensors, software, and other technologies to connect and exchange data with other devices and systems over the Internet.
# Wearable devices are equipped with laser sensors to collect data.
# Heat Index (temperature + humidity) is one common data recorded on these IoT readers.
# Put yourself in the shoes of a quality analyst whose task is to test the efficacy of new IoT devices. 
# You need to create time-series plots for daily temperature variation for the given duration and find any inconsistencies in the temperature readings (if there are any).

import pandas as pd
import datetime as dt
import numpy as np
df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/iot-devices/IoT-device.csv')
print("DataFrame Info:\n", df.info())
df = df.drop(axis = 0, columns= "room_id/id")
print("New DataFrame Info:\n", df.info())

# Converting noted_date column to DateTime
new_dates = pd.to_datetime(df["noted_date"])
df["DateTime"] = new_dates
print("New DataFrame Info with DateTime:\n", df.info())

# Sort by dates
df = df.sort_values("DateTime", ascending = True)

# Create new columns for year, month, day, day name, hours and minutes values and add to the DataFrame.
year = new_dates.dt.year
month = new_dates.dt.month
day = new_dates.dt.day
day_name = new_dates.dt.day_name()
hours = new_dates.dt.hour
minutes = new_dates.dt.minute
df["Year"] = year
df["Month"] = month
df["Day"] = day
df["Day Name"] = day_name
df["Hour"] = hours
df["Minute"] = minutes
in_temp_df = df[df['out/in'] == 'In']
out_temp_df = df[df['out/in'] == 'Out']

# Create a time series line plot for the indoor temperature records.
import matplotlib.pyplot as plt
plt.figure(figsize = (21,7))
plt.plot(in_temp_df["DateTime"], in_temp_df["temp"])
plt.show()
# Create a time series line plot for the outdoor temperature records.
plt.figure(figsize = (21,7))
plt.plot(out_temp_df["DateTime"], out_temp_df["temp"])
plt.show()
plt.figure(figsize = (21,7))
plt.plot(in_temp_df["DateTime"], in_temp_df["temp"])
plt.plot(out_temp_df["DateTime"], out_temp_df["temp"])
plt.show()

# Create a box plot to represent the distribution of indoor and outdoor temperatures for the whole year.
import seaborn as sns
# pass the 'out/in' and 'temp' columns inside the 'x' and 'y' attributes of the 'boxplot()' function.
plt.figure()
sns.boxplot(x=df["out/in"], y=df["temp"])
plt.show()

# Get the maximum and minimum temperatures for each day in each month.
df.groupby(by = ["Month", "Day"]).agg(func={'temp' : ['max', 'min']})
estimate = np.median(df["temp"])
month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
plt.figure()
sns.barplot(x = df["Month"], y=df["temp"], data=df, hue =df["out/in"], estimator=np.median)
# pass the list holding the name of months inside the 'xticks()' function
plt.xticks(ticks= np.arange(12), labels = month_name)
plt.show()

# Function to label each temperature value on a given day and time with the heat indices as advised in the data-description.
def heat_index(temp_series):
  heat_index_list = []
  for temp in temp_series:
    if temp <= 32:
      heat_index_list.append('Green')
    elif (temp > 32) and (temp <= 41):
      heat_index_list.append('Yellow')
    elif (temp > 41) and (temp <= 54):
      heat_index_list.append('Orange')
    else:
      heat_index_list.append('Red')
  return pd.Series(data=heat_index_list, index=temp_series.index)
print("Heat Index:\n", heat_index(df['temp']))
df['heat_index'] = heat_index(df['temp'])
group_heat_index = df.groupby(by=['heat_index', 'out/in'])
heat_index_agg = group_heat_index.agg(func={'temp' : ['max', 'count']})
heat_index_agg[('temp', 'percent')] = heat_index_agg[('temp', 'count')] * 100 / df.shape[0]
print("Percentage distribution of the heat zones:\n", heat_index_agg)