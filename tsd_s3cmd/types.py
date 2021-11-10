from enum import Enum

class TsdEnvironment(str, Enum):
    prod = "prod"
    alt = "alt"
    test = "test"