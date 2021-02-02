import requests


class Subscriber2ServiceClient:
	def __init__(self, main_url):
		self.url = main_url + "/subscriber2rates/"

	def post(self, subscriber_id, rate_id):
		return requests.post(url=self.url, data={'subscriberId': subscriber_id,
		                                         'rateId': rate_id})

	def get_by_id(self, subscriber_id, rate_id):
		return requests.get(url=f'{self.url + str(subscriber_id)} {str(rate_id)}')

	# def get_all(self):
	# 	return requests.get(url=self.url)

	def delete_by_id(self, subscriber_id, rate_id):
		return requests.delete(url=f'{self.url + str(subscriber_id)} {str(rate_id)}')


