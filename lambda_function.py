import requests

from schedule import Schedule


def lambda_handler(event, context):
    schedules = get_schedules()
    return 'hello'


# create a method to call the database library api and get one schedule at a time
# with each schedule we get from the database we should call the ingestion api with
# those specific parameters
def get_schedules():
    schedules_request = requests.get("http://127.0.0.1:8080/schedule/all")
    schedules_json = schedules_request.json()

    schedules = []
    for schedule_json in schedules_json:
        print(schedule_json)
        symbol = schedule_json.get('symbol')
        function = schedule_json.get('function')
        interval = schedule_json.get('interval')
        from_currency = schedule_json.get('fromCurrency')
        to_currency = schedule_json.get('toCurrency')
        market = schedule_json.get('market')

        schedule = Schedule(symbol, function, interval, from_currency, to_currency, market)
        schedules.append(schedule)

    return schedules


# create a method that calls the ingestion api
def trigger_ingestion_api(schedule):
    uri = 'http://127.0.0.1:8081/ingest/stocks'

    uri += '/' + schedule.function
    uri += '/' + schedule.symbol
    uri += '/' + schedule.interval
    uri += '/full'

    print(uri)

    request = requests.get(uri)

    return 1


schedules = get_schedules()

for s in schedules:
    trigger_ingestion_api(s)
