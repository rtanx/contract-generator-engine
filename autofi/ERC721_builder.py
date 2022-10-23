
from .contract_template import ContractTemplate


class ERC721Builder(ContractTemplate):

    def contract_name(self, name: str = "TykoonNft"):
        self._render_args['contract_name'] = name
        pass

    # def set_symbol_name(self, token_name: str, token_symbol: str) -> None:
    #     self._render_args['token_name'] = token_name
    #     self._render_args['token_symbol'] = token_symbol

    # def mintable(self, with_auto_increment_id: bool = True):
    #     self._render_args['mintable'] = {
    #         'is_mintable': True,
    #         'auto_increment_id': with_auto_increment_id
    #     }

    # def baseURI(self, uri: str, changeable: bool = False):
    #     self._render_args['base_uri'] = {
    #         'uri': uri,
    #         'changeable': changeable
    #     }

    def render(self) -> str:
        return self._erc721().render(self._render_args)
