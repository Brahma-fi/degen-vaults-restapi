from dataclasses import dataclass

@dataclass
class ResponseKeys():
    timestamp: str
    buffer: str
    claimed_rewards: str

RESPONSE_KEYS = ResponseKeys("timestamp","buffer","claimed_rewards")