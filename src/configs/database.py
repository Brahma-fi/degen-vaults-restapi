from dataclasses import dataclass,fields

@dataclass
class VaultInfo():
    name: str
    address: str
    token: str
    decimals: int

@dataclass
class Vaults():
    ethmaxi: VaultInfo
    pmusdc: VaultInfo

    def is_valid_vault(self, vault_name) -> bool:
        for field in fields(self.__class__):
            if field.name == vault_name:
                return True
        return False

    def get_vaults(self):
        return [field.name for field in fields(self.__class__)]

@dataclass
class TableNames():
    historic_rewards: str
    buffer_values: str
    open_positions: str
    share_price_db: str 
    ethmaxi_share_price_db: str

DATABASE_NAME = 'protected_moonshots_activity'
VAULTS = Vaults(
    VaultInfo(
        'ethmaxi',
        '0xAa0508FcD0352B206F558b2B817dcC1F0cc3F401', 
        '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
        1e18
    ), 
    VaultInfo(
        'pmusdc', 
        '0x1C4ceb52ab54a35F9d03FcC156a7c57F965e081e',
        '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
        1e6
    )
)
TABLE_NAMES = TableNames(
    'historic_rewards',
    'buffer_values',
    'open_positions',
    'share_price_db',
    'ethmaxi_share_price_db'
)