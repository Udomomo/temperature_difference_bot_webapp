from forecastiopy import *


#fetch Tokyo's weather forecast from Dark Sky
apikey = "08c19e7bfc9504e9c4f8db40bf1d9605"

Tokyo = [35.689781, 139.762202]

fio = ForecastIO.ForecastIO(apikey,
                            units=ForecastIO.ForecastIO.UNITS_SI,
                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                            latitude=Tokyo[0], longitude=Tokyo[1])

print('Latitude', fio.latitude, 'Longitude', fio.longitude)
print('Timezone', fio.timezone, 'Offset', fio.offset)
print(fio.get_url()) # You might want to see the request url

#extract the temperature from the data
temperatureData=[]
if fio.has_daily() is True:
    daily = FIODaily.FIODaily(fio)
    outputKey = ["time", "temperatureMax", "temperatureMin"]
    for day in range(2):
        dailyTemperature = {}
        for item in outputKey:
            dailyTemperature[item] = str(daily.get_day(day+1)[item]) # daily.get_day(day) fetches ['daily'] ['data'][day-1]
        temperatureData.append(dailyTemperature)
    print(temperatureData)
else:
    print('No Daily data')
