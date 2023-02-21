from dataclasses import dataclass, field
from haptic_master.base import Base


@dataclass
class Object(Base):
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

    def get_stiffness_msg(self) -> str:
        return 'get ' + self.name + ' stiffness'

    def get_dampfactor_msg(self) -> str:
        return 'get ' + self.name + ' dampfactor'
    
    def get_no_pull_msg(self) -> str:
        return 'get ' + self.name + ' no_pull'

    def get_tang_damping_msg(self) -> str:
        return 'get ' + self.name + ' tang_damping'
    
    def get_damping_forcemax_msg(self) -> str:
        return 'get ' + self.name + ' damping_forcemax'
    
    def get_friction_msg(self) -> str:
        return 'get ' + self.name + ' friction'

    def get_ejection_velmax_msg(self) -> str:
        return 'get ' + self.name + ' ejection_velmax'

    def get_ejection_damping_msg(self) -> str:
        return 'get ' + self.name + ' ejection_damping'
    
    def get_outward_forcemax_msg(self) -> str:
        return 'get ' + self.name + ' no_outward_forcemax'

    def get_powermax_msg(self) -> str:
        return 'get ' + self.name + ' powermax'
    
    

    def set_stiffness_msg(self, value: float) -> str:
        return 'set ' + self.name + ' stiffness ' + str(value)

    def set_dampfactor_msg(self, value: float) -> str:
        return 'set ' + self.name + ' dampfactor ' + str(value)
    
    def set_no_pull_msg(self, value: bool) -> str:
        return 'set ' + self.name + ' no_pull ' + str(value).lower()

    def set_tang_damping_msg(self, value: float) -> str:
        return 'set ' + self.name + ' tang_damping ' + str(value)
    
    def set_damping_forcemax_msg(self, value: float) -> str:
        return 'set ' + self.name + ' damping_forcemax ' + str(value)
    
    def set_friction_msg(self, value: float) -> str:
        'set ' + self.name + ' friction ' + str(value)

    def set_ejection_velmax_msg(self, value: float) -> str:
        return 'set ' + self.name + ' ejection_velmax ' + str(value)

    def set_ejection_damping_msg(self, value: float) -> str:
        return 'set ' + self.name + ' ejection_damping ' + str(value)
    
    def set_outward_forcemax_msg(self, value: float) -> str:
        return 'set ' + self.name + ' no_outward_forcemax ' + str(value)

    def set_powermax_msg(self, value: float) -> str:
        return 'set ' + self.name + ' powermax ' + str(value)
    
    


class Block(Object):
    size = field(default_factory=lambda: [0.0, 0.0, 0.0])

    def get_size_msg(self) -> str:
        return 'get ' + self.name + ' size'

    def set_size_msg(self, value: list) -> str:
        return 'set ' + self.name + ' size ' + str(value).replace(' ', '')


class Sphere(Object):
    radius: float = 0.0

    def get_radius_msg(self) -> str:
        return 'get ' + self.name + ' radius'

    def set_radius_msg(self, value: float) -> str:
        return 'set ' + self.name + ' radius ' + str(value)
    

class FlatPlane(Object):
    normal: list = field(default_factory=lambda: [0.0, 0.0, 1.0])

    def get_normal_msg(self) -> str:
        return 'get ' + self.name + ' normal'

    def set_normal_msg(self, value: list) -> str:
        return 'set ' + self.name + ' normal ' + str(value).replace(' ', '')


class Cylinder(Object):
    radius: float = 0.0
    length: float = 0.0

    def get_radius_msg(self) -> str:
        return 'get ' + self.name + ' radius'
    
    def get_length_msg(self) -> str:
        return 'get ' + self.name + ' length'

    def set_radius_msg(self, value: float) -> str:
        return 'set ' + self.name + ' radius ' + str(value)
    
    def set_length_msg(self, value: float) -> str:
        return 'set ' + self.name + ' length ' + str(value)
    

class Torus(Object):
    ring_radius: float = 0.0
    tube_radius: float = 0.0

    def get_ring_radius_msg(self) -> str:
        return 'get ' + self.name + ' ring_radius'

    def get_tube_radius_msg(self) -> str:
        return 'get ' + self.name + ' tube_radius'

    def set_ring_radius_msg(self, value: float) -> str:
        return 'set ' + self.name + ' ring_radius ' + str(value)

    def set_tube_radius_msg(self, value: float) -> str:
        return 'set ' + self.name + ' tube_radius ' + str(value)
