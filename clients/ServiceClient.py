import requests
from clients.BaseClient import BaseClient


class ServiceClient(BaseClient):
	def __init__(self, main_url):
		self.url = main_url + "/subscribers/"

	def post(self, name, price):
		return requests.post(url=self.url, data={'name': name, 'price': price})

	def get_by_id(self, identity):
		return requests.get(url=self.url + str(identity))

	def get_all(self):
		return requests.get(url=self.url)