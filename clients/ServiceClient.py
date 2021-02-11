from clients.BaseClient import BaseClient


class ServiceClient(BaseClient):
	def post(self, name, price):
		return self.session.post(url=self.url, data={'name': name, 'price': price})

	def get_by_id(self, identity):
		return self.session.get(url=self.url + str(identity))

	def get_all(self):
		return self.session.get(url=self.url)

