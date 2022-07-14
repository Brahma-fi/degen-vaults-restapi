from enum import Enum
from ..utils.queries import Queries
from ..utils.formatting import Formattor

class Pools(Enum):
    FRAX = 'frax'
    SUSD = 'susd'

def get_pools():
    try:
        result = []
        # @TODO: Move to a service
        for pool in Pools: 
            result.append(Queries().get_pool(pool._value_))

    except Exception as e:
       print(e)
       return Formattor().formatted_response(400,{
            'error': "failed to fetch all pools"
        }) 

    return Formattor().formatted_response(200, result)

def get_pool_health(pool_name):
    try:
        result = Queries().get_pool_health(pool_name)
    except:
       return Formattor().formatted_response(400,{
            'error': f"{pool_name} :: is not a valid pool"
        }) 

    return Formattor().formatted_response(200, result)

def get_pool_apy(pool_name):
    try:
        result = Queries().get_pool_apy(pool_name)
    except:
       return Formattor().formatted_response(400,{
            'error': f"{pool_name} :: is not a valid pool"
        }) 

    return Formattor().formatted_response(200, result)