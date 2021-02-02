import requests
from clients.BaseClient import BaseClient


class ApplicationClient(BaseClient):
	def __init__(self, main_url):
		self.url = main_url + "/applications/"

	def post(self, subscriber_id, status, title, description):
		return requests.post(url=self.url, data={
			'subscriberId': subscriber_id,
			'status': status,
			'title': title,
			'description': description
		})
