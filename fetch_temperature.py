from forecastiopy import *
import os

#fetch Tokyo's weather forecast from Dark Sky
def fetch_forecast_data():
    apikey = os.environ["DARKSKY_APIKEY"]
    location = [35.689781, 139.762202]

    forecast_data = ForecastIO.ForecastIO(apikey,
                            units=ForecastIO.ForecastIO.UNITS_SI,
                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                            latitude=location[0], longitude=location[1])

    return forecast_data

#extract the temperature from the data
def extract_temperature():
    fio = fetch_forecast_data()
    temperatureData=[]
    if fio.has_daily() is True:
        daily = FIODaily.FIODaily(fio)
        outputKey = ["time", "temperatureMax", "temperatureMin"]
        for day in range(2):
            dailyTemperature = {}
            for item in outputKey:
                dailyTemperature[item] = str(daily.get_day(day+1)[item]) # daily.get_day(day) fetches ['daily'] ['data'][day-1]
            temperatureData.append(dailyTemperature)
        return(temperatureData)
    else:
        return('No Daily data')

