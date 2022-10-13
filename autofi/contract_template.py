from jinja2 import Environment, PackageLoader, Template, select_autoescape
from .constants import TokenStandard


class ContractTemplate:

    _render_args = {}

    def __init__(self) -> None:
        self._jinja_env = Environment(loader=PackageLoader(
            'autofi'), autoescape=select_autoescape(), trim_blocks=True, lstrip_blocks=True)
        pass

    def _erc721(self) -> Template:
        template = self._jinja_env.get_template('erc721.sol.jinja')
        return template
