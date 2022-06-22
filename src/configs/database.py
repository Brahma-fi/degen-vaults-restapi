from dataclasses import dataclass,fields

@dataclass
class TableNames():
    historic_rewards: str
    buffer_values: str
    usdc_balances: str
    open_positions: str
    share_price_db: str 
    ethmaxi_share_price_db: str
    steth_monitor: str
    frax_monitor: str
    stablecoin_health: str
    basepool_apy: str

ACTIVITY_DB = 'protected_moonshots_activity'
PMUSDC_DB = 'pmusdc'

TABLE_NAMES = TableNames(
    'historic_rewards',
    'buffer_values',
    'usdc_balances',
    'open_positions',
    'share_price_db',
    'ethmaxi_share_price_db',
    'steth_monitor',
    'frax_monitor',
    'stablecoin_health_db',
    'basepool_apy_db'
)