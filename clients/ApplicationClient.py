import requests
from clients.BaseClient import BaseClient


class ApplicationClient(BaseClient):
	def post(self, subscriber_id, status, title, description):
		return self.session.post(url=self.url, data={
			'subscriberId': subscriber_id,
			'status': status,
			'title': title,
			'description': description
		})
