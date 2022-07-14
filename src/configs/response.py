from dataclasses import dataclass

@dataclass
class ResponseKeys():
    timestamp: str
    buffer: str
    claimed_rewards: str
    price: str
    apr: str
    slippage: str
    value: str
    health: str
    apy: str
    name: str

RESPONSE_KEYS = ResponseKeys(
    "timestamp",
    "buffer",
    "claimed_rewards",
    "price",
    "apr",
    "slippage",
    "value",
    "health",
    "apy",
    "name"
)