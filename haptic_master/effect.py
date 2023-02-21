from dataclasses import dataclass, field
from typing import List


@dataclass
class Effect:
    name: str
    pos: List = field(default_factory=lambda: [0.0, 0.0, 0.0])
    vel: List = field(default_factory=lambda: [0.0, 0.0, 0.0])
    att: List = field(default_factory=lambda: [0.0, 0.0, 0.0, 1.0])

    
@dataclass
class Spring(Effect):
    stiffness: float = 0.0
    dampfactor: float = 0.0
    deadband: float = 0.0
    direction: List = field(default_factory=lambda: [0.0, 0.0, 1.0])
    maxforce: float = 0.0
    dampglobal: bool = 0.0


@dataclass
class Damper(Effect):
    dampcoef: List = field(default_factory=lambda: [0.0, 0.0, 0.0])


@dataclass
class BiasForce(Effect):
    force: List = field(default_factory=lambda: [0.0, 0.0, 0.0]) 
