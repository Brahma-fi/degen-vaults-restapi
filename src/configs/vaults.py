from dataclasses import dataclass,fields

from configs.database import TABLE_NAMES

@dataclass
class VaultInfo():
    name: str
    address: str
    batcher: str
    token: str
    decimals: int

@dataclass
class MonitoredTokenInfo():
    name: str
    table: str

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
class MonitoredTokens():
    frax: str
    steth: str

    def is_valid_token(self, token_name) -> bool:
        for field in fields(self.__class__):
            if field.name == token_name:
                return True
        return False

    def get_tokens(self):
        return [field.name for field in fields(self.__class__)]


VAULTS = Vaults(
    VaultInfo(
        'ethmaxi',
        '0xAa0508FcD0352B206F558b2B817dcC1F0cc3F401',
        '0x47c84A87A2a972769cc5DeDa28118617E3A48F8C',
        '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
        1e18
    ), 
    VaultInfo(
        'pmusdc', 
        '0x1C4ceb52ab54a35F9d03FcC156a7c57F965e081e',
        '0x1b6BF7Ab4163f9a7C1D4eCB36299525048083B5e',
        '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
        1e6
    )
)
MONITORED_TOKENS = MonitoredTokens(
    MonitoredTokenInfo(
        'frax',
        TABLE_NAMES.frax_monitor
    ),
    MonitoredTokenInfo(
        'steth',
        TABLE_NAMES.steth_monitor
    )
)