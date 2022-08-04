import requests
import json
from pprint import pprint


# 1st endpoint

# Give Country Code
country_code = 'PK'
url = f'http://dataservice.accuweather.com/locations/v1/adminareas/{country_code}?'

# Use api key taken from accuweather
api_key = "GP41lGEhrM35tGsoOSJoQAAeJXNRIfHs"

query_params = { 'apikey' : api_key } 
response = requests.get(
    url= url,
    params=query_params,
)
locations_json = response.content.decode('utf-8')
locations = json.loads(locations_json)
# Print locations in specific country
pprint(locations)


# 2nd endpoint

url2 = f'https://dataservice.accuweather.com/locations/v1/cities/search?'
# input some words that specific to your city
input_words = 'Karachi,Sindh,Pakistan'
query_params2 = { 'apikey' : api_key, 'q' : input_words } 
response2 = requests.get(
    url= url2,
    params=query_params2,
)
city_details_json = response2.content.decode('utf-8')
city_details = json.loads(city_details_json)
pprint(city_details)
# Get city key from it

city_key = city_details[0]['Key']

# 3rd endpoint
# Use that city key to get current conditions of your respective city

url3 = f'https://dataservice.accuweather.com/currentconditions/v1/{city_key}?'
query_params3 = { 'apikey' : api_key } 
response3 = requests.get(
    url= url3,
    params=query_params3,
)
city_current_conditions_json = response3.content.decode('utf-8')
city_current_conditions = json.loads(city_current_conditions_json)
pprint(city_current_conditions)

