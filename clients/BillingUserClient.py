from clients.BaseClient import BaseClient


class BillingUserClient(BaseClient):
    def post(self, name, password, privilege):
        return self.session.post(url=self.url, data={
            'name': name,
            'password': password,
            'privilege': privilege
        })
