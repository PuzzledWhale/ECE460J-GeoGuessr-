import pandas as pd
from geopy.geocoders import Nominatim
import ssl
import certifi
import time
import requests



# Load the CSV file
df = pd.read_csv('Streetview_Image_Dataset/coordinates.csv')
print(df.head())

def get_country(latitude, longitude,row_number):
    api_key = ""  # Replace with your Google Maps API key
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    #print(response.json())
    data = response.json()
    if data['status'] == 'OK':
        results = data['results']
        if results:
            for result in results:
                address_components = result['address_components']
                for component in address_components:
                    if 'country' in component['types']:
                        return component['long_name']
    return None


for i in range(0, len(df), 500):
    print(i)
    df2 = df[i:i+500]
    df2['Country'] = df2.apply(lambda x: get_country(x['latitude'], x['longitude'], x.name), axis=1)
    df2.to_csv(f'Everything{i}.csv', index=False)
    df2.drop(columns=['latitude', 'longitude'], inplace=True)
    df2.to_csv(f'Onlycountries{i}.csv', index=False)
