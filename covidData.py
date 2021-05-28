import pandas as pd
import requests
import time
from tqdm import tqdm


def readURL(url):
    throttled_request_error: int = 429
    status_code = throttled_request_error
    while status_code == throttled_request_error:
        r = requests.get(url)
        status_code = r.status_code
        if status_code == throttled_request_error:
            time.sleep(1)

    return r.json()


def countryCovidData(country, start, end):
    url = f"https://api.covid19api.com/country/{country}?from={start}&to={end}"
    url_data = readURL(url)
    url_df = pd.DataFrame(url_data)
    return url_df


def countriesCovidData(countries, start, end):
    df_list = []
    for country in tqdm(countries):
        covid_data = countryCovidData(country, start, end)
        dropColumns = ['ID', 'Province', 'CountryCode', 'City', 'CityCode']  # , 'Lat', 'Lon']
        sparse_covid_data = covid_data.drop(columns=dropColumns)
        df_list.append(sparse_covid_data)

    full_df = pd.concat(df_list)
    return full_df
