from .haptic_master import HapticMaster
from dataclasses import dataclass

@dataclass(frozen=True)
class Base:
    name: str
    robot: HapticMaster

    def get_pos(self) -> list:
        msg = 'get ' + self.name + ' pos'

        return self.robot.send_message(self.robot.sock, msg)

    def get_vel(self) -> str:
        return 'get ' + self.name + ' vel'
    
    def get_att(self) -> str:
        return 'get ' + self.name + ' att'
    
    def get_enable(self) -> str:
        return 'get ' + self.name + ' enabled'
    
    def set_pos(self, value: list) -> str:
        return 'set ' + self.name + ' pos ' + str(value).replace(' ', '')
    
    def set_vel(self, value: list) -> str:
        return 'set ' + self.name + ' vel ' + str(value).replace(' ', '')
    
    def set_att(self, value: list) -> str:
        'set ' + self.name + ' att ' + str(value).replace(' ', '')

    def set_enable(self) -> str:
        return 'set ' + self.name + ' enable'
    
    def set_disable(self) -> str:
        return 'set ' + self.name + ' disable'