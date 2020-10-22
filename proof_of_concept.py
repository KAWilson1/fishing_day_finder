import secret

from weatherbit.api import Api

api = Api(secret.API_KEY)
api.set_granularity('hourly')

history = api.get_history(city="Carmel", state="Indiana", country="US", start_date="2020-10-18", end_date="2020-10-19")
for day in history.get_series(['pres']):
	date = day['datetime'].strftime("%m/%d/%y @ %H")
	print("Pressure on " + date, ":", day['pres'] / 33.864, "inHg") #convert milibar to inHg
print()

history = api.get_history(city="Carmel", state="Indiana", country="US", start_date="2020-10-19", end_date="2020-10-20")
for day in history.get_series(['pres']):
	date = day['datetime'].strftime("%m/%d/%y @ %H")
	print("Pressure on " + date, day['pres'] / 33.864, "inHg") #convert milibar to inHg
print()

history = api.get_history(city="Carmel", state="Indiana", country="US", start_date="2020-10-20", end_date="2020-10-21")
for day in history.get_series(['pres']):
	date = day['datetime'].strftime("%m/%d/%y @ %H")
	print("Pressure on " + date, day['pres'] / 33.864, "inHg") #convert milibar to inHg
print()

history = api.get_history(city="Carmel", state="Indiana", country="US", start_date="2020-10-21", end_date="2020-10-22")
for day in history.get_series(['pres']):
	date = day['datetime'].strftime("%m/%d/%y @ %H")
	print("Pressure on " + date, day['pres'] / 33.864, "inHg") #convert milibar to inHg
print()

forecast = api.get_forecast(city="Carmel", state="Indiana", country="US")
for day in forecast.get_series(['pres']):
	date = day['datetime'].strftime("%m/%d/%y @ %H")
	print("Pressure on " + date, day['pres'] / 33.864, "inHg") #convert milibar to inHg
	print()
