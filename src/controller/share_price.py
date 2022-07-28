from dataclasses import dataclass
from ..configs.curve import CURVE_POOL_ADDRESSES
from ..configs.database import TABLE_NAMES
from ..configs.vaults import VAULTS
from ..configs.response import RESPONSE_KEYS
from ..utils.queries import Queries
from ..utils.on_chain import OnChainQueries
from ..utils.share_price import SharePriceResult


def get_latest_ethmaxi_share_price():
    latest_data = Queries().get_latest_timestamp_value_data(
        TABLE_NAMES.ethmaxi_share_price_db, 
        RESPONSE_KEYS.price
    )
    steth_price = OnChainQueries().get_latest_token_price_from_curve_pool(CURVE_POOL_ADDRESSES.steth,1,0)

    eth_share_price = latest_data[RESPONSE_KEYS.price]
    steth_share_price = eth_share_price / steth_price

    return {
        "eth": eth_share_price,
        "steth": steth_share_price
    }

def get_latest_generic_share_price(key):
    latest_data = Queries().get_latest_timestamp_value_data(
     TABLE_NAMES.share_price_db, 
     RESPONSE_KEYS.price
    )

    return {
        f"{key}": latest_data[RESPONSE_KEYS.price]
    } 


EthMaxiSharePrice = SharePriceResult(
    TABLE_NAMES.ethmaxi_share_price_db,
    get_latest_ethmaxi_share_price
)
PMUSDCSharePrice = SharePriceResult(
    TABLE_NAMES.share_price_db,
    lambda: get_latest_generic_share_price("usdc")
)

SharePriceControllers = {
    f"{VAULTS.ethmaxi.name}": EthMaxiSharePrice,
    f"{VAULTS.pmusdc.name}": PMUSDCSharePrice
}