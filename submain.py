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

app_cli = ApplicationClient(main_url)
billing_user_cli = BillingUserClient(main_url)
debit_cli = DebitClient(main_url)
payment_cli = PaymentClient(main_url)
rate_cli = RateClient(main_url)
service_cli = ServiceClient(main_url)
sub_to_rate_cli = Subscriber2RateClient(main_url)
sub_to_service_cli = Subscriber2ServiceClient(main_url)
sub_cli = SubscriberClient(main_url)

subs = sub_cli.get_by_id(10)

for subscriber in subs.json():
    print(f'{subscriber}')

#
# print(f'firs {sub_cli.get_by_id(identity).json()}')
# resp = sub_cli.get_by_id(identity)
#
# subscriber = resp.json()
# print(f'id is {subscriber["id"]}')
# resp = app_cli.post(subscriber['id'], 'WORK', 'NOTHING', 'FUCKFUCKFUCKFUCKFUCK')
# print(f'resp status code = {resp.status_code}')
# print(f'resp json code = {resp.json()}')
# print(f'after {sub_cli.get_by_id(identity).json()}')
