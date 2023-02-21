from dataclasses import dataclass

@dataclass(repr=True)
class Shaker:
    frequency1: float
    frequency2: float
    direction: list
    posmax: float
    velmax: float
    accmax: float
    stiffness: float
    dampfactor: float
    deadband: float
    maxforce: float
