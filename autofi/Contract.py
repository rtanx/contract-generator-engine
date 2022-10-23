import json


class Contract(dict):
    def __init__(self, file_name: str, contract_name: str, mapping=None):
        super().__init__(mapping)
        self._file_name = file_name
        self._contract_name = contract_name

    @property
    def bytecode(self):
        return self.get('contracts', {}).get(self._file_name, {}).get(self._contract_name, {}).get('evm', {}).get('bytecode', {}).get('object', None)

    @property
    def abi(self):
        return self.json_loads.get('output', {}).get('abi')

    @property
    def json_loads(self):
        return json.loads(self.get('contracts', {}).get(self._file_name, {}).get(self._contract_name, {}).get('metadata', {}))
