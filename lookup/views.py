from django.shortcuts import render

# Create your views here.

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=89129&distance=5&API_KEY=1C856C7F-40FB-4C12-BF44-E34F3AC82E01

def home(request) :
	import json
	import requests

	print("Jisdfhidshifh")

	api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=1C856C7F-40FB-4C12-BF44-E34F3AC82E01')

	api = json.loads(api_request.content)

	qualityDesc = {

		'Good' : 'Good (0 - 50) : Air quality is considered satisfactory, and air pollution poses little or no risk.',
		'Moderate' : 'Moderate (51 - 100) : Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.',
		'Unhealthy for Sensitive Groups' : 'Unhealthy for Sensitive Groups (101 - 150) : Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.',
		'Unhealthy' : 'Unhealthy (151 - 200) : Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.',
		'Very Unhealthy' : 'Very Unhealthy (201 - 300) : Health alert: everyone may experience more serious health effects.',
		'Hazardous' : 'Hazardous (301 - 500) : Health warnings of emergency conditions. The entire population is more likely to be affected.',

	}

	key = api[0]['Category']['Name']

	content = {
		'api' : api,
		'qualitydesc' : qualityDesc[key],
	}

	return render(request, 'home.html', content)

def about(request):
	return render(request, 'about.html', {})
