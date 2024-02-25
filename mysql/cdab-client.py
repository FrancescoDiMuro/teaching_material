from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.location import Location
from json import dump
import requests
import argparse

# Definizione del base URL e dell'endpoint per effettuare la richiesta
BASE_URL: str = 'https://api.open-meteo.com/v1'
FORECAST_ENDPOINT: str = 'forecast'

def config_parser() -> argparse.ArgumentParser:
    
    # Creazione e configurazione del parser per la CLI
    parser = argparse.ArgumentParser(prog='cdab-client', 
                                     description='CDAB-Client used to gather data from Weather API and save them to a JSON file.',
                                     epilog='More info at [link]')

    parser.add_argument('--lat', 
                        type=float,
                        required=True,
                        help='Latitude coordinate of the place to retrieve weather data')
                        
    parser.add_argument('--lon', 
                        type=float, 
                        required=True,
                        help='Longitude coordinate of the place to retrieve weather data')

    parser.add_argument('-v', '--variables', 
                        required=True, 
                        help='List of variables to get data from', 
                        metavar='v1,v2,v3,...vn')

    parser.add_argument('-sd', '--start-date', 
                        help='Start date to get data from', 
                        metavar='YYYY-MM-DD')

    parser.add_argument('-ed', '--end-date', 
                        help='End date to get data from', 
                        metavar='YYYY-MM-DD')
    
    return parser


def get_response_body(base_url: str, endpoint: str, parser_args: argparse.Namespace) -> dict:

    # Ottenimento dei valori dei parametri della richiesta dalla riga di comando
    latitude: float = parser_args.lat
    longitude: float = parser_args.lon
    variables: str = parser_args.variables.replace(' ', '')
    start_date: str = parser_args.start_date
    end_date: str = parser_args.end_date

    # Composizione del dict dei query parameters da passare alla richiesta
    query_parameters: dict = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': variables
    }

    if start_date:
        query_parameters['start_date'] = start_date

    if end_date:
        query_parameters['end_date'] = end_date

    # Definizione dell'URL della richiesta
    request_url: str = f'{base_url}/{endpoint}'

    # Effettuazione della richiesta
    response: requests.Response = requests.get(url=request_url, params=query_parameters)

    # Se la rihiesta e' andata a buon fine
    if response.status_code == 200:

        # Ottenimento del response body
        response_body: dict = response.json()

        return response_body


def get_city_name_from_coordinates(latitude: float, longitude: float) -> str:

    # Ottenimento del geolocator per ottenere il nome della citta'
    # partendo dai parametri di latitudine e longitudine
    geolocator = Nominatim(user_agent='MyApp')
    coordinates: str = f'{latitude},{longitude}'
    location: Location = geolocator.reverse(coordinates)
    address: dict = location.raw['address']
    city: str = address['city']

    return city


def get_time_delta(start_date: str, end_date: str) -> int:

    DEFAULT_TIME_DELTA: int = 7
    DATE_FORMAT: str = '%Y-%m-%d'
    
    if start_date == None or end_date == None:
        return DEFAULT_TIME_DELTA
    
    if start_date < end_date:
        time_delta: int = (datetime.strptime(end_date, DATE_FORMAT) - datetime.strptime(start_date, DATE_FORMAT)).days

    return time_delta

def write_json(file_name: str):
    
    # Creazione e apertura del file in modalita' "scrittura", serializzando la response per essere scritta nel file
    with open(file=file_name, mode='w') as output:
        dump(response_body, output)


if __name__ == '__main__':

    parser: argparse.ArgumentParser = config_parser()
    
    parser_args: argparse.Namespace = parser.parse_args()
    
    response_body: dict = get_response_body(base_url=BASE_URL, 
                                            endpoint=FORECAST_ENDPOINT, 
                                            parser_args=parser_args)

    if response_body:
        city: str = get_city_name_from_coordinates(latitude=parser_args.lat, 
                                                   longitude=parser_args.lon)
    
        time_delta = get_time_delta(start_date=parser_args.start_date,
                                    end_date=parser_args.end_date)
    
        file_name: str = f'{city}_{FORECAST_ENDPOINT}_{time_delta}_day{'s' if time_delta > 1 else ''}.json'

        write_json(file_name=file_name)