import requests


class BaseClient:
	url = ''
	session = requests.Session()

	def __init__(self, main_url, session):
		self.url = main_url + "/payments/"
		self.session = session

	def get_by_id(self, identity):
		return self.session.get(url=self.url + str(identity))

	def get_all(self):
		return self.session.get(url=self.url)

	def delete_by_id(self, identity):
		return self.session.delete(url=self.url + str(identity))

