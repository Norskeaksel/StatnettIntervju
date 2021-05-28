import keplergl
import countrygroups
from covidData import *
from geoData import *
from mapConfiguration import c

countries = countrygroups.EUROPEAN_UNION.names
countries += ['United Kingdom', 'Norway', 'Switzerland']

start = '2020-01-01T00:00:00Z'
end = '2021-05-26T00:00:00Z'

print('Loading Covid Data')
covid_data = countriesCovidData(countries, start, end)
covid_data.to_csv('covidDataBackup.csv', index=False)
# covid_data=pd.read_csv("covidDataBackup.csv")

print('Adding geo data')
covid_gdf = gpd.GeoDataFrame(covid_data, geometry=gpd.points_from_xy(covid_data.Lon, covid_data.Lat))
historic_covid_gdf = covid_gdf.loc[covid_gdf['Date'] != end]
myMap = keplergl.KeplerGl(height=500, config=c)
myMap.add_data(data=historic_covid_gdf, name='Historic Covid Data')

last_covid_data = covid_data.loc[covid_data['Date'] == end]
aggregated_last_covid_data = last_covid_data.groupby('Country').sum().reset_index()
aggregated_last_covid_data['Date'] = end
last_covid_geo_data = addGeoData(aggregated_last_covid_data)
myMap.add_data(data=last_covid_geo_data, name='Last Covid Data')

myMap.save_to_html(file_name='Covid_Data.html')

"""countries_url="https://api.covid19api.com/countries"
available_countries=readURL(countries_url)
countries=[]
for dict in available_countries:
    countries.append(dict['Country'])
tolerance = 10 * 360 / 43200
world["geometry"] = world.geometry.simplify(tolerance=tolerance, preserve_topology=True)    
"""
