from haptic_master.base import Base


class Effect(Base):
    pass

    
class Spring(Effect):
    def create(self) -> bool:
        msg = 'create spring ' + self.name

        if f'Effect spring with name {self.name} created' in self.robot.send_message(msg):
            return True
        else:
            return False
    
    def get_stiffness(self) -> float:
        msg = 'get ' + self.name + ' stiffness'

        return float(self.robot.send_message(msg))

    def set_stiffness(self, value: float) -> bool:
        msg = 'set ' + self.name + ' stiffness ' + str(value)

        if 'Spring\'s stiffness set' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_dampfactor(self) -> float:
        msg = 'get ' + self.name + ' dampfactor'

        return float(self.robot.send_message(msg))
    
    def set_dampfactor(self, value: float) -> bool:
        msg = 'set ' + self.name + ' dampfactor ' + str(value)

        if 'Spring\'s damp factor set' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_deadband(self) -> float:
        msg = 'get ' + self.name + ' deadband'

        return float(self.robot.send_message(msg))
    
    def set_deadband(self, value: float) -> bool:
        msg = 'set ' + self.name + ' deadband ' + str(value)

        if 'Spring\'s deadband set' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_direction(self) -> list:
        msg = 'get ' + self.name + ' direction'

        return self.robot._string_to_list(self.robot.send_message(msg))

    def set_direction(self, value: list) -> bool:
        msg = 'set ' + self.name + ' direction ' + str(value).replace(' ', '')

        if 'Spring\'s direction set' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_maxforce(self) -> float:
        msg = 'get ' + self.name + ' maxforce'

        return float(self.robot.send_message(msg))

    def set_maxforce(self, value: float) -> bool:
        msg = 'set ' + self.name + ' maxforce ' + str(value)

        if 'Spring\'s maximum force set' in self.robot.send_message(msg):
            return True
        else:
            return False

    def get_dampglobal(self) -> bool:
        msg = 'get ' + self.name + ' dampglobal'

        return self.robot._string_to_bool(self.robot.send_message(msg))
    
    def set_dampglobal(self, value: bool) -> bool:
        msg = 'set ' + self.name + ' dampglobal ' + str(value).lower()

        if 'Spring\'s damping global set' in self.robot.send_message(msg):
            return True
        else:
            return False


class Damper(Effect):
    def create(self) -> bool:
        msg = 'create damper ' + self.name

        if f'Effect damper with name {self.name} created' in self.robot.send_message(msg):
            return True
        else:
            return False
        
    def get_dampcoef(self) -> list:
        msg = 'get ' + self.name + ' dampcoef'

        return self.robot._string_to_list(self.robot.send_message(msg))
    
    def set_dampcoef(self, value: list) -> bool:
        msg = 'set ' + self.name + ' dampcoef ' + str(value).replace(' ', '')

        if 'Damper\'s damp coefficient set' in self.robot.send_message(msg):
            return True
        else:
            return False


class BiasForce(Effect):
    def create(self) -> bool:
        msg = 'create biasforce ' + self.name

        if f'Effect biasforce with name {self.name} created' in self.robot.send_message(msg):
            return True
        else:
            return False
        
    def get_force(self) -> list:
        msg = 'get ' + self.name + ' force'

        return self.robot._string_to_list(self.robot.send_message(msg))
    
    def set_force(self, value: list) -> bool:
        msg = 'set ' + self.name + ' force ' + str(value).replace(' ', '')
     
        if 'Bias force\'s force set' in self.robot.send_message(msg):
            return True
        else:
            return False
    