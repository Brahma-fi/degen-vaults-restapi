from ..controller.share_price import SharePriceControllers
from ..utils.queries import Queries
from ..utils.formatting import Formattor

from ..configs.vaults import MONITORED_TOKENS, VAULTS
from ..configs.database import TABLE_NAMES
from ..configs.response import RESPONSE_KEYS

def get_slippage(token_name):
    if not(MONITORED_TOKENS.is_valid_token(token_name=token_name)):
        return Formattor().formatted_response(400,{
            'error': f"{token_name} :: is not a valid vault name"
        })

    result = Queries().get_withdraw_slippage(
        MONITORED_TOKENS.frax if token_name == MONITORED_TOKENS.frax.name else MONITORED_TOKENS.steth
    )
    return  Formattor().formatted_response(200, result)

def get_apr_values(vault_name):
    if not(VAULTS.is_valid_vault(vault_name=vault_name)):
        return Formattor().formatted_response(400,{
            'error': f"{vault_name} :: is not a valid vault name"
        })

    result = Queries().get_latest_timestamp_value_data(
        TABLE_NAMES.share_price_db 
        if vault_name == VAULTS.pmusdc.name else 
        TABLE_NAMES.ethmaxi_share_price_db, 
        RESPONSE_KEYS.apr,
        -1
    )
    return  Formattor().formatted_response(200, result)

def get_share_prices(vault_name):
    if not(VAULTS.is_valid_vault(vault_name=vault_name)):
        return Formattor().formatted_response(400,{
            'error': f"{vault_name} :: is not a valid vault name"
        })

    share_price_controller = SharePriceControllers[vault_name]

    result = share_price_controller.get_all_share_prices()
    return  Formattor().formatted_response(200, result)

def get_latest_share_price(vault_name):
    if not(VAULTS.is_valid_vault(vault_name=vault_name)):
        return Formattor().formatted_response(400,{
            'error': f"{vault_name} :: is not a valid vault name"
        }) 

    share_price_controller = SharePriceControllers[vault_name]

    result = share_price_controller.get_latest_share_price()
    return Formattor().formatted_response(200, result) 