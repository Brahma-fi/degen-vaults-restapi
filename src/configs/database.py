from dataclasses import dataclass

@dataclass
class TableNames():
    historic_rewards: str
    buffer_values: str

DATABASE_NAME = 'protected_moonshots_activity'
TABLE_NAMES = TableNames('historic_rewards','buffer_values')