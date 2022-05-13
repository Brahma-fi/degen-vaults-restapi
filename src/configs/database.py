from dataclasses import dataclass,fields
@dataclass
class Vaults():
    ethmaxi: str
    pmusdc: str

    def is_valid_vault(self, vault_name) -> bool:
        for field in fields(self.__class__):
            if field.name == vault_name:
                return True
        return False
@dataclass
class TableNames():
    historic_rewards: str
    buffer_values: str
    open_positions: str
    share_price_db: str 
    ethmaxi_share_price_db: str

DATABASE_NAME = 'protected_moonshots_activity'
VAULTS = Vaults('ethmaxi', 'pmusdc')
TABLE_NAMES = TableNames(
    'historic_rewards',
    'buffer_values',
    'open_positions',
    'share_price_db',
    'ethmaxi_share_price_db'
)