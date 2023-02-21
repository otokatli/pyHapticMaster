from dataclasses import dataclass, field
from typing import List


@dataclass
class Object:
    name: str
    pos: List = field(default_factory=lambda: [0.0, 0.0, 0.0])
    vel: List = field(default_factory=lambda: [0.0, 0.0, 0.0])
    att: List = field(default_factory=lambda: [0.0, 0.0, 0.0, 1.0])
    stiffness: float = 0.0
    dampfactor: float = 0.0
    no_pull: bool = False
    tang_damping: float = 0.0
    damping_forcemax: float = 0.0
    friction: float = 0.0
    ejection_velmax: float = 0.0
    ejection_damping: float = 0.0
    outward_forcemax: float = 0.0
    powermax: float = 0.0


class Block(Object):
    size = field(default_factory=lambda: [0.0, 0.0, 0.0])


class Sphere(Object):
    radius: float = 0.0


class FlatPlane(Object):
    normal: List = field(default_factory=lambda: [0.0, 0.0, 1.0])


class Cylinder(Object):
    radius: float = 0.0
    length: float = 0.0


class Torus(Object):
    ring_radius: float = 0.0
    tube_radius: float = 0.0
