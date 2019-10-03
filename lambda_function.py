import requests

def lambda_handler(event, context):
    request = requests.get('https://www.alphavantage.co/query?apikey=LKYU6TKSQMII6B85&outputsize=15min&symbol=MSFT&interval=1min&function=TIME_SERIES_INTRADAY')
    print(request)
    return 'hello'
