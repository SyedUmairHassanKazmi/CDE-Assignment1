import requests
import json
from pprint import pprint
country_code = 'PK'
url = f'http://dataservice.accuweather.com/locations/v1/adminareas/{country_code}?'
api_key = "GP41lGEhrM35tGsoOSJoQAAeJXNRIfHs"
query_params = { 'apikey' : api_key } 
response = requests.get(
    url= url,
    params=query_params,
)
locations_json = response.content.decode('utf-8')
locations = json.loads(locations_json)
pprint(locations)

'''
Output


>>> import requests
>>> import json
>>> from pprint import pprint
>>> country_code = 'PK'
>>> url = f'http://dataservice.accuweather.com/locations/v1/adminareas/{country_code}?'
>>> api_key = "GP41lGEhrM35tGsoOSJoQAAeJXNRIfHs"
>>> query_params = { 'apikey' : api_key }
>>> response = requests.get(
...     url= url,
...     params=query_params,
... )
>>> 
>>> locations_json = response.content.decode('utf-8')
>>> locations = json.loads(locations_json)
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


  '''