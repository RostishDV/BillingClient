import requests


class BaseClient:
	url = ''

	def get_by_id(self, identity):
		return requests.get(url=self.url + str(identity))

	def get_all(self):
		return requests.get(url=self.url)

	def delete_by_id(self, identity):
		return requests.delete(url=self.url + str(identity))

