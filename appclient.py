import requests
import os

port = os.environ['FLASK_PORT']
if not port:
    port = 1738


r = requests.get('http://10.92.21.107:{}/'.format(port))
print(r.text)
