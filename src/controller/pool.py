from services.pool import PoolService, Pools
from utils.queries import Queries
from utils.formatting import Formattor



def get_pools():
    try:
        result = PoolService().get_all_pools()
    except Exception as e:
       print('error on get_pools', e)
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