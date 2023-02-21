from haptic_master.base import Base
from .communication import send_message
import socket


class Effect(Base):
    def get_pos(self) -> str:
        return 'get ' + self.name + ' pos'
    
    def get_vel(self) -> str:
        return 'get ' + self.name + ' vel'
    
    def get_att(self) -> str:
        return 'get ' + self.name + ' att'
    
    def set_pos(self, value: list) -> str:
        return 'set ' + self.name + ' pos ' + str(value).replace(' ', '')
    
    def set_vel(self, value: list) -> str:
        return 'set ' + self.name + ' vel ' + str(value).replace(' ', '')
    
    def set_att(self, value: list) -> str:
        return 'set ' + self.name + ' att ' + str(value).replace(' ', '')

    
class Spring(Effect):
    def create(self, s: socket) -> bool:
        msg = 'create spring ' + self.name

        if f'Effect spring with name {self.name} created' in send_message(s, msg):
            return True
        else:
            return False
    
    def get_stiffness(self, s: socket) -> float:
        msg = 'get ' + self.name + ' stiffness'

        return float(send_message(s, msg))

    def get_dampfactor(self) -> str:
        return 'get ' + self.name + ' dampfactor'

    def get_deadband(self) -> str:
        return 'get ' + self.name + ' deadband'

    def get_direction(self) -> str:
        return 'get ' + self.name + ' direction'

    def get_maxforce(self) -> str:
        return 'get ' + self.name + ' maxforce'

    def get_dampglobal(self) -> str:
        return 'get ' + self.name + ' dampglobal'
    
    def set_stiffness(self, s: socket, value: float) -> bool:
        msg = 'set ' + self.name + ' stiffness ' + str(value)

        if 'Spring\'s stiffness set' in send_message(s, msg):
            return True
        else:
            return False

    def set_dampfactor(self, value: float) -> str:
        return 'set ' + self.name + ' dampfactor ' + str(value)

    def set_deadband(self, value: float) -> str:
        return 'set ' + self.name + ' deadband ' + str(value)

    def set_direction(self, value: list) -> str:
        return 'set ' + self.name + ' direction ' + str(value).replace(' ', '')

    def set_maxforce(self, value: float) -> str:
        return 'set ' + self.name + ' maxforce ' + str(value)

    def set_dampglobal(self, value: bool) -> str:
        return 'set ' + self.name + ' dampglobal ' + str(value).lower()


class Damper(Effect):
    def get_dampcoef(self) -> str:
        return 'get ' + self.name + ' dampcoef'
    
    def set_dampcoef(self, value: list) -> str:
        return 'set ' + self.name + ' dampcoef ' + str(value).replace(' ', '')


class BiasForce(Effect):
    def get_force(self) -> str:
        return 'get ' + self.name + ' force'
    
    def set_force(self, value: list) -> str:
        return 'set ' + self.name + ' force ' + str(value).replace(' ', '')
