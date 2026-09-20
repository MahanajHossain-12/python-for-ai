import requests
from datetime import date, datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()  # Get the current date and time
week_ago = today - timedelta(days=7)  # Get the date 7 days ago

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Dhaka weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=23.8103&longitude=90.4125&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(
    url
)  # Making a GET request to the specified URL to retrieve weather data for Dhaka for the past week
data = (
    response.json()
)  # json data is string based, we need to convert it to a dictionary to access the data
print(data)

# _______________________________________________________________#

# Extract the daily data
daily_data = data[
    "daily"
]  # Extracting the 'daily' key from the JSON response to get daily weather data

# Create a DataFrame
df = pd.DataFrame(
    {
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    }
)

# Convert date strings to datetime
df["date"] = pd.to_datetime(
    df["date"]
)  # Converting the 'date' column in the DataFrame from string format to datetime objects for easier manipulation and plotting because json data is string based, we need to convert it to a datetime object to work with it in pandas

print(df)


# _______________________________________________________________#


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max_temp"], marker="o", label="Max Temp")
plt.plot(df["date"], df["min_temp"], marker="o", label="Min Temp")

# Add labels and title
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Dhaka Weather - Past 7 Days")
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig("weather_chart.png")
plt.show()

# _______________________________________________________________#


# Create data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Save to CSV
df.to_csv("data/dhaka_weather.csv", index=False)
print("Data saved to data/dhaka_weather.csv")
