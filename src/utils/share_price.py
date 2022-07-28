from configs.response import RESPONSE_KEYS
from ..configs.database import TABLE_NAMES
from ..utils.queries import Queries


class SharePriceResult:
    def __init__(self, table_name: TABLE_NAMES, latest_share_price) -> None:
        self.table_name = table_name
        self.get_latest_share_price = latest_share_price

    def get_all_share_prices(self):
        return Queries().get_all_timestamp_value_data(
            self.table_name, 
            RESPONSE_KEYS.price
        )

    def get_latest_share_price(self):
        return self.latest_share_price()
