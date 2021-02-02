import requests
from clients.BaseClient import BaseClient


class DebitClient(BaseClient):
	def __init__(self, main_url):
		self.url = main_url + "/debits/"

	def post(self, subscriber_id, debited_money, previous_balance):
		return requests.post(url=self.url, data={'subscriberId': subscriber_id,
		                                         'debitedMoney': debited_money,
		                                         'previousBalance': previous_balance})

