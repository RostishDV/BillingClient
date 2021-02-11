from clients.BaseClient import BaseClient


class SubscriberClient(BaseClient):
    def post(self, surname, name, patronymic, city, street, house, building, apartment, phone):
        return self.session.post(url=self.url, data={
            'surname': surname,
            'name': name,
            'patronymic': patronymic,
            'city': city,
            'street': street,
            'house': house,
            'building': building,
            'apartment': apartment,
            'phone': phone
        })
