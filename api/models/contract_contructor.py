from pydantic import BaseModel, Field
from pydantic import HttpUrl


class ContractConstructor(BaseModel):
    token_name: str = Field(description='The token name must be less than 256 character', max_length=256)
    token_symbol: str = Field(description='The token symbol length must be not greater than 10 character contains only uppercase letters', max_length=10, regex='^[A-Z]+$')
    base_uri: HttpUrl
    max_supply: int
    nft_price_in_idrt: int
    idrt_address: str
