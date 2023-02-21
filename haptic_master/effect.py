from dataclasses import dataclass, field
from haptic_master.base import Base


@dataclass
class Effect(Base):
    name: str
    pos: list = field(default_factory=lambda: [0.0, 0.0, 0.0])
    vel: list = field(default_factory=lambda: [0.0, 0.0, 0.0])
    att: list = field(default_factory=lambda: [0.0, 0.0, 0.0, 1.0])

    def get_pos_msg(self) -> str:
        return 'get ' + self.name + ' pos'
    
    def get_vel_msg(self) -> str:
        return 'get ' + self.name + ' vel'
    
    def get_att_msg(self) -> str:
        return 'get ' + self.name + ' att'
    
    def set_pos_msg(self, value: list) -> str:
        return 'set ' + self.name + ' pos ' + str(value).replace(' ', '')
    
    def set_vel_msg(self, value: list) -> str:
        return 'set ' + self.name + ' vel ' + str(value).replace(' ', '')
    
    def set_att_msg(self, value: list) -> str:
        return 'set ' + self.name + ' att ' + str(value).replace(' ', '')

    
@dataclass
class Spring(Effect):
    stiffness: float = 0.0
    dampfactor: float = 0.0
    deadband: float = 0.0
    direction: list = field(default_factory=lambda: [0.0, 0.0, 1.0])
    maxforce: float = 0.0
    dampglobal: bool = False

    def get_stiffness_msg(self) -> str:
        return 'get ' + self.name + ' stiffness'

    def get_dampfactor_msg(self) -> str:
        return 'get ' + self.name + ' dampfactor'

    def get_deadband_msg(self) -> str:
        return 'get ' + self.name + ' deadband'

    def get_direction_msg(self) -> str:
        return 'get ' + self.name + ' direction'

    def get_maxforce_msg(self) -> str:
        return 'get ' + self.name + ' maxforce'

    def get_dampglobal_msg(self) -> str:
        return 'get ' + self.name + ' dampglobal'
    
    def set_stiffness_msg(self, value: float) -> str:
        return 'set ' + self.name + ' stiffness ' + str(value)

    def set_dampfactor_msg(self, value: float) -> str:
        return 'set ' + self.name + ' dampfactor ' + str(value)

    def set_deadband_msg(self, value: float) -> str:
        return 'set ' + self.name + ' deadband ' + str(value)

    def set_direction_msg(self, value: list) -> str:
        return 'set ' + self.name + ' direction ' + str(value).replace(' ', '')

    def set_maxforce_msg(self, value: float) -> str:
        return 'set ' + self.name + ' maxforce ' + str(value)

    def set_dampglobal_msg(self, value: bool) -> str:
        return 'set ' + self.name + ' dampglobal ' + str(value).lower()


@dataclass
class Damper(Effect):
    dampcoef: list = field(default_factory=lambda: [0.0, 0.0, 0.0])

    def get_dampcoef_msg(self) -> str:
        return 'get ' + self.name + ' dampcoef'
    
    def set_dampcoef_msg(self, value: list) -> str:
        return 'set ' + self.name + ' dampcoef ' + str(value).replace(' ', '')


@dataclass
class BiasForce(Effect):
    force: list = field(default_factory=lambda: [0.0, 0.0, 0.0])

    def get_force_msg(self) -> str:
        return 'get ' + self.name + ' force'
    
    def set_force_msg(self, value: list) -> str:
        return 'set ' + self.name + ' force ' + str(value).replace(' ', '')
