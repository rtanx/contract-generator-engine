import os

import brownie
from brownie import network, accounts, project


class ContractService:

    def __init__(self) -> None:
        net = os.getenv('NETWORK')
        account_pk = os.getenv('PRIVATE_KEY')
        account_addr = os.getenv('OWNER_ACCOUNT_ADDRESS')
        if not network.is_connected():
            network.connect(net)
        try:
            accounts.at(account_addr)
        except:
            accounts.add(account_pk)

        self._project = None

        for p in project.get_loaded_projects():
            if p.dict().get('Tykoon') is not None:
                self._project = p
                break

        if self._project is None:
            self._project = project.load('project', name='Tykoon')

    def __del__(self):
        network.disconnect()
        self._project.close()

    def scaffold(self, token_name: str, token_symbol: str, metadata_base_uri: str) -> str:
        proj = self._project['Tykoon']
        acc_addr = os.getenv('OWNER_ACCOUNT_ADDRESS')
        deployed_contract = proj.deploy(token_name, token_symbol, metadata_base_uri, {'from': accounts.at(acc_addr), 'required_confs': 0}, publish_source=True)
        return deployed_contract.txid
