from haptic_master.base import Base


class Object(Base):
    def get_stiffness(self) -> float:
        msg = 'get ' + self.name + ' stiffness'

        return float(self.robot.send_message(msg))

    def set_stiffness(self, value: float) -> bool:
        msg = 'set ' + self.name + ' stiffness ' + str(value)

        return self.robot.send_message(msg)

    def get_dampfactor(self) -> float:
        msg = 'get ' + self.name + ' dampfactor'
    
        return float(self.robot.send_message(msg))
    
    def set_dampfactor(self, value: float) -> bool:
        msg = 'set ' + self.name + ' dampfactor ' + str(value)
    
        return self.robot.send_message(msg)

    def get_no_pull(self) -> bool:
        msg = 'get ' + self.name + ' no_pull'

        return self.robot._string_to_bool(self.robot.send_message(msg))
    
    def set_no_pull(self, value: bool) -> bool:
        msg = 'set ' + self.name + ' no_pull ' + str(value).lower()

        return self.robot.send_message(msg)

    def get_tang_damping(self) -> float:
        msg = 'get ' + self.name + ' tang_damping'
    
        return float(self.robot.send_message(msg))
    
    def set_tang_damping(self, value: float) -> bool:
        msg = 'set ' + self.name + ' tang_damping ' + str(value)
    
        return self.robot.send_message(msg)

    def get_damping_forcemax(self) -> float:
        msg = 'get ' + self.name + ' damping_forcemax'
    
        return float(self.robot.send_message(msg))

    def set_damping_forcemax(self, value: float) -> bool:
        msg = 'set ' + self.name + ' damping_forcemax ' + str(value)
    
        return self.robot.send_message(msg)

    def get_friction(self) -> float:
        msg = 'get ' + self.name + ' friction'

        return float(self.robot.send_message(msg))
    
    def set_friction(self, value: float) -> bool:
        'set ' + self.name + ' friction ' + str(value)

        return self.robot.send_message(msg)

    def get_ejection_velmax(self) -> float:
        msg = 'get ' + self.name + ' ejection_velmax'

        return float(self.robot.send_message(msg))
    
    def set_ejection_velmax(self, value: float) -> bool:
        msg = 'set ' + self.name + ' ejection_velmax ' + str(value)

        return self.robot.send_message(msg)

    def get_ejection_damping(self) -> float:
        msg = 'get ' + self.name + ' ejection_damping'
    
        return float(self.robot.send_message(msg))
    
    def set_ejection_damping(self, value: float) -> bool:
        msg = 'set ' + self.name + ' ejection_damping ' + str(value)
   
        return self.robot.send_message(msg)

    def get_outward_forcemax(self) -> float:
        msg = 'get ' + self.name + ' no_outward_forcemax'

        return float(self.robot.send_message(msg))
    
    def set_outward_forcemax(self, value: float) -> bool:
        msg = 'set ' + self.name + ' no_outward_forcemax ' + str(value)

        return self.robot.send_message(msg)

    def get_powermax(self) -> float:
        msg = 'get ' + self.name + ' powermax'
    
        return float(self.robot.send_message(msg))
    
    def set_powermax(self, value: float) -> bool:
        msg = 'set ' + self.name + ' powermax ' + str(value)

        return self.robot.send_message(msg)


class Block(Object):
    def create(self):
        msg = 'create block ' + self.name

        if f'Effect block with name {self.name} created' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_size(self) -> list:
        msg = 'get ' + self.name + ' size'

        return self.robot._string_to_list(self.robot.send_message(msg))

    def set_size(self, value: list) -> bool:
        msg = 'set ' + self.name + ' size ' + str(value).replace(' ', '')

        if 'Block\'s size set' in self.robot.send_message(msg):
            return True
        else:
            return False


class Sphere(Object):
    def create(self):
        msg = 'create sphere ' + self.name

        if f'Effect sphere with name {self.name} created' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_radius(self) -> float:
        msg = 'get ' + self.name + ' radius'

        return float(self.robot.send_message(msg))
    
    def set_radius(self, value: float) -> bool:
        msg = 'set ' + self.name + ' radius ' + str(value)

        if 'Sphere\'s radius set' in self.robot.send_message(msg):
            return True
        else:
            return False


class FlatPlane(Object):
    def create(self):
        msg = 'create flatplane ' + self.name
        
        if f'Effect flatplane with name {self.name} created' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_normal(self) -> list:
        msg = 'get ' + self.name + ' normal'

        return self.robot._string_to_list(self.robot.send_message(msg))
    
    def set_normal(self, value: list) -> bool:
        msg = 'set ' + self.name + ' normal ' + str(value).replace(' ', '')

        if 'Flat plane\'s normal set' in self.robot.send_message(msg):
            return True
        else:
            return False


class Cylinder(Object):
    def create(self):
        msg = 'create cylinder ' + self.name

        if f'Effect cylinder with name {self.name} created' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_radius(self) -> float:
        msg = 'get ' + self.name + ' radius'

        return float(self.robot.send_message(msg))
    
    def set_radius(self, value: float) -> bool:
        msg = 'set ' + self.name + ' radius ' + str(value)
    
        if 'Cylinder\'s radius set' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_length(self) -> float:
        msg = 'get ' + self.name + ' length'

        return float(self.robot.send_message(msg))

    def set_length(self, value: float) -> bool:
        msg = 'set ' + self.name + ' length ' + str(value)
    
        if 'Cylinder\'s length set' in self.robot.send_message(msg):
            return True
        else:
            return False


class Torus(Object):
    def create(self):
        msg = 'create torus ' + self.name

        if f'Effect torus with name {self.name} created' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_ring_radius(self) -> float:
        msg = 'get ' + self.name + ' ring_radius'

        return float(self.robot.send_message(msg))

    def set_ring_radius(self, value: float) -> bool:
        msg = 'set ' + self.name + ' ring_radius ' + str(value)

        return self.robot.send_message(msg)

    def get_tube_radius(self) -> float:
        msg = 'get ' + self.name + ' tube_radius'

        return float(self.robot.send_message(msg))
    
    def set_tube_radius(self, value: float) -> bool:
        msg = 'set ' + self.name + ' tube_radius ' + str(value)

        return self.robot.send_message(msg)
