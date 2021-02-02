import requests
from clients.BaseClient import BaseClient


class BillingUserClient(BaseClient):
	def __init__(self, main_url):
		self.url = main_url + "/billingUsers/"

	def post(self, name, password, privilege):
		return requests.post(url=self.url, data={'name': name,
		                                         'password': password,
		                                         'privilege': privilege})
