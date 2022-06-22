from utils.queries import Queries
from utils.formatting import Formattor

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