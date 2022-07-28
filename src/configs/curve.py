from dataclasses import dataclass


@dataclass
class CurvePoolAddresses:
    steth: str

CURVE_POOL_ADDRESSES = CurvePoolAddresses('0xDC24316b9AE028F1497c275EB9192a3Ea0f67022')