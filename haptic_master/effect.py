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

        return float(send_message(self._robot.sock, msg))

    def set_deadbandget_dampfactor(self) -> float:
        msg = 'get ' + self.name + ' dampfactor'

        return float(send_message(self._robot.sock, msg))
    
    def get_deadband(self) -> float:
        msg = 'get ' + self.name + ' deadband'

        return float(send_message(self._robot.sock, msg))

    def get_direction(self) -> list:
        msg = 'get ' + self.name + ' direction'

    def get_maxforce(self) -> float:
        msg = 'get ' + self.name + ' maxforce'

        return float(send_message(self._robot.sock, msg))

    def get_dampglobal(self) -> bool:
        msg = 'get ' + self.name + ' dampglobal'
    
    def set_stiffness(self, value: float) -> bool:
        msg = 'set ' + self.name + ' stiffness ' + str(value)

        if 'Spring\'self._robot.sock stiffness set' in send_message(self._robot.sock, msg):
            return True
        else:
            return False

    def set_dampfactor(self, value: float) -> bool:
        msg = 'set ' + self.name + ' dampfactor ' + str(value)

        if 'Spring\'s damp factor set' in send_message(self._robot.sock, msg):
            return True
        else:
            return False

    def set_deadband(self, value: float) -> bool:
        msg = 'set ' + self.name + ' deadband ' + str(value)

    def set_direction(self, value: list) -> bool:
        msg = 'set ' + self.name + ' direction ' + str(value).replace(' ', '')

    def set_maxforce(self, value: float) -> bool:
        msg = 'set ' + self.name + ' maxforce ' + str(value)

    def set_dampglobal(self, value: bool) -> bool:
        msg = 'set ' + self.name + ' dampglobal ' + str(value).lower()


class Damper(Effect):
    def get_dampcoef(self) -> list:
        msg = 'get ' + self.name + ' dampcoef'
    
    def set_dampcoef(self, value: list) -> bool:
        msg = 'set ' + self.name + ' dampcoef ' + str(value).replace(' ', '')


class BiasForce(Effect):
    def get_force(self) -> list:
        msg = 'get ' + self.name + ' force'
    
    def set_force(self, value: list) -> bool:
        msg = 'set ' + self.name + ' force ' + str(value).replace(' ', '')