'''
Output


>>> import requests
>>> import json
>>> from pprint import pprint
>>> # 1st endpoint
>>> # Give Country Code
>>>
>>> country_code = 'PK'
>>> url = f'http://dataservice.accuweather.com/locations/v1/adminareas/{country_code}?'
>>> # Use api key taken from accuweather
>>>
>>> api_key = "GP41lGEhrM35tGsoOSJoQAAeJXNRIfHs"
>>> query_params = { 'apikey' : api_key } 
>>> response = requests.get(
...     url= url,
...     params=query_params,
... )
>>> 
>>> locations_json = response.content.decode('utf-8')
>>> locations = json.loads(locations_json)
>>> # Print locations in specific country
>>> 
>>> pprint(locations)
[{'CountryID': 'PK',
  'EnglishName': 'Balochistan',
  'EnglishType': 'Province',
  'ID': 'BA',
  'Level': 1,
  'LocalizedName': 'Balochistan',
  'LocalizedType': 'Province'},
 {'CountryID': 'PK',
  'EnglishName': 'Gilgit-Baltistan',
  'EnglishType': 'Pakistan Administered Area',
  'ID': 'GB',
  'Level': 1,
  'LocalizedName': 'Gilgit-Baltistan',
  'LocalizedType': 'Pakistan Administered Area'},
 {'CountryID': 'PK',
  'EnglishName': 'Islamabad',
  'EnglishType': 'Capital Territory',
  'ID': 'IS',
  'Level': 1,
  'LocalizedName': 'Islamabad',
  'LocalizedType': 'Capital Territory'},
 {'CountryID': 'PK',
  'EnglishName': 'Azad Jammu and Kashmir',
  'EnglishType': 'Pakistan Administered Area',
  'ID': 'JK',
  'Level': 1,
  'LocalizedName': 'Azad Jammu and Kashmir',
  'LocalizedType': 'Pakistan Administered Area'},
 {'CountryID': 'PK',
  'EnglishName': 'Khyber Pakhtunkhwa',
  'EnglishType': 'Province',
  'ID': 'KP',
  'Level': 1,
  'LocalizedName': 'Khyber Pakhtunkhwa',
  'LocalizedType': 'Province'},
 {'CountryID': 'PK',
  'EnglishName': 'Punjab',
  'EnglishType': 'Province',
  'ID': 'PB',
  'Level': 1,
  'LocalizedName': 'Punjab',
  'LocalizedType': 'Province'},
 {'CountryID': 'PK',
  'EnglishName': 'Sindh',
  'EnglishType': 'Province',
  'ID': 'SD',
  'Level': 1,
  'LocalizedName': 'Sindh',
  'LocalizedType': 'Province'},
 {'CountryID': 'PK',
  'EnglishName': 'Federally Administered Tribal Areas',
  'EnglishType': 'Territory',
  'ID': 'TA',
  'Level': 1,
  'LocalizedName': 'Federally Administered Tribal Areas',
  'LocalizedType': 'Territory'}]
>>> # 2nd endpoint
>>>
>>> url2 = f'https://dataservice.accuweather.com/locations/v1/cities/search?'
>>> # input some words that specific to your city
>>>
>>> input_words = 'Karachi,Sindh,Pakistan'
>>> query_params2 = { 'apikey' : api_key, 'q' : input_words }
>>> response2 = requests.get(
...     url= url2,
...     params=query_params2,
... )
>>> 
>>> city_details_json = response2.content.decode('utf-8')
>>> city_details = json.loads(city_details_json)
>>> pprint(city_details)
[{'AdministrativeArea': {'CountryID': 'PK',
                         'EnglishName': 'Sindh',
                         'EnglishType': 'Province',
                         'ID': 'SD',
                         'Level': 1,
                         'LocalizedName': 'Sindh',
                         'LocalizedType': 'Province'},
  'Country': {'EnglishName': 'Pakistan',
              'ID': 'PK',
              'LocalizedName': 'Pakistan'},
  'DataSets': ['AirQualityCurrentConditions',
               'AirQualityForecasts',
               'FutureRadar',
               'MinuteCast'],
  'EnglishName': 'Karachi',
  'GeoPosition': {'Elevation': {'Imperial': {'Unit': 'ft',
                                             'UnitType': 0,
                                             'Value': 36.0},
                                'Metric': {'Unit': 'm',
                                           'UnitType': 5,
                                           'Value': 11.0}},
                  'Latitude': 24.89,
                  'Longitude': 67.029},
  'IsAlias': False,
  'Key': '261158',
  'LocalizedName': 'Karachi',
  'PrimaryPostalCode': '',
  'Rank': 11,
  'Region': {'EnglishName': 'Asia', 'ID': 'ASI', 'LocalizedName': 'Asia'},
  'SupplementalAdminAreas': [{'EnglishName': 'Karachi Central',
                              'Level': 2,
                              'LocalizedName': 'Karachi Central'}],
  'TimeZone': {'Code': 'PKT',
               'GmtOffset': 5.0,
               'IsDaylightSaving': False,
               'Name': 'Asia/Karachi',
               'NextOffsetChange': None},
  'Type': 'City',
  'Version': 1}]
>>> # Get city key from it
>>>
>>> city_key = city_details[0]['Key']
>>> # 3rd endpoint
>>> # Use that city key to get current conditions of your respective city
>>>
>>> url3 = f'https://dataservice.accuweather.com/currentconditions/v1/{city_key}?'
>>> query_params3 = { 'apikey' : api_key } 
>>> response3 = requests.get(
...     url= url3,
...     params=query_params3,
... )
>>> 
>>> city_current_conditions_json = response3.content.decode('utf-8')
>>> city_current_conditions = json.loads(city_current_conditions_json)
>>> pprint(city_current_conditions)
[{'EpochTime': 1659599220,
  'HasPrecipitation': False,
  'IsDayTime': True,
  'Link': 'http://www.accuweather.com/en/pk/karachi/261158/current-weather/261158?lang=en-us',
  'LocalObservationDateTime': '2022-08-04T12:47:00+05:00',
  'MobileLink': 'http://www.accuweather.com/en/pk/karachi/261158/current-weather/261158?lang=en-us',
  'PrecipitationType': None,
  'Temperature': {'Imperial': {'Unit': 'F', 'UnitType': 18, 'Value': 90.0},
                  'Metric': {'Unit': 'C', 'UnitType': 17, 'Value': 32.2}},
  'WeatherIcon': 6,
  'WeatherText': 'Mostly cloudy'}]

  
  '''