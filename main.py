import random
import time

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

user = "user"
password = "password"

session = requests.Session()
session.auth = (user, password)

app_cli = ApplicationClient(main_url, session)
billing_user_cli = BillingUserClient(main_url, session)
debit_cli = DebitClient(main_url, session)
payment_cli = PaymentClient(main_url, session)
rate_cli = RateClient(main_url, session)
service_cli = ServiceClient(main_url, session)
sub_to_rate_cli = Subscriber2RateClient(main_url, session)
sub_to_service_cli = Subscriber2ServiceClient(main_url, session)
sub_cli = SubscriberClient(main_url, session)


# sub_resp_list = []
# billing_user_resp_list = []
# debit_resp_list = []
# payment_resp_list = []





# start = time.time()
# for i in range(100):
# 	sub_resp = sub_cli.post('Иванов', 'Иван', 'Иванович', 'Чебоксары', 'пр.Мира', '40', '0', '206', 777777)
#
# 	if sub_resp.status_code == 200:
# 		sub_resp_list.append(sub_resp)
#
# print(f'spend time for add sub requests {time.time() - start}, generated sub_lis {len(sub_resp_list)}')

#
# start = time.time()
# successful_list = []
# unsuccessful_list = []
# for sub_resp in sub_resp_list:
# 	for i in range(10):
# 		app_resp = app_cli.post(sub_resp.json(), 'New', 'Install app', 'Install something application')
# 		if app_resp.status_code == 200:
# 			successful_list.append(app_resp)
# 		else:
# 			unsuccessful_list.append(app_resp)

print(f'spend time for add app requests {time.time() - start}')

#
# for resp in successful_list:
# 	print(f'    {resp.status_code}')
#
# print('unsuccessful')
# for resp in unsuccessful_list:
# 	print(f'    {resp.status_code}')

# start = time.time()
# for sub_resp in sub_resp_list:
# 	new_subs_resp = sub_cli.delete_by_id(sub_resp.json())
#
# print(f'spend time for delete requests {time.time() - start}')
