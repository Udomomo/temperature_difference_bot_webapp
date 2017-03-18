from forecastiopy import *


#fetch Tokyo's weather forecast from Dark Sky
def fetch_forecast_data():
    apikey = "08c19e7bfc9504e9c4f8db40bf1d9605"
    Tokyo = [35.689781, 139.762202]

    forecast_data = ForecastIO.ForecastIO(apikey,
                            units=ForecastIO.ForecastIO.UNITS_SI,
                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                            latitude=Tokyo[0], longitude=Tokyo[1])

    '''for debug
    print('Latitude', forecast_data.latitude, 'Lengitude', forecast_data.longitude)
    print('Timezone', forecast_data.timezone, 'Offset', forecast_data.offset)
    print(forecast_data.get_url()) # You might want to see the request url
    '''
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


