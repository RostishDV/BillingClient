import requests


class Subscriber2RateClient:
    session = requests.Session()

    def __init__(self, main_url, session):
        self.url = main_url + "/subscriber2rates/"
        self.session = session

    def post(self, subscriber_id, rate_id):
        return self.session.post(url=self.url, data={
            'subscriberId': subscriber_id,
            'rateId': rate_id
        })

    # def get_by_id(self, identity):
    # 	return requests.get(url=self.url + str(identity))

    def get_all(self):
        return self.session.get(url=self.url)
