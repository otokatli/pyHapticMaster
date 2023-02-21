from dataclasses import dataclass, field


@dataclass
class Shaker:
    name: str
    frequency1: float = 0.0
    frequency2: float = 0.0
    direction: list = field(default_factory=lambda: [0.0, 0.0, 1.0])
    posmax: float = 0.0
    velmax: float = 0.0
    accmax: float = 0.0
    stiffness: float = 0.0
    dampfactor: float = 0.0
    deadband: float = 0.0
    maxforce: float = 0.0

    def get_frequency1_msg(self) -> str:
        return 'get ' + self.name + ' frequency1'
    
    def get_frequency2_msg(self) -> str:
        return 'get ' + self.name + ' frequency2'
    
    def get_direction_msg(self) -> str:
        return 'get ' + self.name + ' direction'
    
    def get_posmax_msg(self) -> str:
        return 'get ' + self.name + ' posmax'
    
    def get_velmax_msg(self) -> str:
        return 'get ' + self.name + ' velmax'
    
    def get_accmax_msg(self) -> str:
        return 'get ' + self.name + ' accmax'
    
    def get_stiffness_msg(self) -> str:
        return 'get ' + self.name + ' stiffness'
    
    def get_dampfactor_msg(self) -> str:
        return 'get ' + self.name + ' dampfactor'
    
    def get_deadband_msg(self) -> str:
        return 'get ' + self.name + ' deadband'
    
    def get_maxforce_msg(self) -> str:
        return 'get ' + self.name + ' maxforce'
    
    def set_frequency1_msg(self, value: float) -> str:
        return 'set ' + self.name + ' frequency1 ' + str(value)
    
    def set_frequency2_msg(self, value: float) -> str:
        return 'set ' + self.name + ' frequency2 ' + str(value)
    
    def set_direction_msg(self, value: list) -> str:
        return 'set ' + self.name + ' direction ' + str(value).replace(' ', '')
    
    def set_posmax_msg(self, value: float) -> str:
        return 'set ' + self.name + ' posmax ' + str(value)
    
    def set_velmax_msg(self, value: float) -> str:
        return 'set ' + self.name + ' velmax ' + str(value)
    
    def set_accmax_msg(self, value: float) -> str:
        return 'set ' + self.name + ' accmax ' + str(value)
    
    def set_stiffness_msg(self, value: float) -> str:
        return 'set ' + self.name + ' stiffness ' + str(value)
    
    def set_dampfactor_msg(self, value: float) -> str:
        return 'set ' + self.name + ' dampfactor ' + str(value)
    
    def set_deadband_msg(self, value: float) -> str:
        return 'set ' + self.name + ' deadband ' + str(value)
    
    def set_maxforce_msg(self, value: float) -> str:
        return 'set ' + self.name + ' maxforce ' + str(value)
