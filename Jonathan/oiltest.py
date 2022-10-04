import requests

base_currency = 'USD'
symbol = 'BRENTOIL' 
start_date = "2021-09-01"
end_date = "2021-09-25"
endpoint = 'timeseries'
access_key = 'b3ow5l0y74ue0724gtnu0hpqls7j1rf85xlyd9f9cfm9ynp15v2rd9o3zq8g'
resp = requests.get(
    'https://www.commodities-api.com/api/'+endpoint+'?access_key='+access_key+'&start_date='+start_date+'&end_date='+end_date+'&base='+base_currency+'&symbols='+symbol)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /'+endpoint+'/ {}'.format(resp.status_code))
print(resp.json())
