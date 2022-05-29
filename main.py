import requests
from pprint import pprint
import time
import datetime

d = datetime.datetime.now() - datetime.timedelta(days=2)
unixtime = time.mktime(d.timetuple())

url = 'https://api.stackexchange.com/2.3/questions'
param = {
    'creation ':unixtime,
    'tagged':'Python',
    'site':'stackoverflow',
    'order':'desc'
}
res = requests.get(url, params=param).json()

pprint(res['items'])