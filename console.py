import Utils

print('Введите город (латиница с большой буквы) или координаты через пробел:')
x = input()
place = x.split()
if len(place) == 1:
    coordinates = Utils.getCityCoordinates(x)
else:
    coordinates = {'lat': place[0], 'lon': place[1]}
stations = Utils.getWeatherByCoordinates(coordinates['lat'], coordinates['lon'])
print('выберите метеостанцию')
i = 0
for station in stations:
    print(f"{i}) {station.name}")
    i += 1
id = int(input())

print(stations[id])
while True:
    print('1 - прогноз на завтра\n'
          '2 - прогноз на 4 дня\n'
          '3 - почасовой прогноз\n')
    id = input()
    if id == '1':
        print(
            Utils.getDayFromForecast(Utils.getWeatherByCoordinatesForecast(coordinates['lat'], coordinates['lon']), 1))
    if id == '2':
        for i in range(1, 5):
            print(Utils.getDayFromForecast(
                Utils.getWeatherByCoordinatesForecast(coordinates['lat'], coordinates['lon']), i))
    if id == '3':
        print("ВВедите на сколько шагов вперед вам нужен прогноз(шаг - 3 часа, max=40) ")
        x = input()
        for time in Utils.getWeatherByCoordinatesForecast(coordinates['lat'], coordinates['lon'], x):
            print(time)
