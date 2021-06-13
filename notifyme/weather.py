# Samir Mitha - (c) 2021
import pyowm
import requests, json

def fetch_weather(city, country, owm_API_key):
	"""Gets the current temperature and weather conditions from the
	city and country provided

    Parameters
    ----------
    city : str
        The city name of the location
    country: str
    	The country name of the location
    owm_API_key: str
    	The OpenWeatherMap API key to call on own functions

    Returns
    -------
    temp: int
        The temperature in degrees Celsius
    status: str
    	The current weather conditions as a short string
    """
	owm = pyowm.OWM(owm_API_key)
	manager = owm.weather_manager()
	observation = manager.weather_at_place(city + ', ' + country)
	w = observation.weather
	temperature = w.temperature('celsius')
	status = w.detailed_status
	temp = int(temperature['temp'])
	return temp, status

def weather_multiplier(status):
	"""Gets a multiplier to apply to the travel time, based on the current
	time and weather conditions

    Parameters
    ----------
    status : str
        The current weather conditions as a short string

    Returns
    -------
    multiplier: float
    	The multiplier of the current weather condition
    """
	switcher1 = {
		"thunderstorm with light rain":1.041,
		"thunderstorm with rain":1.041,
		"thunderstorm with heavy rain":1.105,
		"light thunderstorm":1,
		"thunderstorm":1,
		"heavy thunderstorm":1,
		"ragged thunderstorm":1,
		"thunderstorm with light drizzle":1.041,
		"thunderstorm with drizzle":1.041,
		"thunderstorm with heavy drizzle":1.105,
		"light intensity drizzle":1,
		"drizzle":1,
		"heavy intensity drizzle":1.041,
		"light intensity drizzle rain":1,
		"drizzle rain":1.041,
		"heavy intensity drizzle rain":1.041,
		"shower rain and drizzle":1.041,
		"heavy shower rain and drizzle":1.105,
		"shower drizzle":1.041,
		"light rain":1.041,
		"moderate rain":1.041,
		"heavy intensity rain":1.105,
		"very heavy rain":1.105,
		"extreme rain":1.105,
		"freezing rain":1.105,
		"light intensity shower rain":1,
		"shower rain":1.041,
		"heavy intensity shower rain":1.041,
		"ragged shower rain":1.041,
		"light snow":1.195,
		"snow":1.195,
		"heavy snow":1.986,
		"sleet":1.195,
		"light shower sleet":1.195,
		"shower sleet":1.195,
		"light rain and snow":1.195,
		"rain and snow":1.195,
		"light shower snow":1.195,
		"shower snow":1.195,
		"heavy shower snow":1.986
	}
	switcher2 = {
		"thunderstorm with light rain":1.2754,
		"thunderstorm with rain":1.2754,
		"thunderstorm with heavy rain":1.6324,
		"light thunderstorm":1,
		"thunderstorm":1,
		"heavy thunderstorm":1,
		"ragged thunderstorm":1,
		"thunderstorm with light drizzle":1.2754,
		"thunderstorm with drizzle":1.2754,
		"thunderstorm with heavy drizzle":1.6324,
		"light intensity drizzle":1,
		"drizzle":1,
		"heavy intensity drizzle":1.2754,
		"light intensity drizzle rain":1,
		"drizzle rain":1.2754,
		"heavy intensity drizzle rain":1.2754,
		"shower rain and drizzle":1.2754,
		"heavy shower rain and drizzle":1.6324,
		"shower drizzle":1.2754,
		"light rain":1.2754,
		"moderate rain":1.2754,
		"heavy intensity rain":1.6324,
		"very heavy rain":1.6324,
		"extreme rain":1.6324,
		"freezing rain":1.6324,
		"light intensity shower rain":1,
		"shower rain":1.2754,
		"heavy intensity shower rain":1.2754,
		"ragged shower rain":1.2754,
		"light snow":1.4428,
		"snow":1.4428,
		"heavy snow":2.6242,
		"sleet":1.4428,
		"light shower sleet":1.4428,
		"shower sleet":1.4428,
		"light rain and snow":1.4428,
		"rain and snow":1.4428,
		"light shower snow":1.4428,
		"shower snow":1.4428,
		"heavy shower snow":2.6242
	}
	switcher3 = {
		"thunderstorm with light rain":1.07,
		"thunderstorm with rain":1.07,
		"thunderstorm with heavy rain":1.255,
		"light thunderstorm":1,
		"thunderstorm":1,
		"heavy thunderstorm":1,
		"ragged thunderstorm":1,
		"thunderstorm with light drizzle":1.07,
		"thunderstorm with drizzle":1.07,
		"thunderstorm with heavy drizzle":1.255,
		"light intensity drizzle":1,
		"drizzle":1,
		"heavy intensity drizzle":1.07,
		"light intensity drizzle rain":1,
		"drizzle rain":1.07,
		"heavy intensity drizzle rain":1.07,
		"shower rain and drizzle":1.07,
		"heavy shower rain and drizzle":1.255,
		"shower drizzle":1.07,
		"light rain":1.07,
		"moderate rain":1.07,
		"heavy intensity rain":1.255,
		"very heavy rain":1.255,
		"extreme rain":1.255,
		"freezing rain":1.255,
		"light intensity shower rain":1,
		"shower rain":1.07,
		"heavy intensity shower rain":1.07,
		"ragged shower rain":1.07,
		"light snow":1.136,
		"snow":1.136,
		"heavy snow":1.59,
		"sleet":1.136,
		"light shower sleet":1.136,
		"shower sleet":1.136,
		"light rain and snow":1.136,
		"rain and snow":1.136,
		"light shower snow":1.136,
		"shower snow":1.136,
		"heavy shower snow":1.59
	}
	switcher4 = {
		"thunderstorm with light rain":1.143,
		"thunderstorm with rain":1.143,
		"thunderstorm with heavy rain":1.3348,
		"light thunderstorm":1,
		"thunderstorm":1,
		"heavy thunderstorm":1,
		"ragged thunderstorm":1,
		"thunderstorm with light drizzle":1.143,
		"thunderstorm with drizzle":1.143,
		"thunderstorm with heavy drizzle":1.3348,
		"light intensity drizzle":1,
		"drizzle":1,
		"heavy intensity drizzle":1.143,
		"light intensity drizzle rain":1,
		"drizzle rain":1.143,
		"heavy intensity drizzle rain":1.143,
		"shower rain and drizzle":1.143,
		"heavy shower rain and drizzle":1.3348,
		"shower drizzle":1.143,
		"light rain":1.143,
		"moderate rain":1.143,
		"heavy intensity rain":1.3348,
		"very heavy rain":1.3348,
		"extreme rain":1.3348,
		"freezing rain":1.3348,
		"light intensity shower rain":1,
		"shower rain":1.143,
		"heavy intensity shower rain":1.143,
		"ragged shower rain":1.143,
		"light snow":1.19,
		"snow":1.19,
		"heavy snow":1.5254,
		"sleet":1.19,
		"light shower sleet":1.19,
		"shower sleet":1.19,
		"light rain and snow":1.19,
		"rain and snow":1.19,
		"light shower snow":1.19,
		"shower snow":1.19,
		"heavy shower snow":1.5254
	}
	current_time = datetime.datetime.now()
	if current_time.hour >= 0 and current_time.hour < 6:
		return switcher1.get(status, 1)
	if current_time.hour >= 19 and current_time.hour <= 23:
		return switcher1.get(status, 1)
	if current_time.hour >= 6 and current_time.hour < 9:
		return switcher2.get(status, 1)
	if current_time.hour >= 9 and current_time.hour < 15:
		return switcher3.get(status, 1)
	if current_time.hour >= 15 and current_time.hour < 19:
		return switcher4.get(status, 1)