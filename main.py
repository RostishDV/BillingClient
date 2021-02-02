import requests
from clients.ApplicationClient import ApplicationClient
from clients.BillingUserClient import BillingUserClient
from clients.DebitClient import DebitClient
from clients.PaymentClient import PaymentClient
from clients.RateClient import RateClient
from clients.ServiceClient import ServiceClient
from clients.Subscriber2RateClient import Subscriber2RateClient
from clients.Subscriber2ServiceClient import Subscriber2ServiceClient
from clients.SubscriberClient import SubscriberClient

main_url = 'http://localhost:8080/'

app_cli = ApplicationClient(main_url)
billing_user_cli = BillingUserClient(main_url)
debit_cli = DebitClient(main_url)
payment_cli = PaymentClient(main_url)
rate_cli = RateClient(main_url)
service_cli = ServiceClient(main_url)
sub_to_rate_cli = Subscriber2RateClient(main_url)
sub_to_service_cli = Subscriber2ServiceClient(main_url)
sub_cli = SubscriberClient(main_url)


sub_resp_list = []

for i in range(100):
	resp = sub_cli.post('Иванов', 'Иван', 'Иванович', 'Чебоксары', 'пр.Мира', '40', '0', '206')

	if resp.status_code == 200:
		sub_resp_list.append(resp)

for resp in sub_resp_list:
	print(resp.json())

