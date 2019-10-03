# lambda function

# import requests module
import requests

# import schedule model
from schedule import Schedule

# import uri constants
from constants import DATABASE_LIBRARY_SCHEDULES_URI
from constants import INGESTION_API_URI

# import schedule keys
from constants import SYMBOL
from constants import FUNCTION
from constants import INTERVAL
from constants import FROM_CURRENCY
from constants import TO_CURRENCY
from constants import MARKET


# lambda handler function invoked by cloud watch
def lambda_handler(event, context):
    schedules = get_schedules()
    return 'hello'


# return a list of all the schedules contained in the database
def get_schedules():
    schedules_request = requests.get(DATABASE_LIBRARY_SCHEDULES_URI)
    schedules_json = schedules_request.json()

    schedules = []
    for schedule_json in schedules_json:
        symbol = schedule_json.get(SYMBOL)
        function = schedule_json.get(FUNCTION)
        interval = schedule_json.get(INTERVAL)
        from_currency = schedule_json.get(FROM_CURRENCY)
        to_currency = schedule_json.get(TO_CURRENCY)
        market = schedule_json.get(MARKET)

        schedule = Schedule(symbol, function, interval, from_currency, to_currency, market)
        schedules.append(schedule)

    return schedules


# trigger the ingestion api to ingest the scheduled stock data
def trigger_ingest_stocks(schedule):
    uri = INGESTION_API_URI

    uri += '/' + schedule.function
    uri += '/' + schedule.symbol
    uri += '/' + schedule.interval
    uri += '/full'

    print(uri)

    request = requests.get(uri)

    return 1


# trigger the ingestion api to ingest the scheduled cryptos data
def trigger_ingest_cryptos(schedule):
    return 1


# trigger the ingestion api to ingest the scheduled forex data
def trigger_ingest_forex(schedule):
    return 1
