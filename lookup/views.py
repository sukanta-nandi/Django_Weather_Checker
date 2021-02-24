from django.shortcuts import render
from django.shortcuts import redirect
import sys

# Create your views here.

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=89129&distance=5&API_KEY=1C856C7F-40FB-4C12-BF44-E34F3AC82E01





def test_view(request):
	import json
	import requests

	#Receives the API request in the form of json Response
	api_request = requests.get('https://api.waqi.info/feed/kolkata/?token=6438f0c4c1e4f5fddd548f2a4e5ac887d6729dde')


	print(api_request)

	#Parses the json Response into list
	request_list = json.loads(api_request.content)

	#print(request_list)

	context = {
		'list' : request_list['data']['aqi']
	}

	return render(request, 'test.html', context)


def airnow(request):

	import requests
	import json

	#default zip code
	zipcode = '90201'

	if request.method == "POST":
		zipcode = request.POST['zipcode']
	
	#Receives the API request in the form of json Response
	api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+ zipcode +'&distance=5&API_KEY=1C856C7F-40FB-4C12-BF44-E34F3AC82E01')


	#Parses the json Response into list
	api = json.loads(api_request.content)


	#get the area
	area = api[0]['ReportingArea']

	# get the state
	state = api[0]['StateCode']

	param_pm25 = {}
	param_O3 = {}
	param_pm10 = {}

	primary_poll = ''

	param_count = len(api)

	max_aqi = -1

	for i in range(0, param_count):

		param = api[i]['ParameterName']

		if param == 'PM2.5':
			param_pm25['aqi'] = api[i]['AQI']
			param_pm25['aqi_status'] = api[i]['Category']['Name']
			

			if int(param_pm25['aqi']) > max_aqi :
				max_aqi = int(param_pm25['aqi'])
				primary_poll = 'PM2.5'

		if param == 'O3':
			param_O3['aqi'] = api[i]['AQI']
			param_O3['aqi_status'] = api[i]['Category']['Name']

			if int(param_O3['aqi']) > max_aqi :
				max_aqi = int(param_O3['aqi'])
				primary_poll = 'O3'

		if param == 'PM10' :
			param_pm10['aqi'] = api[i]['AQI']
			param_pm10['aqi_status'] = api[i]['Category']['Name']

			if int(param_pm10['aqi']) > max_aqi :
				max_aqi = int(param_pm10['aqi'])
				primary_poll = 'PM10'

	primary_poll_aqi = str(max_aqi)
	

	print(primary_poll)
	print(primary_poll_aqi)

	print(param_pm25)
	print(param_pm10)
	print(param_O3)

	context = {
		'area' : area,
		 'st'  : state,
		'zip'  : zipcode,
		'primary' : primary_poll,
		'max_aqi' : primary_poll_aqi,
		'pm25' : param_pm25,
		'pm10' : param_pm10,
		
	}

	return render(request, 'airnow.html', context)
