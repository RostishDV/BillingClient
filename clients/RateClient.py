from clients.BaseClient import BaseClient


class RateClient(BaseClient):
	def post(self, name, price):
		return self.session.post(url=self.url, data={'name': name, 'price': price})

