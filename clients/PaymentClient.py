from clients.BaseClient import BaseClient


class PaymentClient(BaseClient):
    def post(self, subscriber_id, debited_money, previous_balance):
        return self.session.post(url=self.url, data={
            'subscriberId': subscriber_id,
            'debitedMoney': debited_money,
            'previousBalance': previous_balance
        })
