import json
import os

from web3 import Web3

from ..configs.database import TABLE_NAMES, VAULTS, VaultInfo
from ..configs.response import RESPONSE_KEYS
from ..utils.queries import Queries

class OnChainQueries():
    def __init__(self) -> None:
        dirname = os.path.dirname(__file__)
        vault_abi_filename = os.path.join(dirname, '../abi/vault.json')
        
        self.w3 = Web3(Web3.HTTPProvider(os.getenv("MAINNET_RPC")))
        self.vault_abi = json.load(open(vault_abi_filename, 'r'))

    def get_tvl(self):
        balances = {}

        for vault_name in VAULTS.get_vaults():
            vault_info: VaultInfo = getattr(VAULTS,vault_name)
            vault = self.w3.eth.contract(
                address = vault_info.address,
                abi = self.vault_abi
            )

            vault_total_supply = vault.functions.totalSupply().call()
            vault_share_price = (Queries().get_all_timestamp_value_data(
                TABLE_NAMES.share_price_db 
                if vault_name == VAULTS.pmusdc.name else 
                TABLE_NAMES.ethmaxi_share_price_db, 
                RESPONSE_KEYS.price
            ))[-1]['price']
            vault_tvl = round((vault_total_supply * vault_share_price) / vault_info.decimals, 2)

            if vault_info.name in balances:
                balances[vault_info.name] += vault_tvl
            else:
                balances[vault_info.name] = vault_tvl

        return balances


    