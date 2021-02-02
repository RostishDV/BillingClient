import requests
from clients.BaseClient import BaseClient

class RateClient(BaseClient):
	def __init__(self, main_url):
		self.url = main_url + "/subscribers/"

	def post(self, name, price):
		return requests.post(url=self.url, data={'name': name, 'price': price})

