from enum import Enum

from utils.queries import Queries

class Pools(Enum):
    FRAX = 'frax'
    SUSD = 'susd'

class PoolService():
    def get_all_pools(self):
        result = []
        for pool in Pools: 
            result.append(Queries().get_pool(pool._value_))
        return result