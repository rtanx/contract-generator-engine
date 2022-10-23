from typing import Dict, Union, List
from pathlib import Path
from semantic_version import Version
import solcx

from autofi.Contract import Contract


class Compiler:
    def __init__(self, content: str, contract_name: str, solc_version: Version = 'latest') -> None:
        self._solc_version: Version = solc_version
        solcx.install_solc(self._solc_version)

        self._content: str = content
        if contract_name.endswith('.sol'):
            self._file_name = contract_name
            self._contract_name = Path(contract_name).stem
        else:
            self._file_name = f'{contract_name}.sol'
            self._contract_name = contract_name

        self._allowed_paths: Union[List, Path, str] = '.'
        self._input_data: Dict = {
            'language': 'Solidity',
            'sources': {self._file_name: {
                'content': self._content
            }},
            'settings': {
                'outputSelection': {
                    '*': {
                        '*': ['abi', 'metadata', 'evm.bytecode', 'evm.bytecode.sourceMap']
                    }
                },
                'remappings': ['@openzeppelin=contracts/library/node_modules/@openzeppelin', 'erc721a=contracts/library/node_modules/erc721a']
            }
        }

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, contract_content: str) -> None:
        self._content = contract_content

    @property
    def allow_paths(self) -> Union[List, Path, str]:
        return self._allowed_paths

    @allow_paths.setter
    def allow_paths(self, paths: Union[List, Path, str] = None) -> None:
        self._allowed_paths = paths

    @property
    def path_remappings(self) -> List:
        return self._input_data['settings']['remappings']

    @path_remappings.setter
    def path_remappings(self, paths: List) -> None:
        self._input_data['settings']['remappings'] = paths

    def compile(self) -> Contract:
        out = solcx.compile_standard(self._input_data, solc_version=self._solc_version, allow_paths=self._allowed_paths)
        return Contract(self._file_name, self._contract_name, out)
