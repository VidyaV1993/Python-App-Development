import requests

def get_weather_info():
    api_key = "eb0421626dffe4bb7368ebc7ea1f1d86"
    city = "Maple Valley"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    req = requests.get(url)
    json = req.json()
    # print(json)

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}

def main():
    # Printing the results
    weather_info_dict = get_weather_info()
    print("Today's forecast is ", weather_info_dict.get('description'))
    print("The minimum temperature is", weather_info_dict.get('temp_min'))
    print("The maximum temperature is", weather_info_dict.get('temp_max'))

main()