import requests
from clients.BaseClient import BaseClient


class SubscriberClient(BaseClient):
	def __init__(self, main_url):
		self.url = main_url + "/subscribers/"

	def post(self, surname, name, patronymic, city, street, house, building, apartment, phone):
		return requests.post(url=self.url,
		                     data={'surname': surname,
		                           'name': name,
		                           'patronymic': patronymic,
		                           'city': city,
		                           'street': street,
		                           'house': house,
		                           'building': building,
		                           'apartment': apartment,
		                           'phone': phone})

