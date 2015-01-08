import requests

with requests.Session() as c:
    url = ''
    USERNAME = raw_input('Enter your Username: ')
    PASSWORD = raw_input('Enter your Password: ')
    login_data = dict(username=USERNAME, password=PASSWORD)
