from haptic_master.base import Base


class Object(Base):
    def get_stiffness(self) -> str:
        return 'get ' + self.name + ' stiffness'

    def get_dampfactor(self) -> str:
        return 'get ' + self.name + ' dampfactor'
    
    def get_no_pull(self) -> str:
        return 'get ' + self.name + ' no_pull'

    def get_tang_damping(self) -> str:
        return 'get ' + self.name + ' tang_damping'
    
    def get_damping_forcemax(self) -> str:
        return 'get ' + self.name + ' damping_forcemax'
    
    def get_friction(self) -> str:
        return 'get ' + self.name + ' friction'

    def get_ejection_velmax(self) -> str:
        return 'get ' + self.name + ' ejection_velmax'

    def get_ejection_damping(self) -> str:
        return 'get ' + self.name + ' ejection_damping'
    
    def get_outward_forcemax(self) -> str:
        return 'get ' + self.name + ' no_outward_forcemax'

    def get_powermax(self) -> str:
        return 'get ' + self.name + ' powermax'
    
    

    def set_stiffness(self, value: float) -> str:
        return 'set ' + self.name + ' stiffness ' + str(value)

    def set_dampfactor(self, value: float) -> str:
        return 'set ' + self.name + ' dampfactor ' + str(value)
    
    def set_no_pull(self, value: bool) -> str:
        return 'set ' + self.name + ' no_pull ' + str(value).lower()

    def set_tang_damping(self, value: float) -> str:
        return 'set ' + self.name + ' tang_damping ' + str(value)
    
    def set_damping_forcemax(self, value: float) -> str:
        return 'set ' + self.name + ' damping_forcemax ' + str(value)
    
    def set_friction(self, value: float) -> str:
        'set ' + self.name + ' friction ' + str(value)

    def set_ejection_velmax(self, value: float) -> str:
        return 'set ' + self.name + ' ejection_velmax ' + str(value)

    def set_ejection_damping(self, value: float) -> str:
        return 'set ' + self.name + ' ejection_damping ' + str(value)
    
    def set_outward_forcemax(self, value: float) -> str:
        return 'set ' + self.name + ' no_outward_forcemax ' + str(value)

    def set_powermax(self, value: float) -> str:
        return 'set ' + self.name + ' powermax ' + str(value)


class Block(Object):
    def get_size(self) -> str:
        return 'get ' + self.name + ' size'

    def set_size(self, value: list) -> str:
        return 'set ' + self.name + ' size ' + str(value).replace(' ', '')


class Sphere(Object):
    def get_radius(self) -> str:
        return 'get ' + self.name + ' radius'

    def set_radius(self, value: float) -> str:
        return 'set ' + self.name + ' radius ' + str(value)
    

class FlatPlane(Object):
    def get_normal(self) -> str:
        return 'get ' + self.name + ' normal'

    def set_normal(self, value: list) -> str:
        return 'set ' + self.name + ' normal ' + str(value).replace(' ', '')


class Cylinder(Object):
    def get_radius(self) -> str:
        return 'get ' + self.name + ' radius'
    
    def get_length(self) -> str:
        return 'get ' + self.name + ' length'

    def set_radius(self, value: float) -> str:
        return 'set ' + self.name + ' radius ' + str(value)
    
    def set_length(self, value: float) -> str:
        return 'set ' + self.name + ' length ' + str(value)
    

class Torus(Object):
    def get_ring_radius(self) -> str:
        return 'get ' + self.name + ' ring_radius'

    def get_tube_radius(self) -> str:
        return 'get ' + self.name + ' tube_radius'

    def set_ring_radius(self, value: float) -> str:
        return 'set ' + self.name + ' ring_radius ' + str(value)

    def set_tube_radius(self, value: float) -> str:
        return 'set ' + self.name + ' tube_radius ' + str(value)
